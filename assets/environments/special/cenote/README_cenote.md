# Cenote – asset notes (special)

Flooded limestone sinkhole: crystal-clear water lit by a single sun beam from the opening above, dark cave walls
and an overhang with stalactites, jungle roots hanging down through the water, pale limestone silt with sunken
leaves, a fallen tree, stalagmites from when the cave was dry, Maya pottery offerings, a shimmering halocline
and a milky sulfide cloud deeper down. Viewport 384x216, tile 32x32, filter Nearest. Prefix `cn_`.

## tiles/
- ground/cn_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (pale limestone silt with
    sunken leaves and chips), rows 19-20 = LIP, rows 21-31 = silt front face.
    Middle tile is clean; variants: Maya pottery shard, fallen stalactite piece
  - Row 1: TRANSITION — silt -> limestone (variants: leaves, pottery bits)
  - Row 2: GROUND — porous grey limestone with solution holes and fossil shells (variants: big hole, fossil)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, buried root)
- ceiling/cn_cave_ceiling_atlas.png (5x2 tiles, 160x64) — cave overhang along the TOP of the screen
  - Row 0 = solid rock body (repeats in x and y) — put above row 1 for a thicker overhang
  - Row 1 = underside: lumpy bottom with a pale flowstone rim and small stalactites
  - Cols: 0 left end (rounded — the edge of the sinkhole opening), 1 middle, 2 right end, 3-4 middle variants.
    Leave a gap between a right end and a left end for the opening and put effects/ambient/cn_sun_beam.png
    under it.
- terrain/cn_silt_slopes_atlas.png (8x2) — silt bank (e.g. the rubble cone under the opening)
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/cn_water_surface_4f.png — very calm surface line; cn_water_tint.png = light turquoise tint

## vegetation/
- roots: hanging roots long / medium and root curtain — all TOP-anchored (overlap the ceiling underside or
  the top of the screen by a few px)
- plants: water lily tall / short (stems from the bottom up to pads at the surface — place so the pads touch the
  water line), rim fern (TOP-anchored, droops from the edge of the opening), algae-covered rock
- grass: algae tuft, algae tuft small

## decoration/
- rocks: stalagmite tall / short, fallen stalactite, karst boulder large / medium / small
- misc: karst arch (swim-through hide), Maya offering jar, pottery shards, fossil limestone block
- debris: sunken jungle log, jungle leaves brown / green / red, seed pod
- shells: apple snail shell, freshwater clam

## background/  (384x216, fixed screen)
- far: dark-blue cave with a bright zone under the opening, light cone, far walls and the rubble cone
- mid: cave walls with stalactites, stalagmite silhouettes and fallen blocks
- near: dark rock walls framing both sides; centre left open for fish

## effects/
- ambient: cn_sun_beam.png (40x216, bright narrow beam — use 1-3 under the opening, Add or alpha),
  cn_halocline_64x12_4f.png (tileable shimmering layer — run it across the whole width at mid-depth),
  cn_sulfide_cloud_64x28.png (tileable milky cloud layer — near the bottom, above the floor tiles, below fish),
  cn_caustics_64_4f.png
- particles: falling jungle leaf (12x10, 8f), motes (6 specks drifting in the beam), silt puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6 px; frame = size+2), bubble pop (4f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
