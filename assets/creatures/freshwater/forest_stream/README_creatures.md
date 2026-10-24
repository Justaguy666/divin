# Forest Stream - creature style (prefix `fs_`)

Biome look: a shaded Appalachian forest stream - clear water under a leaf canopy, riffles over cobble, sun flecks breaking
through. The roster is the eastern North American stream fauna: daces, shiners and chubs, suckers, darters, sunfish and bass,
percids, pike, shad, lamprey, madtoms, sculpin, giant salamanders, crayfish, a musk turtle and a hornsnail.

In October 2026 the creatures were redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier fs sprite,
size, texture or colour was used. Exception, by request: the hellbender and mudpuppy keep their earlier drawings, re-mapped onto
the forest-stream ramp below and re-outlined with the BW outline rule (the mudpuppy's red gills stay a signature colour).

## Lighting and palette (applied while drawing, not as a post grade)
- Shadows lean to moss brown (#1e2c1c), midtones take a faint leaf-green cast (#7a9a5a, about 7%), highlights lean to warm sun flecks (#f8f2d2).
- The water is green, so bodies stay in olive, bronze, brass, silver and brown families; signature colours are ungraded:
  redbelly / saffron / rosyface / rosyside reds, warpaint red bars, rainbow / redline / tangerine darter colours, bluehead chub head,
  longear sunfish orange and turquoise, rock bass red eye, river redhorse red fins, walleye white tail tip, mudpuppy gills,
  rusty crayfish spots, musk turtle head stripes.
- Translucent fins are tinted toward pale green (#bcd4b0, about 35%) with alpha falling from about 185 at the base to about 110 at
  the edge; fin rays are darker strokes every second pixel, including the leading edge.

## Rendering (matches the BW reference)
- Body value: brightest in the upper third, slightly darker toward the back edge and the ends, stepping darker toward the belly in
  4-5 contour-following bands.
- Outline: a darker shade of the colour just inside each edge pixel, tinted toward #121a10; lit top edge, darker sides, darkest
  belly edge with the row above it pulled down. Stair-corner nubs are removed.
- Markings are flat colours or a fixed number of body tones darker; eyes are a warm highlight over a dark pupil with iris pixels
  behind and a dark socket below.
- Pelvic fins hang below the belly behind the pectorals (October 2026 fix: an earlier version of the fin builder folded them
  up into the body, where they barely showed).

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 25 deg (small), 20-22 deg (darters), 15 deg (deep), 8-14 deg (long).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (the snail uses crawl_R, crawl_L, idle_R, idle_L); the rest pose touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `fs_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a matching
  `fs_<name>.aseprite` (one layer, one tag per row, 0.12 s frames).

## Roster (40 species: 31 swimmers, 9 crawlers)
Darters live on the bottom but are swimmers in the lowest band; the madtom, stonecat, sculpin, salamanders, crayfish, turtle and
snail walk on the floor.

| Group | Species (frame) |
|---|---|
| Small minnows, topminnow and darters | blacknose dace 36x24, longnose dace 38x24, southern redbelly dace 34x24, rosyside dace 38x26, warpaint shiner 38x26, saffron shiner 34x24, rosyface shiner 36x24, northern studfish 38x26, central mudminnow 34x24, rainbow darter 32x20, greenside darter 36x22, redline darter 32x22, tangerine darter 40x24, fantail darter 34x24, tessellated darter 32x20 |
| Medium and large swimmers | central stoneroller 44x26, bluehead chub 46x28, creek chub 48x28, fallfish 56x28, northern hog sucker 48x24, white sucker 54x26, river redhorse 60x30, longear sunfish 40x30, rock bass 44x30, smallmouth bass 60x30, logperch 46x22, walleye 66x28, sauger 60x26, muskellunge 80x28, american shad 60x30, american brook lamprey 48x16 |
| Bottom dwellers and crawlers | northern madtom 36x14, stonecat 44x16, mottled sculpin 36x16, hellbender 58x16, mudpuppy 46x16, appalachian brook crayfish 52x14, rusty crayfish 52x14, eastern musk turtle 32x14, silty hornsnail 28x20 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining features |
|---|---|---|---|
| blacknose dace | swim 36x24 | y 60-220, speed 26 | Rhinichthys atratulus: slender riffle minnow, olive-brown back with dark speckles, black band from the snout through the eye to the tail, silvery-white belly, a rusty-orange tint along the band in breeding males |
| longnose dace | swim 38x24 | y 170-256, speed 22 | Rhinichthys cataractae: long fleshy snout overhanging the mouth, cylindrical riffle dweller, olive-brown mottled with dark scales, faint dark lateral band, cream belly, red lips and fin bases in breeding males |
| southern redbelly dace | swim 34x24 | y 40-200, speed 26 | Chrosomus erythrogaster: two black lateral stripes (thin upper, broad lower) split by a golden stripe, scarlet belly, olive back with small dark spots, yellow fins |
| rosyside dace | swim 38x26 | y 40-200, speed 28 | Clinostomus funduloides: deeper dace with a big mouth, olive back with dark-edged scales, silver sides, rosy-red patch on the lower flank, a faint dark lateral stripe under a thin gold line |
| warpaint shiner | swim 38x26 | y 30-190, speed 28 | Luxilus coccogenis: deep silvery shiner, red bar on the upper gill cover and a red snout ("war paint"), black shoulder bar, dorsal fin with a black band near the top, olive back, dark tail margin |
| saffron shiner | swim 34x24 | y 40-200, speed 28 | Notropis rubricroceus: breeding males blaze saffron-red over body and fins, dark olive back, dusky lateral stripe |
| rosyface shiner | swim 36x24 | y 20-170, speed 30 | Notropis rubellus: slender with a pointed snout, rosy-red head in breeding season, silver sides with a thin dark lateral line, olive back with a dark mid-dorsal stripe |
| northern studfish | swim 38x26 | y 4-110, speed 22 | Fundulus catenatus: large topminnow, flat head, blue-grey sides with rows of red-brown spots forming chains, orange fins with a dark edge in males, dorsal set far back |
| central mudminnow | swim 34x24 | y 170-250, speed 14 | Umbra limi: stout cylindrical, olive-brown with faint bars and fine mottling, a black vertical bar across the tail base, rounded fins, dorsal set far back over the anal |
| rainbow darter | swim 32x20 | y 200-258, speed 14 | Etheostoma caeruleum (male): alternating blue and orange-red bars on the sides, dark saddles on an olive back, first dorsal banded red with blue edges, blue anal fin |
| greenside darter | swim 36x22 | y 198-258, speed 14 | Etheostoma blennioides: big green darter, rounded overhanging snout, olive with W-shaped dark green blotches along the side, small dark saddles, bright green fins in males |
| redline darter | swim 32x22 | y 200-258, speed 14 | Etheostoma rufilineatum: olive-tan with rows of red dots forming lines, two dark bars on the cheek below the eye, dark side blotches, orange-red fins with dark bands in males |
| tangerine darter | swim 40x24 | y 190-256, speed 16 | Percina aurantiaca: big darter, bright orange-yellow lower body (male), black lateral stripe of joined blotches, olive back with dark saddles, a row of small dark spots above the stripe |
| fantail darter | swim 34x24 | y 204-258, speed 12 | Etheostoma flabellare: tan with dark bars and rows of dark dots forming thin lines, low first dorsal with gold knobs on the spine tips (male), large rounded fan-shaped tail with dark bands |
| tessellated darter | swim 32x20 | y 204-258, speed 12 | Etheostoma olmstedi: straw-coloured with small dark X and W marks scattered along the sides (tessellated), faint dark saddles, a dark bar running down from the eye |
| central stoneroller | swim 44x26 | y 180-256, speed 18 | Campostoma anomalum: cylindrical algae-scraping minnow, brown-olive with scattered dark scales, blunt snout over a hard lower jaw, orange and black bands across the dorsal and anal fins in breeding males |
| bluehead chub | swim 46x28 | y 80-230, speed 22 | Nocomis leptocephalus: stout chub, olive back, brassy sides with dark-edged scales, a blue head with a swollen crest in breeding males, rosy lower sides, faint dark caudal spot |
| creek chub | swim 48x28 | y 60-220, speed 24 | Semotilus atromaculatus: big-mouthed chub, olive back, dusky lateral stripe ending in a black caudal spot, a black spot at the front base of the dorsal fin, dark-edged scales, rosy flanks in breeding males |
| fallfish | swim 56x28 | y 30-200, speed 26 | Semotilus corporalis: the largest native minnow of the east, silvery with a dark crescent at the base of every scale (a cross-hatched look), olive-brown back, plain fins |
| northern hog sucker | swim 48x24 | y 200-258, speed 14 | Hypentelium nigricans: broad flat head concave between the eyes, body tapering behind, brown-olive with four or five dark oblique saddles, large fan-like pectoral fins, sucker lips under the snout |
| white sucker | swim 54x26 | y 180-256, speed 16 | Catostomus commersonii: cylindrical sucker, olive-grey back, cream-silver sides, thick-lipped mouth under the snout, breeding males with a dark lateral band over a rosy stripe |
| river redhorse | swim 60x30 | y 170-256, speed 16 | Moxostoma carinatum: large heavy sucker, bronze-gold body with a dark crescent at the base of each scale, big head, brick-red tail, dorsal and anal fins |
| longear sunfish | swim 40x30 | y 80-220, speed 16 | Lepomis megalotis: very deep and colourful, orange belly and breast, turquoise wavy lines over the cheek, long black ear flap with a pale red-white edge, sides orange flecked with blue-green |
| rock bass | swim 44x30 | y 130-240, speed 16 | Ambloplites rupestris: deep, big-mouthed, bright red eye, olive-bronze with rows of dark spots (one per scale) forming lines, dark mottling, a dark spot on the gill cover, large rounded soft dorsal and anal |
| smallmouth bass | swim 60x30 | y 60-230, speed 24 | Micropterus dolomieu: bronze-brown bass with faint dark vertical bars, three dark bars radiating back from the red-orange eye, notched dorsal, emarginate tail |
| logperch | swim 46x22 | y 196-258, speed 16 | Percina caprodes: long darter with a pig-like conical snout, yellow-olive body with 15-20 tiger bars alternating long and short, orange band on the first dorsal in males |
| walleye | swim 66x28 | y 120-250, speed 20 | Sander vitreus: long olive-gold percid, five dark saddles, big glassy eye, sharp teeth, a black blotch at the rear base of the spiny dorsal, white tip on the lower tail lobe |
| sauger | swim 60x26 | y 140-254, speed 18 | Sander canadensis: like the walleye but brassy-brown with three or four distinct blotchy saddles, rows of black spots on the spiny dorsal, no white tail tip |
| muskellunge | swim 80x28 | y 20-200, speed 16 | Esox masquinongy: very long pike with a duckbill snout, dorsal and anal fins set far back, olive-bronze with dark vertical bars, pale belly, dark spots on the reddish-bronze fins, forked tail |
| american shad | swim 60x30 | y 20-180, speed 30 | Alosa sapidissima: deep, compressed, silvery herring with a greenish-blue back, a black shoulder spot followed by a row of smaller spots, saw-edged belly, deeply forked tail |
| american brook lamprey | swim 48x16 | y 220-258, speed 10 | Lethenteron appendix: eel-like, no paired fins, an oval sucking disc for a mouth, a row of seven gill pores behind the eye, two low dorsal fins running into the tail fin, grey-brown back, pale belly |
| northern madtom | crawl 36x14 | floor, speed 8 | Noturus stigmosus: small madtom catfish, tan with bold dark saddles under the dorsal, over the adipose and at the tail base, mottled head, adipose fin joined to the tail, barbels, dark-banded fins |
| stonecat | crawl 44x16 | floor, speed 8 | Noturus flavus: plain yellowish grey-brown catfish, flat head, square tail with a pale edge, long low adipose keel running into the tail, pale-edged fins, barbels |
| mottled sculpin | crawl 36x16 | floor, speed 6 | Cottus bairdii: big flat head, huge fan pectorals, body tapering to the tail, brown mottled with two or three dark saddles, spiny first dorsal with a dark spot and an orange edge in males, eyes high on the head |
| hellbender | crawl 58x16 | floor, speed 5 | Cryptobranchus alleganiensis: the existing hellbender drawing is kept (by request) and re-mapped onto the forest-stream ramp (moss-brown shadows, olive-brown midtones, warm sun-fleck highlights) with the BW outline rule |
| mudpuppy | crawl 46x16 | floor, speed 6 | Necturus maculosus: existing drawing kept and re-mapped onto the forest-stream ramp; the red external gills stay a red signature |
| appalachian brook crayfish | crawl 52x14 | floor, speed 10 | Cambarus bartonii: stream crayfish with a short broad rostrum, olive-tan to brown with darker mottling, broad heavy claws |
| rusty crayfish | crawl 52x14 | floor, speed 10 | Faxonius rusticus: grey-green to brown crayfish with a rusty-red spot on each side of the carapace, big claws with a black band near the tips and orange fingertips |
| eastern musk turtle | crawl 32x14 | floor, speed 6 | Sternotherus odoratus (stinkpot): small, high-domed smooth carapace dark olive-brown to black, two pale yellow stripes on the side of the head (above and below the eye), pointed snout with chin barbels, small plastron |
| silty hornsnail | crawl 28x20 | floor, speed 2 | Pleurocera hornsnail of silty runs: long horn-shaped conical shell, smooth with fine growth lines and faint brown spiral bands, dulled by a silt film, dark aperture, grey foot and slender tentacles; the shell stays fixed while the foot glides |

## Scenes
`scenes/creatures/freshwater/forest_stream/fs_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/fs_aquarium.tscn`.
