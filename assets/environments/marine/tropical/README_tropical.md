# Tropical – asset notes (marine)

Bright, shallow tropical lagoon: clear aqua water, strong sunlight and caustics, rippled white coral sand over
cemented beachrock, scattered coral heads (bommies), seagrass and calcareous green algae, conchs, sand dollars,
sea cucumbers and drift from the beach (coconut, palm frond). Viewport 384x216, tile 32x32, filter Nearest.
Prefix `tp_` = tropical. (For a dense reef use coral_reef; tropical is the open, sandy lagoon.)

## tiles/
- ground/tp_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (rippled white sand with
    shell bits), rows 19-20 = LIP, rows 21-31 = sand front face.
    Middle tile is clean; variants: sand dollar, half-buried queen conch
  - Row 1: TRANSITION — sand -> beachrock (variants: shell hash, ripple layers)
  - Row 2: GROUND — pale beachrock with bedding planes and shell fragments, repeat vertically
    (variants: crack, fossil shell)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, coral chip)
- terrain/tp_sand_slopes_atlas.png (8x2) — sand bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/tp_water_surface_4f.png — bright surface line (4 frames); tp_water_tint.png = very light aqua tint

## vegetation/
- plants: sea-grape caulerpa, shaving-brush algae (Penicillus), mermaid's cup (Acetabularia), turtle grass tall,
  halimeda
- grass: paddle grass (Halophila) M/S, sea-grape runner S
- (roots/: none for this biome)

## decoration/
- coral: coral bommie (limestone head with brain / cushion / finger coral), fire coral (Millepora),
  small pink brain coral
- shells: queen conch, sand dollar, scallop pink/yellow, cone shell, cowrie
- debris: coconut, fallen palm frond, bleached driftwood, dead coral branch
- misc: sea cucumber, carpet anemone, cushion star, tuxedo urchin, orange sea star, garden-eel burrows
- rocks: beachrock large/medium/small

## background/  (384x216, fixed screen)
- far: bright aqua gradient with light rays, pale sand dunes, a few distant bommies
- mid: sand ridge with small coral heads and seagrass patches
- near: beachrock and seagrass framing both sides; centre left open for fish

## effects/
- ambient: tp_caustics_64_4f.png (64x64 tileable, 4f — lay over the floor / lower water, Add or low alpha),
  tp_light_ray.png, tp_sun_glints_32x12_6f.png (tileable sparkle strip just under the surface line)
- particles: floating sargassum (drifts slowly along the surface), plankton (6 flecks), sand puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), bubble pop (4f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
