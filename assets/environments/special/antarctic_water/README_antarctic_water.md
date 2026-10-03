# Antarctic Water – asset notes (special)

Under the Antarctic sea ice next to an ice shelf (McMurdo-style): very clear violet-blue water, a ceiling of
loose platelet ice, the huge blue face of the ice shelf, black volcanic gravel and scoria covered with
sponge-spicule mats, anchor ice growing on rocks, and a dense sponge garden (giant volcano sponges, glass
sponges) with giant anemones, red sea stars, white urchins and stalked sea squirts. Viewport 384x216, tile 32x32,
filter Nearest. Prefix `an_`. (Different from arctic_water: volcanic black floor, platelet ice, sponge garden.)

## tiles/
- ground/an_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (black volcanic gravel with
    pale spicule-mat patches and anchor-ice sparkles), rows 19-20 = LIP, rows 21-31 = gravel front face.
    Middle tile is clean; variants: anchor ice on a pebble, Antarctic scallop shell
  - Row 1: TRANSITION — gravel -> scoria along a smooth wavy line (variants: spicules, ash layers)
  - Row 2: GROUND — black-red vesicular scoria/basalt, repeat vertically (variants: big vesicles, olivine)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, trapped ice lens)
- ice/an_platelet_ice_ceiling_atlas.png (5x2 tiles, 160x64) — sea-ice ceiling along the TOP of the screen;
  the underside is a fringe of loose tilted ice platelets
  - Row 0 = solid ice body (repeats), row 1 = underside; cols 0 / 2 rounded ends, 1 middle, 3-4 variants.
    Leave a gap for a tide crack and put effects/ambient/an_tide_crack_ray.png under it.
- terrain/an_gravel_slopes_atlas.png (8x2) — gravel bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/an_water_surface_4f.png — icy surface line (only for open water); an_water_tint.png = cold blue tint

## decoration/
- ice: anchor ice on a rock, platelet-ice cluster (TOP-anchored — overlap the ceiling underside),
  glacial ice block large / small (blue, layered)
- sponges: volcano sponge large / small, Rossella glass sponge, yellow tube sponges
- misc: giant anemone, red sea star, white urchin, stalked sea squirts
- rocks: scoria boulder large / medium / small
- shells: Antarctic scallop (thin, pinkish), limpet

## vegetation/
- plants: Desmarestia (branching brown alga), Himantothallus (giant strap blade), hydroid tree
- grass: sponge-spicule mat (wide / small)

## background/  (384x216, fixed screen)
- far: violet-blue gradient, ice ceiling with a tide-crack light shaft, the smooth blue ice-shelf wall on the
  right, distant sponge garden
- mid: scoria mounds and volcano / glass sponge silhouettes
- near: black volcanic rock wall on the left, boulders on the right, platelet-ice masses in the top corners

## effects/
- ambient: an_tide_crack_ray.png (24x216, under a gap in the ice)
- particles: rising platelets (16x60, 6f — ice crystals floating UP), ice glint (8x8, 4f — twinkle on anchor
  ice), ice snow (6 flecks), silt puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6 px; frame = size+2)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
