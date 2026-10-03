# Forest Stream – asset notes

Shaded woodland stream: green-tinted clear water, dappled light through the canopy, brown sand with
mossy gravel and fallen leaves, dark forest loam with roots, mossy boulders and logs, ferns hanging
from the bank. Viewport 384x216, tile 32x32, filter Nearest. Prefix `fs_` = forest stream.

## tiles/
- ground/fs_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE seen slightly from above
    (fades toward the water colour at the back), rows 19-20 = bright front LIP, rows 21-31 = front face.
    Middle tile is clean; objects lying on the floor only appear in the variant tiles (cols 3-4)
  - Row 1: TRANSITION — sand -> forest loam with fine rootlets (variants: root tangle, gravel lens)
  - Row 2: GROUND — dark loam with buried pebbles and roots, repeat vertically (variants: big root, buried leaves)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: buried snail shell, pebble)
- terrain/fs_bank_slopes_atlas.png (8x2) — gravel/loam bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/fs_water_surface_4f.png — gently moving green surface, 4 frames 32x32; fs_water_tint.png = green tint

## vegetation/
- plants: fs_hanging_fern.png (ANCHOR AT TOP — droops from the bank), bank fern, java fern, liverwort on rock,
  green cryptocoryne, water starwort, moss trails streaming from a stone
- grass: moss cushions S/M/L (put on rocks/logs), grass tufts strip (5 frames, 20x12 each)
- roots: fs_bank_roots_hanging.png (ANCHOR AT TOP), fs_root_mat.png (bottom, mossy)

## decoration/
- rocks: mossy boulders L/M/S (heavy moss caps that drip down the sides), stepping stones, pebbles strip
- shells: pond snail shell, caddisfly case made of leaf pieces
- debris: maple leaf red/yellow, oak leaf green/brown, pine cone, beech nut, twig
- misc: mossy hollow log (fish hide, opening on the left; with a little fern + mushroom), mossy stump

## background/  (384x216, fixed screen)
- far: green gradient, thin canopy shafts, distant trunks, dappled light
- mid: mossy boulders, fallen branches, weed silhouettes
- near: boulders, bank roots and hanging ferns framing both sides; centre left open for fish

## effects/
- ambient: canopy ray (64x216, soft yellow-green), caustics (64x64 tileable, 4f), light spots
  (64x64 tileable, 4f — dappled sunlight flecks to lay over the bottom or mid-water, low alpha)
- particles: falling leaves (3 rows: green/yellow/brown, 6 frames of 12x12 each), 6 particles (4x4)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Floor overlays (*_floor.png, 4 tiles: L, A, B, R): paint them on a second TileMapLayer directly over the surface
  row — L over the left-edge tile, R over the right-edge tile, A/B over middle tiles. They are tileable in x.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.
