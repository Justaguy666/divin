# Marsh Swamp - creature style (prefix `ms_`)

Biome look: a still, weedy marsh and swamp - peat-stained water, reeds and lily pads, soft mud. The roster gathers European,
East Asian and North American wetland animals: bitterlings, sticklebacks, small sunfishes, killifish, carp-family fish, perch and
ruffe, pike and pickerel, eels, snakehead and catfish, loaches and bullhead, newts and the axolotl, a frog tadpole, pond turtles,
a pond snail and the noble crayfish.

In October 2026 the creatures were redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier ms sprite,
size, texture or colour was used. Exception, by request: the axolotl, the two newts and the two turtles keep their earlier
drawings, re-mapped onto the marsh ramp below and re-outlined with the BW outline rule, with species colours kept as signatures
(axolotl gills, newt bellies, pond-turtle speckles). The newts and the softshell turtle got a one-pixel eye (golden-brown for the
newts, black for the turtle), the softshell turtle's flippers were shortened, and these kept sheets got a 1 px safety margin.

## Lighting and palette (applied while drawing, not as a post grade)
- Shadows lean to peat olive (#1c2012), midtones take a faint reed-gold cast (#9a985a, about 7%), highlights lean to hazy pale straw (#eeecce).
- The water is dark olive, so bodies lean to silver, brass, straw, grey and warm browns; signature colours are ungraded
  (bitterling teal stripe and rosy flush, stickleback red belly and blue eye, pygmy sunfish blue flecks, blackbanded sunfish
  pelvic edge, redbelly dace belly, paradise fish bands, rudd and perch red fins, pumpkinseed ear spot, newt bellies, crayfish red claws).
- Translucent fins are tinted toward dry-grass (#c4c8a2, about 35%) with alpha falling from about 185 at the base to about 110 at
  the edge; fin rays are darker strokes every second (on big fins every third) pixel, including the leading edge.

## Rendering (matches the BW reference)
- Body value: brightest in the upper third, slightly darker toward the back edge and the ends, stepping darker toward the belly in
  4-5 contour-following bands.
- Outline: a darker shade of the colour just inside each edge pixel, tinted toward #141a0e; lit top edge, darker sides, darkest
  belly edge with the row above it pulled down. Stair-corner nubs are removed.
- Markings are flat colours or a fixed number of body tones darker; fish eyes are a warm highlight over a dark pupil with iris
  pixels behind and a dark socket below.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 25 deg (small), 15-20 deg (deep), 8-14 deg (long).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (the snail uses crawl_R, crawl_L, idle_R, idle_L); the rest pose touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `ms_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a
  matching `ms_<name>.aseprite` (one layer, one tag per row, 0.12 s frames).

## Roster (40 species: 31 swimmers, 9 crawlers)
The frog tadpole and the softshell turtle (kept swimming drawing) are swimmers; loaches, bullhead, axolotl, newts, the pond
turtle, the pond snail and the crayfish walk on the floor.

| Group | Species (frame) |
|---|---|
| Small swimmers | european bitterling 36x24, rosy bitterling 36x24, sunbleak 36x24, medaka 32x22, topmouth gudgeon 36x24, three spined stickleback 34x22, ninespine stickleback 32x22, okefenokee pygmy sunfish 28x20, blackbanded sunfish 32x26, bluespotted sunfish 32x26, banded killifish 36x24, northern redbelly dace 34x24, golden shiner 44x26, paradise fish 42x26, frog tadpole 30x20 |
| Medium and large swimmers | crucian carp 48x30, rudd 46x28, tench 54x30, european perch 48x28, ruffe 38x24, pumpkinseed 42x30, amur sleeper 40x26, mandarin fish 56x34, black bullhead 52x26, grass pickerel 52x22, asian swamp eel 58x16, european eel 64x20, northern snakehead 64x24, northern pike 80x28, wels catfish 96x30 |
| Bottom fish, amphibians, turtles, snail, crayfish | stone loach 38x14, european weatherfish 52x12, european bullhead 36x16, axolotl 40x20, chinese fire bellied newt 38x14, great crested newt 40x16, chinese softshell turtle 50x30, european pond turtle 36x20, great pond snail 26x20, noble crayfish 52x14 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining features |
|---|---|---|---|
| european bitterling | swim 36x24 | y 60-220, speed 20 | Rhodeus amarus: small deep-bodied, silvery with a blue-green iridescent stripe on the rear half of the body, red upper iris, breeding males with a pink-red throat and belly |
| rosy bitterling | swim 36x24 | y 60-220, speed 20 | Rhodeus ocellatus: deep compressed, breeding male flushed rosy pink-violet with a green-blue sheen stripe toward the tail, red-orange fins edged dark |
| sunbleak | swim 36x24 | y 0-110, speed 30 | Leucaspius delineatus: slender little silverfish, bright silver lateral band, olive back, upturned mouth, translucent fins |
| medaka | swim 32x22 | y 0-90, speed 22 | Oryzias latipes (wild type): tiny, flat back and upturned mouth, big eye, translucent olive-tan with dark scale edges, a long anal fin and a small dorsal set far back, truncate tail |
| topmouth gudgeon | swim 36x24 | y 80-230, speed 24 | Pseudorasbora parva: small upturned mouth, silvery-olive with a dark stripe along the side and dark crescents on the back scales |
| three spined stickleback | swim 34x22 | y 60-230, speed 20 | Gasterosteus aculeatus (breeding male): three free spines in front of the dorsal, bony side plates, slender keeled tail stalk, red throat and belly, blue eye, green-grey back, strong pelvic spine |
| ninespine stickleback | swim 32x22 | y 100-240, speed 18 | Pungitius pungitius: slender, a row of nine small spines along the back, olive-brown mottled with dark bars, narrow tail stalk |
| okefenokee pygmy sunfish | swim 28x20 | y 150-250, speed 10 | Elassoma okefenokee (male): tiny and dark, near-black body with iridescent blue-green flecks and faint bars, rounded fins edged in blue |
| blackbanded sunfish | swim 32x26 | y 100-230, speed 14 | Enneacanthus chaetodon: deep disc, silver-cream with six bold black vertical bands (the first through the eye), a red-orange front edge on the pelvic fins, rounded tail |
| bluespotted sunfish | swim 32x26 | y 110-240, speed 14 | Enneacanthus gloriosus: deep, dark olive-brown sprinkled with rows of shining blue spots, a dark ear spot, rounded tail |
| banded killifish | swim 36x24 | y 4-120, speed 22 | Fundulus diaphanus: slender killifish with a flat head, olive-tan with 12-20 thin dark vertical bars, pale belly, dorsal set far back over the anal |
| northern redbelly dace | swim 34x24 | y 40-200, speed 26 | Chrosomus eos: small dace with two dark side stripes (the upper one breaking into spots toward the tail), red belly in males, olive back with dark speckles, yellowish fins |
| golden shiner | swim 44x26 | y 30-190, speed 26 | Notemigonus crysoleucas: deep compressed shiner, brassy-gold sides, olive back, a lateral line that dips low, small upturned mouth, orange-tinted fins in spring |
| paradise fish | swim 42x26 | y 0-150, speed 16 | Macropodus opercularis: alternating blue and red-orange vertical bands, a blue-black gill spot ringed orange, long flowing dorsal and anal fins, deeply forked tail with trailing filaments, thread-like pelvic fins |
| frog tadpole | swim 30x20 | y 120-256, speed 12 | frog tadpole: round body flowing into a long muscular tail with fin folds above and below, olive-brown with dark speckles, eyes set on the sides of the head, no paired fins |
| crucian carp | swim 48x30 | y 120-250, speed 14 | Carassius carassius: deep, high-arched back, bronze-gold to olive, long convex dorsal fin, rounded fins, slightly forked tail, no barbels |
| rudd | swim 46x28 | y 20-180, speed 22 | Scardinius erythrophthalmus: deep, compressed, brassy-gold sides, bright red pelvic, anal and tail fins, red-orange eye, dorsal set behind the pelvics, upturned mouth |
| tench | swim 54x30 | y 170-256, speed 12 | Tinca tinca: thick olive-green-gold body with tiny scales (smooth look), small red eye, rounded fins, a short barbel at each corner of the mouth, thick tail stalk, gently convex tail |
| european perch | swim 48x28 | y 60-220, speed 20 | Perca fluviatilis: humped back, green-olive with five to seven dark vertical bars, black spot at the rear of the first dorsal, red-orange pelvic, anal and lower tail fins |
| ruffe | swim 38x24 | y 190-256, speed 14 | Gymnocephalus cernua: small perch-like with a big head of mucus pits, olive-brown mottled with dark spots, joined spiny and soft dorsal with rows of black spots, purplish eye |
| pumpkinseed | swim 42x30 | y 70-220, speed 16 | Lepomis gibbosus: deep sunfish, black ear flap tipped with an orange-red spot, orange spots on olive-green sides, wavy blue lines on the cheek, orange-yellow belly |
| amur sleeper | swim 40x26 | y 170-256, speed 12 | Perccottus glenii: chunky sleeper with a big head and wide mouth, dark olive-brown mottled with darker blotches, two rounded dorsals, rounded tail, pale-edged fins dotted with dark spots |
| mandarin fish | swim 56x34 | y 140-250, speed 14 | Siniperca chuatsi: deep compressed ambush predator with a huge mouth, yellow-olive leopard-patterned with irregular dark blotches, a black stripe from the snout through the eye to the dorsal base, long spiny dorsal |
| black bullhead | swim 52x26 | y 196-258, speed 14 | Ameiurus melas: stout catfish, dark olive-black back, yellowish belly, dark chin barbels, square tail with a pale bar at its base, adipose fin |
| grass pickerel | swim 52x22 | y 20-180, speed 14 | Esox americanus vermiculatus: small pike with a duckbill snout, olive-brown with wavy dark vertical bars, a dark teardrop bar under the eye, dorsal and anal set far back |
| asian swamp eel | swim 58x16 | y 210-258, speed 10 | Monopterus albus: slick eel with no pectoral or pelvic fins, fins reduced to a low fold around the pointed tail, olive-brown finely speckled dark, yellowish belly, small eye, blunt snout |
| european eel | swim 64x20 | y 190-258, speed 12 | Anguilla anguilla (yellow eel): long snake-like body, small pectoral fins, one continuous fin running from mid-back round the tail to the belly, dark olive-brown back, yellow-cream belly |
| northern snakehead | swim 64x24 | y 40-220, speed 14 | Channa argus: long cylindrical body with a snake-like head, long dorsal and anal fins, tan-brown with big dark irregular blotches in two rows (python pattern), rounded tail |
| northern pike | swim 80x28 | y 20-200, speed 16 | Esox lucius: long olive-green predator, rows of pale bean-shaped spots, duckbill snout full of teeth, dorsal and anal set far back, fins blotched dark, forked tail |
| wels catfish | swim 96x30 | y 200-256, speed 12 | Silurus glanis: huge scaleless catfish, broad flat head, two very long whiskers plus four short chin barbels, tiny dorsal, very long anal fin reaching the tail, dark olive-black marbled back, pale mottled belly |
| stone loach | crawl 38x14 | floor, speed 8 | Barbatula barbatula: slender round-bodied loach, olive-yellow with brown blotches and saddles, six short barbels round the mouth, small eyes high on the head, rounded-truncate tail |
| european weatherfish | crawl 52x12 | floor, speed 8 | Misgurnus fossilis: long eel-like loach, dark brown with alternating yellowish and dark longitudinal stripes, ten barbels round the small mouth, rounded tail |
| european bullhead | crawl 36x16 | floor, speed 6 | Cottus gobio: flat broad head, big fan pectorals, body tapering to the tail, brown mottled with dark bands, two dorsal fins, eyes on top of the head |
| axolotl | crawl 40x20 | floor, speed 5 | existing axolotl drawing (leucistic pink) re-mapped onto the marsh ramp; the feathery gills stay a pink-red signature |
| chinese fire bellied newt | crawl 38x14 | floor, speed 6 | existing drawing re-mapped: dark olive-black back on the marsh ramp, the fire-orange belly kept as a signature |
| great crested newt | crawl 40x16 | floor, speed 6 | existing drawing re-mapped: dark brown warty skin on the marsh ramp, orange-yellow belly kept as a signature |
| chinese softshell turtle | swim 50x30 | y 150-256, speed 12 | existing swimming softshell drawing (six direction rows) re-mapped onto the marsh ramp, olive-grey leathery shell |
| european pond turtle | crawl 36x20 | floor, speed 6 | existing drawing re-mapped: dark brown-black shell and skin on the marsh ramp, the yellow speckles kept as a signature |
| great pond snail | crawl 26x20 | floor, speed 2 | Lymnaea stagnalis: thin horn-brown shell with a huge rounded body whorl and a tall sharp spire, a big ear-shaped aperture, grey-olive foot and flat triangular tentacles; the shell stays fixed while the foot glides |
| noble crayfish | crawl 52x14 | floor, speed 10 | Astacus astacus: big dark brown-olive crayfish with rough granular claws whose undersides and joints are red, a long rostrum |

## Scenes
`scenes/creatures/freshwater/marsh_swamp/ms_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/ms_aquarium.tscn`.
