# Muck Sand – asset notes (marine)

"Muck diving" site (Lembeh-style): a gently sloping bottom of fine black volcanic sand, murky green-grey water,
almost no reef — just scattered "muck": sunken branches, coconut shells, old bottles and pots, leaf litter —
plus sparse sessile life: orange sea pens, striped tube anemones, carnation soft corals, stinging hydroids,
sponges, sea squirts and patches of paddle grass. The famous weird critters (frogfish, octopus, ghost pipefish,
nudibranchs...) are left for the game's own creatures — the debris here is where they hide.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `mk_`.

## tiles/
- ground/mk_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (black sand with mineral glints,
    burrow holes, bits of leaf litter), rows 19-20 = LIP, rows 21-31 = black sand front face.
    Middle tile is clean; variants: half coconut shell, paddle-grass clump
  - Row 1: TRANSITION — black sand -> volcanic tuff along a smooth wavy line (variants: glints, buried leaves)
  - Row 2: GROUND — compacted dark volcanic tuff with thin ash layers, repeat vertically
    (variants: pumice, buried glass shard)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, shell)
- terrain/mk_black_sand_slopes_atlas.png (8x2) — black-sand bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/mk_water_surface_4f.png — surface line (4 frames); mk_water_tint.png = murky green-grey tint

## decoration/
- debris: old glass bottle, broken clay pot (hollow — hide), coconut husk, coconut half, sunken branch, leaf litter
- misc: orange sea pen large / small, striped tube anemone, stinging hydroid, sea squirts, yellow sponge
- coral: carnation soft coral (Dendronephthya)
- rocks: black rubble, volcanic rock large / small
- shells: murex shell (spiny), olive shell

## vegetation/
- plants: halimeda
- grass: paddle grass

## background/  (384x216, fixed screen)
- far: murky green-grey gradient with faint rays, a black-sand slope rising to the right
- mid: nearer slope with sea-pen silhouettes and a sunken log
- near: dark rubble mounds at both sides; centre left open for fish

## effects/
- ambient: mk_murk_overlay.png (suspended-particle haze, above fish, light), mk_light_ray.png,
  mk_caustics_64_4f.png (use weakly — murky water)
- particles: black-sand plume (48x30, 6f — heavy dark cloud, settles fast), detritus (6 flecks)
- bubbles: sizes strip (2,3,4,6 px; frame = size+2), bubble pop (4f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
