---
name: captions
description: Write, time and style captions or subtitles for a social video, including word-by-word highlight styles, line breaking, reading speed, SRT/VTT files and accessibility. Use when the user needs captions made, cleaned up or restyled, wants captions for sound-off viewers, or asks how to format subtitles for Reels, TikTok or Shorts.
---

# Captions for social video

Captions serve sound-off viewers, accessibility and retention. Output is clean caption text with timing, plus a style spec for the user's editor.

## Process

1. **Get the source.** A transcript, script or audio-derived text, the language, and the editor or tool that will render captions (built-in auto-captions, CapCut, Premiere, Resolve, or a burned-in export). If only the video file exists, make a first-draft transcript with `scripts/transcribe.py` (runs locally; needs `pip install faster-whisper imageio-ffmpeg`; add `--max-words 3` for punchy short-form chunks) and treat it as a draft, since speech recognition gets names, brands and slang wrong.
2. **Clean the text.** Fix mistakes in names, product terms and numbers. Remove filler words only if the user wants clean verbatim-light captions; keep meaning intact. Do not change what the speaker said in substance.
3. **Break into caption chunks.**
   - Short-form: roughly 1-5 words per chunk (about 2-3 for fast, punchy style), at most two lines.
   - Break at natural phrases, never between an article and its noun, or a preposition and its object, if avoidable.
   - Keep lines roughly balanced.
4. **Time them.** A chunk appears when its first word is spoken and leaves shortly after the last word. Avoid captions flashing for under about 0.5 seconds unless they are single emphasized words. Keep reading speed comfortable (about 15-20 characters per second for full subtitles; short-form chunks are shorter and faster).
5. **Style them** using `references/caption-styles.md`: font, size, weight, position, highlight color and animation, consistent with the `typography` and `color-palettes` skills.
6. **Position safely.** Place captions in the lower-middle area but above the platform's bottom UI, never over the face, and clear of the right-edge buttons.
7. **Deliver.** Give the user the format they need: plain text with timestamps, an SRT or VTT file, or a style spec for their editor. State whether captions are burned in or a separate track.
8. **Check.** Read the captions alongside the audio: spelling, sync, line breaks, and legibility on a phone.

## Output format

- **Caption text** with timestamps (SRT format unless asked otherwise, see reference)
- **Style spec:** font, size, weight, case, colors, highlight, position, animation
- **Notes:** names or terms to verify, places where captions might collide with on-screen text

## Principles

- Accuracy first. Wrong captions are worse than none.
- Be consistent: the same style, position and animation for the whole video.
- Emphasis with highlight color should mark the key word, not every word.
- Do not caption over on-screen text; move one or the other.
- Include meaningful non-speech sounds in captions only when the video is meant to be accessible and the sound matters, for example [laughs].
- Make sure the language, spelling and punctuation match the audience (for example US vs UK spelling).
