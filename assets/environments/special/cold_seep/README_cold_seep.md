# Cold Seep – asset notes (special)

Deep, cold sea floor where methane and oil leak up through the mud: no chimneys and no heat, but streams of
methane bubbles, white mounds of methane hydrate ("burning ice"), porous carbonate slabs and chimneys built
by microbes, a brine pool (an underwater "lake"), white/orange bacterial mats, seep mussel and clam beds and
slow-growing Lamellibrachia tube-worm bushes. Viewport 384x216, tile 32x32, filter Nearest. Prefix `sp_`.
(No moving animals — left for the game's own creatures.)

## tiles/
- ground/sp_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (olive-grey seep mud with
    black reduced spots, white bacterial patches, carbonate nodules, gas holes), rows 19-20 = LIP,
    rows 21-31 = mud front face. Middle tile is clean; variants: bubbling seep hole with mat ring, dead clams
  - Row 1: TRANSITION — mud -> carbonate (variants: buried hydrate lens, shell bits)
  - Row 2: GROUND — cemented carbonate pavement with pores, repeat vertically (variants: gas conduit, oil pocket)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: carbonate pebble, clam shell)
- terrain/sp_mud_slopes_atlas.png (8x2) — mud mound one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/sp_water_surface_4f.png — very dim surface line; sp_water_tint.png = heavy dark teal tint

## decoration/
- hydrate: hydrate mound large / small, oily hydrate (orange-stained). Put
  effects/bubbles/sp_methane_stream_12x80_6f.png (or sp_oil_droplets for the oily one) on top.
- rocks: carbonate slab large / medium / small, carbonate chimney tall / short
- misc: mud volcano (crater on top — good spot for a methane stream), brine pool large / small (wide, low;
  lay effects/ambient/sp_brine_shimmer_64x6_4f.png along its surface line)
- shells: seep mussel bed, clam bed (half-buried line), dead clam (open)
- coral: cold-water coral (grows on old carbonate)
- debris: carbonate rubble

## vegetation/  (sessile animals and microbes used like plants)
- plants: tube-worm bush large / small (Lamellibrachia — long tan tubes, few red plumes)
- grass: bacterial mat white / orange (floor strips)

## background/  (384x216, fixed screen)
- far: dark teal gradient, low mounds and faint bubble columns
- mid: carbonate outcrops, chimney and tube-worm silhouettes, bubble columns
- near: dark carbonate blocks framing both sides; centre left open for fish

## effects/
- bubbles: methane stream (12x80, 6f loop — anchor the bottom on a seep hole / hydrate / mud volcano crater),
  oil droplets (10x60, 6f), small bubbles (2,3,4,6 px)
- ambient: brine shimmer (64x6 tileable, 4f), sp_darkness_overlay.png (384x216 vignette — above fish/props)
- particles: marine snow (6), silt puff (28x18, 5f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
