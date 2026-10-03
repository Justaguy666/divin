# Ocean – asset notes (marine)

Classic open-sea floor: bright ocean-blue water with strong sun rays and caustics, rippled white-gold sand
over layered sandstone, scattered sandstone rocks, sea shells, seagrass and green algae, floating sargassum,
and shipwreck relics (anchor, broken bow, amphora, planks, chain). Moon jellies drift through.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `ob_` = ocean.

## tiles/
- ground/ob_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (sand with current ripple
    marks and shell bits) seen slightly from above, rows 19-20 = LIP, rows 21-31 = sand front face.
    Middle tile is clean; variants: sand dollar, cowrie + conch fragment
  - Row 1: TRANSITION — sand with shell layers -> sandstone (variants: shell layer, pebbles)
  - Row 2: GROUND — layered sandstone with burrows, repeat vertically (variants: burrow trace, ammonite fossil)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, shell)
- terrain/ob_sand_slopes_atlas.png (8x2) — sand dune one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/ob_water_surface_4f.png — 4 frames 32x32; ob_water_tint.png = light blue tint

## vegetation/
- plants: ob_sargassum_floating.png (ANCHOR: water line 4 px below the sprite top; branches hang down),
  turtle grass, halimeda (cactus algae), caulerpa runner (lies along the sand), red sea whip
- grass: seagrass tuft S/M, algae turf
- (roots/: none for this biome)

## decoration/
- rocks: sandstone rocks L/M/S (burrow pits, layer lines), pebbles strip
- shells: queen conch, cowrie, nautilus shell, sand dollar, auger shell
- debris: broken amphora, wreck planks, anchor chain
- misc: anchor (rusty), shipwreck bow (fish hide – gaps between planks), rock outcrop cave (fish hide),
  sea cucumber, brittle star, sea pen, blue sea star

## background/  (384x216, fixed screen)
- far: bright ocean gradient with strong sun rays, distant sunken ship silhouette and rocks
- mid: sandstone outcrops + sea whip silhouettes
- near: rocks framing both sides, sargassum shadows at the surface corners; centre left open for fish

## effects/
- ambient: light ray (64x216, strong), caustics (64x64 tileable, 4f, full strength)
- particles: plankton (6 bits, 4x4), sand puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
- Raised dunes (slopes atlas) have the same top face one tile higher, so props on a dune sit 32 px higher.
