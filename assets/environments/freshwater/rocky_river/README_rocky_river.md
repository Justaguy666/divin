# Rocky River – asset notes

Clear, fast-flowing stream over a cobble bed. Current flows LEFT -> RIGHT (plants, algae, roots and
effects all lean right). Viewport 384x216, tile 32x32, filter Nearest. Prefix `rr_` = rocky river.

## tiles/
- ground/rr_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as planted freshwater
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE seen slightly from above
    (fades toward the water colour at the back), rows 19-20 = bright front LIP, rows 21-31 = front face.
    Middle tile is clean; objects lying on the floor only appear in the variant tiles (cols 3-4)
  - Row 1: TRANSITION — gravel -> packed riverbed (variants: buried mussel, gravel lens)
  - Row 2: GROUND — dark packed riverbed with buried stones, repeat vertically (variants: buried boulder, root)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: shell, jasper pebble)
- terrain/rr_bank_slopes_atlas.png (8x2) — gravel bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/rr_water_surface_4f.png — choppy surface with foam caps, 4 frames 32x32, tiles horizontally
- water/rr_water_tint.png — light blue tint overlay

## vegetation/  (bottom-anchored unless noted)
- plants: water crowfoot (Ranunculus, streaming, white flowers), willow moss (Fontinalis) on stone,
  riverweed clump on rock, bucephalandra on rock, hairy algae streamers, eelgrass bent by current (tall/short)
- grass: moss cushions S/M/L (put on rock tops), stream tufts strip (5 frames, 20x12 each), algae film floor overlay (rr_algae_film_floor.png, 128x32 = 4 tiles: L edge, A, B, R edge)
- roots: rr_bank_roots_hanging.png — ANCHOR AT TOP (hangs from the bank / top edge of screen);
  rr_sunken_branch_algae.png

## decoration/
- rocks: boulders L/M/S (granite, sandstone, slate), mossy basalt boulder, jasper stone, slate slab,
  stone stack (cairn), cobble cluster, pebbles strip
- shells: freshwater mussel (open/closed), river snail, caddisfly larva case, limpet
- debris: oak leaf, alder leaf, leaf pack caught on a stone, twig, acorn
- misc: rock arch (fish hide: two boulders + slab), sunken log with algae

## background/  (384x216, fixed screen)
- far: bright clear-water gradient + strong light rays + distant boulders
- mid: boulder + streaming-weed silhouettes
- near: large boulders framing both sides, bank-root silhouette top-left; centre left open for fish

## effects/
- ambient: current streaks (64x32 tileable, 4f – scroll/loop to show flow), surface foam (32x8 tileable, 4f),
  light ray (64x216), caustics (64x64 tileable, 4f – brighter than planted)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10), turbulence puff 6f (40x24, swept right)
- particles: 6 suspended bits (4x4: grit, sand, algae, bark, glint, quartz), drifting leaf 4f (10x10)


## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Floor overlays (*_floor.png, 4 tiles: L, A, B, R): paint them on a second TileMapLayer directly over the surface
  row — L over the left-edge tile, R over the right-edge tile, A/B over middle tiles. They are tileable in x.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.
