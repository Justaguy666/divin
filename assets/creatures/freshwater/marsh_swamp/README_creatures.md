# Marsh / swamp – creature style (prefix `ms_`)

Biome look: still, dark-green swamp water under a canopy, duckweed and lilies at the surface, black muck and peat
below. Theme: temperate marshes, fens and bogs of the Northern Hemisphere (European reed swamps, East-Asian rice-paddy
marshes, Atlantic peat bogs). The big southern-US icons (gars, bowfin, channel catfish, crappie, mudminnows,
red swamp crawfish) are left for the bayou biome.

## Colour grade (`ms_grade`, applied to every finished frame)
- Shadows (lum < 0.3) sink toward dark moss (26, 32, 20).
- Mid-tones get an olive cast (140, 150, 90, ~10%); everything is desaturated ~8%.
- Highlights move toward pale green-grey (226, 234, 214).
- Translucent fins are tinted green-brown (15% toward (150, 150, 100)) and ~8% more transparent.
- EXCEPTION – saturated reds / oranges (stickleback throat, redbelly dace, rudd fins, newt bellies, pumpkinseed,
  axolotl pinks) and iridescent blues (sunbleak stripe, pygmy / bluespotted sunfish spangles) are NOT graded.

## Shapes / rendering
- Same base as the other freshwater biomes: per-column form shading, outline #141a10 with lit top edge #3e4a30,
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
| Small special | frog tadpole 24x16, great diving beetle 32x20 |
| Medium | paradise fish 36x28, rudd 40x28, tench 44x28, golden shiner 36x28, pumpkinseed 36x32, Amur sleeper 40x24, European perch 44x30, grass pickerel 48x20, Asian swamp eel 56x14, black bullhead 44x24 |
| Showpiece | northern pike 64x24, northern snakehead 60x24, European eel 64x16, wels catfish 72x24, mandarin fish 48x30, Chinese softshell turtle 48x28 |
| Crawlers | European weatherfish 40x14, great crested newt 40x16, axolotl 40x20, Chinese fire-bellied newt 36x14, European pond turtle 36x20, noble crayfish 40x20, great pond snail 24x26, swan mussel 32x16, dragonfly nymph 36x14, caddisfly larva 28x12 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Surface: medaka (6–90), banded killifish (6–110), sunbleak (8–110), golden shiner, diving beetle, tadpoles.
- Mid water: bitterlings, topmouth gudgeon, redbelly dace, stickleback, rudd, perch, paradise fish, sunfishes,
  pike, grass pickerel, softshell turtle (40–230).
- Lower: ninespine stickleback, pygmy sunfish, mandarin fish (120–230).
- Bottom band: tench, Amur sleeper, snakehead, bullhead, wels (160–252), swamp eel and European eel (210–254).
- Large fish use a bigger `crowd_radius` (60–90 medium, 100–120 showpieces).

## Aquarium (`scenes/aquarium/ms_aquarium.tscn`)
75 creatures: small schoolers 2–4 each, tadpoles 4, medium 1–2, showpieces 1 each, crawlers 1–2 each.
