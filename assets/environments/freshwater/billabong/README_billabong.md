# Billabong – asset notes (freshwater)

Australian tropical billabong (oxbow waterhole): clear teal water over red-ochre sandy clay with ironstone
pebbles, shaggy paperbark (Melaleuca) trunks with red root curtains, pandanus stilt roots, pale river red gum
snags, ochre sandstone, gum leaves — and giant blue waterlilies, aponogeton, Ottelia, water snowflake, blyxa,
nardoo. Its fauna (archerfish, barramundi, rainbowfish, saratoga, sooty grunter...) is left for the game's
creatures; decor uses only empty shells and plants.
Different from bayou (olive tea water, grey gumbo) and marsh_swamp (dark green, peat).
Viewport 384x216, tile 32x32, filter Nearest. Prefix `bb_`.

## tiles/
- ground/bb_substrate_atlas.png (5x4) — same 9-slice layout as the other biomes
  - Row 0 perspective floor of red-ochre sand (ironstone grit, gum leaves; variants: gumnuts, paperbark curl)
  - Row 1 smooth wavy transition; rows 2-3 layered red-brown clay with ironstone nodules
  - Variant decals: nodules, pale band, old root channels, quartz grains, sandstone pebble, buried mussel
- terrain/bb_ochre_bank_slopes_atlas.png (8x2 slopes)
- water/bb_water_surface_4f.png, bb_water_tint.png (teal tint)

## decoration/
- misc: paperbark stump (hollow — fish hide), river red gum snag (raised branch, fish swim under)
- debris: gum leaf (green / red), gumnuts, paperbark sheets, pandanus key (fruit segment)
- rocks: ochre sandstone large / medium / small, ironstone pebbles strip
- shells: Velesunio mussel (open, empty), Notopala river snail shell (empty)

## vegetation/
- plants:
  - bb_blue_waterlily_tall (182 px) / _short (122 px) — bottom-anchored; the pads sit on the WATER LINE
    31 px below the sprite top, the violet flower stands above the water
  - bb_aponogeton.png (long wavy ribbon leaves), bb_ottelia_swamp_lily.png (broad oval leaves + bud)
  - bb_water_snowflake_floating.png — TOP-anchored floating leaves + white flowers; water line 6 px below the top
- grass: blyxa L / S, nardoo (four-leaf-clover fern patch)
- roots: bb_pandanus_prop_roots.png (bottom; fish weave between the stilt roots),
  bb_paperbark_root_curtain.png (TOP-anchored fine red roots hanging from an undercut bank)

## background/  (384x216, fixed screen)
- far: teal gradient, rays, red clay bank, distant pale paperbark trunks
- mid: pandanus stilt-root silhouettes, a red gum snag, waterlily stems rising to pads at the surface
- near: paperbark trunk at the left edge, undercut bank with red root curtain top-right, lily pads overhead

## effects/
- ambient: bb_murk_overlay.png (384x216, light, above fish), bb_dappled_light_floor_64x16_4f.png (moving light
  spots on the floor top face, tileable in x), bb_light_ray.png, bb_caustics_64_4f.png
- particles: bb_ochre_silt_puff_36x24_5f.png (red silt kicked up from the floor), bb_particles_6.png
- bubbles: sizes strip, bubble pop 4f

## Placing things on the floor (perspective surface row)
- Put the bottom edge of bottom-anchored sprites inside rows 4-18 of the surface tile row (the top face);
  higher = further back. Use y-sort so things nearer the lip draw in front.
