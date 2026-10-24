# Forest Stream - creature style (prefix `fs_`)

Biome look: a shaded Appalachian forest stream - clear water under a leaf canopy, riffles over cobble, sun flecks breaking
through. The roster is the eastern North American stream fauna: daces, shiners and chubs, suckers, darters, sunfish and bass,
percids, pike, shad, lamprey, madtoms, sculpin, giant salamanders, crayfish, a musk turtle and a hornsnail.

In October 2026 the creatures were redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier fs sprite,
size, texture or colour was used. Exception, by request: the hellbender and mudpuppy keep their earlier drawings, re-mapped onto
the forest-stream colours and re-outlined with the BW outline rule (the mudpuppy's red gills stay a signature colour).

Style v2 (October 2026, after the ac / bw / pf study, as in clear spring): the roster was re-rendered with softer translucent
fins, a lighter outline and warmer highlights, and every swimmer got its own swimming gait (see "Swimming gait" below). Anatomy,
markings and colours per species are unchanged; 13 frame sizes changed with the new fin motion (madtom and stonecat became
flatter). Part-built and kept animals (salamanders, crayfish, turtle, snail) only take the warmer highlights.

Style v3 (October 2026): smoothness and fit to the water, as in clear spring. The forest stream showed the same three gaps:
bodies read as stacked horizontal stripes with uneven stair runs (13% of contour steps vs 0% in bw), several species packed fine
repeats (1 px checker scale rows, checker fin bands, barcode spots), and 45% of the fish pixels sat in the ochre / gold /
yellow-olive band between the water's own green and its complement, so many fish looked pasted onto the tank. v3 renders each
body as one volume with clean silhouettes, colours every species from colour families derived from the green water, and
redesigns every species as one memorable set (body shape + fin set + barbels / filaments + pattern + colour). Motion (the
swimming gaits) is unchanged. The hellbender and mudpuppy still keep their earlier drawings, now re-mapped onto a colour family;
the crayfish, turtle and snail keep their part-built drawings and take family colours.

## Water and colour families (v3)
- The background is one leaf-green hue (OKLab hue 150) at chroma about 0.09: L 0.74 at the surface, 0.68 at mid depth, 0.58-0.50
  in the low water and 0.42-0.46 just above the floor (0.68 on average). Roots and the floor are dark moss green and brown; dark
  roots and red-brown twigs are the only warm colours in the scene.
- Every creature brackets the water. Swimmers: lit parts +0.15 above the average water lightness, body tones -0.20 below it, the
  outline -0.40. Crawlers, measured against the floor water (L about 0.43): lit +0.17, body -0.06, outline -0.16. Swimmers of the
  bottom bands sit over darker water and start one third to one tone step lighter on their ramp (longnose dace, mudminnow, the
  darters, hog sucker, white sucker, logperch, sauger, and the madtom and sculpin on the floor).
- Hue rule: bodies are either analogous to the water (within 45 deg: moss olive, river green, pool teal) or neutral (pearl,
  charcoal); warm complements (over 110 deg: copper, rust, rose) are muted on bodies and saturated only as accents (fins,
  breasts, spots, eyes); turquoise sits at the analogous edge and is used as an accent. Gold, ochre, yellow-olive and blue (45-110
  deg from the water) are not used on bodies: the walleye's olive-gold became moss olive, the river redhorse's bronze-gold and the
  smallmouth's bronze became copper-brown, the bluehead chub's blue head became turquoise and yellow fins became pale olive or
  rust. Body chroma stays at about a third of the water's (0.34; cs 0.53, bw 0.61, ac 0.33).
- Colour families (6 tones dark to light at L 0.26 0.37 0.48 0.60 | 0.82 0.93, so body tones end below the water's average and lit
  tones start above it; generator `pal.FAM_FS`):

| Family | Tones | Use |
|---|---|---|
| G1 moss olive | #22270f #3d4324 #5b623e #7d8563 #c2c8ae #e6eadc | blacknose and longnose dace backs, redbelly dace, mudminnow, tangerine darter, stoneroller and bluehead chub backs, hog sucker, white sucker back, rock bass, logperch, walleye, sculpin, appalachian brook crayfish, musk turtle |
| G2 river green | #122a18 #2c4732 #49664f #6e8872 #b7caba #e1ebe3 | rosyside dace and warpaint shiner backs, greenside darter, creek chub and fallfish backs, longear sunfish, muskellunge |
| G3 pool teal | #0d2a26 #2a4642 #4b6360 #6f8682 #b7c9c6 #e0ebe9 | rosyside and warpaint flanks, rosyface shiner, studfish, fallfish flank, shad back, mudpuppy (one step darker) |
| N1 pearl / charcoal | #27231e #433f39 #615d56 #848078 #c7c3bd #ebe7e2 | bellies, tessellated darter, redline and fantail flanks, bluehead chub, creek chub and white sucker flanks, sauger, stonecat, lamprey, rusty crayfish |
| R1 copper | #381b10 #5d3324 #7f503f #9e7564 #cbc2bc #ebe7e4 | longnose dace and rainbow darter flanks, redline and fantail backs, stoneroller flank, river redhorse, smallmouth bass, madtom, hellbender (one step darker), hornsnail |
| R2 rust red | #460b06 #721d14 #9d3629 #c65b4c #f9aea2 #ffdfd8 | redbelly dace belly, saffron shiner, tangerine darter lower body, longear breast; red fins and fin bands, red spots |
| R3 rose | #420e1b #6d2032 #9c334b #c4576d #f8acb7 #ffdee2 | rosyside dace patch, rosyface shiner head, bluehead chub lower sides, white sucker breeding stripe |
| T1 turquoise | #002c2d #004c4d #006e6f #0f9293 #8dd3d2 #d2efee | bluehead chub head, longear cheek lines, rainbow darter bars and fins |

- Shadows lean to moss brown (#1e2c1c) and the outline tint is #121a10 (both unchanged); highlights are cool leaf-white (#eef6ec)
  instead of the warm sun-fleck cream (#f8ecbe), and midtones take a faint green cast (#88b890, about 8%). Colours not taken from
  a family (accents, eyes, a few part-built details) are fitted the same way by the generator: kept out of the water band and
  steered out of the gold / yellow-olive band.
- Signature accents keep their own colour: redbelly / saffron / tangerine reds, warpaint red snout and gill bar, rosyside /
  rosyface / bluehead rose, studfish rust chains, rainbow darter turquoise bars, redline darter red lines, bluehead chub turquoise
  head, longear breast and cheek lines, rock bass red eye, river redhorse brick-red fins, stoneroller and logperch orange fin
  bands, sculpin orange dorsal edge, walleye white tail tip, mudpuppy red gills, rusty crayfish spots and claw tips.
- Translucent fins keep the body's own hue with only a light green tint (#bcd4b0, about 15%); alpha falls from about 185 at the
  base to about 110 at the edge in fine steps of 12, and the clear membrane lightens slightly toward the free edge. Fin rays are
  sparse (about every third pixel), only about 0.09 darker than the membrane and fade out toward the edge. Clear fins get a faint
  light rim; coloured signature fins a slightly deeper rim of their own hue and a little more opacity. Fin markings (bands, spots)
  run through the margin.

## Rendering (v3: smooth, as in bw)
- One volume per body: in every column the value only falls away from the brightest pixel (upward to the back, downward to the
  belly) - no light/dark/light stripes. Deep bodies get a one-step darker inner rim. Signature patches (breasts, heads) stay at mid
  depth: never washed out, never muddy.
- Tone zones are cleaned: no 1-2 px islands or notches between tones. Near-duplicate colours are merged (OKLab distance under
  0.016), about 32 opaque colours per sprite (bw: 28).
- Silhouettes follow pixel-art curves: on each side of the crest the stair runs are ordered so the slope changes steadily
  (1-2-3-5-8, not 4-2-2-5-3); stair corners are no longer cut.
- Outline: each edge pixel is a darker shade of the colour just inside it, tinted toward #121a10; lit top edge (about 20% darker),
  sides about 38%, belly edge about 58% with the row above it pulled down.
- Markings: at most two or three motifs per species, nothing finer than 2 px except one defining line, repeats spaced at least their
  own width; no 1 px checkers. Lines that run along the body are drawn straight; spots are scattered naturally, not on a grid.
- Heads are clean: no mouth line and no dark gill line. Eyes: highlight pixel above a dark pupil, iris colour on the back side,
  a dark socket pixel under the pupil; large fish use a one-step wider eye.
- Every species is one memorable set - body shape + fin set + barbels / filaments + pattern + colour - listed in the species notes.
- Pelvic fins hang below the belly behind the pectorals.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 25 deg (small), 20-22 deg (darters), 15 deg (deep), 8-14 deg (long).
  Body and markings stay fixed; only fins, tail, barbels and ribbon fins move, in the species' gait (next section); bottom fish
  flick the tail fore-and-aft so they stay on the floor. Detached 1-6 px specks are removed from every frame.
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (the snail uses crawl_R, crawl_L, idle_R, idle_L); the rest pose touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `fs_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a matching
  `fs_<name>.aseprite` (one layer, one tag per row, 0.12 s frames).

## Swimming gait
Each swimmer moves the way its kind swims (as in the ac / bw / pf references): which fins move, how, and the scene's
`animation_fps` come from a gait table in the sprite generator.

| Gait | Motion | fps | Species |
|---|---|---|---|
| riffle | holds station in the current: pectorals spread and flap, short quick tail beat | 9-10 | blacknose dace, longnose dace (9, bigger pectorals) |
| dart | only the caudal lobe tips flick | 10-11 | southern redbelly dace, saffron shiner, rosyface shiner (11) |
| cruise | tail-led, dorsal and anal flutter only at the rear tips | 8-10 | rosyside dace (10), central stoneroller, bluehead chub, creek chub (9) |
| tetra | tail plus the whole (coloured) dorsal and anal fins sway | 10 | warpaint shiner |
| killi | rear-set dorsal and anal swing with the tail | 8 | northern studfish |
| hover | sculls with the pectorals, rear-set fins sway as a unit | 7 | central mudminnow |
| darter | pectorals flap, dorsal margins ripple, short tail beat | 7-9 | rainbow darter, greenside darter (7, bigger pectorals), redline darter (9), tangerine darter (wider tail), fantail darter (stronger dorsal ripple), tessellated darter (7), logperch |
| sucker | hugs the bottom, big pectorals fan, slow beat | 6-7 | northern hog sucker, white sucker, river redhorse (7) |
| sunfish | soft dorsal and anal margins ripple, pectorals scull | 6-7 | longear sunfish, rock bass (6), smallmouth bass (wider tail) |
| stalker | spiny and soft dorsals ripple, tail barely moves | 6-7 | walleye (6), sauger (7) |
| power | wide tail beat, other fins quiet | 8-9 | fallfish (8), american shad |
| gar | lurks: rear-set dorsal and anal move with the tail, pectorals scull | 5 | muskellunge |
| eel | the low dorsal fins and tail ripple as one strip (the body itself does not bend) | 8 | american brook lamprey |

## Roster (40 species: 31 swimmers, 9 crawlers)
Darters live on the bottom but are swimmers in the lowest band; the madtom, stonecat, sculpin, salamanders, crayfish, turtle and
snail walk on the floor.

| Group | Species (frame) |
|---|---|
| Small minnows, topminnow and darters | blacknose dace 36x24, longnose dace 38x24, southern redbelly dace 34x24, rosyside dace 38x26, warpaint shiner 38x28, saffron shiner 34x24, rosyface shiner 36x24, northern studfish 38x26, central mudminnow 34x24, rainbow darter 32x20, greenside darter 36x22, redline darter 32x20, tangerine darter 40x24, fantail darter 34x24, tessellated darter 32x20 |
| Medium and large swimmers | central stoneroller 44x28, bluehead chub 46x28, creek chub 48x28, fallfish 56x30, northern hog sucker 48x26, white sucker 54x26, river redhorse 60x32, longear sunfish 40x30, rock bass 44x32, smallmouth bass 60x32, logperch 46x24, walleye 66x28, sauger 62x26, muskellunge 80x28, american shad 60x32, american brook lamprey 48x16 |
| Bottom dwellers and crawlers | northern madtom 38x12, stonecat 46x14, mottled sculpin 38x16, hellbender 58x16, mudpuppy 46x16, appalachian brook crayfish 52x14, rusty crayfish 52x14, eastern musk turtle 32x14, silty hornsnail 28x20 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining set (v3: shape / fins / barbels / pattern / colour) |
|---|---|---|---|
| blacknose dace | swim 36x24 | y 60-220, speed 26 | slender riffle minnow / moss-olive back, pearl belly / bold BLACK BAND from the snout through the eye to the tail / a rust-orange breeding stripe under the band / clear olive fins, forked tail |
| longnose dace | swim 38x24 | y 170-256, speed 22 | cylindrical riffle dweller with a long FLESHY SNOUT over the mouth / olive back, copper flank with a few dark MOTTLES / red lips and red-based pelvic fins / big paddle pectorals |
| southern redbelly dace | swim 34x24 | y 40-200, speed 26 | small minnow / moss back / TWO BLACK STRIPES (thin upper, broad lower) split by a pale cream stripe / SCARLET belly / cream fins with red-tinted pelvics |
| rosyside dace | swim 38x26 | y 40-200, speed 28 | deeper big-mouthed dace / river-green back, pool-teal silver flank / a ROSE PATCH on the lower flank / one faint dark lateral stripe / clear teal fins |
| warpaint shiner | swim 38x28 | y 30-190, speed 28 | deep silvery shiner / river-green back, pool-teal flank / the WAR PAINT - red snout and a red bar on the upper gill cover / black shoulder bar / dorsal crossed by a black band / dark tail margin |
| saffron shiner | swim 34x24 | y 40-200, speed 28 | the RED-HOT minnow - breeding male glowing rust-red over flank and every fin / dark moss back / dusky lateral stripe ending in a dark tail spot |
| rosyface shiner | swim 36x24 | y 20-170, speed 30 | slender pointed shiner / pool-teal silver / a ROSE HEAD (breeding) / one thin dark lateral line / dark stripe along the top of the back / clear teal fins |
| northern studfish | swim 38x26 | y 4-110, speed 22 | big flat-headed topminnow / pool-teal back and flank / CHAINS of rust-red spots in two rows / rust-orange fins with a dark edge / dorsal set far back |
| central mudminnow | swim 34x24 | y 170-250, speed 14 | chunky cylindrical mudminnow / dark moss olive with three faint bars / a bold BLACK BAR across the tail base / rounded fins, dorsal set far back over the anal |
| rainbow darter | swim 32x20 | y 200-258, speed 14 | the RAINBOW - copper flank crossed by four TURQUOISE bars / dark saddles on a moss back / first dorsal banded red with a turquoise edge / turquoise anal fin |
| greenside darter | swim 36x22 | y 198-258, speed 14 | big GREEN darter with a rounded overhanging snout / river-green body with five dark green V-BLOTCHES / small saddles / bright green fins |
| redline darter | swim 32x20 | y 200-258, speed 14 | pale copper darter with two continuous RED LINES along the side / four dark side blotches / two dark bars on the cheek / rust-red fins with a dark band |
| tangerine darter | swim 40x24 | y 190-256, speed 16 | the BIG darter / moss back with dark saddles / bold BLACK STRIPE of joined blotches / glowing TANGERINE-RED lower body / emarginate tail |
| fantail darter | swim 34x24 | y 204-258, speed 12 | pale pearl-tan darter with five soft bars / low first dorsal with PALE KNOBS on the spine tips / a big rounded FAN TAIL crossed by dark bands |
| tessellated darter | swim 32x20 | y 204-258, speed 12 | pale straw darter speckled with small dark TESSELLATION marks / three faint saddles / a dark TEARDROP bar under the eye / clear pale fins |
| central stoneroller | swim 44x28 | y 180-256, speed 18 | cylindrical algae scraper with a blunt snout over a hard jaw / moss back, brown-copper flank with a few dark scales / the breeding FINS - dorsal crossed by a rust-orange band and a black band, rust band on the anal |
| bluehead chub | swim 46x28 | y 80-230, speed 22 | stout chub / moss back, pearl flank / a TURQUOISE HEAD with a swollen crest (breeding) / ROSE lower sides / faint dark spot on the tail base / moss fins |
| creek chub | swim 48x28 | y 60-220, speed 24 | big-mouthed chub / river-green back, pearl flank / dusky LATERAL STRIPE ending in a black CAUDAL SPOT / a black SPOT at the front base of the dorsal / teal fins |
| fallfish | swim 56x30 | y 30-200, speed 26 | the BIG silver minnow / river-green back, pearl-teal flank / two loose rows of dark scale CRESCENTS on the upper side / plain teal fins, big forked tail |
| northern hog sucker | swim 48x26 | y 200-258, speed 14 | broad FLAT head with a concave crown, body tapering behind / olive-brown with four bold dark OBLIQUE SADDLES / huge FAN pectorals / sucker lips under the snout |
| white sucker | swim 54x26 | y 180-256, speed 16 | long cylindrical sucker with thick lips / moss back, pearl flank / a dark LATERAL BAND riding over a ROSE STRIPE (breeding) / pale fins |
| river redhorse | swim 60x32 | y 170-256, speed 16 | big heavy sucker / copper-bronze body with two loose rows of dark scale crescents / BRICK-RED tail, dorsal and anal / big head, sucker lips |
| longear sunfish | swim 40x30 | y 80-220, speed 16 | the COLOURFUL sunfish / river-green back over a rust-orange BREAST / TURQUOISE wavy cheek lines / long black EAR FLAP with a pale rim / orange flecks along the side / orange anal and pelvics |
| rock bass | swim 44x32 | y 130-240, speed 16 | deep big-mouthed panfish / dark moss-olive with two lines of dark spots / a blazing RED EYE / dark spot on the gill cover / big rounded soft dorsal and anal |
| smallmouth bass | swim 60x32 | y 60-230, speed 24 | copper-bronze bass / six faint vertical bars / three dark BARS RADIATING back from the orange eye / notched spiny + soft dorsal, emarginate tail |
| logperch | swim 46x24 | y 196-258, speed 16 | long darter with a PIG-LIKE conical snout / pale moss body / TIGER BARS alternating long and short / a rust-orange band on the first dorsal / big paddle pectorals |
| walleye | swim 66x28 | y 120-250, speed 20 | long moss-olive percid / five dark SADDLES / big pale GLASSY EYE / a black blotch at the rear of the spiny dorsal / WHITE TIP on the lower tail lobe |
| sauger | swim 62x26 | y 140-254, speed 18 | the walleye's sandy cousin / four BLOTCHY dark saddles / rows of black SPOTS on the spiny dorsal / no white tail tip / glassy eye |
| muskellunge | swim 80x28 | y 20-200, speed 16 | very long DUCKBILL pike, dorsal and anal set far back / river-green with seven dark vertical BARS / pale belly / rust-bronze fins with dark SPOTS / forked tail |
| american shad | swim 60x32 | y 20-180, speed 30 | deep silver HERRING / pool-teal back over a pearl flank / a black SHOULDER SPOT followed by a row of four smaller spots / saw-edged belly / DEEPLY forked tail |
| american brook lamprey | swim 48x16 | y 220-258, speed 10 | EEL-like lamprey with no paired fins / charcoal-grey back, pale belly / a short row of GILL PORES behind the eye / oval sucking-disc mouth / two low dorsal fins running into the tail fin |
| northern madtom | crawl 38x12 | floor, speed 8 | small madtom catfish / sand-copper with THREE bold black SADDLES (under the dorsal, over the adipose, at the tail base) / dark-mottled head / a dark crescent across the rounded tail / pale barbels |
| stonecat | crawl 46x14 | floor, speed 8 | plain grey catfish with a flat head / a PALE NAPE SADDLE in front of the dorsal and a small pale blotch behind it / long low adipose KEEL running into a square tail with a PALE MARGIN / pale barbels |
| mottled sculpin | crawl 38x16 | floor, speed 6 | big FLAT head with high eyes, body tapering to the tail / olive with three dark SADDLES and soft mottling / huge FAN pectorals crossed by dark BARS / spiny first dorsal with a black spot and an ORANGE EDGE |
| hellbender | crawl 58x16 | floor, speed 5 | the existing hellbender drawing (kept by request) - big flat wrinkled salamander, re-mapped onto the copper-brown family: rust-brown body, dark blotches, pale-grey skin folds |
| mudpuppy | crawl 46x16 | floor, speed 6 | the existing mudpuppy drawing (kept) re-mapped onto the pool-teal family - slate-teal body with dark spots - so the RED feathery gills stand out as the signature |
| appalachian brook crayfish | crawl 52x14 | floor, speed 10 | stream crayfish with a short broad rostrum / OLIVE with darker MOTTLING over the carapace and tail / BROAD heavy claws with brown fingertips |
| rusty crayfish | crawl 52x14 | floor, speed 10 | slim grey crayfish / a RUSTY-RED SPOT on each side of the carapace / big claws with a BLACK BAND near the tips and ORANGE fingertips / long rostrum |
| eastern musk turtle | crawl 32x14 | floor, speed 6 | small HIGH-DOMED smooth dark olive shell / dark head with TWO PALE STRIPES (above and below the eye) / pointed snout with chin barbels / small pale plastron |
| silty hornsnail | crawl 28x20 | floor, speed 2 | long HORN-shaped conical shell in copper-brown / dark SPIRAL BANDS and pale growth flecks / dark aperture / grey foot and slender tentacles; the shell stays fixed while the foot glides |

## Scenes
`scenes/creatures/freshwater/forest_stream/fs_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/fs_aquarium.tscn`.
