# Desert Spring – asset notes (special)

Warm, crystal-clear spring pool in a red desert canyon (oasis): bright turquoise water, white gypsum sand over
red cross-bedded sandstone, living stromatolites built by cyanobacteria, travertine terraces, Chara meadows,
sawgrass/reeds rising to the surface, fan-palm roots hanging in from the banks, sand boils where the spring
wells up, tiny endemic spring-snail shells. Viewport 384x216, tile 32x32, filter Nearest. Prefix `ds_`.
(No moving animals — pupfish etc. are left for the game's own creatures.)

## tiles/
- ground/ds_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (rippled white gypsum sand,
    red pebbles, green cyanobacteria spots), rows 19-20 = LIP, rows 21-31 = gypsum front face.
    Middle tile is clean; variants: sand-boil crater, spring-snail shells
  - Row 1: TRANSITION — gypsum -> red sandstone along a smooth wavy line (variants: gypsum crystals, red pebbles)
  - Row 2: GROUND — red sandstone with soft cross-bedding, repeat vertically
    (variants: gypsum "desert rose" crystal, iron concretion)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, buried palm root)
- terrain/ds_gypsum_slopes_atlas.png (8x2) — gypsum sand bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/ds_water_surface_4f.png — bright surface line (4 frames); ds_water_tint.png = very light turquoise tint

## decoration/
- stromatolites: stromatolite large / medium / small, stromatolite cluster (centrepiece)
- rocks: red sandstone large / medium / small (thin green film on top), travertine terrace (stepped rim pools)
- misc: sandstone ledge (undercut fish hide), spring vent (gypsum cone — put the sand-boil effect on it)
- debris: fan-palm frond, fallen dates, cottonwood leaf, dead reeds
- shells: spring-snail shells (tiny scatter)

## vegetation/
- plants: Chara clump, sawgrass tall (place so the tips reach the water line) / short, sago pondweed
- roots: palm roots hanging large / small (TOP-anchored — a small sandstone overhang with roots under it; place it
  at the very top next to the canyon walls so the rock sits at/above the water line)
- grass: Chara carpet strip, cyanobacteria mat

## background/  (384x216, fixed screen)
- far: bright turquoise gradient with rays, smooth rounded red canyon walls (blue-tinted by the water), white sand
- mid: stromatolite domes and Chara/reed silhouettes
- near: dark red canyon walls with palm roots dangling from the banks; centre left open for fish

## effects/
- particles: sand boil (32x28, 6f loop — on ds_spring_vent or the sand-boil floor tile), floating leaves
  (3 variants, just under the surface line), particles (6), sand puff (28x18, 5f)
- ambient: ds_caustics_64_4f.png (strong — desert sun), ds_light_ray.png
- bubbles: sizes strip (2,3,4,6 px; frame = size+2), bubble pop (4f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
