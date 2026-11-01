---
name: color-palettes
description: Build or apply a color palette for a social video - brand colors, text and background colors, graphics and highlights. Use when the user wants a palette for a video or channel, needs colors that match a mood, asks for accessible contrast, or wants a reusable brand palette that other skills can follow.
---

# Color palettes for social video

Create a small, usable palette and say exactly where each color goes. Output is a palette with hex values, roles and usage rules.

## Process

1. **Get context.** Brand colors or logo if they exist, mood or audience, platform, footage color (dominant tones in the shots), and where the palette will be used (text, graphics, backgrounds, overlays).
2. **Check for an existing palette.** If `references/brand-palette.md` has been filled in, use it as the source of truth and only extend it when needed.
3. **Build the palette.** Aim for 4-6 colors:
   - 1 **primary** (the identity color)
   - 1-2 **secondary** or supporting colors
   - 1 **accent** for highlights and calls to action
   - 1 **light neutral** and 1 **dark neutral** (not pure white and black unless intended)
4. **Assign roles with the 60-30-10 idea.** Roughly 60% dominant (often neutrals or a background), 30% secondary, 10% accent.
5. **Check contrast.** Text and its background should reach about 4.5:1 contrast or better. Test the main text and background pairs and report the ratios.
6. **Check against footage.** Palette colors should be distinct from the dominant colors in the footage, or intentionally match them. Mention how the palette interacts with the grade (`color-grading`).
7. **Give usage rules.** Which color for hook text, which for captions highlight, which for backgrounds of cards, which for icons and arrows.

## Output format

| Role | Name | Hex | Use |
| --- | --- | --- | --- |
| Primary | ... | #xxxxxx | ... |

Plus: contrast checks (pair, ratio, pass/fail), do and don't rules, and a one-line mood description.

## Principles

- Fewer colors, used consistently, look more professional than many colors.
- Reserve the accent color for the most important element on screen.
- Do not rely on color alone to carry meaning (some viewers cannot distinguish certain colors).
- Compute contrast ratios properly (WCAG relative luminance) rather than estimating by eye.
- Never invent that a palette matches a real brand; ask for the brand's hex values.
