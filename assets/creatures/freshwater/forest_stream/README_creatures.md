# Forest Stream – creature style (prefix `fs_`)

Biome look: shaded temperate woodland stream, green-tinted clear water, dappled canopy light, mossy boulders, leaf
litter. Theme: Appalachian (eastern North American) forest-stream fauna – the world's richest temperate stream
fauna: darters, dace, shiners, chubs, suckers, stream sunfishes and basses, walleye / sauger, muskellunge, lamprey,
hellbender and mudpuppy, crayfish and stream insects. Every animal is fully aquatic. Trout and other salmonids are left
for rocky_river; species used in bayou / marsh_swamp / clear_spring are not repeated.

## Redesign note
All swimmers and crawlers were redrawn to match the pf_/bw_/ac_ style (see `.agents/rules/pixel_art_guidelines.md` section 0): one muted hue
family per species, flat single-colour markings, large dark masses, per-species fin styles. Aquatic insect nymphs and
the elliptio mussel were replaced (hellgrammite -> northern madtom, stonefly nymph -> tessellated darter, mayfly nymph ->
central mudminnow, water penny -> rusty crayfish, elliptio -> eastern musk turtle). Hellbender and mudpuppy keep their
original drawings, narrowed and recoloured to the shared palette. Generator grade: shadows #1a2a1c, mid cast #7aa05e (~12%),
highlights #eef0d6, fins tinted #8caa6e (~22%), outline tint #121a10.

## Colour grade (legacy description of the original fs_ batch)
- Shadows (lum < 0.3) sink toward deep moss-brown (26, 36, 22).
- Mid-tones get a light moss-green cast (120, 150, 90, ~8%); everything is desaturated ~5%.
- Highlights move toward soft yellow-green white (236, 240, 212).
- Translucent fins are tinted green (14% toward (140, 170, 110)) and ~7% more transparent.
- EXCEPTION – saturated reds / oranges / yellows and blues / blue-greens (darter nuptial colours, dace red bellies,
  warpaint and rosyface heads, longear and studfish, bluehead chub, river redhorse fins, mudpuppy gills) are NOT graded.

## Shapes / rendering
- Per-column form shading, outline = per-pixel dark shade of the adjacent body colour (light tint toward #121a10), lit top edge one step lighter, soft fins with rays, hand-placed markings.
- Darters: blunt head, spiny + soft dorsal, rounded tail and a big pectoral fan for perching on stones.
- Eel-like bodies (lamprey, hellbender, mudpuppy) use `tube_shade`: a 9-tone glossy round-body ramp with a broken wet
  highlight streak along the back and a paler belly; hellbender has lit lateral skin folds, mudpuppy feathery maroon
  external gills, lamprey 7 ringed gill pores and an oral disc.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 20–25° (small), 12–15° (medium), 8–10° (long fish).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames.
- File names: `fs_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `fs_<name>.aseprite`
  with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small | rainbow, greenside, redline, tangerine, fantail darter, blacknose, longnose, southern redbelly, rosyside dace, warpaint, saffron, rosyface shiner (32x28; fantail darter and longnose dace 34x28) |
| Medium | creek chub 48x28, fallfish 52x30, central stoneroller 40x22, bluehead chub 44x24, northern hog sucker 44x24, white sucker 48x24, rock bass 40x30, longear sunfish 38x30, northern studfish 36x22, stonecat 40x18, logperch 44x20, American brook lamprey 52x16 |
| Showpiece | smallmouth bass 56x30, walleye 64x28, sauger 60x26, muskellunge 80x28, river redhorse 56x26, American shad 54x28 |
| Crawlers | hellbender 58x16, mudpuppy 46x16, Appalachian brook crayfish 40x16, rusty crayfish 40x16, mottled sculpin 36x14, northern madtom 34x10, tessellated darter 34x12, central mudminnow 38x12, eastern musk turtle 32x14, silty hornsnail 22x14 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Upper: studfish (10–120), shiners, redbelly / rosyside dace, shad, muskellunge (40–200).
- Mid water: blacknose dace, creek chub, fallfish, bluehead chub, longear sunfish, smallmouth bass.
- Lower: rock bass, walleye, sauger (120–245).
- Bottom band: all darters, longnose dace, stoneroller, suckers, redhorse, stonecat, logperch, lamprey (170–252).
- Large fish use a bigger `crowd_radius` (50–70 medium, 100–140 showpieces).

## Aquarium (`scenes/aquarium/fs_aquarium.tscn`)
71 creatures: small schoolers 2–4 each, medium 1–2, showpieces 1–2, crawlers 1–2 each.
