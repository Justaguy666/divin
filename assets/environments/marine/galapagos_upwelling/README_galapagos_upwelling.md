# Galapagos Upwelling – asset notes (marine)

Cold, nutrient-rich water welling up against the Galapagos lava shelf: green plankton-tinted water, dimmer light,
ropy pahoehoe basalt and coarse olive-green olivine sand, crusted with algae turf, giant barnacles, black coral,
orange cup coral and the endemic Galapagos kelp. Its own fauna (marine iguanas, sea lions, Galapagos penguins,
hammerheads, red-lipped batfish, Moorish idols...) is left for the game's creatures; decor uses only sessile /
near-sessile life and empty shells.
Different from muck_sand (black sand, murky grey) and kelp_forest (tall giant kelp, cold blue).
Viewport 384x216, filter Nearest. Prefix `gu_`.

## tiles/
- ground/gu_substrate_atlas.png (5x4, 32x32)
  - Row 0 perspective floor of olivine sand (basalt grit, olive crests), row 1 smooth wavy transition,
    rows 2-3 ropy pahoehoe basalt (rope folds, vesicles)
  - Cols 0-2 block left/middle/right, cols 3-4 middle variants (sea-lettuce tuft, basalt cobble, algae turf,
    vesicles, acorn barnacles, olivine glints, pebble, pink crust)
- terrain/gu_lava_sand_slopes_atlas.png (8x2 slopes)
- water/gu_water_surface_4f.png, gu_water_tint.png (green tint)

## decoration/
- rocks: pahoehoe rock large / small (rope folds, turf cap, barnacles), lava arch (fish can swim through)
- coral: black coral (large / small — dark wiry branches with yellow-green polyps), cup coral rock
  (orange Tubastraea), red gorgonian
- misc: giant barnacles (Megabalanus cluster), green anemone, chocolate-chip sea star
- shells: spondylus (thorny oyster) shell, urchin test (bare skeleton)

## vegetation/
- plants: Galapagos kelp large / small (claw holdfast, stipe, drooping blade crown)
- grass: sea lettuce clump (Ulva), green turf strip (to edge rocks / sand)

## background/  (384x216, fixed screen)
- far: cold green gradient, faint rays, distant stepped lava ridges and cliffs
- mid: closer lava ridge with kelp and black-coral silhouettes
- near: dark basalt boulders + kelp silhouettes in the bottom corners (above fish)

## effects/
- ambient: gu_plankton_bloom_overlay.png (384x216 green haze, denser near the top; above fish),
  gu_thermocline_shimmer_64x24_6f.png (wavy refraction band where cold and warm water meet — tile across
  mid-water), gu_caustics_64_4f.png, gu_light_ray.png
- particles: gu_upwelling_drift_32x64_6f.png (particles carried UP by the upwelling), gu_plankton_specks_6.png
- bubbles: sizes strip (2,3,4,6 px), bubble pop 4f
