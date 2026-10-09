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
  - Animation: 4 frames per row (tail/fin wave), 0.12 s per frame in the `.aseprite`.
  - Draw only the E-facing frames; SE/NE are the E frames rotated (RotSprite), W/SW/NW are mirrors.
  - Tilt: 25° for small fish, 12-20° for deep-bodied/larger fish, 8-10° for very long fish (needlefish, arowana, sturgeon).
  - **E/W rows must swim level.** Never bake a head-up/head-down posture into the base frames (players read it as "always diving" — e.g. headstander, pencilfish were rejected for this).
- **Crawlers (Bottom-dwellers, snails, shrimp, crabs)**:
  - Layout: 4 rows (walk_R, walk_L, idle_R, idle_L). For snails, use crawl_R/L.
  - Animation: 4 frames per row. Body bottom sits on a fixed row so `floor_height` in the scene matches it.
  - Crabs are drawn from the front (they walk sideways).
- **Canvas Sizes**: Match the creature's form factor and keep the size in the file name: `<prefix>_<name>_<swim|crawl>_<W>x<H>_4f.png` (e.g. small fish `32x28`, discus `44x44`, altum `44x52`, stingray `56x16`, arowana `64x24`). Tiny species (chili rasbora, ruby tetra) keep the 32x28 frame and simply draw a smaller body.
- Every sheet has a matching `<prefix>_<name>.aseprite` with one tag per row.

## 2. Rendering & Shapes (Core Style)
- **Silhouette first**: every species has its own body profile (depth, head shape, fin positions). Never reuse another species' body template and only recolour it.
- **Form Shading**: Light always comes from above. Shade forms rounded per column. Add 1-2 highlight pixels on the back or forehead to define volume.
- **Outlines**: Never use pure black. Outline = a near-black tinted toward the biome/body colour, with the lit top edge one step lighter (values per biome below).
- **Markings**: Hand-place bars, stripes, spots and blotches. Sparse fixed-seed speckles are fine for scales/spangles; never a uniform noise texture or regularly repeating pattern that reads as a grid.
- **Fins**: soft, translucent (alpha ~150-230), with rays and a smooth base→edge gradient; signature fin colours (red edges, black tips, white leading edges) go on the rim or tip. Long filaments must sit on a fin membrane — bare dark lines read as "spider legs".
- **Eyes**: Dark pupil + highlight + coloured ring (e.g. red ring for discus/altum, red upper iris for diamond tetra).
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
- **Outline**: `#1a0e0a`, lit edge `#5a3420`.
- **EXCEPTION (Iridescence)**: Signature neon/iridescent lines or markings (e.g., the cardinal tetra's blue line, discus turquoise lines, apistogramma cheek spangles) are **NOT graded** (hue 165-230°, saturated). They must remain pure and bright so they glow against the dark water.

### 3.3 Ancient Cold Lake (prefix `ac_`)
Baikal-style ultra-clear, very cold, deep lake (species mix: Baikal core + Ohrid, Biwa, Khövsgöl, Sevan endemics).
- **Shadows**: sink toward cold blue-grey (`#1a2630`). Never warm brown.
- **Mid-tones**: icy cast (`#96bed2`, ~10%), slightly desaturated (~8%).
- **Highlights**: silver-white with a blue hint (`#ecf6fc`), never pure white.
- **Translucent Fins**: glassy, tinted pale blue (`#b4d7eb`, ~15%) and a bit more transparent (alpha ×0.88).
- **Outline**: `#0e1820`, lit edge `#3a5060`.
- **EXCEPTION (warm signatures)**: saturated reds/oranges/yellows (hue ≤55° or ≥330°) are **NOT graded** — char/taimen bellies, roach eye ring, ayu gill spot, amphipod shells, yellowfin sculpin fins — so they pop against the blue water.
- Silvery species use the shared silver ramp `#3a4650 → #eef2f4`; golomyankas are translucent pinkish with visible gut.

### 3.4 Biomes without creatures yet — art direction
Apply the same mechanism (shadow tint, mid-tone cast, highlight colour, fin tint, signature exception) when their creatures are made. Directions below come from each biome's water tint and backgrounds; confirm before the first batch.

| Biome (prefix) | Shadows → | Mid-tone cast | Highlights | Fin tint | Keep ungraded |
|---|---|---|---|---|---|
| rocky_river (`rr_`) | cool slate `#1c2a30` | light teal | clear white-cyan | clear, faint teal | trout spots, red fin edges |
| clear_spring (`cs_`) | aqua-grey `#1a3034` | pale aqua | bright white-aqua | very clear | iridescent blues |
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
| cold_water (`cw_`) | steel blue `#121e2a` | grey-blue | cold white | pale steel | lumpsucker/wolf-eel accents |
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
| underwater_cave (`uc_`) | near-black `#0a0e12` | dark | dim | dark | blind-fish pinks |
