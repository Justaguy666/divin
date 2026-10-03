# Kelp Forest – asset notes (marine)

Temperate giant-kelp forest: golden-green water lit through a floating canopy, tall kelp stipes with gas floats
rising to the surface, coarse shell sand over sandstone reef bored by piddocks, pink coralline, purple and red
urchins, abalone, bat stars, strawberry anemones. Viewport 384x216, tile 32x32, filter Nearest. Prefix `kf_`.

## tiles/
- ground/kf_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (coarse shell sand with
    cobbles and drifted kelp bits), rows 19-20 = LIP, rows 21-31 = sand front face.
    Middle tile is clean; variants: purple urchin, red abalone shell
  - Row 1: TRANSITION — sand -> sandstone (variants: shell bits, kelp bits)
  - Row 2: GROUND — grey-brown sandstone with piddock bore holes, repeat vertically (variants: coralline, holes)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, fossil shell)
- terrain/kf_sand_slopes_atlas.png (8x2) — sand bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/kf_water_surface_4f.png — surface line (4 frames); kf_water_tint.png = golden-green tint

## vegetation/
- plants: giant kelp tall (~200 px, reaches the surface when placed on the floor) / medium / short,
  kf_giant_kelp_medium_sway_4f.png (4 frames side by side, all same size — base stays fixed, use as
  AnimatedSprite frames), bull kelp (one float + streaming blades), feather boa kelp, sea palm,
  coralline algae (pink jointed), red fan algae
- grass: surfgrass, coralline turf, small coralline algae
- roots: kelp holdfast hide (tangled base with two holes for small fish)

## decoration/
- shells: red abalone, black turban snail, wavy turban snail, purple urchin test
- misc: purple urchin, red urchin, bat star, strawberry anemones (on a rock chip), golden gorgonian
- debris: kelp piece with floats, drifted kelp blade
- rocks: sandstone reef boulder large/medium/small (with coralline + barnacles), cobbles

## background/  (384x216, fixed screen)
- far: golden-green gradient with rays and many pale kelp stipes up to the surface
- mid: darker kelp stipes and reef mounds
- near: dark kelp stipes and rocks framing both sides; centre left open for fish

## effects/
- ambient: kf_canopy_dapple_64_4f.png (64x64 tileable, moving light/shadow from the canopy — tile over the
  scene at low alpha), kf_caustics_64_4f.png, kf_light_ray.png
- particles: drifting kelp blade (16x10, 6f), plankton (6 flecks), sand puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6 px; frame = size+2), bubble pop (4f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
