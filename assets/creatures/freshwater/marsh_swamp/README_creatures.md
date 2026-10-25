# Marsh Swamp - creature style (prefix `ms_`)

Biome look: a still, weedy marsh and swamp - peat-stained water, reeds and lily pads, soft mud. The roster gathers European,
East Asian and North American wetland animals: bitterlings, sticklebacks, small sunfishes, killifish, carp-family fish, perch and
ruffe, pike and pickerel, eels, snakehead and catfish, loaches and bullhead, newts and the axolotl, a frog tadpole, pond turtles,
a pond snail and the noble crayfish.

In October 2026 the creatures were redrawn from scratch following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), with the species names as the only input: no earlier ms sprite,
size, texture or colour was used. Exception, by request: the axolotl, the two newts and the two turtles keep their earlier
drawings, re-mapped onto the marsh colours and re-outlined with the BW outline rule, with species colours kept as signatures
(axolotl gills, newt bellies, pond-turtle speckles). The newts and the softshell turtle got a one-pixel eye (golden-brown for the
newts, black for the turtle), the softshell turtle's flippers were shortened, and these kept sheets got a 1 px safety margin.

Style v3 (October 2026, after the clear spring and forest stream restyles): marsh swamp skipped the v2 step, so v3 brings both at
once - the softer translucent fins and tail-led motion of v2 with a swimming gait per species (see "Swimming gait"), and the v3
smoothness and fit to the water. The marsh water is dark like bw / ac (L 0.42 on average), but the old roster sat at the water's
own lightness (body +0.02, lit parts only +0.20 vs +0.33 in bw), at 0.8 of its chroma (bw 0.5, ac 0.3) and 84% in its own olive
hue, so most fish melted into the swamp. v3 renders each body as one volume with clean silhouettes, colours every species from
colour families derived from the water, and redesigns every species as one memorable set (body shape + fin set + barbels /
filaments + pattern + colour). The axolotl, newts and turtles still keep their earlier drawings, now re-mapped onto a colour
family; the snail and crayfish take family colours.

## Water and colour families (v3)
- The background is one murky olive-green hue (OKLab hue 130) at chroma 0.05-0.08, dark like bw (0.46) and ac (0.49): L 0.67 at
  the surface, 0.57 in the upper water, 0.52 mid, 0.35 low and 0.29 at the floor (0.42 on average). A dark brown cypress trunk and
  rust cattail heads are the only warm colours.
- As in bw / ac, every creature reads as a lighter shape with a darker outline: swimmers' bodies sit a little above the average
  water (+0.05; bw +0.08), lit parts well above (+0.38; bw +0.33) and the outline below (-0.16; bw -0.13). Crawlers, against the
  floor water (L about 0.29): body +0.07, lit +0.31, outline -0.07. The outline is one step deeper than in cs / fs (dark water).
- Hue rule: analogous to the water (within 45 deg) here means gold, brass, olive and reed green; neutral is pearl, charcoal and
  peat; the complement (over 110 deg) is crimson, rose, violet, indigo and slate - slate and mahogany muted on bodies, crimson,
  rose and indigo saturated only as accents. Orange, amber, rust-orange and cyan / sky blue (45-110 deg from the water) are not
  used on bodies: the bitterlings' teal sheen became indigo, the pygmy and bluespotted sunfish flecks indigo, orange bellies and
  fins crimson or gold. Body chroma stays at about half the water's (0.48 overall; bw 0.47).
- Colour families (6 tones dark to light at L 0.24 0.36 0.48 0.60 | 0.80 0.92; generator `pal.FAM_MS`):

| Family | Tones | Use |
|---|---|---|
| O1 brass olive | #23200b #433e21 #645e3d #87815f #c3bfa3 #e7e5d8 | medaka, banded killifish, ninespine stickleback, golden shiner back, crucian carp, rudd and tench flanks, mandarin fish, grass pickerel, stone loach, softshell turtle (one step darker), pond snail |
| G1 reed green | #172313 #32422d #51644b #75866f #b5c2b1 #e0e7de | stickleback back, bluespotted sunfish, rudd and tench backs, perch, pumpkinseed, european eel, pike |
| Y1 gold (accent) | #281e00 #4a3c00 #6f5c00 #957f23 #d0be79 #ede5c7 | golden shiner flank, mandarin fish flank, gold bellies (pumpkinseed, bullhead, eels), redbelly dace fins, weatherfish stripe, newt belly, turtle speckles |
| N1 pearl / charcoal | #201f1a #3e3d37 #5f5e57 #81807a #bfbeb7 #e5e5e0 | bellies, bitterling and sunbleak silver, pygmy and blackbanded sunfish, paradise fish, black bullhead, fire-bellied newt and pond turtle (one step darker) |
| N2 peat | #261e14 #453b30 #675c4f #897e72 #c5bcb3 #e8e4df | tadpole, ruffe, amur sleeper, asian swamp eel, weatherfish, crested newt and noble crayfish (one step darker) |
| S1 slate | #18202b #333e4c #525f6f #758191 #b5bfcb #e0e5eb | sunbleak back, stickleback flank, wels catfish |
| M1 mahogany | #2e1818 #523432 #775351 #987775 #ccb9b7 #ebe2e1 | snakehead back, european bullhead (one step darker), axolotl |
| R1 crimson (accent) | #40030c #6f1821 #9d343b #c6585d #f2a7a6 #fedbda | stickleback throat, redbelly dace belly, rudd and perch fins, rosy bitterling fins, paradise fish bands and tail, pumpkinseed spots, newt belly, crayfish claws |
| R2 rose (accent) | #360e24 #622344 #8d3d67 #b4608a #e6a9c5 #f8dce8 | rosy bitterling, european bitterling throat, axolotl gills |
| B1 indigo (accent) | #0f1e3b #253c67 #3e5c96 #5f80bc #a5bfec #dae5f9 | bitterling sheen, pygmy and bluespotted sunfish flecks, paradise fish bands and fins, pumpkinseed cheek lines, stickleback eye |

- Shadows lean to peat olive (#1c2012) and the outline tint is #141a0e (both unchanged); highlights are cool swamp-white
  (#f0f4e4) instead of hazy straw (#eeecce), and midtones take a faint olive cast (#92a67f, about 8%). Colours not taken from a
  family are fitted the same way by the generator: steered out of the orange / amber and cyan bands.
- Signature accents keep their own colour: rosy bitterling rose, bitterling throat, stickleback crimson throat and blue eye, pygmy
  and bluespotted indigo flecks, blackbanded sunfish pelvic edge, redbelly dace belly, golden shiner gold, paradise fish bands,
  rudd and perch crimson fins, pumpkinseed ear spot, cheek lines and gold breast, tench red eye, axolotl gills, newt bellies,
  pond-turtle speckles, crayfish claws.
- Translucent fins keep the body's own hue with only a light dry-grass tint (#c4c8a2, about 15%); alpha falls from about 185 at
  the base to about 110 at the edge in fine steps of 12, and the clear membrane lightens slightly toward the free edge. Fin rays are
  sparse (about every third pixel), only about 0.09 darker than the membrane and fade out toward the edge. Clear fins get a faint
  light rim; coloured signature fins a slightly deeper rim of their own hue and a little more opacity. Fin markings run through the
  margin.

## Rendering (v3: smooth, as in bw)
- One volume per body: in every column the value only falls away from the brightest pixel (upward to the back, downward to the
  belly) - no light/dark/light stripes. Deep bodies get a one-step darker inner rim. Signature patches (throats, breasts) stay at
  mid depth: never washed out, never muddy. Dark species (tench, bullhead, wels, crucian carp, pumpkinseed) start lower on the
  ramp with a longer tone span, so the body darkens but keeps its highlight.
- Tone zones are cleaned: no 1-2 px islands or notches between tones. Near-duplicate colours are merged (OKLab distance under
  0.016), about 24 opaque colours per sprite (bw: 28).
- Silhouettes follow pixel-art curves: on each side of the crest the stair runs are ordered so the slope changes steadily
  (1-2-3-5-8, not 4-2-2-5-3); stair corners are no longer cut.
- Outline: each edge pixel is a darker shade of the colour just inside it, tinted toward #141a0e; lit top edge (about 30% darker),
  sides about 48%, belly edge about 64% with the row above it pulled down (one step deeper than cs / fs, for the dark water).
- Markings: at most two or three motifs per species, nothing finer than 2 px except one defining line, repeats spaced at least their
  own width; no 1 px checkers. Lines that run along the body are drawn straight; spots are scattered naturally, not on a grid.
- Heads are clean: no mouth line and no dark gill line. Eyes: highlight pixel above a dark pupil, iris colour on the back side,
  a dark socket pixel under the pupil; large fish use a one-step wider eye.
- Every species is one memorable set - body shape + fin set + barbels / filaments + pattern + colour - listed in the species notes.
- Pelvic fins hang below the belly behind the pectorals.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 25 deg (small), 15-20 deg (deep), 8-14 deg (long).
  Body and markings stay fixed; only fins, tail, barbels and ribbon fins move, in the species' gait (next section); bottom fish
  flick the tail fore-and-aft so they stay on the floor. Detached 1-6 px specks are removed from every frame.
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (the snail uses crawl_R, crawl_L, idle_R, idle_L); the rest pose touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt; see `ms_<name>_<swim|crawl>_<W>x<H>_4f.png`. Every sheet has a
  matching `ms_<name>.aseprite` (one layer, one tag per row, 0.12 s frames). Seven frame sizes changed with v3 (topmouth gudgeon,
  golden shiner, frog tadpole, asian swamp eel, northern snakehead, stone loach, european bullhead).

## Swimming gait
Each swimmer moves the way its kind swims (as in the ac / bw / pf references): which fins move, how, and the scene's
`animation_fps` come from a gait table in the sprite generator.

| Gait | Motion | fps | Species |
|---|---|---|---|
| dart | only the caudal lobe tips flick | 10-11 | sunbleak (11), northern redbelly dace |
| tetra | tail plus the whole dorsal and anal fins sway | 10 | european bitterling, rosy bitterling |
| cruise | tail-led, dorsal and anal flutter only at the rear tips | 7-10 | topmouth gudgeon (10), golden shiner (9), rudd (8), crucian carp (7) |
| killi | rear-set dorsal and anal swing with the tail | 8-9 | medaka (9), banded killifish |
| hover | rows with the pectorals while the rear fins sway as a unit, short tail beat | 7-9 | three spined stickleback, ninespine stickleback (9, big pectoral strokes), amur sleeper (7) |
| sunfish | soft dorsal and anal margins ripple, pectorals scull | 7-8 | okefenokee pygmy sunfish (8), blackbanded sunfish, bluespotted sunfish, pumpkinseed |
| cichlid | long soft dorsal and anal ripple, pectorals scull | 7 | paradise fish |
| stalker | spiny and soft dorsals ripple, tail barely moves | 6-8 | ruffe (8), european perch (7), mandarin fish, northern snakehead (6, long ripple) |
| deep | thick body, steady tail, pectorals scull | 6 | tench |
| catfish | long anal fin ripples, barbels sway | 5-6 | black bullhead (6), wels catfish (5) |
| gar | lurks: rear-set dorsal and anal move with the tail, pectorals scull | 5 | grass pickerel, northern pike |
| eel | the fin folds and tail ripple as one strip (the body itself does not bend) | 8-10 | frog tadpole (10), asian swamp eel, european eel |

## Roster (40 species: 31 swimmers, 9 crawlers)
The frog tadpole and the softshell turtle (kept swimming drawing) are swimmers; loaches, bullhead, axolotl, newts, the pond
turtle, the pond snail and the crayfish walk on the floor.

| Group | Species (frame) |
|---|---|
| Small swimmers | european bitterling 36x24, rosy bitterling 36x24, sunbleak 36x24, medaka 32x22, topmouth gudgeon 36x26, three spined stickleback 32x22, ninespine stickleback 32x22, okefenokee pygmy sunfish 28x20, blackbanded sunfish 32x26, bluespotted sunfish 32x26, banded killifish 36x24, northern redbelly dace 34x24, golden shiner 44x28, paradise fish 42x28, frog tadpole 30x22 |
| Medium and large swimmers | crucian carp 48x30, rudd 46x28, tench 54x30, european perch 48x28, ruffe 38x24, pumpkinseed 42x30, amur sleeper 40x26, mandarin fish 56x34, black bullhead 52x26, grass pickerel 52x22, asian swamp eel 58x18, european eel 64x20, northern snakehead 64x26, northern pike 80x28, wels catfish 96x30 |
| Bottom fish, amphibians, turtles, snail, crayfish | stone loach 40x14, european weatherfish 52x12, european bullhead 38x16, axolotl 40x20, chinese fire bellied newt 38x14, great crested newt 40x16, chinese softshell turtle 50x30, european pond turtle 36x20, great pond snail 26x20, noble crayfish 52x14 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining set (v3: shape / fins / barbels / pattern / colour) |
|---|---|---|---|
| european bitterling | swim 36x24 | y 60-220, speed 20 | small DEEP pearl-silver bitterling / a short indigo-blue SHEEN STRIPE on the rear half only / a ROSE THROAT and belly (breeding) / red upper iris / clear fins |
| rosy bitterling | swim 36x24 | y 60-220, speed 20 | deep bitterling whose breeding male glows ROSE-VIOLET all over / a pale indigo sheen stripe toward the tail / CRIMSON dorsal and anal fins with a dark edge / crimson eye |
| sunbleak | swim 36x24 | y 0-110, speed 30 | slender little SILVERFISH of the surface / slate back / one BRIGHT SILVER BAND along the whole side with a dark upper edge / upturned mouth / clear fins |
| medaka | swim 32x22 | y 0-90, speed 22 | TINY rice fish with a flat back, upturned mouth and a BIG EYE / translucent brass with one pale line along the side / a LONG ANAL FIN under a small dorsal set far back / square tail |
| topmouth gudgeon | swim 36x26 | y 80-230, speed 24 | small minnow with a tiny UPTURNED mouth / brass back, pearl flank with one bold dark STRIPE from the snout to the tail / a loose row of dark scale CRESCENTS above it / clear grey fins |
| three spined stickleback | swim 32x22 | y 60-230, speed 20 | breeding male stickleback / reed-green back over a slate-silver flank / a blazing CRIMSON THROAT and belly / pale BLUE eye / THREE free spines in front of the dorsal and a strong pelvic spine / slender keeled tail stalk |
| ninespine stickleback | swim 32x22 | y 100-240, speed 18 | slender stickleback with a row of NINE small spines along the back / brass-olive with five soft dark bars / the breeding male's BLACK THROAT / narrow tail stalk |
| okefenokee pygmy sunfish | swim 28x20 | y 150-250, speed 10 | TINY near-black sunfish / charcoal body sprinkled with bright INDIGO-BLUE flecks / two faint bars / every fin edged in blue / rounded tail |
| blackbanded sunfish | swim 32x26 | y 100-230, speed 14 | deep pearl DISC with five bold BLACK BANDS (the first through the eye) / black front of the dorsal / a CRIMSON front edge on the pelvic fins / rounded tail |
| bluespotted sunfish | swim 32x26 | y 110-240, speed 14 | deep DARK reed-green sunfish sprinkled with shining BLUE SPOTS / a black EAR SPOT / red eye / dusky rounded fins with a few blue spots |
| banded killifish | swim 36x24 | y 4-120, speed 22 | slender flat-headed killifish of the surface / brass-olive with EIGHT thin dark vertical BARS on the rear two thirds / pearl belly / dorsal set far back over the anal / square tail |
| northern redbelly dace | swim 34x24 | y 40-200, speed 26 | small dace / brass back / TWO DARK STRIPES - the upper one breaking into dashes toward the head - over a CRIMSON belly / pale gold fins |
| golden shiner | swim 44x28 | y 30-190, speed 26 | deep compressed shiner / a GOLD flank under a brass-olive back / one thin lateral line that DIPS low under the belly curve / small upturned mouth / crimson-tinted pelvic and anal fins |
| paradise fish | swim 42x28 | y 0-150, speed 16 | the BANDED labyrinth fish - alternating INDIGO and CRIMSON vertical bands over a charcoal body / a blue-black GILL SPOT ringed crimson / long flowing indigo dorsal and anal / deeply forked crimson tail with trailing filaments / thread pelvics |
| frog tadpole | swim 30x22 | y 120-256, speed 12 | round BODY flowing into a long muscular TAIL with clear fin folds above and below / peat-brown with a few dark speckles and pale gold flecks / eyes on the sides of the head / no paired fins |
| crucian carp | swim 48x30 | y 120-250, speed 14 | deep carp with a HIGH-ARCHED back and no barbels / plain brass-bronze body / a long convex dorsal / a dark SPOT on the tail base / rounded brass fins, slightly notched tail |
| rudd | swim 46x28 | y 20-180, speed 22 | deep compressed cyprinid with an upturned mouth / reed-green back over a brass flank / blazing CRIMSON pelvic, anal and tail fins / red-orange eye / dorsal set behind the pelvics |
| tench | swim 54x30 | y 170-256, speed 12 | THICK smooth-skinned fish with a thick tail stalk / dark reed-green with a brass sheen on the flank, no pattern / a tiny RED EYE / big rounded dark fins / one short barbel at the mouth corner |
| european perch | swim 48x28 | y 60-220, speed 20 | HUMP-backed perch / reed-green with six dark vertical BARS / a black SPOT at the rear of the spiny dorsal / CRIMSON pelvic, anal and lower tail lobe |
| ruffe | swim 38x24 | y 190-256, speed 14 | small big-headed perch / peat-brown sprinkled with dark spots / one long joined dorsal crossed by ROWS of black spots / violet eye |
| pumpkinseed | swim 42x30 | y 70-220, speed 16 | deep sunfish / reed-green with crimson-coral SPOTS / wavy INDIGO lines on the cheek / black EAR FLAP tipped with a crimson spot / GOLD breast and belly |
| amur sleeper | swim 40x26 | y 170-256, speed 12 | chunky SLEEPER with a big head and a wide mouth / dark peat-brown with darker soft BLOTCHES / two rounded dorsals / rounded fins with rows of dark dots and a PALE EDGE |
| mandarin fish | swim 56x34 | y 140-250, speed 14 | deep AMBUSH predator with a HUGE mouth / brass-gold LEOPARD body with big irregular dark blotches / a black STRIPE from the snout through the eye to the dorsal base / long spiny dorsal |
| black bullhead | swim 52x26 | y 196-258, speed 14 | stout CATFISH / charcoal-black back over a pale gold belly / dark whisker barbels / square tail with a PALE BAR across its base / adipose fin |
| grass pickerel | swim 52x22 | y 20-180, speed 14 | small DUCKBILL pike / brass-olive with NINE wavy dark vertical BARS / a dark TEARDROP bar under the eye / dorsal and anal set far back / forked tail |
| asian swamp eel | swim 58x18 | y 210-258, speed 10 | slick EEL with NO paired fins and only a low fold round the pointed tail / peat-olive with a few dark speckles / pale gold belly / small eye, blunt snout |
| european eel | swim 64x20 | y 190-258, speed 12 | long snake-like YELLOW EEL / dark reed-green back over a gold-cream belly / small PECTORAL fins / one continuous fin from mid-back round the tail to the belly |
| northern snakehead | swim 64x26 | y 40-220, speed 14 | long cylinder with a SNAKE-LIKE head / mahogany-tan with big dark PYTHON BLOTCHES in two rows / long low dorsal and anal fins along most of the body / a dark streak behind the eye / rounded tail |
| northern pike | swim 80x28 | y 20-200, speed 16 | long reed-green PIKE / rows of pale BEAN-SHAPED SPOTS / duckbill snout / dorsal and anal set far back / fins blotched dark / forked tail |
| wels catfish | swim 96x30 | y 200-256, speed 12 | HUGE scaleless catfish with a broad flat head / slate-grey back marbled darker over a pale belly / TWO VERY LONG WHISKERS and four short chin barbels / tiny dorsal, long anal fin reaching the tail |
| stone loach | crawl 40x14 | floor, speed 8 | slender round-bodied LOACH / brass-olive with big soft brown BLOTCHES along the side / SIX short barbels round the mouth / small eyes high on the head / a dark bar at the tail base |
| european weatherfish | crawl 52x12 | floor, speed 8 | long EEL-LIKE loach / peat-brown with a pale GOLD STRIPE along the upper side over a broad dark midline stripe / TEN barbels round the small mouth / rounded tail |
| european bullhead | crawl 38x16 | floor, speed 6 | FLAT broad head with eyes on top, body tapering to the tail / mahogany-brown with three dark BANDS and soft mottling / huge FAN pectorals crossed by dark bars / two dorsal fins |
| axolotl | crawl 40x20 | floor, speed 5 | the existing axolotl drawing (kept) - leucistic, re-mapped onto the pale mahogany-rose family / feathery GILLS kept as a rose signature / broad smiling head, tail fin |
| chinese fire bellied newt | crawl 38x14 | floor, speed 6 | the existing drawing (kept) - charcoal-black warty back on the pearl / charcoal family, the CRIMSON belly kept as a signature |
| great crested newt | crawl 40x16 | floor, speed 6 | the existing drawing (kept) - dark peat-brown warty skin, the GOLD belly kept as a signature |
| chinese softshell turtle | swim 50x30 | y 150-256, speed 12 | the existing swimming softshell drawing (six direction rows, kept) - flat leathery shell, re-mapped onto the brass-olive family |
| european pond turtle | crawl 36x20 | floor, speed 6 | the existing drawing (kept) - near-black shell and skin on the charcoal family, the GOLD speckles kept as a signature |
| great pond snail | crawl 26x20 | floor, speed 2 | thin HORN-coloured shell with a huge rounded body whorl and a tall SHARP SPIRE / faint spiral lines / big ear-shaped dark aperture / grey foot and flat triangular tentacles; the shell stays fixed while the foot glides |
| noble crayfish | crawl 52x14 | floor, speed 10 | BIG dark peat-brown crayfish / rough heavy claws whose undersides and joints are CRIMSON / long rostrum |

## Scenes
`scenes/creatures/freshwater/marsh_swamp/ms_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/ms_aquarium.tscn`.
