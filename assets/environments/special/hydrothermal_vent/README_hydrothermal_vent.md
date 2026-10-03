# Hydrothermal Vent – asset notes (special)

Deep-sea vent field: pitch-dark water, sulfide chimneys ("black smokers" and a pale "white smoker") puffing
mineral smoke, dark basalt grit with white bacterial mats and yellow sulfur, giant tube worms with red
plumes, vent mussel beds and big white vent clams. Viewport 384x216, tile 32x32, filter Nearest. Prefix `hv_`.
(No moving animals — vent shrimp / crabs are left for the game's own creatures.)

## tiles/
- ground/hv_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (dark basalt grit, sulfide
    pebbles, white bacterial mat patches, sulfur dots), rows 19-20 = LIP, rows 21-31 = grit front face.
    Middle tile is clean; variants: tiny chimney stub, vent mussel cluster
  - Row 1: TRANSITION — grit -> massive sulfide (variants: sulfur crumbs, buried bacterial mat)
  - Row 2: GROUND — dark sulfide rock with rust stains and sulfur veins, repeat vertically
    (variants: old fluid conduit, metallic crystals)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: basalt pebble, clam shell)
- terrain/hv_grit_slopes_atlas.png (8x2) — grit mound one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/hv_water_surface_4f.png — very dim surface line (only if you show the top at all);
  hv_water_tint.png = heavy dark tint

## decoration/
- chimneys: black smoker tall / medium / short, white smoker, chimney cluster (big centrepiece).
  Put effects/ambient/hv_black_smoke_24x72_6f.png (or hv_white_smoke) with its bottom-centre on the dark
  orifice at the top of a chimney, optionally hv_vent_glow_40.png behind it.
- rocks: sulfide mound, sulfur-crust rock, pillow basalt large / small
- debris: broken chimney fragments
- shells: vent mussel bed, vent clam (closed / open)
- misc: vent anemones on a rock chip

## vegetation/  (sessile animals used like plants)
- plants: giant tube worms large / small (white tubes, red plumes)
- grass: Pompeii worm tubes, bacterial mat white / orange (floor strips)

## background/  (384x216, fixed screen)
- far: near-black gradient, distant chimneys with faint smoke columns
- mid: chimney silhouettes with smoke, tube-worm thickets
- near: two huge dark chimneys framing both sides; centre left open for fish

## effects/
- ambient: black smoke / white smoke plumes (24x72, 6f, loop), heat shimmer (16x48, 4f — just above an
  orifice), vent glow (40x40, warm accent), hv_darkness_overlay.png (384x216 vignette — above fish/props)
- particles: mineral flecks (6), silt puff (28x18, 5f)
- bubbles: liquid CO2 droplets (sizes 2-5, shiny beads rising slowly), small bubbles (2,3,4 px)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
