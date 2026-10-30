# Clear Spring - creature style (prefix `cs_`)

Biome look: crystal-clear aquamarine spring water, strong sun from above, white sand and limestone. The roster mixes the
Florida spring runs (shiners, killifish, sunfish, gar, sturgeon, snook, mullet) and the clear springs of Bonito / Pantanal in
Brazil (characins, cichlids, catfish, pacu, dorado, crab). Every animal is fully aquatic.

All 40 creatures were redrawn from scratch in October 2026 following the BW workflow
(`assets/creatures/freshwater/blackwater/README_creatures.md`), using only the species names as input: no earlier cs sprite,
size, texture or colour was used. Each species was first defined by its real anatomy and markings (step 1), then drawn at 1:1.

Style v2 (October 2026): after a study of the ac / bw / pf creatures (motion, colour and fin texture), the whole roster was
re-rendered with softer translucent fins, a lighter outline and warmer highlights, and every swimmer got its own swimming gait
(how its fins move and how fast it beats; see "Swimming gait" below). Anatomy, markings and colours per species are unchanged;
several frame sizes changed with the new fin motion (cambeva, cascudo and southern flounder became flatter). Part-built animals
(crayfish, crab, turtles, snail) only take the warmer highlights. (Correction: the warmer highlight listed for v2 was never
actually applied by the generator; the v2 sheets used #fff6dc. v3 replaces both.)

Style v3 (October 2026): smoothness and fit to the water. A comparison with bw / ac showed three gaps. (1) Bodies read as stacked
horizontal stripes (three colour bands, each with its own tone ramp, plus 1 px highlight lines and thin markings; 2.5 light/dark
reversals per column vs 2.0 in bw, about 50 colours per sprite vs 28) and silhouettes had uneven stair runs (9% of contour steps
vs 0% in bw). (2) Several species packed fine repeats (1 px checkers, many thin stripes, barcode bars). (3) The water is far
lighter than in bw / ac (L 0.73 vs 0.46-0.49) and a single cyan hue, while most fish sat in yellow-olive - neither the water's
colour family nor its complement - so they looked pasted on. v3 renders each body as one volume with clean silhouettes, colours
every species from fixed colour families derived from the background, and redesigns every species as one memorable set (body
shape + fin set + barbels / filaments + pattern + colour). Motion (the swimming gaits) is unchanged.

Style v4 (October 2026, the 30 swimmers): shading and fins measured against the ac / bw / pf sprites species by species (110
features per sprite, compared as distributions and against the reference fish of the same shape, not as averages). v3 bodies
were too flat or too glossy: the light tones jumped 0.23 in lightness from tone 3 to tone 4 (bw: about 0.10 per step), so the
brightest pixels stood out as a patch, the light sat mid-body (bw: upper third) and the back under the dorsal fin was darker than
the body. Fins drew their rays as alpha stripes, used 6-7 colours (refs 10-13), sat 0.17-0.32 lighter than the body (refs
0.03-0.14) and moved mostly at the tips. v4 keeps every species' anatomy, set, colours and frame size and changes how they are
rendered (generator `v4/build_v4.py cs`, settings per species in `v4/params/cs.json`; process in
`.agents/rules/creature_workflow.md`, stage 2). Pacu and banded cichlid are kept matte on purpose.

## Water and colour families (v3)
For the 30 swimmers the v4 pass ("Shading and fins" below) replaces the lit tones 4-5, the highlight colour and the fin
rendering described here; the families, hue rule, chroma and tones 0-3 still apply. Crawlers keep v3 as written.

- The background (far + mid + near) is one cyan-teal hue (OKLab hue -176) at low chroma (0.055-0.09) and very light where the fish
  swim: L 0.81 at the surface, 0.71 at mid depth, 0.54-0.60 just above the floor; the floor and rocks are dark grey-green. There is
  no warm colour in the scene.
- Every creature brackets the water: its lit parts sit above the water lightness (+0.13 on average), its body tones below it
  (-0.21) and its outline well below (-0.35). No body tone sits inside the band the fish swim in (L 0.70-0.82).
- Hue rule: bodies are either analogous to the water (within 45 deg: teal, aqua, sea green, azure) or neutral (silver, pearl,
  charcoal); warm complements (over 110 deg: sand, bronze, amber, coral, red) are muted on bodies and saturated only as accents
  (fins, spots, eyes, breasts). Yellow-olive, lime and violet (45-110 deg from the water) are not used on bodies; yellow tails
  became amber. Body chroma stays at about half the water's (0.53), like bw (0.61) and ac (0.33).
- Colour families (6 tones dark to light at L 0.28 0.40 0.52 0.63 | 0.86 0.95; generator `pal.FAM`):

| Family | Tones | Use |
|---|---|---|
| A1 aqua silver | #112e2e #314e4d #556f6e #788e8e #c3d5d5 #e6f1f1 | silver tetras, shiners, mullet, silverside, piau, curimbata |
| A2 slate teal | #052f35 #284e55 #4e7076 #718f95 #bfd6da #e4f1f4 | dark backs, pacu, spotted sunfish, pintado |
| A3 sea green | #0a3123 #285140 #4a7361 #6d9382 #bdd9cb #e3f3eb | moenkhausia, flagfish, banded cichlid, chubsucker, piracanjuba, gar |
| A4 azure steel | #0f2c3c #2b4c5f #4f6d7f #728e9e #bfd5e2 #e5f0f7 | seminole killifish, sailfin molly |
| N1 pearl / charcoal | #2c2822 #4b4741 #6d6861 #8d8881 #d4d0ca #f1eee9 | pike cichlid, sturgeon back, cascarudo, fat sleeper, bellies |
| C1 sand bronze | #372513 #5b422a #7f6347 #a18366 #e4ccb6 #f8ece1 | coastal shiner, pyrrhulina, darter, chanchito, bass, knifefish, snook back, bottom fish |
| C2 amber gold | #3d2200 #683c00 #925b00 #b97a13 #fac787 #ffeacb | golden dorado; amber fins and tails |
| C3 coral tangerine | #4a1500 #792c00 #a84811 #d16631 #ffbc9a #ffe5d3 | redbreast and pacu breasts, ironcolor blush, orange fins |
| C4 signal red | #4f0b08 #831b16 #b6322b #dd574b #ffb5a9 #ffe3dc | red fins and eyes |

- Shadows and the outline tint lean to deep teal (#123a44 / #0c2228); highlights are cool water-white (#eef8f2), not cream.
  Colours not taken from a family (the part-built animals, a few accents) are fitted the same way by the generator: kept out of
  the water band and steered out of the yellow-olive band.
- Signature accents keep their own colour: Buenos Aires tetra / piraputanga / piracanjuba red fins, yellowtail lambari amber tail,
  flagfish red lines, redbreast and pacu orange breasts, Suwannee bass turquoise chin, golden dorado gold, piau and snook amber fins,
  fat sleeper blue shoulder spot, crab claws.
- Translucent fins keep the body's own hue with only a light aqua tint (#a6dcd4, about 15%); alpha falls from about 185 at the base
  to about 110 at the edge in fine steps of 12, and the clear membrane lightens slightly toward the free edge. Fin rays are sparse
  (about every third pixel), only about 0.09 darker than the membrane and fade out toward the edge. Clear fins get a faint light
  rim; coloured signature fins a slightly deeper rim of their own hue and a little more opacity. Fin markings run through the margin.

## Rendering (v3: smooth, as in bw)
Swimmers: texture, bottom outline, fin junctions and eyes as changed by v4 (next section); crawlers as written.

- One volume per body: in every column the value only falls away from the brightest pixel (upward to the back, downward to the
  belly) - no light/dark/light stripes. Deep bodies get a one-step darker inner rim (the bw severum look). Signature patches
  (breasts, chin) stay at mid depth: never washed out, never muddy.
- Tone zones are cleaned: no 1-2 px islands or notches between tones. Near-duplicate colours are merged (OKLab distance under
  0.016), about 30 opaque colours per sprite (bw: 28).
- Silhouettes follow pixel-art curves: on each side of the crest the stair runs are ordered so the slope changes steadily
  (1-2-3-5-8, not 4-2-2-5-3); stair corners are no longer cut.
- Outline: each edge pixel is a darker shade of the colour just inside it, tinted toward #0c2228; lit top edge (about 20% darker),
  sides about 38%, belly edge about 58% with the row above it pulled down.
- Markings: at most two or three motifs per species, nothing finer than 2 px except one defining line, repeats spaced at least their
  own width; no 1 px checkers. Lines that run along the body are drawn straight; spots are scattered naturally, not on a grid.
- Heads are clean: no mouth line and no dark gill line. Eyes: highlight pixel above a dark pupil, iris colour on the back side,
  a dark socket pixel under the pupil; large fish use a one-step wider eye.
- Every species is one memorable set - body shape + fin set + barbels / filaments + pattern + colour - listed in the species notes.
- Pelvic fins hang below the belly behind the pectorals.

## Shading and fins (v4, swimmers)
- Light tones climb in even steps of about 0.11 (bw 0.11, pf 0.085); the brightest tenth of the body is one small step above its
  neighbours (median 0.13, bw deep-bodied fish 0.13). The light sits in the upper third (0.35 from the back edge; bw 0.33, pf
  0.35) and the band under the back stays about +0.06 above the body's median instead of darkening. No highlight spot, no
  near-white: the lightest tone a body may use is set per species (pacu and banded cichlid stop one step lower: matte).
- Neighbouring tones mix in small clusters where the form turns (2 px cells, anchored to the body so frames do not flicker); no
  single pixel sits alone in another colour. The largest flat one-colour area is about 18% of the body (refs at most 26%).
- Colour: lights drift a few degrees toward yellow and darks away from it (bw +8 / +7, ours +4 / +5); dark tones are desaturated
  like the refs; outline hues stay out of the water's discord band; the bottom outline follows the body's lightness instead of a
  fixed floor; the outline continues where the body meets a translucent fin. Pupil #060d0c with a cool catchlight #e3eeec.
- Fins: alpha falls smoothly from the base (about 180) to the free edge (about 155, edge pixels a little thinner) with no ray
  alpha; the membrane lightens from base to edge in four bands with a soft mottle, rays are only a faint colour line; fins carry
  10-15 colours and sit close to the body's tone (median +0.02 to +0.05).
- Fin motion keeps each species' gait and gives each fin kind its own movement: the tail swings up and down as one piece (most of
  its pixels change every frame, as in the refs); dorsal and anal fins move at the trailing tips (tips / ripple / whole per gait)
  and trace a loop - back in frame B, lifting away from the body in D - instead of mirroring the tail; the anal fin follows the
  tail's vertical direction; pectorals scull or flap per gait. Frames A and C stay identical.

## Sheets
- Swimmers: 6 rows E, SE, SW, W, NW, NE x 4 frames (A-B-A-C); tilt 25 deg (small), 15-16 deg (deep), 8-12 deg (long).
  Body and markings stay fixed; only fins, tail, barbels and ribbon fins move, in the species' gait (next section); bottom fish
  flick the tail fore-and-aft so they stay on the floor. Detached 1-6 px specks are removed from every frame.
- Crawlers: 4 rows walk_R, walk_L, idle_R, idle_L (the snail uses crawl_R, crawl_L, idle_R, idle_L); the rest pose touches y = H-1.
- Frame sizes come from each animal's anatomy plus its tilt (1 px safety); see the file names `cs_<name>_<swim|crawl>_<W>x<H>_4f.png`.
- Every sheet has a matching `cs_<name>.aseprite` (one layer, one tag per row, 0.12 s frames).

## Swimming gait
Real fish do not all swim the same way, and neither do the ac / bw / pf references: a neon only flicks its tail tip, a cichlid
ripples its soft dorsal and anal fins and sculls with its pectorals, an arowana sways its rear fins with the tail as one unit, a
knifefish moves only its ribbon fin, and big slow fish beat at 5-6 fps while small darting ones beat at 10. Each cs swimmer
therefore has a gait (a table in the sprite generator) that sets which fins move, how, and the scene's `animation_fps`:

| Gait | Motion | fps | Species |
|---|---|---|---|
| dart | quick tail beat, the other fins hold still | 10-11 | coastal shiner, ironcolor shiner, tidewater silverside (11) |
| tetra | tail plus the whole dorsal and anal fins sway | 10 | buenos aires tetra, moenkhausia bonita |
| cruise | tail-led, dorsal and anal flutter only at the rear tips | 7-10 | yellowtail lambari (10), lake chubsucker (7), three spot piau, striped mullet (9), curimbata, common snook (7) |
| power | wide tail beat, other fins quiet | 8-9 | golden dorado (8), piraputanga, piracanjuba |
| killi | rear-set dorsal and anal swing with the tail (flagfish: its long dorsal ripples) | 8 | seminole killifish, florida flagfish |
| hover | sculls with the pectorals, small tail beat, dorsal ripples | 8 | spotted pyrrhulina |
| sail | the sail dorsal ripples along its whole length | 8 | sailfin molly |
| darter | big pectoral fans flap, short tail beat | 8 | swamp darter |
| cichlid | soft dorsal and anal margins ripple, pectorals scull | 7 | banded cichlid, chanchito |
| sunfish | as cichlid with stronger pectoral sculling | 7 | redbreast sunfish, spotted sunfish, suwannee bass (wider tail, less pectoral) |
| stalker | long dorsal ripples, tail barely moves | 7 | pike cichlid |
| gar | dorsal and anal (set far back) move with the tail as one unit, pectorals scull | 5 | florida gar |
| deep | deep body, steady tail, pectorals scull | 6 | pacu |
| catfish | long anal fin ripples, barbels sway | 6 | pintado |
| sturgeon | heavy slow tail beat, barbels | 5 | gulf sturgeon |
| ribbon | only the anal ribbon fin waves | 8 | banded knifefish |

Since v4 the tail swings as one piece in every gait (as in the refs); the gait still decides which other fins move, how, and
the beat.

## Roster (40 species: 30 swimmers, 10 crawlers)
| Group | Species (frame) |
|---|---|
| Small swimmers | buenos aires tetra 38x28, coastal shiner 38x26, ironcolor shiner 36x26, moenkhausia bonita 38x28, yellowtail lambari 40x30, spotted pyrrhulina 38x26, seminole killifish 38x26, swamp darter 30x20, tidewater silverside 38x24, florida flagfish 36x26, sailfin molly 38x30 |
| Medium swimmers | banded cichlid 44x36, chanchito 42x32, pike cichlid 50x22, lake chubsucker 46x30, redbreast sunfish 44x32, spotted sunfish 40x30, suwannee bass 48x28, three spot piau 50x24, striped mullet 50x24, banded knifefish 50x20 |
| Large swimmers | curimbata 58x34, piraputanga 56x28, piracanjuba 62x30, golden dorado 64x30, common snook 64x30, florida gar 62x26, pacu 58x40, pintado 84x28, gulf sturgeon 78x26 |
| Bottom dwellers and crawlers | cambeva 42x12, cascarudo 46x14, cascudo 48x22, fat sleeper 42x22, southern flounder 42x22, florida cave crayfish 52x14, pantanal crab 34x20, loggerhead musk turtle 36x16, toad headed turtle 40x14, rasp elimia 26x18 |

## Species notes and scene tuning
| Species | Sheet | Band / speed | Defining set (v3: shape / fins / barbels / pattern / colour) |
|---|---|---|---|
| buenos aires tetra | swim 38x28 | y 40-200, speed 26 | compact aqua-silver tetra / slate back / black CROSS on the peduncle (wedge + upright bar) that runs on as a black streak through the red tail / red anal, pelvic and adipose / one faint silver-blue lateral line / small humeral spot |
| coastal shiner | swim 38x26 | y 20-170, speed 30 | slim pointed minnow / sand-bronze back over a pearl belly / ONE dusky lateral band from the gill that ends in a round black CAUDAL SPOT / clear sandy fins with a forked tail |
| ironcolor shiner | swim 36x26 | y 40-200, speed 28 | small minnow / slate back, aqua-silver flank / bold BLACK BAND from the lips through the eye to the tail base, a pale sand stripe riding on top / tangerine blush on the lower flank and the fins (breeding colours) |
| moenkhausia bonita | swim 38x28 | y 30-200, speed 26 | small high-backed tetra / sea-green silver with a pale shine line / RED EYE / black WEDGE on the peduncle that runs into the tail base / white-tipped dorsal and anal fins / dark humeral comma |
| yellowtail lambari | swim 40x30 | y 20-180, speed 30 | lively silver characin / slate back, aqua-silver flank / TWO BLACK SPOTS - a long oval humeral blotch and a diamond on the tail base / bright AMBER tail, amber adipose and anal / faint dusky midline joining the two spots |
| spotted pyrrhulina | swim 38x26 | y 8-120, speed 20 | slim cylindrical surface fish / sand back, pearl flank / dark EYE STRIPE from snout to gill / two loose rows of rust-red dots / BLACK SPOT on the dorsal / long UPPER tail lobe / tangerine anal and pelvic fins |
| seminole killifish | swim 38x26 | y 4-110, speed 24 | big flat-headed killifish with an UPTURNED snout / azure-steel back, pearly flank / a few black dots on the rear half only / dorsal and anal set far back, opposite each other, square tail with a dusky edge |
| swamp darter | swim 30x20 | y 196-256, speed 12 | tiny bottom darter perched on big FAN PECTORALS / sand body / four square brown SADDLE-BLOTCHES along the side / dark TEARDROP under the eye / a dark bar on the tail base / spiny + soft dorsals |
| tidewater silverside | swim 38x24 | y 0-80, speed 32 | slender glassy pencil / sea-green back, aqua-silver body / bright SILVER RACING STRIPE with a dark upper edge / big eye / two tiny dorsals, long anal, DEEPLY FORKED tail |
| florida flagfish | swim 36x26 | y 120-240, speed 16 | deep square killifish / sea-green body / two continuous red FLAG LINES across the lower flank / one black BLOTCH mid-side under a long rounded dorsal that carries a black spot / tangerine anal / rounded tail |
| sailfin molly | swim 38x30 | y 0-120, speed 18 | male molly / azure-steel with a pearly flank and a few soft dark dots / the HUGE SAIL dorsal from the nape - amber rim and three dark spots / rounded tail with an amber edge / small upturned head |
| banded cichlid | swim 44x36 | y 90-230, speed 16 | tall sea-green disc / three broad soft bars fading out on the lower flank + one bold black bar on the peduncle / red-brown worm marks on the cheek / long POINTED dorsal and anal lobes trailing past the tail / red eye |
| chanchito | swim 42x32 | y 110-240, speed 16 | chunky sand-bronze chameleon cichlid / five dark bars and one big black BLOTCH mid-side / turquoise cheek spots / red eye / long soft dorsal and anal with dark-spotted rear lobes |
| pike cichlid | swim 50x22 | y 150-250, speed 22 | long pike-shaped predator with a PROJECTING lower jaw / pearl-grey / dark STRIPE from snout through the eye along the body / amber-ringed black OCELLUS behind the pectoral / black spot on the tail base / long low dorsal along the whole back |
| lake chubsucker | swim 46x30 | y 150-250, speed 16 | stout oval sucker / sea-green back over a pearl flank / one broad dusky LATERAL BAND (the young fish's mark) / tiny mouth under the snout / HIGH rounded dorsal / tangerine-tinted lower fins |
| redbreast sunfish | swim 44x32 | y 60-220, speed 18 | deep round sunfish / slate-teal back over a coral-orange BREAST / the long narrow BLACK EAR FLAP running back off the gill cover / two turquoise cheek streaks / a few big coral flank spots / spiny + soft dorsal, coral pelvics |
| spotted sunfish | swim 40x30 | y 80-230, speed 16 | the DARK sunfish - deep slate-charcoal body peppered with black specks / short black ear flap with a PALE RIM / faint rust breast / red eye / dusky rounded fins |
| suwannee bass | swim 48x28 | y 100-240, speed 20 | chunky bronze bass with a big jaw / row of dark lateral BLOTCHES / red eye / bright TURQUOISE chin, cheek and breast / spiny + soft dorsal, emarginate tail |
| three spot piau | swim 50x24 | y 120-250, speed 22 | cylindrical headstander / slate back, aqua-silver flank / THREE round BLACK SPOTS along the midline / three faint saddles over the back / small mouth / tangerine-amber fins and tail |
| striped mullet | swim 50x24 | y 10-150, speed 26 | torpedo with a broad BLUNT head / slate back, silver flank with two thin dark scale stripes / TWO widely spaced dorsals / a dark spot at the pectoral base set high on the side / forked tail |
| banded knifefish | swim 50x20 | y 190-256, speed 12 | eel-like knifefish with NO tail or dorsal fin / sand-bronze body with OBLIQUE dark bands slanting back / one long rippling RIBBON fin under the body / small eye |
| curimbata | swim 58x34 | y 130-250, speed 18 | high-backed silver migratory fish / slate back over a bright aqua-silver flank / two faint scale lines / pale fleshy sucker LIPS on the snout / tall dorsal with a dark edge / forked tail crossed by bold dark ZIGZAG bands / sandy lower fins |
| piraputanga | swim 56x28 | y 10-160, speed 30 | sleek silver Brycon / slate-blue back / BRIGHT RED TAIL with a black streak through its middle that runs onto the peduncle / red adipose / small dark humeral spot / amber-edged anal fin |
| piracanjuba | swim 62x30 | y 40-200, speed 28 | deeper, darker Brycon / sea-green back sprinkled with a few dark dots, silver flank / a big dark HUMERAL BLOTCH / RED tail and RED anal fin / black streak through the middle of the tail |
| golden dorado | swim 64x30 | y 30-200, speed 32 | big muscular GOLD torpedo (the one all-gold fish of the spring) / amber back, gold flank / three rows of short dark dashes (the scale lines), staggered / BLACK STREAK from the peduncle through the middle of a red-orange tail / orange adipose |
| common snook | swim 64x30 | y 80-230, speed 24 | long predator with a CONCAVE forehead and a jutting lower jaw / bronze back over a silver flank / one bold BLACK LATERAL LINE from the gill into the tail / spiny + soft dorsal / amber pelvic and tail fins |
| florida gar | swim 62x26 | y 10-140, speed 14 | long round tube with a short broad snout / sea-green back, sandy lower flank / big round dark SPOTS scattered over head, body AND every fin / dorsal and anal set far back opposite each other / rounded spotted tail |
| pacu | swim 58x40 | y 60-220, speed 18 | the big DARK DISC / slate back and sides / warm ORANGE throat and belly / dark fins with an orange pelvic / small blunt-toothed mouth, small adipose |
| pintado | swim 84x28 | y 190-256, speed 16 | long SHOVEL-NOSED catfish / slate back, silver flank, pearl belly / short dark vertical BARS over the back and a few round spots below them / very LONG barbels / forked tail with dark spots / adipose |
| gulf sturgeon | swim 78x26 | y 200-256, speed 14 | huge shark-like sturgeon / charcoal back, sand flank, pearl belly / three rows of pale bony SCUTES (back, side, belly) / shovel snout with four barbels / long upper tail lobe |
| cambeva | crawl 42x12 | floor, speed 10 | long PENCIL catfish with a flat head / sand-bronze with a few irregular dark BLOTCHES / three pairs of whisker BARBELS / tiny eyes on top / dorsal set far back, rounded tail |
| cascarudo | crawl 46x14 | floor, speed 8 | ARMOURED catfish / dark charcoal / two rows of big slanted bony PLATES meeting at a pale sea-green midline seam / two pairs of LONG barbels / short spined dorsal and adipose spine, rounded tail |
| cascudo | crawl 48x22 | floor, speed 6 | PLECO - flat belly under a high arched back / sand body with sparse round dark spots / a tall SAIL dorsal with dark spots / forked tail with a longer LOWER lobe / sucker mouth, eye high on the head, adipose |
| fat sleeper | crawl 42x22 | floor, speed 8 | chunky DARK sleeper resting on the floor / charcoal-brown with a few pale spots / a bright BLUE SHOULDER SPOT above the pectoral / spiny + soft dorsals / big rounded tail |
| southern flounder | crawl 42x22 | floor, speed 6 | flat oval FLATFISH lying on the sand, eyed side up / sand-bronze with a few big soft dark blotches / two pale-ringed dark OCELLI / both eyes close together on the head / fringe dorsal and anal fins rippling along the edges |
| florida cave crayfish | crawl 52x14 | floor, speed 10 | cave crayfish: ghost-white, slightly pink and translucent, eyes reduced to pale nubs, long antennae, slender claws held forward, low body = carapace + segmented abdomen ending in a tail fan, four short walking legs per side drawn one by one |
| pantanal crab | crawl 34x20 | floor, speed 10 | Dilocarcinus pagei: freshwater crab from the Pantanal seen from the front, walking sideways: broad red-brown carapace, eyes on short stalks, orange-red claws with dark fingertips, four jointed walking legs on each side |
| loggerhead musk turtle | crawl 36x16 | floor, speed 6 | Sternotherus minor minor: small turtle with a high keeled carapace, brown-orange shell with dark streaks and dark-edged scutes, oversized head (loggerhead) pinkish-grey with dark spots, small yellowish plastron, short tail |
| toad headed turtle | crawl 40x14 | floor, speed 6 | Mesoclemmys toad-headed turtle (side-necked): low, flat oval carapace dark olive-brown, broad flat toad-like head, grey-olive skin, pale yellow jaw and throat with two small chin barbels, yellow plastron |
| rasp elimia | crawl 26x18 | floor, speed 2 | Elimia floridensis: tall turreted shell with strong spiral cords and axial ribs ("rasp"), olive-brown, dark aperture, grey foot gliding forward, two slender tentacles; the shell stays fixed while the foot and tentacles move |

## Scenes
`scenes/creatures/freshwater/clear_spring/cs_<name>.tscn` inherit `swimmer_base.tscn` or `crawler_base.tscn` and set the sheet,
`frame_size`, `animation_fps`, `speed`, the swim `area` band (surface 0, floor about 264), `crowd_radius` and, for slow species,
`rest_time` / `move_time` / `idle_time`. The showcase is `scenes/aquarium/cs_aquarium.tscn`.
