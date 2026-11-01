#!/usr/bin/env python3
"""Transcribe a video or audio file on your own computer.

Writes caption-friendly subtitles (.srt, .vtt), a plain transcript (.txt) and a
JSON file with word-level timestamps. Nothing is uploaded: the speech model runs
locally (it is downloaded once, on first use).

Setup (once):
    pip install faster-whisper imageio-ffmpeg
    (imageio-ffmpeg ships a private copy of ffmpeg, so you do not need to install ffmpeg yourself)

Examples:
    python transcribe.py reel.mp4
    python transcribe.py reel.mp4 --language en --model small --output-dir transcripts
    python transcribe.py reel.mp4 --max-chars 28 --max-lines 2
    python transcribe.py reel.mp4 --max-words 3      # punchy 1-3 word captions

Notes:
    - Handles any format ffmpeg can read (mp4, mov, m4a, wav, ...). The audio is
      extracted with ffmpeg first; if no ffmpeg is available it falls back to the
      decoder built into faster-whisper.
    - Model sizes, smallest/fastest to largest/most accurate:
      tiny, base, small, medium, large-v3. "small" is a good default for short videos.
    - Always read the result: names, brands and slang are the usual mistakes.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Word:
    start: float
    end: float
    text: str


@dataclass
class Cue:
    start: float
    end: float
    text: str


# ---------------------------------------------------------------- formatting

def fmt_time(seconds: float, sep: str) -> str:
    """Seconds -> HH:MM:SS<sep>mmm (sep is ',' for SRT and '.' for VTT)."""
    ms = int(round(max(0.0, seconds) * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def wrap_lines(text: str, max_chars: int) -> list[str]:
    """Greedy word wrap, never splitting a word."""
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if current and len(candidate) > max_chars:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def build_cues(
    words: list[Word],
    max_chars: int = 32,
    max_lines: int = 2,
    max_duration: float = 3.5,
    max_gap: float = 0.7,
    max_words: int | None = None,
) -> list[Cue]:
    """Group words into short on-screen caption cues.

    A new cue starts when the text would exceed max_chars * max_lines, when the
    cue would run longer than max_duration, when the speaker pauses for more than
    max_gap seconds, or after sentence-ending punctuation once the cue has
    reasonable length. If max_words is set, a cue never holds more words than that
    (use 3 for fast, punchy short-form captions). Short cues suit vertical video.
    """
    cues: list[Cue] = []
    buf: list[Word] = []

    def flush() -> None:
        if buf:
            cues.append(Cue(buf[0].start, buf[-1].end, " ".join(w.text for w in buf)))
            buf.clear()

    limit = max_chars * max_lines
    for w in words:
        text = w.text.strip()
        if not text:
            continue
        w = Word(w.start, w.end, text)
        if buf:
            joined_len = len(" ".join(x.text for x in buf)) + 1 + len(text)
            too_long = joined_len > limit
            too_slow = (w.end - buf[0].start) > max_duration
            paused = (w.start - buf[-1].end) > max_gap
            too_many = max_words is not None and len(buf) >= max_words
            if too_long or too_slow or paused or too_many:
                flush()
        buf.append(w)
        if text[-1] in ".?!" and len(" ".join(x.text for x in buf)) >= max_chars // 2:
            flush()
    flush()
    return cues


def to_srt(cues: list[Cue], max_chars: int) -> str:
    out = []
    for i, c in enumerate(cues, 1):
        out.append(str(i))
        out.append(f"{fmt_time(c.start, ',')} --> {fmt_time(c.end, ',')}")
        out.extend(wrap_lines(c.text, max_chars))
        out.append("")
    return "\n".join(out)


def to_vtt(cues: list[Cue], max_chars: int) -> str:
    out = ["WEBVTT", ""]
    for c in cues:
        out.append(f"{fmt_time(c.start, '.')} --> {fmt_time(c.end, '.')}")
        out.extend(wrap_lines(c.text, max_chars))
        out.append("")
    return "\n".join(out)



# ------------------------------------------------------------ audio loading

def find_ffmpeg() -> str | None:
    """System ffmpeg if present, otherwise the copy bundled with imageio-ffmpeg."""
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def load_audio(path: Path):
    """Decode any media file to 16 kHz mono float32 samples, or None if ffmpeg is unavailable."""
    exe = find_ffmpeg()
    if exe is None:
        return None
    import numpy as np

    cmd = [exe, "-nostdin", "-v", "error", "-i", str(path),
           "-vn", "-ac", "1", "-ar", "16000", "-f", "f32le", "-"]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode != 0:
        sys.exit("ffmpeg could not read this file:\n" + result.stderr.decode(errors="replace").strip())
    audio = np.frombuffer(result.stdout, dtype=np.float32)
    if audio.size == 0:
        sys.exit("This file has no audio track.")
    return audio

# ------------------------------------------------------------ transcription

def transcribe(path: Path, model_name: str, language: str | None, device: str):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit(
            "faster-whisper is not installed.\n"
            "Install it with:  pip install faster-whisper imageio-ffmpeg"
        )

    audio = load_audio(path)
    source = audio if audio is not None else str(path)
    model = WhisperModel(model_name, device=device, compute_type="int8")
    segments, info = model.transcribe(
        source,
        language=language,
        word_timestamps=True,
        vad_filter=True,      # skip silence and music; reduces made-up text
        beam_size=5,
    )
    words: list[Word] = []
    segment_dump = []
    for seg in segments:
        seg_words = [Word(w.start, w.end, w.word) for w in (seg.words or [])]
        words.extend(seg_words)
        segment_dump.append(
            {
                "start": round(seg.start, 3),
                "end": round(seg.end, 3),
                "text": seg.text.strip(),
                "words": [
                    {"start": round(w.start, 3), "end": round(w.end, 3), "word": w.text.strip()}
                    for w in seg_words
                ],
            }
        )
    return words, segment_dump, info


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Transcribe a video or audio file locally.")
    p.add_argument("input", type=Path, help="video or audio file")
    p.add_argument("--model", default="small", help="tiny, base, small, medium, large-v3 (default: small)")
    p.add_argument("--language", default=None, help="language code such as en or nl (default: auto-detect)")
    p.add_argument("--device", default="auto", help="auto, cpu or cuda (default: auto)")
    p.add_argument("--output-dir", type=Path, default=None, help="where to write files (default: next to the input)")
    p.add_argument("--max-chars", type=int, default=32, help="characters per caption line (default: 32)")
    p.add_argument("--max-lines", type=int, default=2, help="lines per caption (default: 2)")
    p.add_argument("--max-words", type=int, default=None, help="max words per caption, e.g. 3 for punchy short-form chunks (default: no limit)")
    args = p.parse_args(argv)

    if not args.input.is_file():
        sys.exit(f"File not found: {args.input}")
    out_dir = args.output_dir or args.input.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.input.stem

    print(f"Transcribing {args.input.name} with the '{args.model}' model...", file=sys.stderr)
    words, segments, info = transcribe(args.input, args.model, args.language, args.device)
    if not words:
        sys.exit("No speech was found in this file.")

    cues = build_cues(words, args.max_chars, args.max_lines, max_words=args.max_words)
    full_text = " ".join(s["text"] for s in segments)

    files = {
        out_dir / f"{stem}.srt": to_srt(cues, args.max_chars),
        out_dir / f"{stem}.vtt": to_vtt(cues, args.max_chars),
        out_dir / f"{stem}.txt": full_text + "\n",
        out_dir / f"{stem}.json": json.dumps(
            {
                "language": info.language,
                "language_probability": round(info.language_probability, 3),
                "duration": round(info.duration, 3),
                "segments": segments,
            },
            ensure_ascii=False,
            indent=2,
        ),
    }
    for path, content in files.items():
        path.write_text(content, encoding="utf-8")
        print(f"wrote {path}")
    print(f"Detected language: {info.language} ({info.language_probability:.0%})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
