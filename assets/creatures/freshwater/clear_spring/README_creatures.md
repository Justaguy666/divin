# Clear Spring - creature style (prefix `cs_`)

Biome look: crystal-clear aquamarine spring water, strong sun from above, white sand and limestone. The roster mixes the
Florida spring runs (shiners, killifish, sunfish, gar, sturgeon, snook, mullet) and the clear springs of Bonito / Pantanal in
Brazil (characins, cichlids, catfish, pacu, dorado, crab). Every animal is fully aquatic.

All 40 creatures were redrawn from scratch in October 2026 following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), using only the species names as input: no earlier cs sprite,
size, texture or colour was used. Each species was first defined by its real anatomy and markings (step 1), then drawn at 1:1.

## Lighting and palette (applied while drawing, not as a post grade)
- Shadows lean to deep teal (#123a44), midtones take a faint aqua cast (#5cb8b0, about 7%), highlights lean to sunlit cream (#fff6dc).
- Signature colours stay ungraded: Buenos Aires tetra red fins, yellowtail lambari tail, flagfish red lines, redbreast belly,
  Suwannee bass blue chin, piraputanga / piracanjuba red tails, golden dorado gold, pacu belly, three-spot piau fins, crab claws.
- Translucent fins are tinted toward aqua (#a6dcd4, about 35%) with alpha falling from about 185 at the base to about 110 at the edge;
  fin rays are darker strokes (about 0.2 darker than the membrane) every second pixel, including the leading edge.

## Rendering (matches the BW reference)
- Body value: brightest in the upper third, slightly darker toward the back edge and the two ends, stepping darker toward the belly
  in 4-5 contour-following bands; no white belly and no specular streak.
- Outline: each edge pixel is a darker shade of the colour just inside it, tinted toward #0c2228. The top edge is lit (about 36%
  darker), the sides darker (about 52%), the belly edge darkest (about 68%) and the row above it is pulled down too, so the belly
  shadow and the outline merge. Stair-corner nubs are removed from the silhouette.
- Markings are flat colours or a fixed number of body tones darker (bars and stripes that follow the shading).
- Eyes: warm highlight pixel above a dark pupil, iris colour on the back side, a dark socket pixel under the pupil; large fish use
  a one-step wider eye.
- Silhouettes are spindle shaped with a pointed snout for small fish; deep-bodied fish keep a sloping forehead.
- Pelvic fins hang below the belly behind the pectorals (October 2026 fix: an earlier version of the fin builder folded them
  up into the body, where they barely showed).

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 25 deg (small), 15-16 deg (deep), 8-12 deg (long).
  Body and markings stay fixed; only fins, tail and ribbon fins move.
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (the snail uses crawl_R, crawl_L, idle_R, idle_L); the rest pose touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt (1 px safety); see the file names `cs_<name>_<swim|crawl>_<W>x<H>_4f.png`.
- Every sheet has a matching `cs_<name>.aseprite` (one layer, one tag per row, 0.12 s frames).

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small swimmers | buenos aires tetra 38x28, coastal shiner 38x26, ironcolor shiner 36x26, moenkhausia bonita 36x26, yellowtail lambari 40x28, spotted pyrrhulina 36x26, seminole killifish 38x26, swamp darter 30x22, tidewater silverside 38x24, florida flagfish 36x26, sailfin molly 38x30 |
| Medium swimmers | banded cichlid 44x36, chanchito 42x32, pike cichlid 50x22, lake chubsucker 44x28, redbreast sunfish 44x32, spotted sunfish 40x30, suwannee bass 48x26, three spot piau 50x24, striped mullet 50x22, banded knifefish 50x18 |
| Large swimmers | curimbata 58x32, piraputanga 56x26, piracanjuba 62x30, golden dorado 64x30, common snook 64x30, florida gar 62x26, pacu 58x42, pintado 84x28, gulf sturgeon 78x26 |
| Bottom dwellers and crawlers | cambeva 42x16, cascarudo 44x16, cascudo 46x26, fat sleeper 40x22, southern flounder 40x26, florida cave crayfish 52x14, pantanal crab 34x20, loggerhead musk turtle 36x16, toad headed turtle 40x14, rasp elimia 26x18 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining features |
|---|---|---|---|
| buenos aires tetra | swim 38x28 | y 40-200, speed 26 | silver tetra, black cross-shaped mark on the caudal peduncle running into the middle caudal rays, red fins |
| coastal shiner | swim 38x26 | y 20-170, speed 30 | slender minnow: straw-olive back with dark-edged scales, dusky lateral stripe ending in a small caudal spot, white belly |
| ironcolor shiner | swim 36x26 | y 40-200, speed 28 | wide black band from the lips through the eye to the caudal base, pale straw stripe above it, dusky back, orange-gold blush |
| moenkhausia bonita | swim 36x26 | y 30-200, speed 26 | small Bonito tetra: silvery olive, small humeral spot, black blotch on the caudal peduncle, red upper iris |
| yellowtail lambari | swim 40x28 | y 20-180, speed 30 | silvery characin, black horizontal humeral blotch, dark midline ending in a caudal spot, bright yellow tail |
| spotted pyrrhulina | swim 36x26 | y 8-120, speed 20 | cylindrical, tan back, cream flanks with rows of red-brown dots, dark stripe snout-to-gill, black dorsal spot, long upper caudal lobe |
| seminole killifish | swim 38x26 | y 4-110, speed 24 | Florida's big killifish: flat head, upturned mouth, olive-grey back, rows of small black dots, dorsal set far back over the anal |
| swamp darter | swim 30x22 | y 196-256, speed 12 | tiny darter: straw with dark mottling, a row of small blotches, dark teardrop under the eye, three dots on the tail base, two dorsals |
| tidewater silverside | swim 38x24 | y 0-80, speed 32 | slender and translucent: pale olive-straw, bright silver stripe with a dark upper edge, two small dorsals, long anal, big eye |
| florida flagfish | swim 36x26 | y 120-240, speed 16 | deep compressed killifish: olive-gold with rows of red horizontal lines (the "flag"), dark blotch mid-side under a long dorsal |
| sailfin molly | swim 38x30 | y 0-120, speed 18 | male: huge sail dorsal from the nape, olive-grey with rows of dark-edged scales, orange margin + dark spots on the sail, orange-edged tail |
| banded cichlid | swim 44x36 | y 90-230, speed 16 | Heros severus: deep oval, yellow-olive gold, 7 faint bars, the last bar on the peduncle bold from dorsal to anal base, red-brown dots on the cheek, long pointed dorsal + anal reaching past the tail base, red eye |
| chanchito | swim 42x32 | y 110-240, speed 16 | Australoheros facetus: olive-brown chameleon cichlid, 6 dark bars, a dark blotch mid-side, blue-green iridescent cheek spots, red eye |
| pike cichlid | swim 50x22 | y 150-250, speed 22 | Crenicichla lepidota: long pike-like cichlid, projecting lower jaw, dark stripe snout-eye-body, gold-ringed black ocellus behind the pectoral, black spot on the tail base, long low dorsal along the back |
| lake chubsucker | swim 44x28 | y 150-250, speed 16 | Erimyzon sucetta: stout oval sucker, brassy olive with dark-edged scales, small mouth under the snout, high rounded dorsal |
| redbreast sunfish | swim 44x32 | y 60-220, speed 18 | Lepomis auritus: long narrow black ear flap, orange-red breast and belly, olive back, orange spots, blue lines on the cheek |
| spotted sunfish | swim 40x30 | y 80-230, speed 16 | Lepomis punctatus: dusky olive with a black speck on nearly every scale, short black ear flap with a pale edge, faint orange breast |
| suwannee bass | swim 48x26 | y 100-240, speed 20 | Micropterus notius: chunky bronze-brown bass, row of dark lateral blotches, red eye, turquoise-blue chin, cheek and breast (male) |
| three spot piau | swim 50x24 | y 120-250, speed 22 | Leporinus friderici: cylindrical silvery-grey headstander, three round black spots along the midline, faint dark saddles, small terminal mouth, yellow-orange fins, adipose |
| striped mullet | swim 50x22 | y 10-150, speed 26 | Mugil cephalus: torpedo body with a broad blunt head, olive-grey back, silver sides with thin dark stripes along the scale rows, two widely spaced dorsals, a dark spot at the pectoral base set high on the side |
| banded knifefish | swim 50x18 | y 190-256, speed 12 | Gymnotus carapo: eel-like, tapering to a pointed tail with no caudal or dorsal fin, one long ribbon anal fin that ripples, brown with oblique dark and pale bands slanting backward |
| curimbata | swim 58x32 | y 130-250, speed 18 | Prochilodus lineatus: deep, high-backed silver migratory fish, grey back, thin dark lines along the scale rows, protrusible fleshy lips, high dorsal and a forked tail with dark bands |
| piraputanga | swim 56x26 | y 10-160, speed 30 | Brycon hilarii: slender silvery characin, blue-grey back, red tail and adipose, black stripe along the middle caudal rays running onto the peduncle, small dark humeral spot, orange-edged anal fin |
| piracanjuba | swim 62x30 | y 40-200, speed 28 | Brycon orbignyanus: deeper, darker green-grey back with dark dots on the upper scales, large humeral blotch, red caudal and anal fins, black mid-caudal stripe |
| golden dorado | swim 64x30 | y 30-200, speed 32 | Salminus brasiliensis: big golden-orange predator, rows of small dark scale spots forming thin lines, black bar across the middle of the tail, red-orange tail lobes, large mouth |
| common snook | swim 64x30 | y 80-230, speed 24 | Centropomus undecimalis: long body, concave sloping forehead, projecting lower jaw, bold black lateral line from the gill to the tail fin, olive-brown back, silver sides, two separate dorsals, yellow pelvic and caudal fins |
| florida gar | swim 62x26 | y 10-140, speed 14 | Lepisosteus platyrhincus: long cylindrical gar with a short broad snout, olive-brown back, dark round spots all over the head, body and fins, pale yellowish belly, dorsal and anal set far back opposite each other, rounded spotted tail |
| pacu | swim 58x42 | y 60-220, speed 18 | Piaractus mesopotamicus: very deep disc-like body, grey-silver back, darker grey sides, yellow-orange belly and throat, dark fins, small mouth with blunt teeth, small adipose |
| pintado | swim 84x28 | y 190-256, speed 16 | Pseudoplatystoma corruscans: long shovel-nosed catfish, flattened head, very long barbels, grey back with dark round spots and short vertical bars on the upper flank, white belly, forked spotted tail, adipose |
| gulf sturgeon | swim 78x26 | y 200-256, speed 14 | Acipenser oxyrinchus desotoi: huge, shark-like, shovel snout with four barbels underneath, rows of pale bony scutes (one along the back, one along the side, one above the belly), brown-grey back, pale belly, upper tail lobe much longer |
| cambeva | crawl 42x16 | floor, speed 10 | Trichomycterus pencil catfish: long cylindrical, flattened head, tiny eyes on top, nasal and maxillary barbels, brown-olive with irregular dark spots, dorsal set far back, rounded tail |
| cascarudo | crawl 44x16 | floor, speed 8 | Callichthys callichthys: armoured catfish, two rows of overlapping bony plates meeting at a midline seam, dark olive-brown, blunt flattened head, two pairs of long barbels, short spined dorsal, adipose spine, rounded tail |
| cascudo | crawl 46x26 | floor, speed 6 | Hypostomus pleco: flat belly and high arched back, brown body covered in dark spots, rows of bony plates, sail-like dorsal, ventral sucker mouth, eye high on the head, forked tail with a longer lower lobe, adipose |
| fat sleeper | crawl 40x22 | floor, speed 8 | Dormitator maculatus: chunky goby-like sleeper, blunt head, dark brown with rows of pale spots, a blue shoulder spot above the pectoral, spiny first dorsal and soft second dorsal, big rounded tail; rests on the bottom |
| southern flounder | crawl 40x26 | floor, speed 6 | Paralichthys lethostigma: flat oval flatfish lying on the sand, eyed side up: mottled brown with diffuse dark spots and a few pale-ringed ocelli, both eyes close together on the head, fringe dorsal and anal fins rippling along the edges |
| florida cave crayfish | crawl 52x14 | floor, speed 10 | cave crayfish: ghost-white, slightly pink and translucent, eyes reduced to pale nubs, long antennae, slender claws held forward, low body = carapace + segmented abdomen ending in a tail fan, four short walking legs per side drawn one by one |
| pantanal crab | crawl 34x20 | floor, speed 10 | Dilocarcinus pagei: freshwater crab from the Pantanal seen from the front, walking sideways: broad red-brown carapace, eyes on short stalks, orange-red claws with dark fingertips, four jointed walking legs on each side |
| loggerhead musk turtle | crawl 36x16 | floor, speed 6 | Sternotherus minor minor: small turtle with a high keeled carapace, brown-orange shell with dark streaks and dark-edged scutes, oversized head (loggerhead) pinkish-grey with dark spots, small yellowish plastron, short tail |
| toad headed turtle | crawl 40x14 | floor, speed 6 | Mesoclemmys toad-headed turtle (side-necked): low, flat oval carapace dark olive-brown, broad flat toad-like head, grey-olive skin, pale yellow jaw and throat with two small chin barbels, yellow plastron |
| rasp elimia | crawl 26x18 | floor, speed 2 | Elimia floridensis: tall turreted shell with strong spiral cords and axial ribs ("rasp"), olive-brown, dark aperture, grey foot gliding forward, two slender tentacles; the shell stays fixed while the foot and tentacles move |

## Scenes
`scenes/creatures/freshwater/clear_spring/cs_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/cs_aquarium.tscn`.
