# Asian Peat Swamp – asset notes (freshwater)

Borneo / Sumatra peat-swamp forest: very acidic, wine-dark tannin water, deep black-brown fibrous peat with streaks
of white kerangas quartz sand, slender stilt-rooted trees, plank buttresses, pneumatophores, rattan and sago
debris, winged dipterocarp seeds — with Barclaya, Cryptocoryne cordata, pygmy crypts and Nepenthes pitchers.
Its fauna (bettas, chocolate & sparkling gouramis, Boraras/Paedocypris, licorice gouramis...) is left for the
game's creatures; decor uses only plants, wood and empty shells.
Different from blackwater (Amazon: amber tea water, pale sand, catappa leaves) and marsh_swamp (green, cattails).
Viewport 384x216, tile 32x32, filter Nearest. Prefix `ap_`.

## tiles/
- ground/ap_substrate_atlas.png (5x4) — same 9-slice layout as the other biomes
  - Row 0 perspective floor of black peat with dead leaves (variants: white kerangas sand streak, winged seed)
  - Row 1 smooth wavy transition; rows 2-3 matted fibrous peat with buried wood
  - Variant decals: wood, leaf bits, quartz grains, root strands, quartz pebble, seed
- terrain/ap_peat_bank_slopes_atlas.png (8x2 slopes)
- water/ap_water_surface_4f.png (very calm), ap_water_tint.png (wine-dark tint),
  ap_tannin_foam_strip_64x8_4f.png (brown tannin foam patches on the water line, slow drift)

## decoration/
- misc: hollow peat log with shelf fungi (hide), plank buttress root (arched gap fish swim through),
  pneumatophores (breathing-root pegs)
- debris: dipterocarp seed (2-wing / 5-wing), Dillenia leaf, rattan segment, sago frond piece, swamp figs
- rocks: peat block large / small, white quartz pebbles
- shells: Brotia snail shell (spiny spire), Clea snail shell (banded cone) — both empty

## vegetation/
- plants: Barclaya (large / small — wavy wine-red ribbons), Crypt cordata (purple heart leaves),
  Nepenthes ground pitchers (cluster on the peat at the swamp edge)
- grass: pygmy crypt patch
- roots: ap_nepenthes_vine_hanging.png (TOP-anchored vine with dangling pitchers), ap_stilt_roots.png (bottom)

## background/  (384x216, fixed screen)
- far: wine-dark gradient, narrow canopy beams, slender stilt-rooted pole trees
- mid: two buttressed trunks, pneumatophores, drooping rattan stems
- near: big buttressed trunk at the right edge, leaf-litter mound bottom-left, Nepenthes vine top-left

## effects/
- ambient: ap_tannin_murk_overlay.png (384x216, heavy; above fish), ap_canopy_sunbeam.png (32x216), ap_caustics_64_4f.png
- particles: ap_peat_puff_36x24_5f.png (dark peat cloud from the floor), ap_peat_particles_6.png
- bubbles: sizes strip, bubble pop 4f

## Placing things on the floor (perspective surface row)
- Put the bottom edge of bottom-anchored sprites inside rows 4-18 of the surface tile row (the top face);
  higher = further back. Use y-sort so things nearer the lip draw in front.
