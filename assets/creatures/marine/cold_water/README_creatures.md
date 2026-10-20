# Cold Water – creature style (prefix `cw_`)

Biome look: cool boreal North Atlantic coast (kelp edge, rocky and sandy bottom), steel-blue water, cold white light.
Theme: North Atlantic / Northeast Pacific-style cold-water fauna – herring, sandeel, gadoids (cod, haddock, pollock, ling),
wrasses and gobies, wolffish, halibut, monkfish, rays and dogfish, lobster, crabs, whelks. Every animal is fully aquatic.
Sea stars, urchins and anemones are left to props; jellyfish are reserved for a future animal class.

## Colour grade (`cw_grade`, applied to every finished frame)
- Shadows (lum < 0.3) sink toward steel blue (18, 30, 42), mid-tones get a faint grey-blue cast, highlights move to cold
  white (236, 244, 250); saturation is NOT reduced, so colours stay as vivid as the pf_ reference.
- Translucent fins are tinted pale steel (10% toward (130, 170, 195)) and keep alpha >= ~190 so rays read clearly.
- Fin edges get a darker, saturated rim (`fin_rim`).
- EXCEPTION – saturated reds / oranges / yellows and blues (cuckoo wrasse, lumpfish belly, gurnard, crabs, lobster,
  squat lobster, sea cucumber feet, shorthorn belly) are NOT graded.

## Shapes / rendering (shared `cw_lib.finish` / `shade2`)
- Glossy form shading: 11-tone ramp with hue shift (shadows cool, lights warm), upper band + specular bump, dark belly with
  a rim/bounce light on the lowest edge, broken 1px wet sheen along the back, forehead highlight, dithered band joins.
- Bellies get soft tonal patches and a warm/cool drift (never one flat colour).
- Outline: every pixel is a dark shade of the neighbouring body colour (lit top edge lighter) – never one fixed colour.
- Bodies are deep and round like the pf_ fish; fins have rays, base→edge gradient and coloured rims.
- Backward swimmers: the cuttlefish frames show the mantle leading and arms/eyes trailing.
- Flat fish (halibut, thornback ray) are drawn in side view, with fin fringes / wing margin attached to the silhouette.
- Crawlers use `part()` (shade2 + tinted outline); crabs are drawn from the front.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 20–25° (small), 12–15° (medium), 8–12° (long / big fish).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames.
- File names: `cw_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `cw_<name>.aseprite`
  with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small | Atlantic herring, lesser sandeel, poor cod, goldsinny wrasse, corkwing wrasse, rock cook wrasse, two-spotted goby, black goby, fifteen-spined stickleback, cunner, radiated shanny, Montagu's sea snail (all 32x28) |
| Medium | Atlantic mackerel 48x24, pollock 48x26, haddock 48x26, ballan wrasse 44x26, cuckoo wrasse 44x24, tautog 40x26, lumpfish 36x32, sea raven 40x28, snake pipefish 52x14, John Dory 40x40, red gurnard 44x26, common cuttlefish 40x28 |
| Showpiece | Atlantic cod 68x36, Atlantic wolffish 64x30, Atlantic halibut 72x40, ling 76x26, spiny dogfish 76x26, thornback ray 72x30 |
| Crawlers | European lobster 60x24, edible crab 48x26, squat lobster 30x16, northern shrimp 30x14, common hermit crab 30x24, common whelk 34x26, orange-footed sea cucumber 44x16, monkfish 56x22, shorthorn sculpin 40x16, rock gunnel 46x12 |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Upper: herring, mackerel, stickleback, dogfish (20–200).
- Mid water: pollock, lumpfish, John Dory, cuttlefish, wrasses, cod.
- Lower / bottom band: haddock, gobies, shanny, sea snail, sandeel, sea raven, gurnard, wolffish, halibut, ray (190–255).
- Large fish use a bigger `crowd_radius` (50–60 medium, 90–120 showpieces).

## Aquarium (`scenes/aquarium/cw_aquarium.tscn`)
71 creatures: small schoolers 2–5 each (herring 5, mackerel 4), medium 1–2, showpieces 1 each, crawlers 1–3 each.
