# Billabong – creature style (prefix `bb_`)

Biome look: Australian tropical billabong (oxbow waterhole), clear teal water over red-ochre sandy clay, paperbark and
pandanus roots, giant blue waterlilies. Theme: the northern-Australian freshwater fauna (rainbowfish, blue-eyes,
gudgeons, grunters, archerfish, barramundi, saratoga, sawfish, whipray, lungfish, tandans, redclaw, cherabin,
side-necked and pig-nosed turtles, file snake). Every animal in the roster is fully aquatic. The planted-tank
rainbowfish (Boeseman's, neon dwarf, threadfin) stay in planted_freshwater.

## Colour grade (`bb_grade`, applied to every finished frame)
- Shadows (lum < 0.3) sink toward teal-brown (26, 36, 32) ≈ #1a2420.
- Mid-tones get a teal cast (96, 150, 140, ~10%); everything is desaturated ~8%.
- Highlights move toward sandy white (236, 228, 206).
- Translucent fins are tinted teal (15% toward (120, 164, 152)) and ~8% more transparent.
- EXCEPTION – saturated reds / oranges / yellows (rainbowfish fins and scale rows, gudgeon fin bands, barramundi eye,
  saratoga scale spots, redclaw claw patch) and blues / greens (rainbowfish iridescence, blue-eye rings, tarpon back)
  are NOT graded.

## Shapes / rendering
- Per-column form shading, outline = per-pixel dark shade of the adjacent body colour (light tint toward #141e1c), lit top edge one step lighter, soft fins with rays, hand-placed markings.
- Rainbowfish: arched back, small first dorsal, long second dorsal + anal reaching the tail; blue-eyes have a bright
  blue eye ring and long striped / spotted male fins.
- Eel-tailed catfish (tandan, Rendahl's) and the lungfish have a continuous fringe fin round a pointed tail.
- Freshwater whipray is drawn as a disc seen obliquely from above (a true side view is only a thin line), its wing
  margins rippling front to back.
- Turtles reuse the bayou leg rig (legs emerge under the shell rim, bend, plant flat clawed feet); the pig-nosed
  turtle has leathery scute-less skin and paddle flippers instead.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 18–25° (small), 15° (deep-bodied), 6–12° (long fish, ray).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames.
- File names: `bb_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `bb_<name>.aseprite`
  with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small | checkered, western, exquisite, black-banded rainbowfish, delicate / Pacific / spotted blue-eye, sailfin glassfish, empire gudgeon, purple-spotted gudgeon, Midgley's carp gudgeon, fly-specked hardyhead (all 32x28) |
| Medium | spangled perch 40x30, banded grunter 40x30, sooty grunter 44x32, seven-spot archerfish 44x30, primitive archerfish 40x28, mouth almighty 40x30, bony bream 40x30, Hyrtl's tandan 48x22, Rendahl's catfish 40x20, salmon-tailed catfish 52x24, freshwater longtom 60x14, snub-nosed garfish 44x14 |
| Showpiece | barramundi 64x28, northern saratoga 64x22, freshwater sawfish 80x24, freshwater whipray 64x24, oxeye tarpon 56x26, Australian lungfish 72x22 |
| Crawlers | redclaw crayfish 44x20, cherabin 52x16, glass shrimp 24x12, Notopala river snail 24x20, Velesunio mussel 32x16, water scorpion 40x12, northern snake-necked turtle 48x20, pig-nosed turtle 44x22, northern snapping turtle 40x22, Arafura file snake 64x12 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Surface: archerfish (0–80), saratoga (0–90), longtom, garfish, blue-eyes, hardyhead.
- Mid water: rainbowfish, glassfish, spangled perch, bony bream, tarpon, barramundi (80–230).
- Lower: banded / sooty grunter, empire / Midgley's gudgeons, mouth almighty (60–245).
- Bottom band: purple-spotted gudgeon, tandans, salmon-tailed catfish, sawfish, lungfish, whipray (180–256).
- Large fish use a bigger `crowd_radius` (50–80 medium, 100–140 showpieces).

## Aquarium (`scenes/aquarium/bb_aquarium.tscn`)
74 creatures: small schoolers 2–4 each, medium 1–3, showpieces 1 each, crawlers 1–3 each.
