# Ancient cold lake – creature style (prefix `ac_`)

Biome look: very old, deep, crystal-clear cold lakes (Baikal, Biwa, Ohrid, Khövsgöl, Sevan, Frolikha). Blue-grey light, pale stony floor. Every creature follows these rules so the set reads as one biome.

## Colour grade (`ac_grade`, applied to every finished frame)
- Shadows (lum < 0.3) sink toward cold blue-grey (26, 38, 48).
- Mid-tones get a light icy cast (150, 190, 210, ~10%); everything is desaturated ~8%.
- Highlights move toward silver-white (236, 246, 252).
- Translucent fins are glassy pale blue (15% toward (180, 215, 235)) and ~12% more transparent.
- EXCEPTION – saturated warm signature colours (red / orange / yellow: char belly, taimen tail, koayu gill spot, yellowfin sculpin pectorals, Ohrid roach eye, trout spots) are NOT graded.

## Shapes / rendering (same base as planted_freshwater / blackwater)
- Form shading: light from above, rounded per column; outline #0e1820 with lit top edge #3a5060.
- Salmonids: adipose fin, gill-cover arc, fork tail; graylings use a long "flag" dorsal with a coloured fringe and rows of spots.
- Golomyankas and the deep-water sculpin are translucent (body alpha 165–215, backbone / gut visible).
- Markings are hand-placed rows (spots, scutes, blotches), not repeating noise.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 20–25° (small), 15–18° (deep-bodied / grayling sail), 8–12° (long showpieces).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames (snails also use walk_).
- File names: `ac_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `ac_<name>.aseprite` with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small schooling | Siberian dace, Ohrid spirlin, Ohrid roach, honmoroko, isaza goby, koayu, small golomyanka, Biwa higai (all 32x28) |
| Salmonids / whitefish | omul 40x28, Baikal whitefish 40x28, black grayling 42x32, white grayling 42x32, Khövsgöl grayling 42x32, lenok 44x28, Frolikha char 42x28, Ohrid belvica 36x28 |
| Sculpins / carp / bottom fish | yellowfin sculpin 36x28, longfin sculpin 36x28, nigorobuna 40x34, gengoro-buna 40x34, Ohrid trout 44x28, Biwa rock catfish 44x24, burbot 48x22, Sevan khramulya 40x28 |
| Showpiece | big golomyanka 44x24, Baikal sturgeon 72x24, taimen 64x24, Biwa trout 52x24, Biwa giant catfish 64x24, Sevan trout 52x24 |
| Crawlers | giant spiny amphipod 40x22, blue Baikal amphipod 24x14, stone sculpin 32x16, fat sculpin 34x18, deep-water sculpin 32x16, Benedictia snail 26x20, Baicalia snail 22x22, Baikal giant flatworm 40x10, Ohrid spined loach 34x12, Biwa yoshinobori 28x14 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Upper: koayu (10–130), graylings (10–160), Biwa trout (20–170), dace, spirlin, honmoroko, belvica.
- Mid water: omul, lenok, taimen, Ohrid / Sevan trout (30–200), Ohrid roach, yellowfin sculpin.
- Deep / lower: isaza goby, small golomyanka, longfin sculpin, whitefish, char, crucians, higai, khramulya (80–236), big golomyanka (140–250).
- Bottom band: Biwa rock catfish (190–250), burbot (200–252), Biwa giant catfish (205–252), Baikal sturgeon (215–252).
- Large fish use a bigger `crowd_radius` (60–80 medium, 90–120 showpieces).

## Aquarium (`scenes/aquarium/ac_aquarium.tscn`)
71 creatures: small schoolers 2–4 each, salmonids 1–3, showpieces 1 each, crawlers 1–3 each.
