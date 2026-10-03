# High Andes Lake – asset notes (freshwater)

A high-altitude Andean lake in the style of Lake Titicaca: cold, ultra-clear cobalt water lit hard by the thin-air
sun, pale calcareous silt full of tiny snail shells, andesite boulders and travertine crust, beds of totora reeds,
floating reed islands, a sunken reed boat and drowned Inca stonework — with Chara meadows, water-milfoil and
quillworts. Its fauna (Orestias killifish, Titicaca water frog, catfish, introduced trout...) is left for the
game's creatures; decor uses only stone, reed, plants and empty shells.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `ha_`.

## tiles/
- ground/ha_substrate_atlas.png (5x4) — same 9-slice layout as the other biomes
  - Row 0 perspective floor of pale calcareous silt with shell hash (variants: andesite cobble, chara tuft)
  - Row 1 smooth transition; rows 2-3 banded lake marl with buried shells
  - Variant decals: shells, organic band, cobble, buried reed, pumice, coiled shell
- terrain/ha_silt_bank_slopes_atlas.png (8x2 slopes)
- water/ha_water_surface_4f.png, ha_water_tint.png (light cobalt tint)

## decoration/
- misc: Inca carved block (stepped-cross relief), Inca wall ruin (fitted stones, trapezoid doorway — fish hide),
  sunken totora reed boat
- rocks: andesite boulder large / medium / small, travertine crust
- shells: Heleobia shell bed (tiny empty snails), pea-clam shells
- debris: cut totora reed bundle

## vegetation/
- plants: ha_totora_reeds_tall (122 px) / _short (83 px) — emergent clumps that continue above the water
  (pick the height that reaches past your water line; ~26 px of the tall one should be above it),
  ha_water_milfoil.png
- grass: Chara meadow (strip), quillwort rosette
- roots: ha_floating_reed_island.png — TOP-anchored floating reed island seen from below (water line ~12 px below
  the sprite top; root curtain hangs down)

## background/  (384x216, fixed screen)
- far: bright cobalt gradient, strong slanted rays, a drowned stepped temple platform, distant reed bed
- mid: totora reed beds on both sides rising to the surface, fitted-stone wall ruins, low chara meadow
- near: foreground totora stems at the left edge, a reed-island underside with roots top-right, a dark
  andesite boulder bottom-right

## effects/
- ambient: ha_sun_glints_32x12_6f.png (hard sun sparkling under the surface — tile along the water line),
  ha_clear_overlay.png, ha_light_ray.png, ha_caustics_64_4f.png
- particles: ha_silt_puff_36x24_5f.png (pale silt), ha_particles_6.png
- bubbles: sizes strip, bubble pop 4f

## Placing things on the floor (perspective surface row)
- Put the bottom edge of bottom-anchored sprites inside rows 4-18 of the surface tile row (the top face);
  higher = further back. Use y-sort so things nearer the lip draw in front.
