# Rocky Coast – asset notes (marine)

Wave-battered rocky shore just below the tide line: aerated blue-green surf water with white water under the
surface, rounded beach pebbles over dark wave-cut rock with quartz veins, barnacle and mussel bands on the
rocks, sea lettuce, Irish moss, sea palms, giant green anemones, ochre stars, limpets, chitons and gooseneck
barnacles. Viewport 384x216, tile 32x32, filter Nearest. Prefix `rc_`.

## tiles/
- ground/rc_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (pebble beach seen from above
    with bits of sea lettuce), rows 19-20 = LIP, rows 21-31 = packed gravel front face.
    Middle tile is clean; variants: limpets on a flat cobble, closed giant green anemone
  - Row 1: TRANSITION — gravel -> dark rock (variants: pebbles, shell bits)
  - Row 2: GROUND — dark wave-cut rock with joints and a short quartz vein, repeat vertically
    (variants: quartz vein, crack)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, periwinkles)
- terrain/rc_pebble_slopes_atlas.png (8x2) — pebble bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/rc_water_surface_4f.png — choppy surface line (bigger wave amplitude); rc_water_tint.png

## vegetation/
- plants: sea lettuce (Ulva), Irish moss, sea palm (Postelsia), turkish towel (red blade algae)
- grass: sea lettuce small, green turf, red turf
- (roots/: none for this biome)

## decoration/
- rocks: surf rock large/medium/small (barnacle band at the top, mussels in the middle, green algae fringe
  at the base), pebbles
- shells: limpet, chiton, gooseneck barnacles, periwinkles, moon snail shell, mussel cluster
- misc: crevice rock hide (two rocks with a dark gap for fish + anemone inside), giant green anemone,
  aggregating anemones (mat), ochre star (purple), orange encrusting sponge
- debris: torn sea lettuce, driftwood

## background/  (384x216, fixed screen)
- far: blue-green gradient, white-water band under the surface, distant crags
- mid: faceted rock outcrops with algae silhouettes
- near: tall dark crags on both sides speckled with barnacles/mussels; centre left open for fish

## effects/
- ambient: rc_surge_foam_64x20_4f.png (tileable white-water band — place right under the surface line),
  rc_surge_strands_64x40_4f.png (back-and-forth surge lines), rc_caustics_64_4f.png, rc_light_ray.png
- particles: wave splash (40x28, 6f — a wave crashing in at the surface), drift bits (6 flecks: algae, foam,
  gravel), gravel puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), bubble pop (4f) — use lots near the surface

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
