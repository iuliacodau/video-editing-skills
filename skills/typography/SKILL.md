---
name: typography
description: Choose and apply fonts, sizes, hierarchy and placement for on-screen text in a social video - titles, hooks, lower thirds, labels and end cards. Use when the user asks which font to use, how large text should be, how to make text readable on a phone, or how to pair fonts for a brand.
---

# Typography for social video

Make on-screen text readable in one glance on a phone, and consistent across videos. Captions have their own skill (`captions`); this one covers designed text.

## Process

1. **Get context.** Platform, video tone, brand fonts if any, editor (some fonts are not available in every app), and what the text has to do (hook, label, quote, price, call to action).
2. **Define a small type system.** Two fonts at most, ideally one family with a few weights:
   - **Display** for hooks and titles (bold, distinctive, short text).
   - **Text** for supporting lines (clear, neutral, readable at small sizes).
3. **Set a hierarchy.** At most three levels in view at once: headline, supporting line, small label. Differ by size, weight or color, not by adding more fonts.
4. **Size for phones.** On a 1080x1920 canvas, headline text is generally large (roughly 80-140 px), supporting text roughly 50-70 px, and anything below about 40 px is hard to read on a phone. Treat these as starting points and test on a real phone.
5. **Place text safely.** Keep text away from the top, bottom and right edges where platform UI overlaps it, and away from faces. Check current platform safe zones (see `references/type-guidelines.md`).
6. **Ensure contrast.** Light text on a dark area or dark text on a light area, with a subtle shadow, outline or background box when the video behind is busy. Check against the `color-palettes` skill for contrast.
7. **Time and animate text.** Each text card stays long enough to read (see timing rules in the reference), with simple, consistent motion in and out.
8. **Check licensing.** Prefer open-license fonts (for example from Google Fonts, SIL Open Font License) for anything published or monetized, and confirm commercial-use rights for others.

## Output format

```
Fonts: Display = <name, weight>, Text = <name, weight>
Sizes (1080x1920): headline ..., support ..., label ...
Placement: ...
Colors / contrast: ...
Motion: ...
Licensing: ...
```

## Principles

- Fewer words, larger text. If it needs more than about six words, consider voiceover or a caption instead.
- Consistency across videos builds recognition more than novelty does.
- Avoid thin weights, narrow condensed styles for body text, and busy script fonts for anything important.
- Align text deliberately (left or center, not mixed) and keep consistent margins.
- Do not recommend a font as available in an editor unless the user confirms it, offer a close fallback.
