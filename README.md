# video-editing-skills

A set of skills that help ideate and edit a video for social media.

Each skill is a focused folder with a `SKILL.md` (what Claude reads) and a `references/` folder with longer material that is only loaded when needed. Together they are packaged as one Claude plugin.

## Skills

| Skill | Use it for |
| --- | --- |
| [storytelling](skills/storytelling/SKILL.md) | Assessing a draft or idea against story principles, interviewing you to fill gaps (want, obstacle, stakes, change), then shaping the structure and hook |
| [scriptwriting](skills/scriptwriting/SKILL.md) | Turning an idea into a spoken script, with visuals and on-screen text per beat |
| [cinematography](skills/cinematography/SKILL.md) | Framing, shot lists, camera movement, lighting and b-roll for vertical video |
| [color-grading](skills/color-grading/SKILL.md) | Correcting footage, matching shots and applying a consistent look |
| [typography](skills/typography/SKILL.md) | Choosing fonts, sizes, hierarchy and placement for on-screen text |
| [color-palettes](skills/color-palettes/SKILL.md) | Building and applying a palette for graphics, text and branding |
| [captions](skills/captions/SKILL.md) | Writing, timing and styling captions and subtitles |
| [social-media-optimisation](skills/social-media-optimisation/SKILL.md) | Pre-publish review of packaging for Instagram Reels, posts and carousels: first seconds, cover and grid crop, eligibility, caption, hashtags |

A typical flow: **storytelling → scriptwriting → cinematography → (edit) → color-grading → typography + color-palettes → captions → social-media-optimisation (before posting).**

## Structure

```
.claude-plugin/
  plugin.json            # plugin manifest
skills/
  <skill-name>/
    SKILL.md             # instructions and trigger description
    references/          # longer reference material, loaded on demand
    scripts/             # optional helper scripts (for example captions/scripts/transcribe.py)
```

## Install

As a plugin in Claude Code, once this repo is pushed to GitHub:

```
/plugin marketplace add iuliacodau/video-editing-skills
/plugin install video-editing-skills
```

Or copy individual skills into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project):

```
cp -r skills/captions ~/.claude/skills/
```

## Adding or improving a skill

1. Create `skills/<skill-name>/SKILL.md` with `name` (matching the folder) and a `description` that says what the skill does and when to use it.
2. Keep `SKILL.md` short and procedural. Move long lists and examples to `references/`.
3. Add the skill to the table above.
4. Bump `version` in `.claude-plugin/plugin.json`.
