# Underwater Cave - creature style (prefix `uc_`)

Biome look: a pitch-dark flooded sea cave, near-black water with a faint blue glow at the entrance. The roster gathers cave and
crevice fauna of the Caribbean, Atlantic and Mediterranean: soldier- and squirrelfish, bigeyes, sweepers, cardinalfish, comber,
anthias, a dwarf lionfish, pearlfish, spadefish, snapper, meagre, forkbeard, groupers, tarpon, nurse and sand tiger sharks, moray,
conger and two blind or dark cave brotulas; on the floor a scorpionfish, a triplefin blenny, four cave gobies, the octopus,
spiny and slipper lobsters, banded coral shrimp, the Hawaiian red shrimp, a spider crab, the giant isopod and the trumpet triton.

In October 2026 the creatures were redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier uc sprite,
size, texture or colour was used. Exceptions, by request: the blue devilfish and the common octopus keep their earlier drawings
exactly as they were (no recolour), so 38 species are new and 2 are unchanged.

## Lighting and palette (applied while drawing, not as a post grade)
- Shadows lean to blue-black (#0e121a), midtones take a faint cool violet-blue cast (#4e5c86, about 7%), highlights lean to cold
  white (#e8ecf2).
- The cave water is almost black, so bodies are kept bright enough to read: reds, pinks, coppers, silvers, sandy browns and
  white; signature colours are ungraded (soldierfish, squirrelfish, bigeye and cardinalfish reds, swallowtail seaperch pink and
  yellow, golden sweeper gold, yellowtail snapper stripe and tail, blackface blenny yellow, coral shrimp red bands, red shrimp).
- Translucent fins are tinted toward pale blue-grey (#b0b8c8, about 35%) with alpha falling from about 185 at the base to about 110
  at the edge; fin rays are darker strokes every second pixel, including the leading edge. Pelvic fins hang below the belly.

## Rendering (matches the BW reference)
- Body value: brightest in the upper third, slightly darker toward the back edge and the ends, stepping darker toward the belly in
  4-5 contour-following bands.
- Outline: a darker shade of the colour just inside each edge pixel, tinted toward #080a12; lit top edge, darker sides, darkest
  belly edge with the row above it pulled down. Stair-corner nubs are removed.
- Markings are flat colours or a fixed number of body tones darker; fish eyes are a warm highlight over a dark pupil with iris
  pixels behind and a dark socket below; the Cuban cave cusk eel has no eye (blind).
- Special cases: shark teeth and the squirrelfish gill spine are fine pegs and lines; forkbeard pelvic fins are long filaments;
  bottom gobies keep the pelvic disc (and, for Bentuvia's goby, the anal fin) still so every frame stays on the floor; the spiny
  lobster, slipper lobster and Hawaiian red shrimp are part-built crawlers enlarged 1.15x, 1.3x and 1.3x; the spider crab is seen
  from the front walking sideways; detached specks under 6-8 px are removed.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 14-20 deg (small), 11-13 deg (deep-bodied), 7-10 deg (long fish).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (trumpet triton: crawl_R, crawl_L, idle_R, idle_L); every frame touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `uc_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a
  matching `uc_<name>.aseprite` (one layer, one tag per row, 0.12 s frames) and its Godot `.import` file.

## Roster (40 species: 26 swimmers, 14 crawlers)

| Group | Species (frame) |
|---|---|
| Small swimmers | blackbar soldierfish 42x28, longspine squirrelfish 46x28, glasseye 40x28, red bigeye 44x26, glassy sweeper 40x26, golden sweeper 32x22, red cardinalfish 34x22, sawcheek cardinalfish 28x20, painted comber 42x24, swallowtail seaperch 44x28, dwarf lionfish 36x24, pearlfish 40x16 |
| Medium and large swimmers | atlantic spadefish 50x50, yellowtail snapper 60x28, brown meagre 58x30, forkbeard 54x24, dusky grouper 72x34, goliath grouper 110x48, atlantic tarpon 106x40, nurse shark 108x32, sand tiger shark 116x34, spotted moray 76x24, european conger 86x24, cuban cave cusk eel 48x20, black cave brotula 52x22 |
| Floor dwellers (crawl) | madeira rockfish 38x18, blackface blenny 32x12, leopard spotted goby 34x14, steinitzs cave goby 36x14, bentuvias goby 30x14, liechtensteins goby 24x12, caribbean spiny lobster 60x18, slipper lobster 48x14, banded coral shrimp 46x16, hawaiian red shrimp 26x10, mediterranean spider crab 46x18, giant isopod 46x12, trumpet triton 32x18 |
| Kept from the earlier set (by request) | blue devilfish 34x28 (swim), common octopus 38x26 (crawl) |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining features |
|---|---|---|---|
| blackbar soldierfish | swim 42x28 | y 80-230, speed 12 | Myripristis jacobus: red soldierfish with a huge dark eye, rough scales outlined darker, a broad black bar from the top of the head down behind the gill cover, white leading edges on the red fins |
| longspine squirrelfish | swim 46x28 | y 80-230, speed 12 | Holocentrus rufus: red and white striped squirrelfish with a big eye, a long sharp spine on the gill cover, a tall spiny dorsal with white spots near its tips, and a very long upper tail lobe |
| glasseye | swim 40x28 | y 100-240, speed 10 | Heteropriacanthus cruentatus: deep, compressed bigeye with an enormous eye, rough red-silver body that can blotch silver-white, a large dark-spotted soft dorsal and anal, rounded-truncate tail, upturned mouth |
| red bigeye | swim 44x26 | y 80-230, speed 12 | Priacanthus arenatus: oblong bright red bigeye with a huge eye, a long low spiny-soft dorsal and anal, long dark-tinted pelvic fins, slightly forked tail, steeply upturned mouth |
| glassy sweeper | swim 40x26 | y 40-200, speed 16 | Pempheris schomburgkii: hatchet-shaped sweeper, deep keeled belly tapering to a slender tail, coppery-bronze and translucent, a dark band along the base of the very long anal fin, a short high dorsal near the front, big eye |
| golden sweeper | swim 32x22 | y 30-190, speed 18 | Parapriacanthus ransonneti: small translucent golden-yellow sweeper schooling in caves, a golden head shading to a clear pinkish body, the dark spine showing through, a short dorsal near the front, long anal, forked tail |
| red cardinalfish | swim 34x22 | y 100-240, speed 10 | Apogon imberbis: small, stout cardinalfish, bright orange-red, a big eye crossed by two pale lines, two separate dorsals, a dark spot at the tail base, a large mouth |
| sawcheek cardinalfish | swim 28x20 | y 100-240, speed 10 | Apogon quadrisquamatus: tiny pale, translucent pinkish cardinalfish with a dusky stripe from the snout through the eye, a round dark spot at the tail base, two dorsals, big eye, serrated cheek edge |
| painted comber | swim 42x24 | y 150-250, speed 14 | Serranus scriba: perch-like comber, reddish-brown with five dark vertical bars, a blue-violet patch on the belly, wavy blue and red scribbles over the head, a yellowish belly, long spiny dorsal, square tail |
| swallowtail seaperch | swim 44x28 | y 60-220, speed 14 | Anthias anthias: pink-red anthias with yellow-edged stripes across the snout and cheek, a deeply forked swallow tail with long lobes, very long yellow-tipped pelvic fins, a long third dorsal spine |
| dwarf lionfish | swim 36x24 | y 140-245, speed 6 | Dendrochirus brachypterus: small, stocky lionfish banded red-brown and cream, huge fan-like pectoral fins banded dark, a tall spiny dorsal, fleshy tabs above the eyes and on the chin, slow hovering |
| pearlfish | swim 40x16 | y 180-250, speed 10 | Carapus acus: slender, eel-like, translucent pearly-white fish that hides inside sea cucumbers, silvery gut and organs showing as a pearly sheen, faint reddish spots along the back, tapering to a thin point, long low fins along back and belly |
| atlantic spadefish | swim 50x50 | y 40-200, speed 14 | Chaetodipterus faber: deep, nearly round disc, silver-grey with four to six dark vertical bars (the first through the eye), tall pointed lobes at the front of the soft dorsal and anal, a small mouth, slightly concave tail |
| yellowtail snapper | swim 60x28 | y 40-210, speed 24 | Ocyurus chrysurus: streamlined snapper, blue-grey to violet back speckled yellow, silvery sides, a bright yellow stripe from the snout to the deeply forked, all-yellow tail |
| brown meagre | swim 58x30 | y 120-245, speed 12 | Sciaena umbra: humpbacked croaker, dark bronze-brown with a golden sheen, black pelvic and anal fins with a bright white leading edge, long two-part dorsal, truncate tail, blunt snout |
| forkbeard | swim 54x24 | y 170-250, speed 12 | Phycis phycis: brown cod-like fish with a short first dorsal and a long second dorsal, a long anal, a chin barbel, and pelvic fins reduced to a pair of long trailing filaments, rounded tail, dark spot at the pectoral base |
| dusky grouper | swim 72x34 | y 130-250, speed 12 | Epinephelus marginatus: heavy grouper, dark reddish-brown with irregular pale blotches in rows, a yellowish belly, a big jaw, and pale edges on the rounded tail, soft dorsal and anal |
| goliath grouper | swim 110x48 | y 150-250, speed 8 | Epinephelus itajara: enormous grouper with a broad flat head and tiny eyes, yellowish-brown to olive with irregular dark oblique bands and small black spots on the head and fins, rounded fins and tail |
| atlantic tarpon | swim 106x40 | y 20-200, speed 20 | Megalops atlanticus: huge, bright silver tarpon with big shiny dark-edged scales, a dark grey-blue back, an upturned bony lower jaw, a long filament trailing from the last dorsal ray, deeply forked tail |
| nurse shark | swim 108x32 | y 210-258, speed 10 | Ginglymostoma cirratum: sluggish yellow-brown to tan shark, two rounded dorsal fins set far back and nearly equal in size, a pair of fleshy barbels at the nostrils, small eyes, a long upper tail lobe with almost no lower lobe |
| sand tiger shark | swim 116x34 | y 60-230, speed 14 | Carcharias taurus: bulky light grey-brown shark with scattered rusty-brown spots, a pointed snout, ragged needle teeth sticking out of the mouth, two large dorsal fins of nearly equal size set well back, a long upper tail lobe |
| spotted moray | swim 76x24 | y 200-258, speed 8 | Gymnothorax moringa: moray eel, pale yellowish-white densely covered in dark brown-black spots and blotches, a continuous dorsal fin starting on the head, no pectoral fins, a gaping mouth and a big head |
| european conger | swim 86x24 | y 200-258, speed 10 | Conger conger: big scaleless eel, slate grey-blue to near black above, pale grey below, a dorsal fin starting just behind the pectoral and edged black, big eyes, thick lips, pointed pectoral fins |
| cuban cave cusk eel | swim 48x20 | y 190-258, speed 8 | Lucifuga dentata: blind cave fish with tiny skin-covered eyes, pale pinkish-violet to brown, an eel-like body tapering to a pointed tail joined to the long dorsal and anal fins, pelvic fins reduced to thin filaments under the throat, a big blunt head |
| black cave brotula | swim 52x22 | y 190-258, speed 8 | cave brotula: eel-like, velvety dark brown-black fish of cave crevices, small eyes, a long dorsal and anal running into the rounded tail, thread-like pelvic fins under the throat, a short barbel-fringed snout |
| madeira rockfish | crawl 38x18 | floor, speed 4 | Scorpaena maderensis: small scorpionfish, mottled red-brown with dark bands and pale blotches, fleshy tabs over the eyes and on the head, a venomous spiny dorsal with a dark spot, big fan pectorals, big mouth |
| blackface blenny | crawl 32x12 | floor, speed 7 | Tripterygion delaisi (male): triplefin blenny with three separate dorsal fins, a bright yellow body and a jet-black head, pointed snout, big eyes set high, rounded tail |
| leopard spotted goby | crawl 34x14 | floor, speed 7 | Thorogobius ephippiatus: pale grey-cream goby covered in large orange-brown leopard spots edged darker, a dark-edged first dorsal, big eyes on top of the head, rounded tail |
| steinitzs cave goby | crawl 36x14 | floor, speed 7 | Amblyeleotris steinitzi: slender goby that shares a burrow with a shrimp, white with five broad orange-brown bars and scattered small yellow spots, a tall first dorsal, rounded tail |
| bentuvias goby | crawl 30x14 | floor, speed 7 | Didogobius bentuvii: small, pale cave goby, translucent pinkish-cream with faint orange-brown blotches along the side, small eyes, two dorsals, rounded tail |
| liechtensteins goby | crawl 24x12 | floor, speed 6 | Corcyrogobius liechtensteini: tiny cave goby, translucent pale with yellow-orange saddles across the back and a pale blue sheen on the head, big dark eyes, two dorsals |
| caribbean spiny lobster | crawl 60x18 | floor, speed 8 | Panulirus argus: clawless spiny lobster, orange-brown with cream spots on the tail (two big pale spots on the second segment), very long, thick, spiny antennae swept forward, striped legs, a broad tail fan |
| slipper lobster | crawl 48x14 | floor, speed 6 | Scyllarides aequinoctialis: flat, broad, armoured slipper lobster with no claws, the antennae turned into wide flat shovel plates in front of the head, mottled orange-brown with darker spots, short legs, a broad tail fan |
| banded coral shrimp | crawl 46x16 | floor, speed 7 | Stenopus hispidus: boxer shrimp banded red and white along the body and claws, a pair of very long banded claws held forward, long white antennae, translucent white legs |
| hawaiian red shrimp | crawl 26x10 | floor, speed 6 | Halocaridina rubra: tiny bright red cave shrimp (opae ula), a short rostrum, black eyes, a curved abdomen and tail fan, fine legs |
| mediterranean spider crab | crawl 46x18 | floor, speed 8 | Maja squinado seen from the front: a pear-shaped, knobbly orange-red carapace covered in spines with two forward horns, long spindly hairy legs, slender claws, often bits of algae caught on the spines |
| giant isopod | crawl 46x12 | floor, speed 5 | Bathynomus giganteus: huge pill-bug of the deep, lilac-grey segmented armour plates, a broad head shield with big compound eyes, short antennae, seven pairs of walking legs beneath, a fan-like tail plate |
| trumpet triton | crawl 32x18 | floor, speed 2 | Charonia: big, tall, trumpet-shaped spiral shell patterned with cream and brown crescents, a flared orange aperture with white ridges, a pale orange foot spotted dark and two tentacles; the shell stays fixed while the foot glides |
| blue devilfish | swim 34x28 | unchanged | earlier drawing kept exactly as it was, by request (sprite, .aseprite and scene untouched) |
| common octopus | crawl 38x26 | unchanged | earlier drawing kept exactly as it was, by request (sprite, .aseprite and scene untouched) |

## Audit (`.agents/tools/creature_audit.py special/underwater_cave`)
0/40 dimension mismatches, 0/156 A=C mismatched rows, 0/156 edge-touching rows, 10/40 per-sprite advisories (reviewed, intended).
Swimmer summary: deep share 0.23, colours 53 and L range 70.1 are within the hints; body aspect 2.87 sits above the 2.60 hint
because of the long fish (two sharks, moray, conger, tarpon, the cave brotulas and the pearlfish).

## Scenes
`scenes/creatures/special/underwater_cave/uc_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The two kept species keep their earlier scenes. The showcase is
`scenes/aquarium/uc_aquarium.tscn`.
