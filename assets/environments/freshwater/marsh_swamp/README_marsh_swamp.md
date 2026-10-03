# Marsh / Swamp – asset notes

Still, dark-green swamp water under a canopy: duckweed carpeting the surface, water lilies on long stems,
cattails, bladderwort, black organic muck over fibrous peat, cypress knees, rotting wood, gas bubbles
seeping from the bottom. Viewport 384x216, tile 32x32, filter Nearest. Prefix `ms_` = marsh swamp.

## tiles/
- ground/ms_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (black muck with sunk
    duckweed and reed bits) seen slightly from above, rows 19-20 = LIP, rows 21-31 = muck front face.
    Middle tile is clean; variants: methane seep with a gas bubble, fallen cattail head
  - Row 1: TRANSITION — muck -> fibrous peat (variants: root mat, reed fibres)
  - Row 2: GROUND — peat with roots and plant fibres, repeat vertically (variants: bog wood, gas pockets)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: snail shell, stone)
- terrain/ms_muck_slopes_atlas.png (8x2) — muck bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/ms_water_surface_4f.png — almost still surface, 4 frames 32x32; ms_water_tint.png = green tint

## vegetation/
- plants: water lily tall (150 px) / short (100 px) — bottom-anchored, pads + flower on the TOP edge, so pick
  the one whose height matches the distance from the floor to your water line; cattail tall/short (emergent);
  ms_bladderwort.png (ANCHOR: water line 12 px below the sprite top, yellow flowers above);
  dark hornwort; frogbit (floating, anchored to the water line); algae blanket ('pond scum' on the bottom);
  ms_duckweed_dense_tile32.png (tile 32x8, lay along the water surface)
- grass: sphagnum moss S/L, sedge
- roots: dark cypress knees (bottom), ms_hanging_moss.png (ANCHOR AT TOP), bog wood tangle with algae strands

## decoration/
- rocks: mossy bog stones L/S, peat clump
- shells: pond snail, ramshorn
- debris: dead lily pad, fallen cattail head, dead reeds
- misc: rotten stump (fish hide)

## background/  (384x216, fixed screen)
- far: dark green haze, drowned cypress trunks, hanging moss; mid: reeds, stumps, lily stems rising to the surface;
  near: big trunks + branches framing both sides, spanish moss from above; centre left open for fish

## effects/
- ambient: ms_murk_overlay.png (384x216 green haze, put above fish/props), dim light ray (64x216)
- bubbles: methane stream (16x64, 6f loop — place over a seep tile), sizes strip, pop 4f
- particles: 6 particles (4x4)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.

