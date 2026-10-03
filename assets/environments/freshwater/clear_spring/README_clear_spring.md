# Clear Spring – asset notes

Crystal-clear limestone spring (Florida springs / Bonito style): turquoise water, bright sunbeams and
strong caustics, white limestone sand with flow ripples, layered limestone bedrock, spring vents with
"sand boils", lush bright-green plants, bleached wood and cypress knees.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `cs_` = clear spring.

## tiles/
- ground/cs_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE seen slightly from above
    (fades toward the water colour at the back), rows 19-20 = bright front LIP, rows 21-31 = front face.
    Middle tile is clean; objects lying on the floor only appear in the variant tiles (cols 3-4)
  - Row 1: TRANSITION — sand -> creamy marl -> bedrock (variants: pebble lens, shell bits)
  - Row 2: GROUND — layered limestone bedrock with solution pores, repeat vertically (variants: cavity, fossils)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pore, calcite vein)
- terrain/cs_sand_slopes_atlas.png (8x2) — white sand dune one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/cs_water_surface_4f.png — glassy surface, 4 frames 32x32; cs_water_tint.png = very light tint

## vegetation/
- plants: tape grass tall/short (Vallisneria americana), sagittaria, chara (muskgrass), pondweed (Potamogeton),
  algae tuft on a limestone rock
- grass: short grass S/M, meadow carpet floor overlay (cs_meadow_carpet_floor.png, 128x32 = 4 tiles: L edge, A, B, R edge)
- roots: cs_cypress_knees.png (bottom-anchored), cs_hanging_roots_pale.png (ANCHOR AT TOP)

## decoration/
- rocks: limestone boulders L/M/S (porous), spring vent rock (vent mouth on top + sand fan), tufa mound, pebbles strip
- shells: clam, apple snail, small snail
- debris: live-oak leaf, cypress twig, bleached log
- misc: limestone ledge with cave (fish hide)

## background/  (384x216, fixed screen)
- far: bright turquoise gradient + strong sunbeams + distant grass meadow
- mid: grass silhouettes + low limestone ledges
- near: limestone rocks and tall grass framing both sides; centre left open for fish

## effects/
- ambient: sunbeam (64x216, brighter than other biomes), caustics (64x64 tileable, 4f, strong),
  vent shimmer (16x48, 4f — place above a vent, low alpha upwelling lines)
- particles: sand boil (32x28, 6f — loop on top of cs_spring_vent_rock or the vent-dimple tile),
  6 particles (4x4: pollen, sand, plant bits, glint)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Floor overlays (*_floor.png, 4 tiles: L, A, B, R): paint them on a second TileMapLayer directly over the surface
  row — L over the left-edge tile, R over the right-edge tile, A/B over middle tiles. They are tileable in x.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.
