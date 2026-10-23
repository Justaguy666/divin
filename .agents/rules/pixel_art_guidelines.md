---
description: Guidelines for creating and grading pixel art creature assets (spritesheet layout, core rendering style, and the colour grade / art direction of every biome).
trigger: "When generating, evaluating, or discussing pixel art, spritesheets, or creature assets."
---

# Pixel Art Guidelines for Creatures

These rules define the correct way to draw pixel art assets for creatures in the game. All creatures must adhere to strict rendering, shading, and spritesheet layout rules to ensure visual consistency across the project.
Tank/viewport is 640x360; creature sprites are drawn at 1:1 pixel scale (no scaling in-engine).

## 1. Spritesheet Layouts and Animation
- **Swimmers (Fish)**:
  - Layout: 6 rows corresponding to directions (E, SE, SW, W, NW, NE). No straight N/S rows.
  - Animation: 4 frames per row, 0.12 s per frame in the `.aseprite`, pattern A-B-A-C (frame 3 = frame 1).
  - **The body is static** (body bend = 0 px — bending makes the shading/markings flicker). Only fins move: dorsal/anal/pelvic/pectoral flutter ±1-1.5 px at the outer edge with the base anchored; the caudal moves only ~1-2 px at the trailing edge.
  - Eels and long-finned species (conger, ling, pipefish, cusk-eels, knifefish): tail fixed, a travelling sine wave runs along the long dorsal/anal fin (4 phases) plus pectoral fanning.
  - Draw only the E-facing frames; SE/NE are the E frames rotated (RotSprite), W/SW/NW are mirrors.
  - Tilt: 25° for small fish, 12-20° for deep-bodied/larger fish, 8-10° for very long fish (needlefish, arowana, sturgeon).
  - **E/W rows must swim level.** Never bake a head-up/head-down posture into the base frames (players read it as "always diving" — e.g. headstander, pencilfish were rejected for this).
- **Crawlers (Bottom-dwellers, snails, shrimp, crabs)**:
  - Layout: 4 rows (walk_R, walk_L, idle_R, idle_L). For snails, use crawl_R/L.
  - Animation: 4 frames per row. Body does not bob; legs, claws, antennae, foot or fins carry the motion.
  - The lowest pixel of every frame sits exactly on the last row (y = H-1). Bottom fish clip fin pixels below the belly at the floor.
  - Crustacean legs and antennae are separate crisp 1-px lines (each walking leg distinct, spaced ≥2 px); never a blob of legs.
  - Shelled species (whelk, hermit crab, triton, elimia): shell compact and low, angled back over the body.
  - Crabs are drawn from the front (they walk sideways).
- **Canvas Sizes**: Match the creature's form factor and keep the size in the file name: `<prefix>_<name>_<swim|crawl>_<W>x<H>_4f.png` (e.g. small fish `32x28`, discus `44x44`, altum `44x52`, stingray `56x16`, arowana `64x24`). Tiny species (chili rasbora, ruby tetra) keep the 32x28 frame and simply draw a smaller body.
- **Size hierarchy** (deep, full bodies but compact): small fish frame 32-36 x 28 (body 27-32 px); medium frame 34-44 (body 30-40); showpieces frame 46-62 (body 44-60, never wider than 62); small crawlers 24-38 px, large crawlers 34-48 px (long eels up to 58x16).
- Keep ≥1 px empty margin on every side in every row (fin tips, claws, antennae, rotated SE/NE rows included).
- Every sheet has a matching `<prefix>_<name>.aseprite` with one tag per row.

## 2. Rendering & Shapes (Core Style)
- **Silhouette first**: every species has its own body profile (depth, head shape, fin positions). Never reuse another species' body template and only recolour it.
- **Form Shading**: Light always comes from above. Shade forms rounded per column. Add 1-2 highlight pixels on the back or forehead to define volume.
- **Smooth transitions**: no flat monochrome areas and no hard colour boundaries. Every colour-region join (back → flank → belly) gets 1-2 intermediate tones; the belly is pulled ~20-26% toward the body's dominant hue. Body parts of crawlers meet with a soft intermediate tone, never a dark interior line.
- **Outlines**: Never use pure black and never one fixed near-black for the whole sprite. Each outline pixel = a dark shade of the body colour right next to it (same hue, about 55% of its lightness; keep it roughly between OKLab L 0.17 and 0.42), with the lit top edge one step lighter. A light biome tint (~10%) may be mixed in (tint values per biome below).
  - Outlines may vary along the body, but each outline pixel must be a dark shade of the body colour next to it (e.g. blue head -> dark blue outline, orange flank -> dark brown-orange outline). Never one fixed outline colour on a multi-coloured fish.
- **Markings**: Hand-place bars, stripes, spots and blotches, each with 1-2 halo rings of intermediate tone, with breathing room between them; no lone 1-px dots. A marking must be ≥2 px so it survives in every row. Sparse fixed-seed speckles are fine for scales/spangles; never a uniform noise texture or regularly repeating pattern that reads as a grid.
- **Fins**: drawn only OUTSIDE the body silhouette — no fin base or ray lines across the body (the pectoral may show as a soft lighter patch on the flank). Soft, translucent (alpha ~150-230), with rays and a smooth base→edge gradient; signature fin colours (red edges, black tips, white leading edges) go on the rim or tip. Long filaments must sit on a fin membrane — bare dark lines read as "spider legs".
- **Eyes** (standard set by the planted-freshwater sprites):
  - Core = exactly 2 px stacked vertically: a white/off-white highlight directly ABOVE a single near-black pupil. Never side by side, never diagonal, never a 2-px-wide or tall black pupil.
  - Highlight colour: the sprite's own off-white (`#f0ece0`, `#fbe4b2`, `#eff1e5` or similar, warm gold in blackwater); pupil: near-black from the palette (e.g. `#100905`). No pure `#ffffff`/`#000000`.
  - Exactly one eye per visible side. Remove any second white dot, fake eye or dark blob (spots, mouth ends, band ends) that reads as another eye near the head. Exception: flatfish (halibut, flounder) show both eyes on the top side, each with the same 2-px core and ring, spaced identically in E, SE and NE.
  - Optional coloured ring (e.g. red for discus/altum, orange `#c89040` for bass): pixels hugging the pupil, normally the bottom-left corner (left of, below and diagonal to the pupil). On busy/banded or low-contrast bodies (banded grunter, mackerel) this contrasting ring is REQUIRED so the eye stands out from the pattern.
  - Keep the cells around the eye calm: no checkerboard of light/dark pixels, no extra highlight pixels beside the eye; subocular/cheek bars must not run into the pupil.
  - Place the eye at the same anatomical spot in E, SE and NE (rays/flat-headed species: near the front of the head, not mid-body) and keep it in the same relative position in all 4 frames.
- **Mouths**: none on small heads (a mouth slit or white teeth read as a second eye). Do not draw a horizontal (or diagonal) dark mouth line across the head. At most a 1-3 px dark notch at the snout tip; avoid pixels at the tip that read as a second eye.
- **Bellies**: never a single flat colour. Give the underside a soft tonal gradient (rim/bounce light on the lowest edge, a gentle warm/cool drift along the length, patches of one-step variation or a dither band along the ventral line).
- **Backward swimmers** (cuttlefish, squid when jetting, etc.): the E-facing frames show the mantle leading and the arms/tentacles/eyes trailing behind, because the animal moves tail-first.
- **Translucent species** (glass bloodfin, golomyanka, isaza): lower the body alpha behind the head and show spine / gut / swim-bladder pixels.

## 3. Biome Styles
Each biome has ONE shared style for all of its creatures. Grades are applied to every finished frame as a post-process; the listed signature colours are excluded from the grade.

### 3.1 Planted Freshwater (prefix `pf_`) — reference style, no grade
Clear, bright, slightly green-tinted aquarium light.
- Natural, saturated colours; highlights may go to off-white (`#f4f0e4`), never pure `#ffffff`.
- Outline: dark version of the body colour (e.g. `#1a080a` for red fish), lit edge one step lighter.
- Fins: clear to lightly tinted with the body colour, alpha ~170-230.
- This is the reference for sizes and rendering detail for all other biomes.

### 3.2 Blackwater (prefix `bw_`)
Blackwater biomes represent tannin-rich "tea" water, dim amber light from above, and a dark humus floor.

**Colour Grading Rule**: Every finished frame for a blackwater creature must receive this specific color grade:
- **Shadows**: Must sink toward warm brown (`#2a1408`). NEVER use navy or black-blue for shadows.
- **Mid-tones**: Must have a light amber cast (`#be7c3c`, ~12% opacity) and be slightly desaturated.
- **Highlights**: Must be warm gold (`#ffe2a0`). NEVER use pure white.
- **Translucent Fins**: Must be tinted amber and slightly more transparent than typical freshwater assets.
- **Outline**: per-pixel dark shade of the adjacent body colour, lightly tinted toward warm `#1a0e0a`; lit top edge one step lighter (tint reference `#5a3420`).
- **EXCEPTION (Iridescence)**: Signature neon/iridescent lines or markings (e.g., the cardinal tetra's blue line, discus turquoise lines, apistogramma cheek spangles) are **NOT graded** (hue 165-230°, saturated). They must remain pure and bright so they glow against the dark water.

### 3.3 Ancient Cold Lake (prefix `ac_`)
Baikal-style ultra-clear, very cold, deep lake (species mix: Baikal core + Ohrid, Biwa, Khövsgöl, Sevan endemics).
- **Shadows**: sink toward cold blue-grey (`#1a2630`). Never warm brown.
- **Mid-tones**: icy cast (`#96bed2`, ~10%), slightly desaturated (~8%).
- **Highlights**: silver-white with a blue hint (`#ecf6fc`), never pure white.
- **Translucent Fins**: glassy, tinted pale blue (`#b4d7eb`, ~15%) and a bit more transparent (alpha ×0.88).
- **Outline**: per-pixel dark shade of the adjacent body colour, lightly tinted toward cool `#0e1820`; lit top edge one step lighter (tint reference `#3a5060`).
- **EXCEPTION (warm signatures)**: saturated reds/oranges/yellows (hue ≤55° or ≥330°) are **NOT graded** — char/taimen bellies, roach eye ring, ayu gill spot, amphipod shells, yellowfin sculpin fins — so they pop against the blue water.
- Silvery species use the shared silver ramp `#3a4650 → #eef2f4`; golomyankas are translucent pinkish with visible gut.

### 3.4 Cold Water (prefix `cw_`)
- Shadows → steel blue (`#121e2a`), faint grey-blue mid cast, highlights → cold white; saturation is NOT reduced.
- Fins tinted pale steel (10% toward `#82aac3`), alpha ≥ ~190, darker saturated rim.
- Not graded: saturated reds/oranges/yellows and blues (cuckoo wrasse, lumpfish belly, gurnard, crabs, lobster).

### 3.5 Underwater Cave (prefix `uc_`)
- Shadows → near-black `#0a0e12`, faint dark blue-grey mid cast, highlights dimmed, ~8% darker overall.
- Fins tinted dark blue (14% toward `#283c50`).
- Not graded: saturated reds/oranges/yellows, blues and blind-fish pinks (cardinalfish, soldierfish, shrimps, crabs).

### 3.6 Clear Spring (prefix `cs_`) — lightest grade
- Shadows → blue-teal `#122230` (~25% at black), mid-tones a faint turquoise cast (`#5aaaaa`, ~6%), highlights → `#f4faf8`; no extra desaturation.
- Fins tinted aqua (12% toward `#96c8c8`) and ~6% more transparent; outline tint `#0e1a20`.
- Not graded: saturated reds/oranges/yellows (dorado, characin fins, redbreast breast, flagfish stripes, molly sail edge) and blues (Suwannee bass cheeks, chanchito spangles).

### 3.7 Biomes without finished creatures yet — art direction
Apply the same mechanism (shadow tint, mid-tone cast, highlight colour, fin tint, signature exception) when their creatures are made. Directions below come from each biome's water tint and backgrounds; confirm before the first batch.

| Biome (prefix) | Shadows → | Mid-tone cast | Highlights | Fin tint | Keep ungraded |
|---|---|---|---|---|---|
| rocky_river (`rr_`) | cool slate `#1c2a30` | light teal | clear white-cyan | clear, faint teal | trout spots, red fin edges |
| forest_stream (`fs_`) | mossy green-black `#18241a` | soft green | pale yellow-green | green-tinted | red/orange spawning colours |
| rift_lake (`rl_`) | deep cobalt `#141c34` | blue | cool white | blue-tinted | cichlid yellows/oranges and blues (all saturated colours) |
| muddy_river (`mr_`) | olive-brown `#241e12` | khaki, desaturated more (~15%) | dull cream | murky brown, less transparent | none (low contrast biome) |
| marsh_swamp (`ms_`) | dark moss `#1a2014` | olive | pale green-grey | green-brown | red/orange eyes and bellies |
| koi_pond (`kp_`) | jade-grey `#16262a` | light jade | warm white | jade-tinted | koi reds, oranges, golds |
| bayou (`by_`) | olive-black `#1c1e10` | olive-yellow | pale straw | olive | reds |
| billabong (`bb_`) | teal-brown `#1a2420` | teal | sandy white | teal | rainbowfish iridescence |
| asian_peat_swamp (`ap_`) | wine-brown `#24100e` | wine-red cast | warm rose-gold | wine-tinted | iridescent blues/greens |
| high_andes_lake (`ha_`) | cobalt-grey `#16203a` | light cobalt | cold white | pale cobalt | orange/red |
| hillstream (`hs_`) | grey-green `#1a2624` | light turquoise | white | clear turquoise | loach/goby colours |
| ocean (`ob_`) | ocean blue `#101c34` | light blue | white-blue | blue | reef-fish yellows, oranges, purples |
| tropical (`tp_`) | aqua-navy `#10243a` | very light aqua | bright white | clear aqua | all saturated reef colours |
| coral_reef (`ce_`) | turquoise-navy `#0e2236` | light turquoise | bright white | clear | all saturated reef colours |
| seagrass_meadow (`sg_`) | green-grey `#16241c` | light green | pale green-white | green | seahorse/pipefish oranges |
| kelp_forest (`kf_`) | olive-teal `#16201a` | golden-green | warm light | golden-green | garibaldi orange |
| rocky_coast (`rc_`) | slate `#18222a` | grey-teal | white | grey-teal | anemone/nudibranch colours |
| mangrove (`mg_`) | green-brown `#1c2016` | green-brown | pale green | green-brown | crab/goby reds |
| muck_sand (`mk_`) | murky grey-green `#161c1a` | grey-green, desaturated | dim white | grey | frogfish/octopus vivid colours |
| deep_water (`dw_`) | near-black blue `#06101c` | dark blue | dim blue-white | dark, low alpha | bioluminescent blues/greens and reds |
| galapagos_upwelling (`gu_`) | green-grey `#14201c` | green | pale | green | yellows |
| open_pelagic (`op_`) | ultramarine `#0c1a3a` | blue | white | blue | dorado/tuna yellows |
| sargassum_sea (`sr_`) | cobalt `#0e1a34` | blue | white | blue | sargassum-golds (camouflaged fish) |
| twilight_zone (`tz_`) | black-indigo `#06081a` | indigo | dim | very dark | bioluminescent photophores |
| antarctic_water (`an_`) | icy navy `#101a2c` | pale ice-blue | white-blue | glassy | icefish pale bloodless whites stay untinted |
| arctic_water (`ar_`) | icy grey `#141c26` | ice-grey | white | glassy | char reds |
| cenote (`cn_`) | dark turquoise `#0c1e24` | turquoise | white | turquoise | cave-fish pinks |
| cold_seep (`sp_`) | dark teal `#0c1a1a` | teal, heavy | dim | dark teal | tube-worm reds |
| desert_spring (`ds_`) | aqua-sand `#1a2a28` | very light turquoise | warm white | clear | pupfish blues |
| hydrothermal_vent (`hv_`) | black-teal `#08100e` | dark | warm orange glow near vents | dark | vent-shrimp/worm reds and whites |
