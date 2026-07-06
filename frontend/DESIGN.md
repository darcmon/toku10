# Notches design language

Direction: **hybrid** — light editorial stat surfaces ("the stat room") with dark
broadcast-styled islands ("the arena") for everything era/card/community related.
Chosen in the July 2026 design session; token values live in `src/style.css`
(Tailwind v4 `@theme`).

## The two zones

| | Stat room (light) | Arena (dark) |
|---|---|---|
| Content | Scores, line score, stat tables, comparisons | Era cards, unlocks, voting, submissions |
| Surfaces | `paper` / `paper-dim`, `hairline` borders | `arena-950` panel, `arena-900` cards, `arena-700` hairlines |
| Text | `ink` / `ink-dim` / `ink-faint` | `arena-50` / `arena-300` / `arena-400` |
| Headings | Inter 500, sentence case | Barlow Condensed 600, uppercase, letterspaced |

The arena always appears as a contained inset panel (own border radius) inside a
light page — a stage in the room, never a page-wide theme toggle. Full-screen
arena takeovers are reserved for unlock reveals so they feel earned.

## Rules

1. **Mono digits everywhere.** Every numeral in both zones renders in IBM Plex
   Mono (`font-mono`): scores, stat cells, vote counts. This is the shared DNA
   that makes the zones read as one language.
2. **Condensed caps are arena-only.** Barlow Condensed (`font-display`,
   uppercase, `tracking-wider`+) never appears on a light surface.
3. **The legendary leak.** Rarity colors stay inside the arena, with one
   exception: legendary-tier era badges render as dark chips
   (`legendary-900`/`600`/`300`) even when inline on light stat tables. Lower
   tiers use quiet light pills (`{rarity}-100` bg, `{rarity}-800` text).
   Scarcity of dark ink on a light screen = rarity signal.
4. **Winner gets the ink.** The winning side renders `ink`; the losing side's
   score drops to `ink-faint`. Applies to headers, line scores, totals.
5. **One loud action.** `gold-400` is the arena's primary action (submit, vote).
   At most one gold element per screen; everything else is bordered/ghost.
6. **Team colors are data, not chrome.** In the light zone teams get neutral
   tinted avatars, not brand-colored UI. The comparison-bar accent is
   `accent-400` for the leader, never team colors.

## Rarity mapping

| Rarity (data) | Token ramp | Dark chip | Light pill |
|---|---|---|---|
| 5 (legendary) | `legendary-*` | always (rule 3) | never |
| 4 (epic) | `epic-*` | `epic-900/600/300` | `epic-100` + `epic-800` |
| 2–3 (rare) | `rare-*` | `rare-900/600/300` | `rare-100` + `rare-800` |
| 1 (common) | `common-*` | `common-900/600/300` | `common-100` + `common-800` |

## Reference mockups

Session artifacts (light / dark / hybrid comparisons) were produced in the
2026-07-05 Claude Code design session; the hybrid boxscore mockup is the
canonical reference for the boxscore view. Next screens to design: era card
detail, unlock reveal, card submission flow.
