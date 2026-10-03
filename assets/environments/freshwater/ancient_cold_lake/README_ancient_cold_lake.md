# Ancient Cold Lake – asset notes (freshwater)

An ancient, very deep, ultra-clear cold lake in the style of Lake Baikal: crystal blue water with huge
visibility, grey diatom silt and shore gravel over banded gneiss, rounded boulders, steep ledged walls dropping
into the deep — and the lake's endemic green freshwater sponges (branching Lubomirskia, cushion sponges, sponge
crusts), bright filamentous algae and cold-water moss. Optional winter ice with frozen bubbles.
Its fauna (golomyankas, Baikal sculpins, omul, grayling, endemic amphipods...) is left for the game's creatures;
decor uses only sessile sponges, plants, stone, wood and empty shells.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `ac_`.

## tiles/
- ground/ac_substrate_atlas.png (5x4) — same 9-slice layout as the other biomes
  - Row 0 perspective floor of grey silt with shore pebbles (variants: sponge-crusted pebble, larch cone)
  - Row 1 smooth transition; rows 2-3 banded gneiss bedrock
  - Variant decals: pebble, quartz vein, dark pebble, feldspar flecks, crack, shell
- terrain/ac_gravel_bank_slopes_atlas.png (8x2 slopes)
- water/ac_water_surface_4f.png, ac_water_tint.png (very light blue tint)

## decoration/
- coral (sponges — sessile): Lubomirskia sponge large / small (green finger branches), cushion sponge,
  sponge-crusted rock
- rocks: gneiss boulder large / medium / small, shore pebbles strip
- misc: boulder cave (three leaning boulders with a dark gap — hide)
- debris: ancient larch log (hollow end — hide), larch cones, drowned root plate
- shells: Benedictia shell, Baicalia shell (endemic snails, empty)

## vegetation/
- plants: Draparnaldia tuft (feathery bright-green algae on a pebble), cold-water moss (long trailing stems)
- grass: Ulothrix fringe on a flat stone (strip)

## background/  (384x216, fixed screen)
- far: crystal blue gradient, strong rays, ledged rock walls on both sides dropping into the deep, slope falling away
- mid: boulder slope with silhouettes of the sponge "forest"
- near: dark boulders in the bottom corners with sponge silhouettes (above fish)

## effects/
- ambient: ac_clear_depth_overlay.png (384x216, very light — darkens a little with depth), ac_light_ray.png,
  ac_caustics_64_4f.png,
  ac_winter_ice_cover_384x30.png — OPTIONAL winter layer: clear ice along the top with fine cracks and stacks of
  frozen bubbles (put it over the water-surface tiles)
- particles: ac_silt_puff_36x24_5f.png (grey silt), ac_diatom_particles_6.png
- bubbles: sizes strip, bubble pop 4f

## Placing things on the floor (perspective surface row)
- Put the bottom edge of bottom-anchored sprites inside rows 4-18 of the surface tile row (the top face);
  higher = further back. Use y-sort so things nearer the lip draw in front.
