# Coral Reef – asset notes (marine)

Shallow tropical coral reef: bright turquoise water, strong rays and caustics, white coral sand with
colourful grit, porous reef limestone, and lots of hard corals, sea fans, soft corals and anemones.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `ce_` = coral reef.

## tiles/
- ground/ce_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (coral sand with ripples
    and rubble bits) seen slightly from above, rows 19-20 = LIP, rows 21-31 = sand front face.
    Middle tile is clean; variants: mushroom coral, zoanthid colony on a rubble chip
  - Row 1: TRANSITION — sand with coral rubble -> reef limestone (variants: rubble, shell bits)
  - Row 2: GROUND — porous reef limestone with fossil coral heads, repeat vertically (variants: fossil head, cavity)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, dead coral branch)
- terrain/ce_sand_slopes_atlas.png (8x2) — sand bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/ce_water_surface_4f.png — 4 frames 32x32; ce_water_tint.png = very light turquoise tint

## decoration/coral/  (hard corals, all bottom-anchored)
- brain coral green / yellow small, staghorn orange / pink, table coral, plate coral (purple), pillar coral,
  bubble coral, sun coral (Tubastrea), finger coral, elkhorn, mushroom coral

## vegetation/
- plants: sea fan purple / orange (gorgonians), pink soft coral tree, toadstool leather, bubble-tip anemone
  (clownfish home), Kenya tree, seagrass, halimeda
- grass: zoanthid colonies S/M
- (roots/: none for this biome)

## decoration/
- rocks: live rock L/M/S (coralline crust + tiny coral colonies)
- shells: giant clam (blue mantle), tiger cowrie, trochus
- debris: coral rubble, dead (bleached) coral branch
- misc: long-spine urchin, christmas tree worms on rock, feather star, blue linckia star, reef arch (fish hide)

## background/  (384x216, fixed screen)
- far: turquoise gradient, rays, distant reef wall
- mid: colourful coral-head and sea-fan silhouettes
- near: reef rock towers framing both sides; centre left open for fish

## effects/
- ambient: light ray (64x216, strong), caustics (64x64 tileable, 4f, full strength)
- particles: coral spawn (24x48, 6f loop — pink egg bundles rising, nice night event), plankton (6 bits), sand puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
- Corals can also be stacked on live rock (put their base on the rock's top), like the table coral in the preview.
