# Rift Lake – asset notes

African rift lake (Malawi / Tanganyika style): deep clear blue alkaline water, golden sand beaches
strewn with empty snail shells (shell beds), huge rounded granite boulders piled into caves and
coated in "aufwuchs" algae, sparse plants (twisted Vallisneria, hornwort).
Viewport 384x216, tile 32x32, filter Nearest. Prefix `rl_` = rift lake.

## tiles/
- ground/rl_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE seen slightly from above
    (fades toward the water colour at the back), rows 19-20 = bright front LIP, rows 21-31 = front face.
    Middle tile is clean; objects lying on the floor only appear in the variant tiles (cols 3-4)
  - Row 1: TRANSITION — sand with a buried shell bed -> granite (variants: dense shell bed, pebbles)
  - Row 2: GROUND — pinkish granite bedrock, repeat vertically (variants: quartz vein, cavity)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: fossil shell, gneiss band)
- terrain/rl_sand_slopes_atlas.png (8x2) — sand bank with shells one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/rl_water_surface_4f.png — 4 frames 32x32; rl_water_tint.png = blue tint

## vegetation/
- plants: twisted Vallisneria tall/short, hornwort (Ceratophyllum), aufwuchs-coated rock
- grass: aufwuchs lawn strip (tile 32x6 — for rock tops), aufwuchs lawn floor overlay (rl_aufwuchs_lawn_floor.png, 128x32 = 4 tiles: L edge, A, B, R edge), algae tuft
- roots: bleached branch (algae-coated), fallen reed stems (rift lakes have little wood)

## decoration/
- rocks: boulder stack with caves (signature mbuna rockwork), boulders L/M/S with algae film,
  holey rock (porous limestone), flat slab, pebbles strip
- shells: Neothauma shell large/small, Lanistes shell, shell bed cluster (homes for shell-dwelling cichlids)
- debris: shell fragments, reed pieces
- misc: rock cave hide (two boulders + capstone)

## background/  (384x216, fixed screen)
- far: deep blue gradient, light rays, distant rock slope rising to the right
- mid: piled boulder silhouettes along the bottom
- near: tall boulder piles framing both sides; centre left open for fish

## effects/
- ambient: light ray (64x216), caustics (64x64 tileable, 4f)
- particles: sand puff (28x18, 5f — cichlid digging / fish touching the sand), 6 plankton bits (4x4)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Floor overlays (*_floor.png, 4 tiles: L, A, B, R): paint them on a second TileMapLayer directly over the surface
  row — L over the left-edge tile, R over the right-edge tile, A/B over middle tiles. They are tileable in x.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.
