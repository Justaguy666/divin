# Bayou - creature style (prefix `by_`)

Biome look: a slow southern bayou - tea-dark olive water among cypress knees and roots, duckweed light, soft black mud. The roster
gathers the Gulf Coast and lower-Mississippi fauna: topminnows, killifish, mosquitofish, silverside and small minnows, a darter,
pirate perch and mudminnow; sunfishes, crappie, largemouth bass, drum and buffalo, threadfin shad, channel and flathead catfish,
the bowfin, three gars and the paddlefish; on the floor the American alligator, alligator snapping and musk turtles, blue crab,
red swamp crawfish, grass shrimp, two eel-like salamanders, the rainbow snake, the tadpole madtom and the hogchoker.

In October 2026 the creatures were redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier by sprite,
size, texture or colour was used. Exception, by request: the lesser siren and the three-toed amphiuma keep their earlier drawings,
re-mapped onto the bayou ramp below and re-outlined with the BW outline rule (the siren's pink-red gill tufts kept as a signature),
with a 1 px side margin added so no frame touches the sheet edge.

## Lighting and palette (applied while drawing, not as a post grade)
- Shadows lean to tannin olive-black (#1e1e10), midtones take a faint tea-amber cast (#a8844a, about 7%), highlights lean to hazy
  warm cream (#f2e8c4).
- The water is dark olive, so bodies lean to olive, bronze, silver and browns; signature colours are ungraded (bluegill orange
  breast and purple cheek, redear red ear rim, warmouth red eye and cheek streaks, flier eyespot, bluefin killifish blue fins and
  red tail, taillight shiner rosy fins, rainwater killifish orange fins, cypress darter red dorsal spots, threadfin shad yellow tail,
  bowfin orange-ringed tail spot, blue crab blue claws and red fingertips, red swamp crawfish, rainbow snake red stripes, siren gills).
- Translucent fins are tinted toward pale tannin straw (#ccc6a0, about 35%) with alpha falling from about 185 at the base to about
  110 at the edge; fin rays are darker strokes every second pixel, including the leading edge. Pelvic fins hang below the belly.

## Rendering (matches the BW reference)
- Body value: brightest in the upper third, slightly darker toward the back edge and the ends, stepping darker toward the belly in
  4-5 contour-following bands.
- Outline: a darker shade of the colour just inside each edge pixel, tinted toward #14140a; lit top edge, darker sides, darkest
  belly edge with the row above it pulled down. Stair-corner nubs are removed.
- Markings are flat colours or a fixed number of body tones darker; fish eyes are a warm highlight over a dark pupil with iris
  pixels behind and a dark socket below.
- Special cases: the alligator is a part-built crawler (bumpy scute ridge, pale belly and jaw with a tooth row, raised eye and
  nostril bumps, thick sprawling legs, tail swaying from the hips); the blue crab is seen from the front walking sideways; the grass
  shrimp is made see-through after rendering (body alpha about 140, outline about 200, the black eye stays opaque); the hogchoker is
  drawn like the other flatfish (eyed side up) with nearly flat shading and rippling fringe fins, and crumbs the ripple leaves
  floating above the fin are removed.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 18-24 deg (small), 11-16 deg (deep-bodied), 7-10 deg (long fish).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L; every frame touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `by_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a
  matching `by_<name>.aseprite` (one layer, one tag per row, 0.12 s frames) and its Godot `.import` file.

## Roster (40 species: 29 swimmers, 11 crawlers)

| Group | Species (frame) |
|---|---|
| Small swimmers | bantam sunfish 32x26, flier 40x32, pirate perch 38x24, central mudminnow 34x24, blackstripe topminnow 36x22, golden topminnow 34x22, bluefin killifish 30x20, rainwater killifish 30x22, least killifish 22x16, western mosquitofish 28x20, brook silverside 40x24, pugnose minnow 36x22, taillight shiner 38x24, cypress darter 28x20 |
| Medium and large swimmers | bluegill 44x32, redear sunfish 46x32, warmouth 42x28, white crappie 46x34, largemouth bass 70x34, freshwater drum 62x34, bigmouth buffalo 74x38, threadfin shad 44x24, channel catfish 72x28, flathead catfish 76x30, bowfin 72x30, spotted gar 74x28, longnose gar 88x28, alligator gar 112x36, paddlefish 110x32 |
| Floor crawlers | american alligator 98x14, alligator snapping turtle 48x16, common musk turtle 32x14, blue crab 34x18, red swamp crawfish 52x14, mississippi grass shrimp 38x14, lesser siren 50x14, three toed amphiuma 58x12, rainbow snake 66x8, tadpole madtom 34x14, hogchoker 32x26 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining features |
|---|---|---|---|
| bantam sunfish | swim 32x26 | y 100-230, speed 14 | Lepomis symmetricus: small, deep, rounded sunfish, olive-green flecked with dark spots and faint bars, a plain black ear spot, a dark blotch at the rear base of the soft dorsal, rounded tail |
| flier | swim 40x32 | y 60-220, speed 16 | Centrarchus macropterus: round, compressed sunfish with huge dorsal and anal fins of equal size, olive-silver with rows of dark spots forming lines along the sides, a dark teardrop under the eye, an orange-ringed black eyespot on the soft dorsal |
| pirate perch | swim 38x24 | y 170-256, speed 10 | Aphredoderus sayanus: stout, big-headed little perch, dark purplish-brown peppered with darker specks, a dark bar at the tail base and a dark teardrop under the eye, one dorsal with a few short spines in front, slightly notched tail |
| central mudminnow | swim 34x24 | y 170-256, speed 12 | Umbra limi: chunky little cylinder with a blunt head, dark olive-brown with about a dozen faint narrow pale bars, a black bar across the tail base, rounded tail and fins, dorsal set well back over the anal |
| blackstripe topminnow | swim 36x22 | y 0-70, speed 22 | Fundulus notatus: slender surface killifish with a flat head and upturned mouth, a broad black stripe from the snout to the tail, pale olive back dotted dark, white belly, a shiny gold spot on top of the head, dorsal set far back |
| golden topminnow | swim 34x22 | y 0-80, speed 20 | Fundulus chrysotus: stocky topminnow, olive-gold sprinkled with shining brassy flecks, males with rows of small red-brown spots, rounded fins with a few red dots, gold spot on the head, dorsal far back |
| bluefin killifish | swim 30x20 | y 40-180, speed 20 | Lucania goodei: small slender killifish with a dark zigzag stripe from the snout to the tail, straw-olive back, males with brilliant blue dorsal and anal fins edged black and a red-orange tail base |
| rainwater killifish | swim 30x22 | y 30-170, speed 20 | Lucania parva: small, fairly deep killifish, straw-olive with dark-edged scales giving a crosshatched look, males with an orange-tinted dorsal and anal edged black and a dark spot at the front of the dorsal |
| least killifish | swim 22x16 | y 20-150, speed 16 | Heterandria formosa: one of the tiniest fish, olive-tan with a dark stripe from the eye to the tail crossed by faint narrow bars, a dark spot at the base of the dorsal, rounded tail |
| western mosquitofish | swim 28x20 | y 0-80, speed 22 | Gambusia affinis (female): small and plump-bellied, translucent grey-olive with dark-edged scales, a black teardrop under the eye, a dark gravid spot above the anal fin, dorsal set far back, rounded tail with rows of tiny dots |
| brook silverside | swim 40x24 | y 0-90, speed 30 | Labidesthes sicculus: very slender, glassy pale green, a bright silver stripe along the side, a long beak-like snout and big eye, two small dorsals, a long sickle-shaped anal, forked tail |
| pugnose minnow | swim 36x22 | y 60-200, speed 24 | Opsopoeodus emiliae: small minnow with a tiny, almost vertical upturned mouth (pug nose), silvery-olive with a dusky stripe along the side, dark-edged back scales, males with a dark band through the dorsal fin |
| taillight shiner | swim 38x24 | y 40-190, speed 26 | Notropis maculatus: slender shiner with a big round black spot at the tail base (the taillight), a dusky stripe along the side, breeding males flushed rosy-red on the body and fins |
| cypress darter | swim 28x20 | y 200-258, speed 12 | Etheostoma proeliare: tiny darter, straw-olive with a row of about nine dark dashes along the side, dark saddles, a dark teardrop under the eye, two dorsals (the first with a row of red-orange spots in males), rounded tail, big fan pectorals |
| bluegill | swim 44x32 | y 60-220, speed 16 | Lepomis macrochirus: deep round sunfish, olive-green with five to eight dusky vertical bars, a plain black ear flap, a dark blotch at the rear of the soft dorsal, a purple-blue sheen on the cheek and an orange-yellow breast |
| redear sunfish | swim 46x32 | y 120-240, speed 14 | Lepomis microlophus: deep sunfish, olive-gold with faint darker flecks and bars, a short black ear flap with a bright red-orange rim, pale yellowish belly, long pointed pectoral fins |
| warmouth | swim 42x28 | y 140-250, speed 12 | Lepomis gulosus: thick-bodied, big-mouthed sunfish, olive-brown heavily mottled with dark blotches, three or four dark red-brown streaks radiating back from the red eye across the cheek, dark-spotted fins |
| white crappie | swim 46x34 | y 40-200, speed 16 | Pomoxis annularis: deep, compressed, silvery-white panfish with a dipped forehead and big upturned mouth, five to ten faint dusky vertical bars (often paired), big dorsal and anal of equal size set far back, both dotted dark |
| largemouth bass | swim 70x34 | y 40-220, speed 20 | Micropterus salmoides: big olive-green bass with a dark ragged band of blotches along the side, pale belly, a jaw reaching past the eye, a deeply notched dorsal (spiny and soft parts almost separate), emarginate tail |
| freshwater drum | swim 62x34 | y 150-250, speed 16 | Aplodinotus grunniens: humpbacked silver-grey drum with a blunt rounded snout and low mouth, a long dorsal made of a short spiny part and a very long soft part, the lateral line running out onto the pointed-round tail, pale fins |
| bigmouth buffalo | swim 74x38 | y 60-220, speed 16 | Ictiobus cyprinellus: big, deep-bodied sucker with a large oblique mouth at the tip of the snout, olive-bronze to slate back, brassy sides, a long sickle-shaped dorsal (tall in front, low behind), forked tail, dusky fins |
| threadfin shad | swim 44x24 | y 0-110, speed 28 | Dorosoma petenense: small silvery shad, blue-grey back, a dark spot behind the gill, a long thread trailing from the last dorsal ray, bright yellow tail and fins, deeply forked tail, protruding lower jaw |
| channel catfish | swim 72x28 | y 190-256, speed 16 | Ictalurus punctatus: slim catfish with a deeply forked tail, blue-grey to olive back and silver-white belly, scattered small black spots, four pairs of barbels (long ones at the mouth corners), adipose fin, spined dorsal and pectorals |
| flathead catfish | swim 76x30 | y 200-258, speed 12 | Pylodictis olivaris: heavy catfish with a broad flat head and a jutting lower jaw, mottled yellow-brown and olive, a square tail with a pale tip on the upper lobe, short barbels, large adipose fin, small eyes |
| bowfin | swim 72x30 | y 130-250, speed 14 | Amia calva: long cylindrical living fossil, olive-green mottled darker, pale belly, a long low dorsal fin rippling along most of the back, rounded tail with a black eyespot ringed orange at its upper base, big head with a bony plate and short tube nostrils |
| spotted gar | swim 74x28 | y 0-120, speed 14 | Lepisosteus oculatus: long gar with a medium-length snout, olive-brown back, pale belly, round dark spots all over the head, body and fins, dorsal and anal far back opposite each other, rounded spotted tail |
| longnose gar | swim 88x28 | y 0-130, speed 16 | Lepisosteus osseus: slender gar with a very long, narrow beak (about twice the head length), olive-brown back, silvery-white belly, a few dark spots on the rear body and the dorsal, anal and tail fins |
| alligator gar | swim 112x36 | y 20-200, speed 12 | Atractosteus spatula: giant gar with a short, broad alligator-like snout lined with a double row of teeth, heavy body, olive-brown back mottled darker, pale yellowish belly, dark blotches on the rear fins, rounded tail |
| paddlefish | swim 110x32 | y 60-230, speed 14 | Polyodon spathula: shark-like grey fish with a long flat paddle-shaped snout (a third of its length), a tiny eye, a huge pointed gill flap reaching back along the side, smooth scaleless skin, small dorsal set far back, forked tail with a longer upper lobe |
| american alligator | crawl 98x14 | floor, speed 6 | Alligator mississippiensis: long armoured reptile walking on the bottom, olive-black back with rows of raised bony scutes and a double crest along the thick tail, pale cream belly and jaw, broad rounded snout with a row of pale teeth showing, raised eyes and nostrils, short sprawling legs |
| alligator snapping turtle | crawl 48x16 | floor, speed 4 | Macrochelys temminckii: massive turtle whose carapace carries three rows of tall spiky keels (a jagged, dinosaur-like back), dark brown-grey often greened with algae, a huge head with a sharply hooked beak, small eyes ringed with a star pattern, thick legs and a long tail edged with spiky scales |
| common musk turtle | crawl 32x14 | floor, speed 6 | Sternotherus odoratus (stinkpot): small, smooth, high-domed carapace olive-brown to black, two pale yellow stripes on the side of the head above and below the eye, a pointed snout with fleshy chin barbels, tiny plastron |
| blue crab | crawl 34x18 | floor, speed 12 | Callinectes sapidus seen from the front, walking sideways: wide olive-green carapace with a long sharp spine at each side and small teeth along the front edge, eyes on short stalks, bright blue claws with red-orange fingertips, blue walking legs and a rear pair of flat swimming paddles |
| red swamp crawfish | crawl 52x14 | floor, speed 10 | Procambarus clarkii: dark blood-red crawfish with a black wedge stripe along the top of the abdomen, long narrow claws covered in raised bright red bumps, a pointed rostrum |
| mississippi grass shrimp | crawl 38x14 | floor, speed 8 | Palaemonetes kadiakensis: small clear shrimp, nearly invisible apart from faint brown speckles and stripes, a long upturned toothed rostrum, black eyes on short stalks, long whip antennae, thin legs, small first claws, a tail fan |
| lesser siren | crawl 50x14 | floor, speed 6 | Siren intermedia: the existing drawing is kept (by request) and re-mapped onto the bayou ramp with the BW outline rule; the pink-red external gill tufts stay a signature colour |
| three toed amphiuma | crawl 58x12 | floor, speed 6 | Amphiuma tridactylum: the existing drawing is kept (by request) and re-mapped onto the bayou ramp with the BW outline rule |
| rainbow snake | crawl 66x8 | floor, speed 7 | Farancia erytrogramma: glossy iridescent blue-black snake with three narrow red stripes running along the back and sides, a red and yellow belly with rows of black spots, small head with a pointed snout, short tail with a spine-like tip |
| tadpole madtom | crawl 34x14 | floor, speed 8 | Noturus gyrinus: tiny tadpole-shaped catfish, a plump head tapering to a thin tail, plain yellow-brown to grey with a thin dark line along the side, the adipose fin joined to the rounded tail in one long fold, short barbels |
| hogchoker | crawl 32x26 | floor, speed 6 | Trinectes maculatus: small, almost round sole lying on the mud, eyed side brown crossed by seven or eight thin dark bars, small eyes close together near the top of the head, no pectoral fins, dorsal and anal fringes running round the body and rippling |

## Audit (`.agents/tools/creature_audit.py freshwater/bayou`)
0/40 dimension mismatches, 0/174 A=C mismatched rows, 0/174 edge-touching rows. Swimmer summary: deep share 0.24, colours 56 and
L range 69.5 are within the hints; body aspect 2.65 sits just above the 2.60 hint because the roster carries three gars, the
paddlefish, the bowfin and two catfish. The per-sprite advisories were reviewed visually and are intended.

## Scenes
`scenes/creatures/freshwater/bayou/by_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/by_aquarium.tscn`.
