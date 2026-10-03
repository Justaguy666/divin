# Bayou – asset notes (freshwater)

Louisiana cypress-tupelo bayou: slow olive "tea" water lit warm-gold, soft brown mud over grey gumbo clay,
bald-cypress trunks with wide fluted buttresses, crawfish mud chimneys, rust cypress needles, American lotus,
spatterdock, pickerelweed and floating alligator weed — plus old Cajun junk: a sunken pirogue, crawfish trap,
stoneware jug, rusted drum, broken dock piling. Its fauna (alligator gar, bowfin, channel catfish, crappie,
spotted gar, mudminnows...) is left for the game's creatures; decor has no animals (chimneys / trap are empty).
Different from marsh_swamp (dark green, peat, cattails, lilies) and muddy_river (current, silt, willow).
Viewport 384x216, tile 32x32, filter Nearest. Prefix `by_`.

## tiles/
- ground/by_substrate_atlas.png (5x4) — same 9-slice layout as the other biomes
  - Row 0 perspective floor of brown mud with fallen cypress needles (variants: crawfish burrow, needle spray)
  - Row 1 smooth wavy transition into grey gumbo clay; rows 2-3 gumbo clay with root fibres and iron mottles
  - Variant decals: fibres, iron mottle, shell bits, buried wood, clay clod, needles
- terrain/by_mud_bank_slopes_atlas.png (8x2 slopes)
- water/by_water_surface_4f.png (calm, 4f), by_water_tint.png (olive tint),
  by_pollen_film_strip_tile32.png (32x6 yellow pollen film, lay along the water line in patches)

## decoration/
- misc: sunken pirogue (upside-down canoe, fish hide underneath), hollow cypress stump (hide),
  crawfish chimney large / small (empty mud towers), broken dock piling with rope
- debris: cypress needle spray, magnolia leaf, red tupelo leaf, pecan, stoneware jug, empty crawfish trap,
  rusted drum
- rocks: gumbo clay clod large / small, old brick pile
- shells: washboard mussel (empty), fingernail clam shells

## vegetation/
- plants:
  - by_american_lotus_tall (150 px) / _short (100 px) — bottom-anchored, round leaves + bloom held ABOVE the
    water; the water line is 14 px below the sprite top (pick the height that matches your water depth)
  - by_pickerelweed.png — emergent; water line ~26 px below the sprite top
  - by_spatterdock_underwater.png — submerged lettuce-like leaf rosette (bottom)
  - by_southern_naiad.png — low fine bushy clump (bottom)
  - by_alligator_weed_floating.png — TOP-anchored floating mat; water line 6 px below the sprite top
- grass: spikerush S / L
- roots: by_tupelo_roots_hanging.png (TOP-anchored under a bank / screen top), by_cypress_root_flare.png
  (snaking roots with two low knees on the floor; fish weave through)

## background/  (384x216, fixed screen)
- far: olive-gold gradient, warm rays, distant cypress trunks with flared bases
- mid: two closer cypress trunks with fluted buttresses, knees, lotus stalks rising to pads at the surface
- near: big buttress trunk at the left edge, undercut bank with hanging roots top-right, lotus pads overhead

## effects/
- ambient: by_tannin_murk_overlay.png (384x216, above fish), by_light_ray_gold.png, by_caustics_64_4f.png,
  by_rain_ripples_64x16_6f.png (rain hitting the surface seen from below — tile along the water line)
- particles: by_mud_puff_36x24_5f.png (mud kicked up from the floor), by_particles_6.png
- bubbles: sizes strip, bubble pop 4f

## Placing things on the floor (perspective surface row)
- Put the bottom edge of bottom-anchored sprites inside rows 4-18 of the surface tile row (the top face);
  higher = further back. Use y-sort so things nearer the lip draw in front.
