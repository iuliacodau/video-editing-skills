---
name: color-grading
description: Correct footage and apply a consistent look to a social video. Use when the user asks about color correction, matching shots from different cameras or lighting, applying a LUT or style, fixing skin tones, or choosing a look in DaVinci Resolve, Premiere, Final Cut, CapCut or similar editors.
---

# Color grading for social video

Grade in two stages: **correct first, style second.** Output is a step-by-step grading plan for the user's editor, with specific controls to adjust.

## Process

1. **Get context.** Editor, camera or phone, shooting format (log, HDR, standard), the mood wanted, and whether there is a brand palette (see the `color-palettes` skill).
2. **Check the source.** Is footage log, HDR, or standard? Log or HDR footage needs a proper conversion to the working color space before any look is applied. Do not stack a look LUT on footage that has not been converted.
3. **Correct each clip.**
   - Exposure: set a sensible midtone and keep highlights and shadows from clipping.
   - Contrast: shape with a gentle curve rather than only a contrast slider.
   - White balance: neutralize a known neutral (white, gray) if available.
   - Skin: keep faces natural and consistent. Check against the skin tone line on a vectorscope if the editor has one.
4. **Match shots.** Pick a hero shot per scene and match the others to it for brightness, white balance and saturation. Matching matters more than the look.
5. **Apply the look.** Build it with a few deliberate moves (see `references/looks.md`), applied to the whole timeline or per scene. Keep it subtle enough to survive phone screens and platform compression.
6. **Check.** Compare before and after, view on a phone, and view at low brightness. Fix any shot that sticks out. Watch skin, blacks and clipped highlights.

## Output format

```
Source: <format / editor>
Correction steps (per clip): ...
Matching plan: hero shot = ..., adjust others by ...
Look: <name> - <the specific moves>
Checks: ...
```

Name the actual controls in the user's software (for example "Lift/Gamma/Gain wheels", "Curves", "HSL Secondary", "Temperature/Tint").

## Principles

- Trust scopes (waveform, vectorscope, histogram) over your eyes on an uncalibrated screen.
- Consistency across the video beats a dramatic look on single shots.
- Protect skin tones first; push color into backgrounds and graphics instead.
- Social platforms compress heavily: very subtle gradients and deep, noisy shadows can band or blotch. Avoid crushing blacks.
- Do not claim a specific LUT or preset exists unless the user has it. Describe the look in controls instead.
