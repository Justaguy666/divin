# Blackwater – creature style (prefix `bw_`)

Biome look: tannin "tea" water, dim amber light from above, dark humus floor. Every creature follows these rules so the set reads as one biome.

## Colour grade (applied to every finished frame)
- Shadows sink toward warm brown (#2a1408), never navy/black-blue.
- Mid-tones get a light amber cast (#be7c3c, ~12%) and are slightly desaturated.
- Highlights are warm gold (#ffe2a0), never pure white.
- Translucent fins are tinted amber and a bit more transparent than in planted_freshwater.
- EXCEPTION – signature iridescence (cardinal blue line, discus turquoise lines, apisto cheek spangles)
  is NOT graded: it must glow against the dark water.

## Shapes / rendering (same base as planted_freshwater)
- Form shading: light from above, rounded per column, 1–2 highlight pixels on back/forehead.
- Outline: warm near-black #1a0e0a; lit top edge #5a3420.
- Soft fins with rays and gradient; hand-placed markings (no repeating noise).
- Eyes: dark pupil + warm highlight + coloured ring (red for discus/altum).

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 25° (small) / 12–20° (deep-bodied).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames (snails: crawl_R/L).
- Sizes: see the roster below (frame size is also in every file name: `bw_<name>_<swim|crawl>_<W>x<H>_4f.png`).
- Every sheet has a matching `bw_<name>.aseprite` with one tag per row and 0.12 s frames.


## Roster (40 species: 30 swimmers, 10 crawlers)
Theme: Amazon / Rio Negro flooded forest. No species overlap with planted_freshwater.

| Group | Species (frame) |
|---|---|
| Small schooling | cardinal tetra, green neon tetra, black phantom tetra, red phantom tetra, black neon tetra, bleeding heart tetra, penguin tetra, diamond tetra, glass bloodfin, ruby tetra (all 32x28), pygmy cory (32x28, hovers mid-water), marbled hatchetfish 32x28, pencilfish 32x28 |
| Dwarf cichlids / medium | apistogramma 32x28, checkerboard cichlid 40x30, festivum 40x40, eartheater 44x32, dwarf pike cichlid 48x24, spotted headstander 36x28 (head-down pose baked into the sheet), hemiodus 40x20, banded leporinus 48x22, silver dollar 40x40, freshwater needlefish 48x14 (surface) |
| Large / showpiece | discus 44x44, altum angelfish 44x52, uaru 48x44, severum 44x40, leaf fish 36x28 (drifts, speed 5), black ghost knifefish 56x16 (ribbon-fin wave), silver arowana 64x24 (surface band only) |
| Crawlers | sterbai cory 32x18, bumblebee catfish 32x18, banjo catfish 40x14, clown pleco 40x18, spotted raphael 36x18, farlowella 44x12, freshwater stingray 56x16, amazon crab 32x20 (front view, walks sideways), apple snail 32x24, wood shrimp 32x16 |

## Swim layers (scene `area`)
- Surface: arowana (y 0–90), needlefish (y 0–50), glass bloodfin, penguin tetra, hatchetfish.
- Mid water: tetras, festivum, silver dollar, hemiodus, uaru, severum.
- Lower: pygmy cory, leporinus, leaf fish, headstander, checkerboard, eartheater, pike cichlid, knifefish (y 220–320).
- Large fish use a bigger `crowd_radius` (uaru/severum 80, knifefish 90, arowana 110).
