# Underwater Cave – creature style (prefix `uc_`)

Biome look: flooded sea cave, almost black water lit by blue light from the cave mouth, dark ceiling with stalactites,
grey cave sand. Theme: cave- and crevice-dwelling marine fauna of the Mediterranean, Caribbean and anchialine caves –
cardinalfish, cave gobies, brotulas, sweepers, soldierfish / squirrelfish, bigeyes, groupers, conger, nurse and sand tiger
sharks, spiny and slipper lobsters, cave shrimps, moray, octopus. Every animal is fully aquatic.
Sea stars, urchins and anemones are left to props; jellyfish are reserved for a future animal class.

## Colour grade (`uc_grade`, applied to every finished frame)
- Shadows (lum < 0.35) sink toward near-black (10, 14, 18), mid-tones get a faint dark blue-grey cast, highlights are dimmed
  toward (176, 196, 208); light desaturation and an overall ~8% darkening.
- Translucent fins are tinted dark blue (14% toward (40, 60, 80)) with alpha 90 + a·0.55; fin edges get `fin_rim`.
- EXCEPTION – saturated reds / oranges / yellows and blues and the pinks of blind cave fish (cardinalfish, soldierfish,
  squirrelfish, bigeyes, cusk-eel, devilfish lines, yellowtail, shrimps, crabs) are NOT graded.

## Shapes / rendering (shared `cw_lib.finish` / `shade2`, `uc_lib`)
- Same glossy pf_-style rendering as cold water: 11-tone hue-shifted ramp, specular band, wet sheen, belly patches,
  per-pixel tinted outlines.
- Heads: big fish use `HeadFish` (body = plain profile, head with its own upper / lower contour) so the snout, jaws and
  throat are asymmetric and natural – tarpon with upturned jutting lower jaw, groupers with large terminal mouth and
  projecting lower lip, conger / moray with conical head and overhanging upper jaw. Never end a head in a flat or
  symmetric bullet tip.
- Swimmer sheets are built with `safe_sheet`: frames are padded before the SE/NE rotation and cropped symmetrically
  around the centre, so no row is ever clipped by the frame width/height.
- Crawlers use `part()` (shade2 + tinted outline); spider crab is drawn from the front.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 20–22° (small), 12–15° (medium), 6–12° (big / long).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames.
- File names: `uc_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `uc_<name>.aseprite`
  with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small | red cardinalfish, Steinitz's cave goby, Liechtenstein's goby, leopard-spotted goby, black cave brotula, Cuban cave cusk-eel, glassy sweeper, golden sweeper, blackface blenny, Bentuvia's goby, blue devilfish, sawcheek cardinalfish (all 32x28) |
| Medium | Atlantic spadefish 40x44, blackbar soldierfish 40x28, brown meagre 44x26, dwarf lionfish 44x32, forkbeard 46x28, glasseye 40x30, longspine squirrelfish 46x26, painted comber 44x24, pearlfish 56x18, red bigeye 40x28, swallowtail seaperch 44x28, yellowtail snapper 54x30 |
| Showpiece | Atlantic tarpon 84x44, dusky grouper 68x42, European conger 92x30, goliath grouper 76x50, nurse shark 84x38, sand tiger shark 88x38 |
| Crawlers | Caribbean spiny lobster 64x26, slipper lobster 48x18, banded coral shrimp 42x22, Hawaiian red shrimp 20x12, Mediterranean spider crab 46x32, common octopus 50x28, spotted moray 70x18, Madeira rockfish 42x20, trumpet triton 46x30, giant isopod 46x20 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Open cave water (40–200): cardinalfish, sweepers, swallowtail seaperch, yellowtail snapper, spadefish, tarpon, sand tiger.
- Mid / ledges (80–240): soldierfish, squirrelfish, bigeyes, glasseye, meagre, devilfish, lionfish.
- Near the floor (150–255): gobies, blenny, brotula, cusk-eel, forkbeard, comber, pearlfish, groupers, conger, nurse shark.
- Crawlers walk on the sand; feet never cross the floor line (`crawler.gd` `floor_line = 283`).

`scenes/aquarium/uc_aquarium.tscn` holds 73 creatures (59 swimmers, 14 crawlers).
