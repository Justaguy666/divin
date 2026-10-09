# Bayou – creature style (prefix `by_`)

Biome look: Louisiana cypress-tupelo bayou, slow olive "tea" water lit warm gold, soft brown mud over grey clay.
Theme: the classic southern-US swamp fauna (gars, bowfin, catfish, sunfishes, crappie, crawfish, alligator, snapping
turtle). Temperate marsh species (pumpkinseed, golden shiner, black bullhead, grass pickerel, banded killifish,
Okefenokee / blackbanded / bluespotted sunfish, softshell turtle) live in marsh_swamp instead. Every animal in the
roster is fully aquatic.

## Colour grade (`by_grade`, applied to every finished frame)
- Shadows (lum < 0.3) sink toward olive-black (28, 30, 16).
- Mid-tones get an olive-yellow cast (170, 160, 90, ~10%); everything is desaturated ~8%.
- Highlights move toward pale straw (240, 232, 200).
- Translucent fins are tinted olive (15% toward (150, 140, 80)) and ~8% more transparent.
- EXCEPTION – saturated reds / oranges (crawfish, redear ear-flap rim, warmouth eye, bowfin ocellus) and blues
  (bluegill chin, bluefin killifish fins, blue-crab claws) are NOT graded.

## Shapes / rendering
- Per-column form shading, outline #18180c with lit top edge #4a4628, soft fins with rays, hand-placed markings.
- Gars: diamond (ganoid) scale lattice, dorsal + anal set just in front of the tail, tapering snout with a flat lower jaw
  (alligator gar shows a row of fangs).
- Turtles: carapace split into vertebral / costal / marginal scutes with seams and growth rings; legs emerge from under
  the shell rim, bend at the knee and plant flat clawed feet, alternating while walking.
- Eel-shaped animals (amphiuma, siren) undulate along the body; the juvenile alligator swims with its tail.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE × 4 frames; tilt 18–25° (small), 15° (deep-bodied), 6–12° (long fish, alligator).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L × 4 frames.
- File names: `by_<name>_<swim|crawl>_<W>x<H>_4f.png`; every sheet has a matching `by_<name>.aseprite`
  with one tag per row and 0.12 s frames.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small schooling | western mosquitofish, least killifish, golden topminnow, blackstripe topminnow, bluefin killifish, rainwater killifish, taillight shiner, pugnose minnow, bantam sunfish, cypress darter, brook silverside, threadfin shad (all 32x28) |
| Medium | bluegill 36x32, redear sunfish 36x32, warmouth 36x30, flier 36x32, white crappie 40x32, largemouth bass 48x28, pirate perch 36x24, central mudminnow 36x20, channel catfish 52x24, freshwater drum 44x30, spotted gar 56x16, longnose gar 60x14 |
| Showpiece | alligator gar 72x20, bowfin 56x22, paddlefish 72x24, flathead catfish 64x24, bigmouth buffalo 56x30, juvenile American alligator 72x20 |
| Crawlers | red swamp crawfish 40x20, alligator snapping turtle 40x22, common musk turtle 32x18, three-toed amphiuma 56x12, lesser siren 48x14, Mississippi grass shrimp 28x14, giant water bug 36x16, tadpole madtom 32x14, hogchoker 34x12, juvenile blue crab 32x20 (front view, walks sideways) |

## Swim layers (scene `area`, world y: surface 0, ground 264)
- Surface: alligator (0–60), brook silverside (4–80), mosquitofish, topminnows, least killifish.
- Mid water: shiners, shad, bluefin / rainwater killifish, bluegill, flier, crappie, bass, gars (10–220), paddlefish, alligator gar.
- Lower: bantam / redear sunfish, warmouth, drum, bowfin, buffalo (90–245).
- Bottom band: cypress darter, pirate perch, mudminnow, channel and flathead catfish (170–252).
- Large fish use a bigger `crowd_radius` (50–80 medium, 90–140 showpieces).

## Aquarium (`scenes/aquarium/by_aquarium.tscn`)
74 creatures: small schoolers 2–4 each, medium 1–2, showpieces 1 each, crawlers 1–3 each.
