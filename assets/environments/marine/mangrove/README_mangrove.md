# Mangrove – asset notes (marine)

Brackish mangrove channel: green-brown tannin water, dappled sunlight through the canopy, red-mangrove prop
roots arching into soft mud, black-mangrove breathing roots, oysters and barnacles on the roots, upside-down
jellyfish, fiddler-crab burrows, fallen leaves and propagules. Viewport 384x216, tile 32x32, filter Nearest.
Prefix `mg_` = mangrove.

## tiles/
- ground/mg_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the other biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (mud with fallen green/yellow
    leaves and small crab holes), rows 19-20 = LIP, rows 21-31 = mud front face.
    Middle tile is clean; variants: Cassiopea jelly, fallen propagule + fiddler-crab burrow
  - Row 1: TRANSITION — mud -> dark root-filled peat (variants: hanging root fibres, shell bits)
  - Row 2: GROUND — dark anoxic peat-mud with root fibres, repeat vertically (variants: buried root, leaves)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: oyster shells, pebble)
- terrain/mg_mud_slopes_atlas.png (8x2) — mud bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/mg_water_surface_4f.png — surface line (4 frames, gentle); mg_water_tint.png = green-brown tint

## vegetation/
- roots: prop roots large/small (bottom-anchored, roots plunge into the mud — set them slightly into the floor
  top face), hanging aerial roots (TOP-anchored: place the limb at/above the water line), pneumatophores
  (breathing-root spikes), root tangle (low arches, small fish can hide underneath)
- plants: shoal grass tall, propagule seedling, red root algae (Bostrychia — put on a root)
- grass: shoal grass short, algae turf

## decoration/
- shells: oyster cluster, mangrove horn snail, periwinkle snail
- debris: leaf green / yellow, propagule, leaf litter strip, bleached driftwood branch
- misc: Cassiopea (upside-down jelly), orange encrusting sponge, sea squirts, crab burrow mound
- rocks: mud lump large/small

## background/  (384x216, fixed screen)
- far: green gradient water with faint mangrove trunks and root arches
- mid: darker trunk + prop-root silhouettes, seagrass tufts
- near: dark root clusters framing both sides; centre left open for fish

## effects/
- ambient: mg_sun_flecks_64_6f.png (64x64 tileable, 6f — dappled light on the floor/water, low alpha or Add),
  mg_light_ray.png, mg_murk_overlay.png (384x216, above fish, darkens bottom/edges slightly)
- particles: falling leaf (12x10, 8f — sinks while see-sawing), floating leaves (3 x 14x6, sit just under the
  surface line), specks (5 tannin/plankton flecks), silt puff (28x18, 5f — when something touches the mud)
- bubbles: sizes strip (2,3,4,6 px; frame = size+2), bubble pop (4f)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
