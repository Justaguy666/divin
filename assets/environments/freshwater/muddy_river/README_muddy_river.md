# Muddy River – asset notes

Slow, turbid lowland river: olive-brown murky water with very low visibility, soft silt bottom over
grey clay, sunken snags and root balls, reeds/bulrushes, floating water hyacinth, everything dusted with
silt. Viewport 384x216, tile 32x32, filter Nearest. Prefix `mr_` = muddy river.

## tiles/
- ground/mr_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (silt with flow ripples,
    leaves and twigs) seen slightly from above, rows 19-20 = LIP, rows 21-31 = mud front face.
    Middle tile is clean; variants: half-buried mussel, catfish burrow hole
  - Row 1: TRANSITION — silty mud -> layered grey clay (variants: buried branch, mussel bed)
  - Row 2: GROUND — banded clay with buried stones/twigs, repeat vertically (variants: stone, root)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: shell, pebble)
- terrain/mr_silt_slopes_atlas.png (8x2) — silt bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/mr_water_surface_4f.png — 4 frames 32x32; mr_water_tint.png = strong brown tint (murky)

## vegetation/
- plants: bulrush tall/short (emergent – continues above the water line), mr_water_hyacinth.png (ANCHOR: the
  water line is 22 px below the sprite top; leaves/flower above, dark feathery roots below), silty eelgrass, silty hornwort
- grass: sedge S/M
- roots: snag tree (big sunken dead tree, bottom), root ball (uprooted root plate), mr_willow_roots_hanging.png (ANCHOR AT TOP)

## decoration/
- rocks: mud-coated stones L/M/S (silt on top), clay lump, rubble
- shells: mussel open/closed, river snail
- debris: cottonwood leaf, silty leaf pack, branch piece
- misc: silted hollow log (fish hide), catfish burrow mound (fish hide)

## background/  (384x216, fixed screen)
- far: hazy olive-brown murk with ghostly snags; mid: snag branches + reeds; near: big snag on the left,
  reeds on the right, willow roots from the top corners; centre left open for fish

## effects/
- ambient: mr_murk_overlay.png (384x216 — suspended-sediment haze, put ABOVE fish/props to sell the murk,
  denser at the bottom), dim light ray (64x216)
- particles: silt cloud (32x22, 5f — fish stirring the bottom), 6 sediment particles (4x4, use many)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites (plants, rocks, shells, debris) somewhere inside that band: higher = further back, lower = closer
  to the front lip. Use y-sort (or z_index by y) so things nearer the lip draw in front.
- Don't put sprite bottoms on row 19-20 (the lip) or below it, or they will look like they float in front of the floor.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.

