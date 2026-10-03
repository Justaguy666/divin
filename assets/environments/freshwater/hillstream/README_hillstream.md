# Hillstream – asset notes (freshwater)

Tropical Asian hill stream: fast, clear turquoise water over golden granite sand, smooth rounded granite
boulders and flat "pancake" stones coated in golden-brown biofilm (the food of hillstream loaches), bamboo litter, Hygrophila pinnatifida on stones, red Lagenandra and Fissidens moss.
Its fauna (hillstream loaches/Sewellia, Rhinogobius gobies, danios, barbs, stream shrimp...) is left for the
game's creatures; decor uses only stones, wood, plants and empty shells.
Different from rocky_river (temperate, mossy boulders, slate, alder/oak leaves) and forest_stream (mossy, ferns).
Viewport 384x216, tile 32x32, filter Nearest. Prefix `hs_`.

## tiles/
- ground/hs_substrate_atlas.png (5x4) — same 9-slice layout as the other biomes
  - Row 0 perspective floor of golden granite sand with current-combed ripples (variants: biofilm stone,
    bamboo leaves)
  - Row 1 smooth transition; rows 2-3 weathered granite with joints
  - Variant decals: gravel, mica, feldspar, quartz vein, stone, snail shell
- terrain/hs_sand_bank_slopes_atlas.png (8x2 slopes)
- water/hs_water_surface_4f.png (lively, choppier surface), hs_water_tint.png (light turquoise tint)

## decoration/
- misc: flat stone stack cave (loach cave, dark gaps between slabs), granite ledge (undercut — fish hide)
- rocks: smooth boulder large / medium / small (biofilm on top), pothole rock, cobble riffle strip
- debris: bamboo leaves, bamboo culm tube (open end — tiny hide), forest leaf, water-worn branch
- shells: Sulcospira stream snail, horned nerite (empty)

## vegetation/
- plants: Hygrophila pinnatifida growing on a stone, Lagenandra red (large / small)
- grass: Fissidens moss cushion on a stone
- roots: hs_bank_roots_hanging.png (TOP-anchored, pale roots leaning downstream)

## background/  (384x216, fixed screen)
- far: turquoise gradient, slanted rays, distant boulders
- mid: big boulders with biofilm tops
- near: dark boulders in the bottom corners, undercut bank with roots top-left

## effects/
- ambient: hs_current_streaks_64x32_4f.png (fast current streaks sliding left→right; tile over mid-water),
  hs_clear_overlay.png, hs_light_ray.png, hs_caustics_64_4f.png
- bubbles: sizes strip, pop 4f
- particles: hs_sand_drift_48x12_4f.png (sand grains hopping along the floor in the current), hs_particles_6.png

## Placing things on the floor (perspective surface row)
- Put the bottom edge of bottom-anchored sprites inside rows 4-18 of the surface tile row (the top face);
  higher = further back. Use y-sort so things nearer the lip draw in front.
