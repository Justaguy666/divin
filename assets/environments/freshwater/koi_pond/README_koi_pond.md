# Koi Pond – asset notes (freshwater)

Japanese garden koi pond: clear jade water over a bed of smooth river pebbles on firm clay, granite and rust
"kurama" stones, a snow-viewing stone lantern, a toppled stone basin, stepping stones, a bamboo water spout,
stone bridge piers, weeping-willow tips, Japanese iris, pink hardy waterlilies, egeria, sweet flag, and fallen
maple / ginkgo leaves and sakura petals. The koi (and goldfish, medaka...) are the game's own creatures; decor
uses only plants, stonework and empty shells.
Viewport 384x216, tile 32x32, filter Nearest. Prefix `kp_`.

## tiles/
- ground/kp_substrate_atlas.png (5x4) — same 9-slice layout as the other biomes
  - Row 0 perspective floor of rounded river pebbles (variants: ginkgo leaf, red maple leaf)
  - Row 1 pebble layer with a smooth transition into clay; rows 2-3 firm pond clay with sunk pebbles
  - Variant decals: pale pebble, moss specks, kurama pebble, clay band, clam shell, root
- terrain/kp_pebble_bank_slopes_atlas.png (8x2 slopes)
- water/kp_water_surface_4f.png, kp_water_tint.png (light jade tint),
  kp_sakura_petals_floating_64x8_4f.png (petals floating on the water line, slow drift — tile along it)

## decoration/
- misc:
  - kp_yukimi_stone_lantern.png — snow-viewing lantern on curved legs; for SHALLOW spots / on a bank slope:
    the roof + light box stay above water, water line ~32 px below the sprite top (under the lantern base)
  - kp_toppled_stone_basin.png (mossy, lying on its side — small hide)
  - kp_bamboo_water_spout.png — TOP-anchored at the screen top; put kp_inlet_stream under its mouth
- debris: ginkgo leaf, red maple leaf, black-pine needles, sunk sakura petals, old roof tile (small cave)
- rocks: granite boulder large / small, kurama stone (rust granite), flat stepping stone
- shells: Japanese trapdoor snail shell, shijimi clam shells (empty)

## vegetation/
- plants:
  - kp_pink_waterlily_tall (164 px) / _short (106 px) — bottom-anchored; pads on the WATER LINE 11 px below
    the sprite top, pink cup flower just above
  - kp_japanese_iris.png — emergent, for shallow edges; water line ~39 px below the sprite top
  - kp_egeria / kp_egeria_small — bushy bright-green stems (bottom)
- grass: kp_sweet_flag.png (variegated Acorus fan)
- roots: kp_willow_tips_hanging.png (TOP-anchored), kp_mossy_edge_stone.png (TOP-anchored overhanging edge slab
  with moss dripping)

## background/  (384x216, fixed screen)
- far: clear jade gradient, rays, a curved wall of stacked rounded stones (pond edge)
- mid: two stone bridge piers rising to the deck at the top, iris silhouettes, lily stems to pads
- near: mossy boulder bottom-left, lily pads overhead, willow tips top-right

## effects/
- ambient: kp_clear_overlay.png (very light, above fish), kp_dappled_light_floor_64x16_4f.png (light spots on
  the floor top face), kp_ripple_rings_48x12_6f.png (rings on the surface from below — koi feeding / drips),
  kp_light_ray.png, kp_caustics_64_4f.png
- bubbles: kp_inlet_stream_16x64_6f.png (aerated water + bubbles under the bamboo spout), sizes strip, pop 4f
- particles: kp_particles_6.png

## Placing things on the floor (perspective surface row)
- Put the bottom edge of bottom-anchored sprites inside rows 4-18 of the surface tile row (the top face);
  higher = further back. Use y-sort so things nearer the lip draw in front.
