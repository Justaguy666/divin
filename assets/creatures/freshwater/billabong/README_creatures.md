# Billabong - creature style (prefix `bb_`)

Biome look: a northern-Australian tropical billabong (oxbow waterhole) - tea-and-teal water over red-ochre sandy clay, paperbark
and pandanus roots, giant waterlilies. The roster gathers the region's freshwater fauna: rainbowfish, blue-eyes, glassfish,
gudgeons and a hardyhead; grunters, archerfish, the mouth almighty, bony bream, eel-tailed and fork-tailed catfish, longtom and
garfish, barramundi, saratoga, tarpon, the lungfish and the freshwater sawfish; on the floor the freshwater whipray, the Arafura
file snake, cherabin, glass shrimp, redclaw, the tadpole shrimp, a river snail and four turtles.

In October 2026 every creature was redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier bb sprite,
size, texture or colour was used.

## Lighting and palette (applied while drawing, not as a post grade)
- Shadows lean to deep tea-teal (#1a2824), midtones take a faint red-ochre clay cast (#b08060, about 7%), highlights lean to warm
  sun-bleached sand (#f6ecd2).
- Bodies lean to silver, olive, brass and warm browns; signature colours are ungraded (rainbowfish stripes and red fin margins,
  blue-eye irises and banded fins, gudgeon red and blue fin bands and purple spots, spangled perch rust spots, barramundi amber-red
  eye, saratoga red scale crescents, salmon-tailed catfish tail, cherabin blue claws, redclaw red claw margin, Mary River turtle
  algae).
- Translucent fins are tinted toward pale water-sage (#c4d2c0, about 35%) with alpha falling from about 185 at the base to about
  110 at the edge; fin rays are darker strokes every second pixel (every third on the long rainbowfish fins), including the
  leading edge.

## Rendering (matches the BW reference)
- Body value: brightest in the upper third, slightly darker toward the back edge and the ends, stepping darker toward the belly in
  4-5 contour-following bands.
- Outline: a darker shade of the colour just inside each edge pixel, tinted toward #121c18; lit top edge, darker sides, darkest
  belly edge with the row above it pulled down. Stair-corner nubs are removed.
- Markings are flat colours or a fixed number of body tones darker; fish eyes are a warm highlight over a dark pupil with iris
  pixels behind and a dark socket below.
- Pelvic fins hang below the belly (from this biome on the shared fin builder no longer folds them up into the body).
- Special cases: the sawfish rostrum carries 1 px rostral teeth standing just outside its edges; the bony bream and tarpon
  trailing dorsal ray is a single fine filament; the whipray is a flat disc seen slightly from above, thick at the head end and
  thin at the wing margins, which ripple; the glass shrimp is made see-through after rendering (body alpha about 130, outline
  about 190, the black eye stays opaque).

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 18-25 deg (small), 12-15 deg (deep-bodied), 8-10 deg (long fish).
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (the snail uses crawl_R, crawl_L, idle_R, idle_L); every frame touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `bb_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a
  matching `bb_<name>.aseprite` (one layer, one tag per row, 0.12 s frames).

## Roster (40 species: 29 swimmers, 11 crawlers)

| Group | Species (frame) |
|---|---|
| Small swimmers | checkered rainbowfish 38x26, western rainbowfish 38x26, exquisite rainbowfish 38x24, black banded rainbowfish 38x24, delicate blue eye 30x22, pacific blue eye 32x24, spotted blue eye 32x22, sailfin glassfish 36x26, empire gudgeon 34x22, purple spotted gudgeon 34x22, midgleys carp gudgeon 32x20, fly specked hardyhead 34x24 |
| Medium and large swimmers | spangled perch 46x28, banded grunter 44x28, sooty grunter 54x34, seven spot archerfish 46x28, primitive archerfish 42x24, mouth almighty 42x26, bony bream 48x28, hyrtls tandan 50x20, rendahls catfish 42x18, salmon tailed catfish 62x26, freshwater longtom 64x22, snub nosed garfish 50x20, barramundi 66x34, northern saratoga 66x26, oxeye tarpon 64x30, australian lungfish 70x24, freshwater sawfish 88x28 |
| Bottom crawlers (ray, snake, prawns, crayfish, triops, snail, turtles) | freshwater whipray 66x10, arafura file snake 70x10, cherabin 64x20, glass shrimp 30x10, redclaw crayfish 52x14, tadpole shrimp 32x8, notopala river snail 24x16, northern snake necked turtle 50x12, northern snapping turtle 40x14, pig nosed turtle 38x10, mary river turtle 42x12 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining features |
|---|---|---|---|
| checkered rainbowfish | swim 38x26 | y 40-200, speed 24 | Melanotaenia splendida inornata: deep arched rainbowfish, silvery-olive to golden with a dark edge on every scale (a checkered look), faint orange stripes, yellowish fins with red margins |
| western rainbowfish | swim 38x26 | y 40-200, speed 24 | Melanotaenia australis: yellow-silver with a dark mid-lateral stripe and thin orange-red stripes between the scale rows, red fins |
| exquisite rainbowfish | swim 38x24 | y 30-190, speed 26 | Melanotaenia exquisita: slender, iridescent blue-silver, a black mid-lateral stripe, fins yellow with red margins |
| black banded rainbowfish | swim 38x24 | y 50-210, speed 24 | Melanotaenia nigrans: olive-brown back, golden sides, a bold black band along the middle, fins yellow to red with a dark edge |
| delicate blue eye | swim 30x22 | y 0-90, speed 24 | Pseudomugil tenellus: tiny translucent golden-olive fish with a bright blue upper eye, yellow-and-black edged fins in males |
| pacific blue eye | swim 32x24 | y 0-100, speed 24 | Pseudomugil signifer: golden-yellow little fish with a blue eye, males with long dorsal and anal fins banded black and yellow |
| spotted blue eye | swim 32x22 | y 0-110, speed 22 | Pseudomugil gertrudae: yellowish body with dark-edged scales, blue eye, yellow fins covered in black spots |
| sailfin glassfish | swim 36x26 | y 60-210, speed 18 | Ambassis agrammus: deep compressed glassy fish, translucent silver body with the dark spine showing through, a tall spiny "sail" dorsal edged dark, silvery belly and gill |
| empire gudgeon | swim 34x22 | y 120-245, speed 16 | Hypseleotris compressa (male): compressed gudgeon, dark olive body with golden flecks and orange-red spots, two dorsals and an anal banded red with blue-white edges |
| purple spotted gudgeon | swim 34x22 | y 190-256, speed 12 | Mogurnda adspersa: stout purple-brown gudgeon with rows of red-orange and blue-violet spots, dark streaks below the eye, fins with red-orange edges and blue lines |
| midgleys carp gudgeon | swim 32x20 | y 130-245, speed 16 | Hypseleotris sp. (Midgley's): small translucent olive-tan gudgeon, faint dark marks along the side, males with orange-red dorsal and anal fins edged white |
| fly specked hardyhead | swim 34x24 | y 0-120, speed 28 | Craterocephalus stercusmuscarum: slim silvery-green fish peppered with dark "fly specks", a bright silver stripe along the side, two small dorsal fins |
| spangled perch | swim 46x28 | y 60-230, speed 20 | Leiopotherapon unicolor: hardy grunter, silvery-olive peppered with small rust-brown spots (spangles), dusky fins |
| banded grunter | swim 44x28 | y 70-230, speed 18 | Amniataba percoides: silvery-yellow grunter with six to eight dark vertical bars and a black blotch on the spiny dorsal |
| sooty grunter | swim 54x34 | y 110-245, speed 16 | Hephaestus fuliginosus: big deep grunter, uniformly sooty dark brown to black, thick lips, dark fins |
| seven spot archerfish | swim 46x28 | y 0-90, speed 18 | Toxotes chatareus: flat-topped archerfish with a big eye and upturned mouth, silvery white with six or seven black blotches along the upper side (big and small alternating), dorsal set far back over the anal |
| primitive archerfish | swim 42x24 | y 0-100, speed 18 | Toxotes lorentzi: slimmer archerfish, olive-gold with rows of small dark spots along the upper side, dusky dorsal and a dark band at the tail base |
| mouth almighty | swim 42x26 | y 150-250, speed 10 | Glossamia aprion: cardinalfish with a huge head and mouth, mottled yellow-brown, dark streaks radiating from the eye, two dorsals, rounded tail |
| bony bream | swim 48x28 | y 30-200, speed 24 | Nematalosa erebi: deep compressed herring, dark back, silvery sides with faint lines, a dark spot behind the gill, blunt snout, deeply forked tail, a trailing filament on the last dorsal ray |
| hyrtls tandan | swim 50x20 | y 200-258, speed 12 | Neosilurus hyrtlii: eel-tailed catfish, body tapering to a point with one continuous fin round the tail, four pairs of barbels, grey-brown to yellowish, short spined first dorsal, no adipose |
| rendahls catfish | swim 42x18 | y 200-258, speed 12 | Porochilus rendahli: small eel-tailed catfish, translucent pinkish-brown, long low fin fringe round the tail, short barbels |
| salmon tailed catfish | swim 62x26 | y 180-256, speed 16 | Neoarius graeffei: fork-tailed catfish, blue-grey back and silver sides, bony head shield, salmon-pink tail, adipose fin, three pairs of barbels |
| freshwater longtom | swim 64x22 | y 0-60, speed 18 | Strongylura krefftii: needlefish with both jaws drawn out into a long toothed beak, olive-green back, silver sides with a dark stripe, dorsal and anal set far back |
| snub nosed garfish | swim 50x20 | y 0-70, speed 22 | Arrhamphus sclerolepis: halfbeak with only a short lower-jaw beak (snub-nosed), silvery-green with a dark stripe along the side, dorsal set far back |
| barramundi | swim 66x34 | y 80-240, speed 20 | Lates calcarifer: big silver-grey perch with an olive-bronze back, concave head profile, big mouth, glowing amber-red eye, two dorsals (spiny and soft), rounded tail |
| northern saratoga | swim 66x26 | y 0-90, speed 18 | Scleropages jardinii: long bony-tongue fish, gold-olive with a red-orange crescent on each of its big scales, upturned mouth with two small chin barbels, dorsal and anal set far back, large pectorals |
| oxeye tarpon | swim 64x30 | y 20-180, speed 24 | Megalops cyprinoides: bright silver tarpon with a blue-green back, a very big eye, upturned lower jaw, deeply forked tail and a long trailing filament on the last dorsal ray |
| australian lungfish | swim 70x24 | y 200-256, speed 10 | Neoceratodus forsteri: heavy, elongated living fossil, olive-brown with scattered dark spots, big scales, paddle-shaped lobed pectoral and pelvic fins, a pointed tail edged by one continuous fin, pale orange-pink belly |
| freshwater sawfish | swim 88x28 | y 200-256, speed 12 | Pristis pristis: shark-like ray with a long flat saw-snout lined with teeth, yellow-brown to olive-grey, flat head, two big dorsal fins, large pectoral fins, shark-like tail |
| freshwater whipray | crawl 66x10 | floor, speed 6 | Urogymnus dalyensis: huge flat round disc lying on the mud, plain yellowish-brown to grey-brown above with faint darker mottling and a pale cream underside showing along the rim, eyes and spiracles raised on top of the front of the disc, a long thin whip tail trailing far behind; the disc margins ripple as it glides |
| arafura file snake | crawl 70x10 | floor, speed 6 | Acrochordus arafurae: heavy, baggy-skinned aquatic snake lying along the bottom, grey-brown with a darker reticulated network of bands, small flat head with eyes on top, body thickest in the middle and tapering to a short tail |
| cherabin | crawl 64x20 | floor, speed 8 | Macrobrachium spinipes (giant freshwater prawn): arched translucent olive-blue body, long toothed rostrum, banded abdomen ending in a tail fan, very long slender blue second claws held forward, long whip antennae, thin walking legs and swimmerets |
| glass shrimp | crawl 30x10 | floor, speed 8 | Paratya australiensis (glass shrimp): tiny see-through shrimp with faint reddish-brown lines and a dark gut line, black eyes, short toothed rostrum, thin legs and antennae |
| redclaw crayfish | crawl 52x14 | floor, speed 10 | Cherax quadricarinatus: smooth blue-green to olive-blue crayfish with four keels on the head, cream speckles, big blue claws with a bright red patch along the outer margin of each claw |
| tadpole shrimp | crawl 32x8 | floor, speed 10 | Triops australiensis: flat horseshoe-like shield covering the front half, two close-set eyes on top of the shield, many small leaflike legs beating underneath, a segmented abdomen and two long tail filaments; olive-brown with a paler rim |
| notopala river snail | crawl 24x16 | floor, speed 2 | Notopala river snail (viviparid): solid globular shell with a big rounded body whorl, short blunt spire and dark spiral bands on olive-brown, round aperture, grey foot and short tentacles; the shell stays fixed while the foot glides |
| northern snake necked turtle | crawl 50x12 | floor, speed 6 | Chelodina rugosa: broad, flat, oval dark brown carapace with rugose scutes (growth rings) and a ridged rim of marginal scutes, an extremely long, thick, wrinkled neck nearly as long as the shell (dark above, pale cream-grey below, studded with small tubercles), a broad flat head with forward-set eyes and a pale lower jaw, cream plastron; neck folds sideways (side-necked) |
| northern snapping turtle | crawl 40x14 | floor, speed 6 | Elseya dentata: big olive-brown turtle with a broad, moderately domed carapace whose rear edge is serrated, a large head with a strong hooked jaw, cream-yellow lower jaw and throat, grey-olive skin and a cream plastron |
| pig nosed turtle | crawl 38x10 | floor, speed 7 | Carettochelys insculpta: grey-olive leathery shell without scutes, finely pitted, a pale rim; rests low on its plastron and rows with long paddle flippers like a sea turtle's, a fleshy pig-like snout with nostrils at the tip, a pale patch behind the eye |
| mary river turtle | crawl 42x12 | floor, speed 6 | Elusor macrurus: streamlined, elongated brown carapace often carrying green algae tufts, a very long thick tail, two long fleshy barbels under the chin, olive-grey skin with a pinkish throat, cream plastron |

## Audit (`.agents/tools/creature_audit.py freshwater/billabong`)
Swimmer summary within every hint (body aspect 2.52, deep share 0.24, colours 51, L range 72.4); 0/40 dimension mismatches,
0/174 A=C mismatched rows, 0/174 edge-touching rows. The advisory flags (dE_bg on dark or olive fish, hard_step on bold bars and
stripes) were reviewed visually and are intended.

## Scenes
`scenes/creatures/freshwater/billabong/bb_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/bb_aquarium.tscn`.
