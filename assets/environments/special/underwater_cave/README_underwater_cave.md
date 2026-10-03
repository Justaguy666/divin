# Underwater Cave – asset notes (special)

Flooded sea cave: almost black water lit only by blue light from the cave mouth, a dark rock ceiling hung with
stalactites, drapery curtains and soda straws, a trapped air pocket shimmering under the roof, grey cave sand
with breakdown rubble, stalagmites, flowstone, rimstone pools with cave pearls, crystal pockets, and the
sessile life of caves (cup corals, sponges, white anemones, hydroids). Viewport 384x216, tile 32x32,
filter Nearest. Prefix `uc_`.

## tiles/
- ground/uc_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (grey cave sand, rubble chips,
    broken soda straws), rows 19-20 = LIP, rows 21-31 = sand front face.
    Middle tile is clean; variants: cave-pearl nest in a little rimstone cup, fallen stalactite tip
  - Row 1: TRANSITION — sand -> dark cave rock (variants: rubble, cave pearls)
  - Row 2: GROUND — dark wet rock with white calcite veins and crystal pockets (variants: crystal vug, flowstone)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, buried soda straw)
- ceiling/uc_cave_ceiling_atlas.png (5x2 tiles, 160x64) — cave roof along the TOP of the screen
  - Row 0 = solid rock body (repeats in x and y) — put above row 1 for a thicker roof
  - Row 1 = underside: lumpy bottom with a tan flowstone rim and small stalactites
  - Cols: 0 left end (rounded), 1 middle, 2 right end (rounded), 3-4 middle variants (more / longer stalactites)
- terrain/uc_sand_slopes_atlas.png (8x2) — sand/rubble bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/uc_water_surface_4f.png — dim surface line (only if a surface is visible); uc_water_tint.png = dark tint

## decoration/
- formations: stalactite large / small, drapery curtain, soda straws (all TOP-anchored — overlap the ceiling
  underside by a few px); stalagmite tall / short, flowstone mound, rimstone pool with cave pearls,
  crystal cluster large / small (bottom-anchored)
- rocks: breakdown block large / medium / small
- misc: cave tunnel (swim-through hide), orange encrusting sponge, purple tube sponges, white cave anemone
- coral: cave cup corals (yellow-orange)
- shells: shell hash (washed in from outside)
- debris: broken soda straws

## vegetation/
- grass: hydroid fuzz (anywhere), entrance algae (only near the mouth where light reaches)
- (no real plants deep in a cave)

## background/  (384x216, fixed screen)
- far: dark cave with the bright blue cave mouth on the right, light spilling in
- mid: roof band with stalactites, stalagmites and fallen blocks
- near: thick dark walls on both sides with stalactites; centre left open for fish

## effects/
- ambient: uc_mouth_light.png (120x180 soft diagonal beam — near the mouth side), uc_air_pocket_64x10_4f.png
  (tileable mirror-like air pocket — run it along the underside of the ceiling), uc_darkness_overlay.png
  (384x216, strong vignette — above fish/props, keeps the centre and the mouth side visible)
- particles: silt-out cloud (64x40, 6f — big billowing cloud when the floor is disturbed), particles (6)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2) — they collect in the air pocket, bubble pop (4f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
