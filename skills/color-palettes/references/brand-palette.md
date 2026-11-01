# Brand palette (fill this in once, reuse everywhere)

Other skills (typography, captions, color-grading) read this file when it is filled in. Replace the placeholders with your real values.

## Palette

| Role | Name | Hex | Use |
| --- | --- | --- | --- |
| Primary | TODO | #TODO | Hook text, key graphics |
| Secondary | TODO | #TODO | Supporting shapes, lower thirds |
| Accent | TODO | #TODO | Highlights, call to action, caption emphasis |
| Light neutral | TODO | #TODO | Text on dark, card backgrounds |
| Dark neutral | TODO | #TODO | Text on light, overlays |

## Approved text and background pairs

| Text | Background | Contrast ratio | OK for |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Rules

- TODO (for example: accent color only for one element per scene)
- TODO (for example: never put primary text on the secondary color)

## Mood

TODO: one line, for example "warm, playful, handmade" or "clean, technical, calm".

---

# Palette reference

## Building from a mood

| Mood | Direction |
| --- | --- |
| Energetic | Saturated warm primary (red, orange, yellow) with a dark neutral |
| Calm / trustworthy | Blues and greens, soft neutrals, low saturation accent |
| Premium / editorial | Deep neutrals, one restrained accent, lots of space |
| Playful | Bright primaries with a light background, a strong accent |
| Natural / wellness | Earth tones, muted greens and warm creams |
| Tech | Dark background with a vivid accent (cyan, violet, lime) |

## Harmony options

- **Monochromatic:** one hue, varied lightness. Safe and cohesive.
- **Analogous:** neighboring hues. Smooth and calm.
- **Complementary:** opposite hues. High energy; use one as the accent.
- **Triadic:** three evenly spaced hues. Playful; keep two muted.

## Contrast formula (WCAG)

Contrast ratio = (L1 + 0.05) / (L2 + 0.05), where L1 is the relative luminance of the lighter color and L2 of the darker one. Targets: about 4.5:1 for normal text, 3:1 for large text.

Relative luminance L = 0.2126 R + 0.7152 G + 0.0722 B, where R, G, B are the sRGB channels converted to linear: for each channel value c in 0-1, linear = c / 12.92 if c <= 0.03928, else ((c + 0.055) / 1.055) ^ 2.4.

## Quick contrast checker (Python)

```python
def lum(hex_color):
    h = hex_color.lstrip("#")
    rgb = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]

def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

print(round(contrast("#FFFFFF", "#1A1A2E"), 2))
```
