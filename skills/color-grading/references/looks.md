# Common looks, described as moves

These describe the adjustments, so they work in any editor. Start from a corrected, matched image.

## Clean and bright (lifestyle, tutorials, beauty)
- Lift exposure slightly, keep whites clean, open the shadows a little.
- Gentle contrast curve, minimal saturation boost.
- Keep white balance neutral to slightly warm.

## Warm and cozy
- Shift highlights and mids slightly toward orange or yellow.
- Slightly lifted blacks, softer contrast.
- Keep skin natural; do not push everything orange.

## Cool and moody
- Cool shadows (teal or blue), keep skin warm for separation.
- Slightly lower exposure, a little more contrast.
- Desaturate the background slightly.

## Teal and orange (cinematic, use with restraint)
- Push shadows toward teal, highlights toward orange.
- Keep skin protected so it does not turn orange.
- Reduce the amount if the footage has lots of skin or branded colors.

## Faded / film-inspired
- Lift the black point, soften highlights, reduce saturation a touch.
- Optional fine grain at low strength.

## High-contrast punchy (energetic, sport, streetwear)
- Stronger S-curve, higher saturation on key colors only.
- Watch for clipped highlights and noisy blacks.

## Black and white
- Convert, then shape tones with a curve. Use the original color channels (red, yellow, blue) to separate skin from background.

## Matching shots

1. Choose a hero shot.
2. Match brightness (waveform), then white balance (vectorscope or parade), then saturation.
3. Apply the same look node, layer, or adjustment on top of all.

## Fixing common problems

| Problem | Fix |
| --- | --- |
| Flat, washed-out log footage | Convert with the camera's transform or a technical LUT, then grade |
| Green or magenta cast under indoor light | Adjust Tint, then temperature |
| Blown-out sky or window | Pull highlights, use a power window or mask, accept some loss |
| Muddy or too dark skin | Lift mids on a face mask, check exposure before saturation |
| Shots from two phones do not match | Match exposure and white balance first; reduce saturation differences last |

## Delivery notes

- Export in the working color space the platform expects (usually Rec.709 / SDR for social). HDR sources need an SDR conversion unless the platform and workflow support HDR.
- Check the exported file on a phone before posting.
