# Arctic Water – asset notes (special)

Under the Arctic sea ice: a ceiling of white-blue ice with ice algae and brinicles, very clear dark-blue water
lit by narrow shafts through open leads, grey glacial silt over stony till with ice-rafted dropstones, soft
"sea strawberry" corals, basket stars, brittle stars. Viewport 384x216, tile 32x32, filter Nearest.
Prefix `ar_`.

## tiles/
- ground/ar_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (grey silt, dropstone gravel,
    worm tracks), rows 19-20 = LIP, rows 21-31 = silt front face.
    Middle tile is clean; variants: dropstone with a white anemone, brittle stars
  - Row 1: TRANSITION — silt -> glacial till (variants: gravel, silt layers)
  - Row 2: GROUND — dark till with mixed angular stones, repeat vertically (variants: big clast, shell)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, trapped ice lens)
- ice/ar_ice_ceiling_atlas.png (5x2 tiles, 160x64) — NEW for this biome: the sea-ice ceiling, placed along
  the TOP of the screen (its own TileMapLayer, drawn above the far/mid backgrounds)
  - Row 0 = solid ice body (repeats in x and y) — use above row 1 if you want a thicker ceiling
  - Row 1 = underside: solid top, lumpy bottom with an ice-algae band and small icicles. One row at y=0 is
    enough for a normal scene.
  - Cols: 0 left end (rounded), 1 middle, 2 right end (rounded), 3-4 middle variants (crack/bubbles, longer
    icicle). Leave a gap between a right end and a left end to make an open lead, and put
    effects/ambient/ar_lead_light_ray.png under the gap.
- terrain/ar_silt_slopes_atlas.png (8x2) — silt bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/ar_water_surface_4f.png — icy surface line (only for open water); ar_water_tint.png = cold blue tint

## vegetation/
- plants: ice algae curtain L/S (TOP-anchored — hang under the ice ceiling), sugar kelp tall/short,
  red leaf algae
- grass: hydroid tuft, algae turf

## decoration/
- ice: brinicle long/short and icicle cluster (TOP-anchored, overlap the ceiling underside by a few px),
  ice block large/small (fallen sea ice resting on the bottom)
- coral: sea strawberry soft coral (Gersemia) large/small
- misc: basket star on a rock knob, white anemone, pale urchin, brittle star
- shells: Arctic whelk, Iceland scallop, Astarte clam
- rocks: dropstone large/medium/small (ice-rafted boulders with a dusting of silt)

## background/  (384x216, fixed screen)
- far: dark-blue gradient, ice ceiling with two open leads and light shafts, distant floor
- mid: ice keels near the top, dropstone mounds and soft-coral silhouettes
- near: dark boulders on both sides, rounded ice keels hanging into the top corners; centre left open

## effects/
- ambient: ar_lead_light_ray.png (24x216, through gaps in the ice), ar_brine_streak_6x40_4f.png (sinking
  brine shimmer under brinicles)
- particles: frazil ice crystals (6 sprites — slow drift, use many), silt puff (28x18, 5f)
- bubbles: under-ice bubble (14x6, 6f — flattened air bubble sliding along the underside of the ice),
  sizes strip (2,3,4,6 px; frame = size+2)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
