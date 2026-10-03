# Planted Freshwater – asset notes

Viewport 384x216, tile 32x32, filter Nearest. Prefix `pf_` = planted freshwater.

## tiles/
- ground/pf_substrate_atlas.png (5x4 tiles, 160x128) — 9-slice layout
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants of the middle column for the same row (with small details)
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE seen slightly from above
    (fades toward the water colour at the back), rows 19-20 = bright front LIP, rows 21-31 = front face.
    Middle tile is clean; objects lying on the floor only appear in the variant tiles (cols 3-4)
  - Row 1: TRANSITION — sand -> aqua soil (variants: buried pebble, white root hairs)
  - Row 2: GROUND — aqua soil, repeat vertically as many rows as needed (variants: pebble, root)
  - Row 3: GROUND BOTTOM — aqua soil with ragged bottom edge (variants: shell, leaf)
  - Paint: 0/1/2 on top, then row 1, then row 2 (xN), then row 3; mix cols 3-4 into the middle
- terrain/pf_mound_slopes_atlas.png (8x2) — aqua-soil mound one tile higher than the base sand row
  - Row 0 = raised level, row 1 = base sand row (place directly below)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
  - Below row 1 use the transition tiles from the substrate atlas
- water/pf_water_surface_4f.png — 4 frames 32x32, tiles horizontally; pf_water_tint.png = light tint overlay

## vegetation/  (all sprites bottom-anchored: set offset so the bottom edge is on the sand)
- plants: amazon sword, vallisneria, rotala red/orange, ludwigia, hygrophila, java fern, anubias, crypt wendtii, cabomba, frogbit (floating, anchored to the water line), duckweed strip (tile 32)
- grass: dwarf hairgrass S/M/L, monte carlo carpet floor overlay (pf_monte_carlo_carpet_floor.png, 128x32 = 4 tiles: L edge, A, B, R edge), grass tufts (strip of 5, 14x12 each)
- roots: spider wood x2, hanging roots

## decoration/
- rocks: seiryu L/M/S, dragon stone L/S, pebbles strip
- shells: ramshorn, mystery snail, nerite, trumpet snail
- debris: catappa (Indian almond) leaf, leaf litter, twig, alder cone
- misc: driftwood log, mossy stump (fish hide), moss ball (marimo) x2

## background/  (384x216, fixed screen, no parallax)
- far: opaque gradient + light rays + far silhouettes
- mid / near: transparent silhouettes, fading with depth; near keeps the centre open for fish

## effects/
- bubbles: sizes strip (2,3,4,6,8,10 px; frame width = size+2), pop 4f (10x10), O2 pearling 6f (8x8)
- particles: 6 suspended particles (4x4), drifting plant fragment
- ambient: pf_light_ray.png (64x216, additive/mix with low alpha), pf_caustics_64_4f.png (64x64 tileable, 4 frames)


## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Floor overlays (*_floor.png, 4 tiles: L, A, B, R): paint them on a second TileMapLayer directly over the surface
  row — L over the left-edge tile, R over the right-edge tile, A/B over middle tiles. They are tileable in x.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.
