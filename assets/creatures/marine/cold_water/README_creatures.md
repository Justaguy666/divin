# Cold Water - creature style (prefix `cw_`)

Biome look: a steel-blue northern sea over cold rock, kelp and gravel. The roster is the north-east Atlantic shore and shelf fauna:
gobies, sticklebacks, pipefish, sandeel and herring, the cod family (cod, haddock, pollack, poor cod, ling), mackerel, john dory,
five wrasses plus cunner and tautog, lumpfish, spiny dogfish, wolffish and the common cuttlefish; on the floor gurnard, monkfish,
halibut, thornback ray, sculpins, a snailfish, a goby and a shanny, and the hermit crab, whelk, edible crab, European lobster,
northern shrimp, squat lobster and orange-footed sea cucumber.

In October 2026 every creature was redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier cw sprite,
size, texture or colour was used. Montagu's sea snail is a snailfish (Liparis montagui) and is drawn as a fish.

## Lighting and palette (applied while drawing, not as a post grade)
- Shadows lean to deep steel navy (#101c26), midtones take a faint cold blue cast (#4a7690, about 7%), highlights lean to cold
  pale white (#eaf0ee).
- The water is a deep steel blue, so bodies lean to olive, bronze, brown, red and grey; signature colours are ungraded (red gurnard,
  cuckoo wrasse orange and electric blue, two-spotted goby blue fin spots, herring and mackerel back blues, rock cook head lines,
  lobster flecks, northern shrimp pink-red, squat lobster red and blue, sea cucumber orange tentacles, hermit crab orange).
- Translucent fins are tinted toward pale sea-grey (#b4c8d0, about 35%) with alpha falling from about 185 at the base to about 110
  at the edge; fin rays are darker strokes every second pixel, including the leading edge. Pelvic fins hang below the belly.

## Rendering (matches the BW reference)
- Body value: brightest in the upper third, slightly darker toward the back edge and the ends, stepping darker toward the belly in
  4-5 contour-following bands.
- Outline: a darker shade of the colour just inside each edge pixel, tinted toward #0a141c; lit top edge, darker sides, darkest
  belly edge with the row above it pulled down. Stair-corner nubs are removed.
- Markings are flat colours or a fixed number of body tones darker; fish eyes are a warm highlight over a dark pupil with iris
  pixels behind and a dark socket below.
- Special cases: spines, finlets and teeth (stickleback, mackerel, dogfish, wolffish) are 1 px pegs standing just outside the body
  edge; the cuttlefish is a fish-style body with a rippling fin skirt and an arm bundle; the red gurnard walks on three free
  pectoral rays; the monkfish has no mouth line (by request) and its jaw flaps rest still on the sand; the thornback ray is a
  part-built rhomboid disc seen slightly from above with a thorny tail; flatfish are drawn eyed side up with nearly flat shading;
  the European lobster is the crayfish rig enlarged 1.35x; crabs are seen from the front walking sideways; the whelk and the
  sea cucumber use crawl_ rows; detached specks under 6 px left by tilt or ripple are removed.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 16-22 deg (small), 12-18 deg (deep-bodied), 6-11 deg (long fish).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (whelk and sea cucumber: crawl_R, crawl_L, idle_R, idle_L); every frame
  touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `cw_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a
  matching `cw_<name>.aseprite` (one layer, one tag per row, 0.12 s frames) and its Godot `.import` file.

## Roster (40 species: 24 swimmers, 16 crawlers)

| Group | Species (frame) |
|---|---|
| Small swimmers | two spotted goby 30x20, fifteen spined stickleback 44x16, snake pipefish 64x16, lesser sandeel 42x18, atlantic herring 48x24, poor cod 36x22, goldsinny wrasse 34x22, rock cook wrasse 34x22, corkwing wrasse 36x22, cuckoo wrasse 44x24, cunner 38x24, rock gunnel 48x18 |
| Medium and large swimmers, cuttlefish | atlantic cod 74x32, haddock 68x32, pollock 70x30, ling 90x26, atlantic mackerel 58x24, john dory 48x44, ballan wrasse 58x30, tautog 56x30, lumpfish 40x32, spiny dogfish 86x26, atlantic wolffish 86x30, common cuttlefish 46x30 |
| Bottom fishes (crawl) | red gurnard 46x20, monkfish 66x26, atlantic halibut 70x34, thornback ray 60x12, sea raven 46x22, shorthorn sculpin 40x20, montagus sea snail 32x14, black goby 34x16, radiated shanny 40x14 |
| Crabs, lobsters, shrimp, whelk, sea cucumber (crawl) | common hermit crab 30x18, common whelk 28x18, edible crab 36x16, european lobster 68x20, northern shrimp 48x16, squat lobster 38x14, orange footed sea cucumber 36x12 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining features |
|---|---|---|---|
| two spotted goby | swim 30x20 | y 60-220, speed 16 | Gobiusculus flavescens: small hovering goby, reddish-brown back with pale saddles, pale belly, a round dark spot at the tail base, males with a second blue-black spot on the flank behind the pectoral and blue-spotted fins, two dorsals |
| fifteen spined stickleback | swim 44x16 | y 100-240, speed 12 | Spinachia spinachia: very long and thin, a pointed tube-like snout, a row of about fifteen small free spines along the back, olive-brown to green with a pale belly, a long slender tail stalk, small dorsal and anal set far back opposite each other |
| snake pipefish | swim 64x16 | y 80-230, speed 8 | Entelurus aequoreus: very long, thin, snake-like pipefish, yellow-brown crossed by many narrow pale blue-edged rings, a tube snout, a small dorsal near the middle, the tail tapering almost to a thread with a tiny tail fin |
| lesser sandeel | swim 42x18 | y 20-200, speed 30 | Ammodytes tobianus: slender, eel-like silver fish with a sharply pointed head and jutting lower jaw, green-blue back, bright silver sides, a long low dorsal running along most of the back, a long anal, small forked tail |
| atlantic herring | swim 48x24 | y 0-140, speed 32 | Clupea harengus: streamlined silver fish with a blue-green back, bright silver sides and a sharp keeled belly, one dorsal fin in the middle of the back, deeply forked tail, big eye, slightly jutting lower jaw |
| poor cod | swim 36x22 | y 120-245, speed 18 | Trisopterus minutus: small cod, coppery-bronze back fading to silvery sides and belly, a small dark spot at the base of the pectoral, three dorsals and two anals, a chin barbel, big eye |
| goldsinny wrasse | swim 34x22 | y 140-250, speed 16 | Ctenolabrus rupestris: small slender wrasse, golden-brown to reddish, a black spot on the top of the tail base and another at the front of the dorsal fin, pale belly, pointed snout |
| rock cook wrasse | swim 34x22 | y 140-250, speed 16 | Centrolabrus exoletus: small stocky wrasse, greenish-brown with a bluish sheen, rows of reddish dots, a broad dark band across the middle of the tail fin, males with blue lines on the head |
| corkwing wrasse | swim 36x22 | y 130-250, speed 16 | Symphodus melops: deep-bodied wrasse, mottled greenish-brown with darker bars, a dark spot in the middle of the tail base and a dark comma behind the eye, males with wavy blue-green lines over the head and gill cover |
| cuckoo wrasse | swim 44x24 | y 100-240, speed 18 | Labrus mixtus (male): long wrasse, bright orange body with an electric-blue head and blue stripes running back along the upper side, blue-edged orange fins |
| cunner | swim 38x24 | y 130-250, speed 14 | Tautogolabrus adspersus: stout wrasse, olive-brown to reddish mottled with darker blotches, pointed snout with thick lips, a long spiny-soft dorsal, rounded tail, pale-blotched fins |
| rock gunnel | swim 48x18 | y 210-258, speed 10 | Pholis gunnellus (butterfish): compressed eel-like fish, yellow-brown mottled darker, a row of about a dozen black spots ringed pale along the base of the long dorsal fin, a dark bar slanting down through the eye, tiny pelvic fins, rounded tail |
| atlantic cod | swim 74x32 | y 120-250, speed 18 | Gadus morhua: heavy cod, olive-brown to greenish back and sides densely leopard-spotted, a pale lateral line arching over the pectoral, white belly, three dorsals and two anals, a long chin barbel, square tail |
| haddock | swim 68x32 | y 140-250, speed 18 | Melanogrammus aeglefinus: dark purple-grey back, silver sides, a black lateral line, a dark blotch above the pectoral (the devil's thumbprint), a tall pointed first dorsal, slightly forked tail, small chin barbel |
| pollock | swim 70x30 | y 40-200, speed 24 | Pollachius pollachius (pollack): streamlined cod with a projecting lower jaw and no barbel, golden-olive to bronze back, silvery sides, a dark lateral line curving up over the pectoral, three dorsals and two anals, slightly forked tail |
| ling | swim 90x26 | y 190-256, speed 12 | Molva molva: long, eel-like cod, mottled brown and olive, a long second dorsal and anal both edged white, a dark spot at the rear of the first dorsal, a chin barbel, rounded tail |
| atlantic mackerel | swim 58x24 | y 0-140, speed 34 | Scomber scombrus: torpedo-shaped, iridescent blue-green back with bold dark wavy tiger bars, silver-white belly, two small dorsals set far apart, a row of little finlets before the deeply forked tail |
| john dory | swim 48x44 | y 60-220, speed 10 | Zeus faber: very deep, thin, oval body, olive-grey to golden with wavy lines, a big black eyespot ringed pale yellow in the middle of the flank, long spiny dorsal rays trailing filaments, a huge upturned protrusible mouth, spiny bony plates along the dorsal and anal bases |
| ballan wrasse | swim 58x30 | y 120-245, speed 14 | Labrus bergylta: big, thick-lipped wrasse, green-brown to reddish-brown, every scale with a pale centre so the flank is covered in pale spots, mottled darker, long spiny-soft dorsal, rounded tail |
| tautog | swim 56x30 | y 140-250, speed 14 | Tautoga onitis (blackfish): stout wrasse with a steep rounded forehead and thick lips, dark grey-black to olive with darker blotches, a pale chin, long spiny-soft dorsal, rounded tail |
| lumpfish | swim 40x32 | y 100-240, speed 8 | Cyclopterus lumpus: globular, almost round fish with three rows of bony knobs along each side, a skin-covered hump instead of a first dorsal, a small soft second dorsal and anal near the tail, blue-grey to green, sucker disc underneath |
| spiny dogfish | swim 86x26 | y 80-240, speed 20 | Squalus acanthias: slender little shark, slate grey with rows of small white spots along the flanks, pale belly, a sharp spine in front of each of the two dorsal fins, no anal fin, pointed snout, big green eye, tail with a longer upper lobe |
| atlantic wolffish | swim 86x30 | y 200-258, speed 10 | Anarhichas lupus: long, heavy, eel-like fish with a big blunt head and strong protruding canine teeth, blue-grey to olive with ten or more dark vertical bars, a long dorsal fin running the length of the back, a long anal, small rounded tail |
| common cuttlefish | swim 46x30 | y 80-230, speed 10 | Sepia officinalis: broad oval mantle fringed all round by a thin rippling fin, zebra-striped brown and cream on the back (male display) with pale spots, a big eye with a W-shaped pupil, eight short arms held together in a point in front of the head |
| red gurnard | crawl 46x20 | floor, speed 8 | Chelidonichthys cuculus: bright red gurnard with a steep armoured head, a row of tall plates along the lateral line, two dorsals, big wing-like pectorals, and three free pectoral rays it uses like legs to walk over the bottom |
| monkfish | crawl 66x26 | floor, speed 3 | Lophius piscatorius: huge flat head with a jutting lower jaw (no mouth line drawn, by request), a fishing-rod lure with a fleshy flap on top of the head, fringed skin flaps round the jaw, body tapering to a small tail, arm-like pectorals, mottled brown |
| atlantic halibut | crawl 70x34 | floor, speed 6 | Hippoglossus hippoglossus: the largest flatfish, lying eyed-side up: plain dark olive-brown with faint paler mottling, both eyes on the upper side of the head, a large mouth, long dorsal and anal fringes rippling, a slightly concave tail |
| thornback ray | crawl 60x12 | floor, speed 6 | Raja clavata: rhomboid disc lying on the bottom, seen slightly from above: brown with cream spots and dark marbling, a row of big hooked thorns down the middle of the back and along the thick tail, two small dorsal fins near the tail tip, eyes and spiracles raised on the head; the wing tips ripple |
| sea raven | crawl 46x22 | floor, speed 5 | Hemitripterus americanus: rough, prickly sculpin with ragged fleshy tabs on the head and chin, a tall ragged first dorsal, mottled red-brown to yellowish, big fan pectorals barred dark, wide mouth |
| shorthorn sculpin | crawl 40x20 | floor, speed 5 | Myoxocephalus scorpius: big-headed sculpin with short spines on the gill cover, broad fan pectorals, mottled dark brown and olive with pale saddles, a pale-spotted reddish belly in breeding males, two dorsals |
| montagus sea snail | crawl 32x14 | floor, speed 5 | Liparis montagui: small tadpole-shaped snailfish with soft loose skin, a round head and tapering body, reddish-brown to yellow with fine dark speckles, a long dorsal and anal running to the rounded tail, a sucker disc under the throat |
| black goby | crawl 34x16 | floor, speed 7 | Gobius niger: stocky dark goby, brown-black mottled darker, a dark spot at the front top of the first dorsal, a tall first dorsal in males, pelvic fins fused into a sucker disc, big eyes set high on the head |
| radiated shanny | crawl 40x14 | floor, speed 7 | Ulvaria subbifurcata: elongated blenny-like prickleback, brown mottled with darker blotches, a dark oval blotch at the front of the long dorsal fin, a dark bar slanting down from the eye, rounded tail |
| common hermit crab | crawl 30x18 | floor, speed 6 | Pagurus bernhardus: a red-orange hermit crab living in a borrowed pale whelk shell, the big right claw and the smaller left claw rough and granular, red-and-white banded walking legs and eyes on long stalks poking out of the shell mouth |
| common whelk | crawl 28x18 | floor, speed 2 | Buccinum undatum: big spiral whelk shell with wavy axial ribs crossed by fine spiral ridges, creamy brown, a wide aperture and a short siphonal canal; a pale grey foot speckled dark, a long siphon tube held up in front and two tentacles; the shell stays fixed while the foot glides |
| edible crab | crawl 36x16 | floor, speed 10 | Cancer pagurus seen from the front, walking sideways: a broad oval reddish-brown carapace with a crimped pie-crust edge, heavy claws with black fingertips, hairy reddish walking legs |
| european lobster | crawl 68x20 | floor, speed 8 | Homarus gammarus: big blue-black lobster speckled with pale yellow-white flecks, a heavy crusher claw and a slimmer cutter claw, long reddish antennae, a segmented tail ending in a broad fan |
| northern shrimp | crawl 48x16 | floor, speed 8 | Pandalus borealis: slender pink-red shrimp, a long upcurved toothed rostrum, a humped abdomen, long red antennae, thin legs, a tail fan; semi-transparent pink with deeper red bands |
| squat lobster | crawl 38x14 | floor, speed 8 | Galathea strigosa: flattened squat lobster with the tail tucked under, a bright orange-red carapace crossed by electric-blue stripes, long spiny arms held out in front ending in slender claws, short rostrum |
| orange footed sea cucumber | crawl 36x12 | floor, speed 1.5 | Cucumaria frondosa: fat, warty, dark brown-purple sea cucumber with rows of orange tube feet underneath and a crown of bushy, branched orange feeding tentacles spread at the front end; it creeps very slowly while the tentacles sway |

## Audit (`.agents/tools/creature_audit.py marine/cold_water`)
0/40 dimension mismatches, 0/144 A=C mismatched rows, 0/144 edge-touching rows, 3/40 per-sprite advisories (reviewed, intended).
The swimmer summary sits outside two hints (body aspect 3.39, deep share 0.12) because the roster is dominated by long, slender
fish - snake pipefish, fifteen-spined stickleback, sandeel, rock gunnel, ling, spiny dogfish and wolffish; colours 53.5 and L range
69.2 are within the hints.

## Scenes
`scenes/creatures/marine/cold_water/cw_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/cw_aquarium.tscn`.
