# Caption styles and formats

## Style options

| Style | Description | Good for |
| --- | --- | --- |
| Classic subtitles | Full phrase, 1-2 lines, white text with dark outline or box, bottom-center | Interviews, tutorials, longer videos |
| Chunked (2-4 words) | Short punchy groups that swap quickly | Talking-head, fast edits |
| Word-by-word highlight | All words of a phrase visible, current word changes color or scale | High-energy, retention-focused content |
| Single-word pop | One large word at a time | Very fast, hook-heavy content (use sparingly) |
| Box / label style | Text inside a solid or semi-transparent box | Busy backgrounds, brand-consistent look |

## Style spec template

```
Font:        <name>, <weight>
Size:        <px at 1080x1920>, <caps / sentence case>
Color:       text <hex>, highlight <hex>
Outline:     <px, hex>  or  Background box: <hex, opacity>
Shadow:      <yes / no, soft>
Position:    centered, <px> from bottom (above platform UI)
Max width:   about 80% of frame width
Animation:   <none / pop / fade>, <duration>
Highlight:   <current word only / key words only>
```

## Starting points (1080x1920)

- Size: roughly 60-90 px for chunked captions (test on a phone).
- Width: keep lines to about 80% of the frame width.
- Outline or shadow so text works on bright and dark footage.
- Highlight color from the brand accent (see `color-palettes`).

## Reading speed

- Full subtitles: about 15-20 characters per second; shorter lines for mobile.
- Minimum display: about 1 second for a full caption (shorter for single-word pops).
- Maximum: about 5-7 seconds on screen.
- Keep gaps between consecutive captions small but visible (a few frames).

## SRT format

```
1
00:00:00,000 --> 00:00:01,800
Stop doing this
if you want better edits.

2
00:00:01,900 --> 00:00:03,600
Here's the one fix
that changed my workflow.
```

Rules: sequential numbers, `HH:MM:SS,mmm` timestamps with a comma before the milliseconds, a blank line between entries, at most two lines per entry.

## VTT format

Starts with a `WEBVTT` line, uses a period before milliseconds (`00:00:01.800`), and does not need numbers.

## Burned-in vs separate track

| | Burned-in | Separate track (SRT/VTT) |
| --- | --- | --- |
| Styling | Full control, animations | Platform decides the look |
| Viewer can turn off | No | Yes |
| Editable after upload | No | Yes |
| Best for | Short-form social | Longer videos, accessibility, multiple languages |

## Quality checklist

- [ ] Spelling of names, brands and numbers verified
- [ ] Sync matches the audio within a few frames
- [ ] No line breaks in awkward places
- [ ] No more than two lines at a time
- [ ] Captions do not overlap faces, on-screen text or platform UI
- [ ] Same style and position throughout
- [ ] Tested on a phone at normal brightness
