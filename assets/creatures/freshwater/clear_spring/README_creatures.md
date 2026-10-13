# Clear Spring – creature style (prefix `cs_`)

Biome look: crystal-clear limestone spring (Florida springs / Bonito, Brazil): turquoise water, strong sun and caustics,
white limestone sand, eel/tape grass meadows. Theme: Florida spring-run fauna (Gulf sturgeon, snook, mullet,
Suwannee bass, redbreast / spotted sunfish, Florida gar, flagfish, molly, killifish, shiners, cave crayfish and
amphipods) + the Bonito / Pantanal clear rivers (piracanjuba, piraputanga, dorado, pacu, pintado, curimbatá, piau, lambari,
Moenkhausia bonita, cichlids, knifefish, cascudo, cascarudo, Pantanal crab). Every animal is fully aquatic. Species
already used elsewhere (bayou sunfishes / gars / bass, blackwater tetras and plecos, planted tank fish) are not repeated.

## Colour grade (`cs_grade`, applied to every finished frame) – the lightest grade of all biomes (clear water)
- Shadows (lum < 0.3) lean toward blue-teal (18, 34, 44), ~25% at black.
- Mid-tones get a faint turquoise cast (90, 170, 170, ~6%); no extra desaturation.
- Highlights move toward bright white (244, 250, 248).
- Translucent fins are tinted aqua (12% toward (150, 200, 200)) and ~6% more transparent.
- EXCEPTION – saturated reds / oranges / yellows (piracanjuba, piraputanga and lambari fins, dorado, redbreast breast, flagfish
  stripes, molly sail edge) and blues (Suwannee bass cheeks, chanchito spangles) are NOT graded.

## Shapes / rendering
- Per-column form shading, outline #0e1a20 with lit top edge #3e6670, soft fins with rays, hand-placed markings.
- Characins (piraputanga, curimbatá, piau, dorado, pacu, tetras) carry an adipose fin; cichlids have a long single
  dorsal and rounded tail; the banded knifefish swims with a rippling ribbon anal fin.
- Piracanjuba (64x26, endangered, endemic to the Paraná–Paraguay basin): silver with golden-olive back and brassy
  flank sheen, dark spot at each scale base, humeral blotch, red-orange fins, orange-edged tail with a black centre.
- Gulf sturgeon: rows of bony scutes, shovel snout with 4 barbels, shark-like tail.
- Turtles reuse the bayou leg rig; the cave crayfish and amphipod are ghost-white and eyeless.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 18–25° (small), 15° (deep-bodied), 6–12° (long fish).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames.
- File names: `cs_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `cs_<name>.aseprite`
  with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small | sailfin molly, Florida flagfish, Seminole killifish, coastal shiner, ironcolor shiner, spotted sunfish, swamp darter, tidewater silverside, yellowtail lambari, Moenkhausia bonita, Buenos Aires tetra, spotted pyrrhulina (all 32x28) |
| Medium | redbreast sunfish 36x32, Suwannee bass 44x28, striped mullet 44x24, Florida gar 56x16, lake chubsucker 40x26, piraputanga 44x28, curimbatá 44x28, three-spot piau 40x22, chanchito 40x30, pike cichlid 48x22, banded knifefish 52x16, banded cichlid 36x28 |
| Showpiece | piracanjuba 64x26, golden dorado 64x26, pacu 56x36, pintado 80x22, common snook 64x24, Gulf sturgeon 80x24 |
| Crawlers | cascudo 44x16, loggerhead musk turtle 32x18, toad-headed turtle 40x20, Florida cave crayfish 40x20, Pantanal crab 32x20, Florida cave amphipod 20x10, rasp elimia 20x20, Florida pondhorn 32x16, cascarudo 36x16, southern flounder 44x14 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Surface: silverside (4–80), molly, pyrrhulina, Seminole killifish, mullet, Florida gar.
- Mid water: shiners, lambari, Moenkhausia, Buenos Aires tetra, piraputanga, piracanjuba (30–190), dorado, pacu, snook.
- Lower: flagfish, sunfishes, Suwannee bass, cichlids, piau (60–245).
- Bottom band: swamp darter, chubsucker, curimbatá, knifefish, pintado, Gulf sturgeon (150–252).
- Large animals use a bigger `crowd_radius` (60–90 medium, 110–140 showpieces).

## Aquarium (`scenes/aquarium/cs_aquarium.tscn`)
75 creatures: small schoolers 2–3 each, medium 1–3, showpieces 1 each, crawlers 1–3 each.
