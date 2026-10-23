# Marsh / swamp – creature style (prefix `ms_`)

Biome look: still, dark-green swamp water under a canopy, duckweed and lilies at the surface, black muck and peat
below. Theme: temperate marshes, fens and bogs of the Northern Hemisphere (European reed swamps, East-Asian rice-paddy
marshes, Atlantic peat bogs). The big southern-US icons (gars, bowfin, channel catfish, crappie, mudminnows,
red swamp crawfish) are left for the bayou biome.

## Redesign note
All creatures were redrawn or recoloured to match the pf_/bw_/ac_ style (see `.agents/rules/pixel_art_guidelines.md` section 0):
one muted hue family per species, flat single-colour markings, large dark masses, per-species patterns and fin styles.
Insects and the swan mussel were replaced (great diving beetle -> crucian carp, dragonfly nymph -> ruffe, caddisfly
larva -> stone loach, swan mussel -> European bullhead). Weatherfish, newts, axolotl, pond turtle, noble crayfish,
great pond snail, softshell turtle and tadpole keep their original drawings, recoloured to the shared palette.
Generator grade: shadows #1a2014, mid cast #8c965a (~12%), highlights #e6ecd6, fins tinted #96966a (~20%), outline tint #141a10.

## Colour grade (legacy description of the original ms_ batch)
- Shadows (lum < 0.3) sink toward dark moss (26, 32, 20).
- Mid-tones get an olive cast (140, 150, 90, ~10%); everything is desaturated ~8%.
- Highlights move toward pale green-grey (226, 234, 214).
- Translucent fins are tinted green-brown (15% toward (150, 150, 100)) and ~8% more transparent.
- EXCEPTION – saturated reds / oranges (stickleback throat, redbelly dace, rudd fins, newt bellies, pumpkinseed,
  axolotl pinks) and iridescent blues (sunbleak stripe, pygmy / bluespotted sunfish spangles) are NOT graded.

## Shapes / rendering
- Same base as the other freshwater biomes: per-column form shading, outline = per-pixel dark shade of the adjacent body colour (light tint toward #141a10), lit top edge one step lighter,
  soft fins with rays, hand-placed markings.
- Eels (swamp eel, European eel) and the tadpole undulate along the body over the 4 frames.
- Non-fish swimmers: tadpole, great diving beetle (sculling hind legs), Chinese softshell turtle (paddling flippers).
- Axolotl uses its own 9-step pink ramp with wet highlights so it reads glossy, not flat.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 20–25° (small), 15–18° (deep-bodied), 8–12° (long fish / eels).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames (snail and mussel also use walk_).
- File names: `ms_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `ms_<name>.aseprite`
  with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small schooling | European bitterling, rosy bitterling, sunbleak, medaka, topmouth gudgeon, three-spined stickleback, ninespine stickleback, Okefenokee pygmy sunfish, blackbanded sunfish, bluespotted sunfish, banded killifish, northern redbelly dace (all 32x28) |
| Small special | frog tadpole 24x16, crucian carp 38x28 |
| Medium | paradise fish 38x28, rudd 40x28, tench 44x28, golden shiner 38x28, pumpkinseed 36x32, Amur sleeper 40x24, European perch 44x30, grass pickerel 48x22, Asian swamp eel 56x14, black bullhead 44x24 |
| Showpiece | northern pike 64x24, northern snakehead 60x24, European eel 64x16, wels catfish 74x26, mandarin fish 48x34, Chinese softshell turtle 48x28 |
| Crawlers | European weatherfish 40x14, great crested newt 40x16, axolotl 40x20, Chinese fire-bellied newt 36x14, European pond turtle 36x20, noble crayfish 40x20, great pond snail 24x26, European bullhead 34x14, ruffe 36x12, stone loach 42x10 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Surface: medaka (6–90), banded killifish (6–110), sunbleak (8–110), golden shiner, diving beetle, tadpoles.
- Mid water: bitterlings, topmouth gudgeon, redbelly dace, stickleback, rudd, perch, paradise fish, sunfishes,
  pike, grass pickerel, softshell turtle (40–230).
- Lower: ninespine stickleback, pygmy sunfish, mandarin fish (120–230).
- Bottom band: tench, Amur sleeper, snakehead, bullhead, wels (160–252), swamp eel and European eel (210–254).
- Large fish use a bigger `crowd_radius` (60–90 medium, 100–120 showpieces).

## Aquarium (`scenes/aquarium/ms_aquarium.tscn`)
75 creatures: small schoolers 2–4 each, tadpoles 4, medium 1–2, showpieces 1 each, crawlers 1–2 each.

## 2026-10 recolour (style contract pass)
All 40 sheets were recoloured so the fish stop blending into the olive water (fish within ΔE 20 of the background:
70% → 20%). Each species now carries its real display colours with a back → flank → belly tonal gradient and soft
mottling (bitterlings violet / pink, sunbleak blue-silver, stickleback blue with red throat, golden shiner / tench /
eel gold, pike green, snakehead tan with irregular dark blotches, wels brown-grey, crawlers in warm browns), signature
reds / oranges / blues kept. Fins of the fish were enlarged ×1.25–1.3 and enclosed gaps filled. The olive mid-tone cast
of `ms_grade` is no longer used. Scripts: `~/work/audit/recolor.py`, `grad.py`, `finscale.py`, `fillholes.py`.
