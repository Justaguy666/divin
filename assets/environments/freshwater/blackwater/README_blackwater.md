# Blackwater – asset notes

Amazon-style blackwater / flooded forest (igapó): tea-coloured tannin water, dim amber light,
pale sand covered in leaf litter, dark humus below, drowned trunks, roots and driftwood, few plants.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `bw_` = blackwater.

## tiles/
- ground/bw_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE seen slightly from above
    (fades toward the water colour at the back), rows 19-20 = bright front LIP, rows 21-31 = front face.
    Middle tile is clean; objects lying on the floor only appear in the variant tiles (cols 3-4)
  - Row 1: TRANSITION — tea-stained sand -> humus (variants: buried branch, leaf layer)
  - Row 2: GROUND — dark humus/peat with leaf fragments, repeat vertically (variants: root, laterite stone)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: snail shell, twig)
- terrain/bw_bank_slopes_atlas.png (8x2) — sand bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/bw_water_surface_4f.png — calm amber surface, 4 frames 32x32; bw_water_tint.png = tea tint overlay
  (tint is stronger than other biomes on purpose — put it over the play area for the tannin look)

## vegetation/
- plants: red root floater (ANCHOR: water line/top, red roots hang down), salvinia strip (tile 32, floats on surface),
  red sword (Echinodorus), brown cryptocoryne, flooded grass tall/short
- grass: leaf pile, small sprouts
- roots: bw_flooded_tree_roots.png and bw_root_curtain.png — ANCHOR AT TOP (hang from the top edge);
  bw_branch_tangle.png — bottom-anchored driftwood tangle with moss

## decoration/
- rocks: laterite (iron-red porous stone) L/S, dark mossy stone
- shells: apple snail shell, dark ramshorn
- debris: catappa (Indian almond) leaf brown/red, curled leaf, seed pod, alder cone, twigs
- misc: hollow log (fish hide, opening on the left), coconut shell hide, cork bark

## background/  (384x216, fixed screen)
- far: dark amber gradient + soft golden rays + distant drowned trunks
- mid: trunks and reaching branches
- near: big trunks framing both sides, branches and aerial roots; centre left open for fish

## effects/
- ambient: light ray (64x216, amber), caustics (64x64 tileable, 4f, dimmer than other biomes)
- bubbles: amber-tinted sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)
- particles: 6 tannin/humus bits (4x4), falling leaf 6f (12x12, rocks while sinking),
  humus puff 5f (24x16, sediment cloud when a fish touches the bottom)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Floor overlays (*_floor.png, 4 tiles: L, A, B, R): paint them on a second TileMapLayer directly over the surface
  row — L over the left-edge tile, R over the right-edge tile, A/B over middle tiles. They are tileable in x.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.
