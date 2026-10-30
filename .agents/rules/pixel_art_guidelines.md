---
description: Guidelines for creating and grading pixel art creature assets (spritesheet layout, core rendering style, and the colour grade / art direction of every biome).
trigger: "When generating, evaluating, or discussing pixel art, spritesheets, or creature assets."
---

# Pixel Art Guidelines for Creatures

These rules describe the game's default rendering and spritesheet conventions. Preserve species readability and approved reference examples when a numeric or universal rule conflicts with them; use audit measurements as review prompts unless a rule is explicitly structural.
Tank/viewport is 640x360; creature sprites are drawn at 1:1 pixel scale (no scaling in-engine).

## 0. Style Contract (read first; references are not a score)
The user identifies `pf_`, `bw_` and `ac_` as the satisfying reference families. Treat them as examples of clear silhouettes, readable value grouping, species-specific markings and controlled pixel clusters—not as one numeric recipe. In particular, AC's long-bodied roster is accepted even though its mean body-aspect estimate is 2.41.

`.agents/tools/creature_audit.py` pins PF and BW to accepted snapshots (`5547197`, `72167f7`) and AC to the `f755afe3` baseline. These measurements cover 30 swimmer sprites per family; they describe those rosters and do not set pass/fail targets.

| Measurement | PF | BW | AC | Use |
|---|---:|---:|---:|---|
| Estimated body aspect, mean | 1.71 | 2.03 | 2.41 | Compare roster and anatomy; do not force every biome below one cutoff. |
| Species below aspect 2.0 | 77% | 50% | 27% | Roster-diversity prompt, not a minimum quota. |
| Distinct RGB colours, median | 46.5 | 34.0 | 62.5 | Read with clusters and markings; never judge flatness or noise by count alone. |
| Visible pixels with alpha 1–254, mean | 34.8% | 29.6% | 29.0% | Transparency proxy only; it does not identify fins or fin quality. |
| CIE L* P95–P5, mean | 72.3 | 74.2 | 65.5 | Reference varies; inspect where the range occurs. |
| OKLab dark share (L < 0.35), median | 18.9% | 21.1% | 10.2% | Do not impose a universal dark-mass quota. |
| Largest 31° OKLab hue window, median | 68% | 72% | 87% | Cohesion can come from form and markings as well as shared hue. |
| OKLab chroma P90, median | 0.172 | 0.078 | 0.037 | Mutedness is biome/species-specific; AC is intentionally restrained. |
| Mean sprite/background ΔE < 20 | 0% | 37% | 7% | Coarse flag only; it is not an accent-contrast test. |

**Before drafting or revising a biome**
- Open `.agents/rules/refs/style_reference.png` beside the preview. It currently shows PF, BW and a repeated PF strip; it has no AC strip. For AC, compare directly with the accepted assets at baseline `f755afe3`. Inspect at native scale and enlarged nearest-neighbour scale.
- Build a roster that reflects its species and habitat. Include varied body depths and silhouettes where the species allow; do not impose a fixed share of deep-bodied fish on rosters such as AC's.
- Check each species against its actual background. Separate its silhouette or key anatomy by value, edge or pattern. Use hue contrast when it supports the species; do not force every accent into the background hue family or cap a defining natural marking at an arbitrary area percentage.
- Give broad anatomical regions a deliberate value path (back → flank → belly) with enough intermediate tones to make the form read. Keep markings legible and internally simple; soften an edge only when the species or material calls for it.
- Vary fin size, shape and treatment by species. Transparent-pixel share is not a substitute for checking fin silhouette, membrane, rays and attachment.

**How to interpret the audit**
- It samples the first frame of each PNG sheet. RGB and RGBA palette counts are reported separately; RGB ignores alpha, RGBA includes it. Both count visible pixels from the whole sprite, including outline and fins.
- `body aspect` is an estimate: a 3×3 cross morphological opening removes some narrow appendages before measuring the bounding box. It can retain broad fins or remove narrow body parts, so inspect the sprite before drawing anatomy conclusions. Full-silhouette aspect is printed alongside it.
- `alpha 1–254` is the fraction of visible pixels that are partially transparent. It may come from fins, body translucency or edge treatment; it is not a fin-share measurement.
- L* range uses opaque pixels when at least ten are present, otherwise all visible pixels. Dark share, hue-window share and C90 use OKLab over visible RGB pixels. The hue window is the most populated sliding 31° window among pixels with chroma ≥ 0.02.
- `blend_share` compares mean visible sprite Lab with the mean of the first far-background PNG. It can miss a small accent or overstate camouflage. `hard_step` is a local pixel-pair heuristic. Both are review prompts, not quality scores.
- Swimmers and crawlers are summarized separately. Sheet checks report canvas dimensions, swimmer A=C equality and whether any frame touches the cell boundary. These checks can find structural errors but cannot grade the drawing.
- Numeric ranges are advisory by default. `--strict` is an opt-in mechanical gate; do not use it as an art-approval decision.

**Colour transitions and value structure**
- Use a readable value path across large anatomical regions. A broad back–belly boundary usually benefits from one or two transition tones; let the species' markings and body shape determine their placement instead of drawing a fixed horizontal band.
- Keep markings simple enough to read at native scale. Flat fills are a reliable starting point; a deliberate highlight, texture or softened edge is acceptable when it clarifies the species, material or lighting.
- Avoid near-black seams on light bellies and at fin attachments. Outline colour and weight should relate to the adjacent region; inspect the join at native scale; do not fix it with a sprite-wide automated pass.
- Keep a coherent palette, but allow distinct hues for natural markings and anatomical regions. The approved references range from PF's more colourful palette to AC's muted silver-blue; neither a 75% hue-family threshold nor one chroma/dark-share range describes all three.
- Fins should feel attached to the body and read as membranes or solid fins. Vary silhouette, size, opacity and accent by species instead of applying one biome-wide recipe.
- Estimate body shape with the silhouette and species anatomy in view. Automated opening/aspect values can help locate outliers, but they do not define whether an oval, disc, eel or ray is correct.
- Give each species a recognizable marking layout. Repeated motifs are fine when biologically plausible; avoid making a whole roster read as one stripe-and-belly template.

**Frame consistency**
- Any recolour, texture, mottle or shading pass must keep static body pixels identical across the four frames in a row. Use a fixed mask/seed, never per-frame clustering or random placement. Check A=C after the edit; the audit reports exact equality by direction row.
- Walking crawlers reuse the shell/body; only legs, claws, antennae and feet should carry the walk motion.

**Workflow**
- Generator-made biomes (`cs`, `fs`, `ms`, `bb`, `by`, `cw`, `uc`) are code in `.agents/tools/creature_gen/` (species modules, renderer, palettes, gaits, install). Restyle or extend them with `.agents/rules/creature_workflow.md` - the process used for cs / fs / ms (and the v4 pass for cs) in October 2026 - instead of editing their PNGs by hand.
- Run `python .agents/tools/creature_audit.py <group>/<biome> --montage _audit/<prefix>.png` before a preview. Resolve structural sheet errors, then use advisory flags to choose sprites for visual review against the accepted references.
- Build each biome from per-species silhouettes, a controlled palette, readable fins and hand-placed markings, followed by at most one light biome grade. Do not stack the previous biome's gloss, dither, sheen or shading passes.
- Do not run project-wide outline, eye or head-shape post-processes without a before/after montage of PF and BW accepted references.
- The `hard_step` and background-distance hints can also fire on accepted reference sprites. Inspect the artwork side by side; do not treat those flags as failures.

## 1. Spritesheet Layouts and Animation
- **Swimmers (Fish)**:
  - Layout: 6 rows corresponding to directions (E, SE, SW, W, NW, NE). No straight N/S rows.
  - Animation: 4 frames per row, 0.12 s per frame in the `.aseprite`, pattern A-B-A-C (frame 3 = frame 1).
  - **The body is static** (body bend = 0 px — bending makes the shading/markings flicker). Only fins move, each fin kind in its own way (never one motion copied to every fin): the caudal swings up and down as one piece, about 1-2 px at the trailing edge (in pf / bw / ac 83-93% of the tail pixels change every frame); dorsal/anal/pelvic/pectoral flutter ±1-1.5 px at the outer edge with the base anchored and do not mirror the tail; the anal fin follows the tail's vertical direction. Generator biomes set this per species with a gait (`gait.py`).
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
- Prefer ≥1 px of safety margin where the species and frame allow it. Some accepted PF/BW/AC swimmer rows touch the cell boundary; inspect those tips in the real viewport and confirm they do not clip before treating contact as an error.
- Every sheet has a matching `<prefix>_<name>.aseprite` with one tag per row.

## 2. Rendering & Shapes (Core Style)
- **Silhouette first**: every species has its own body profile (depth, head shape, fin positions). Never reuse another species' body template and only recolour it.
- **Form shading**: light usually comes from above. Measured on pf / bw / ac (October 2026): light tones climb in small even steps (about 0.10 OKLab L; pf 0.085) and sit in the upper third of the body (bw 0.33 from the back); the brightest tenth is only one small step (~0.13) above its neighbours; the back under the dorsal fin is not darker than the body. No round / elliptical highlight patch, and do not remove light by capping every tone at a mid value (that flattens the body). A matte species is fine on request, but it still mixes its tones visibly (steps 0.06-0.09).
- **Transitions**: flat colour regions and crisp boundaries are valid pixel-art choices. Add intermediate tones where a broad anatomical plane needs volume; do not force gradients or the same band shape onto every species. A belly may shift toward the body hue, but the 20–26% figure is a starting experiment, not a fixed formula.
- **Outlines**: prefer an outline related to the adjacent body colour. Avoid using one fixed near-black across a multicoloured sprite; near-black or pure black pixels are allowed when they serve the eye, silhouette or local contrast (the accepted PF snapshot contains a small number of exact-black pixels). Where a body meets a fin, avoid a seam that makes them look detached, but judge the join at native scale rather than applying a fixed RGB/OKLab percentage to every edge.
  - Outlines may vary along the body, but each outline pixel must be a dark shade of the body colour next to it (e.g. blue head -> dark blue outline, orange flank -> dark brown-orange outline). Never one fixed outline colour on a multi-coloured fish.
- **Markings**: Hand-place bars, stripes, spots and blotches so their shape reads at native scale. Flat fills are a reliable default; a highlight, translucent edge or small detail may be intentional if it supports the species. Avoid accidental halos, stray pixels and uniform noise that obscures the marking.
- **Fins**: drawn only OUTSIDE the body silhouette — no fin base or ray lines across the body (the pectoral may show as a soft lighter patch on the flank). Body-family colour close to the body's tone (pf / bw / ac: 0.03-0.14 lighter), alpha ~150-240 falling smoothly from base to edge (solid dark fins are fine on dark species); rays are faint colour lines, never alpha stripes; 10+ colours per fin (membrane lightening toward the edge, soft mottle) rather than one flat tint; signature fin colours (red edges, black tips, white leading edges) go on the rim or tip. Long filaments must sit on a fin membrane — bare dark lines read as "spider legs".
- **Eyes** (standard set by the planted-freshwater sprites):
  - Core = exactly 2 px stacked vertically: a white/off-white highlight directly ABOVE a single near-black pupil. Never side by side, never diagonal, never a 2-px-wide or tall black pupil.
  - Highlight colour: the sprite's own off-white (`#f0ece0`, `#fbe4b2`, `#eff1e5` or similar, warm gold in blackwater); pupil: near-black from the palette (e.g. `#100905`). No pure `#ffffff`/`#000000`.
  - Exactly one eye per visible side. Remove any second white dot, fake eye or dark blob (spots, mouth ends, band ends) that reads as another eye near the head. Exception: flatfish (halibut, flounder) show both eyes on the top side, each with the same 2-px core and ring, spaced identically in E, SE and NE.
  - Optional coloured ring (e.g. red for discus/altum, orange `#c89040` for bass): pixels hugging the pupil, normally the bottom-left corner (left of, below and diagonal to the pupil). On busy/banded or low-contrast bodies (banded grunter, mackerel) this contrasting ring is REQUIRED so the eye stands out from the pattern.
  - Keep the cells around the eye calm: no checkerboard of light/dark pixels, no extra highlight pixels beside the eye; subocular/cheek bars must not run into the pupil.
  - Place the eye at the same anatomical spot in E, SE and NE (rays/flat-headed species: near the front of the head, not mid-body) and keep it in the same relative position in all 4 frames.
- **Mouths**: none on small heads (a mouth slit or white teeth read as a second eye). Do not draw a horizontal (or diagonal) dark mouth line across the head. At most a 1-3 px dark notch at the snout tip; avoid pixels at the tip that read as a second eye.
- **Bellies**: never a single flat colour. Give the underside a soft tonal gradient (rim/bounce light on the lowest edge, a gentle warm/cool drift along the length, patches of one-step variation or a dither band along the ventral line). In generator biomes the one-volume shading supplies this gradient (v4 swimmers add neighbouring tones mixed in 2 px clusters, fixed across frames); never 1 px checkers or lone single pixels.
- **Backward swimmers** (cuttlefish, squid when jetting, etc.): the E-facing frames show the mantle leading and the arms/tentacles/eyes trailing behind, because the animal moves tail-first.
- **Translucent species** (glass bloodfin, golomyanka, isaza): lower the body alpha behind the head and show spine / gut / swim-bladder pixels.

## 3. Biome Styles
Each biome has ONE shared style for all of its creatures. In the hand-made reference biomes (pf, bw, ac) it is a grade applied to every finished frame; the generator-made biomes (3.4) apply their look while rendering. The listed signature colours are excluded from the grade.

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

### 3.4 Generator-made biomes (`cs`, `fs`, `ms`, `bb`, `by`, `cw`, `uc`)
Their look is code (`.agents/tools/creature_gen/pal.py`) and is documented once, in each biome's README: water measurements,
colour families or palette, shadow / highlight / fin tints, gaits and the species sets. The process and each biome's stage
(v1, v3 restyle, v4 reference match) are in `.agents/rules/creature_workflow.md`. Do not copy those numbers here.

| Biome (prefix) | Water | README |
|---|---|---|
| clear spring (`cs_`) | very light cyan-teal | `assets/creatures/freshwater/clear_spring/README_creatures.md` |
| forest stream (`fs_`) | leaf green | `assets/creatures/freshwater/forest_stream/README_creatures.md` |
| marsh swamp (`ms_`) | dark murky olive | `assets/creatures/freshwater/marsh_swamp/README_creatures.md` |
| billabong (`bb_`) | tea-teal over red-ochre clay | `assets/creatures/freshwater/billabong/README_creatures.md` |
| bayou (`by_`) | tea-dark olive | `assets/creatures/freshwater/bayou/README_creatures.md` |
| cold water (`cw_`) | deep steel blue | `assets/creatures/marine/cold_water/README_creatures.md` |
| underwater cave (`uc_`) | near-black, faint blue glow | `assets/creatures/special/underwater_cave/README_creatures.md` |

### 3.5 Biomes without finished creatures yet — art direction
Apply the same mechanism (shadow tint, mid-tone cast, highlight colour, fin tint, signature exception) when their creatures are made; for generator-made biomes use the v3 colour fit instead (`.agents/rules/creature_workflow.md`, stage 1: measure the water, derive colour families, keep bodies out of the discord band). Directions below come from each biome's water tint and backgrounds; confirm before the first batch.

| Biome (prefix) | Shadows → | Mid-tone cast | Highlights | Fin tint | Keep ungraded |
|---|---|---|---|---|---|
| rocky_river (`rr_`) | cool slate `#1c2a30` | light teal | clear white-cyan | clear, faint teal | trout spots, red fin edges |
| rift_lake (`rl_`) | deep cobalt `#141c34` | blue | cool white | blue-tinted | cichlid yellows/oranges and blues (all saturated colours) |
| muddy_river (`mr_`) | olive-brown `#241e12` | khaki, desaturated more (~15%) | dull cream | murky brown, less transparent | none (low contrast biome) |
| koi_pond (`kp_`) | jade-grey `#16262a` | light jade | warm white | jade-tinted | koi reds, oranges, golds |
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
