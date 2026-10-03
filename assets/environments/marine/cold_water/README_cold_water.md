# Cold Water – asset notes (marine)

Temperate / boreal rocky sea floor: cold blue-green water, grey gravel with shell hash over slate bedrock,
boulders crusted with pink coralline algae and barnacles, red and brown seaweeds, plumose anemones, sea stars,
urchins, mussels. (Kelp is only a minor accent here — kelp_forest gets its own biome.)
Viewport 384x216, tile 32x32, filter Nearest. Prefix `cw_` = cold water.

## tiles/
- ground/cw_substrate_atlas.png (5x4 tiles, 160x128) — same 9-slice layout as the freshwater biomes
  - Cols 0-2 = block: col0 left edge, col1 middle (repeat horizontally), col2 right edge
  - Cols 3-4 = interior variants for the same row; any middle/variant tile can sit next to any other
  - Row 0: SURFACE — perspective floor: rows 0-3 empty, rows 4-18 = flat TOP FACE (grey gravel, small stones,
    shell bits) seen slightly from above, rows 19-20 = LIP, rows 21-31 = gravel front face.
    Middle tile is clean; variants: scallop shell, orange sea star lying on the floor
  - Row 1: TRANSITION — gravel -> slate bedrock (variants: shell layer, cobbles)
  - Row 2: GROUND — dark slate bedrock with quartz veins, repeat vertically (variants: quartz vein, fossil)
  - Row 3: GROUND BOTTOM — ragged bottom edge (variants: pebble, shell)
- terrain/cw_gravel_slopes_atlas.png (8x2) — gravel bank one tile higher than the base surface row
  - Row 0 = raised level, row 1 = base surface row; below row 1 use substrate row 1 (transition)
  - Cols: 0-1 gentle up, 2 top, 3 steep down, 4 steep up, 5 top, 6-7 gentle down
- water/cw_water_surface_4f.png — choppy cold surface with white crests, 4 frames 32x32; cw_water_tint.png

## vegetation/
- plants: bladder wrack (Fucus), red sea oak, dulse, young sugar kelp (single), eelgrass (Zostera)
- grass: red algae turf S/M
- roots: kelp holdfast (torn off), barnacled driftwood

## decoration/
- rocks: boulders L/M/S (coralline crust + barnacles), cobbles
- shells: scallop, whelk, blue mussel cluster, barnacle cluster, urchin test
- debris: drifting kelp blade, shell hash
- misc (invertebrates + hide): plumose anemone tall/small, dahlia anemone, sea star orange/purple,
  green urchin, yellow sponge, tube worms, rock ledge cave (fish hide)

## background/  (384x216, fixed screen)
- far: cold blue-green gradient, soft rays, distant reef boulders and a few kelp stipes
- mid: boulder silhouettes with anemone tufts
- near: big boulders framing both sides, one kelp stipe each side; centre left open for fish

## effects/
- ambient: light ray (64x216), caustics (64x64 tileable, 4f, weak), surge strands (64x40 tileable, 4f — water
  rocking back and forth)
- particles: marine snow (6 flecks, 4x4 — use plenty, drifting slowly down), sand puff (28x18, 5f)
- bubbles: sizes strip (2,3,4,6,8 px; frame = size+2), pop 4f (10x10)

## Placing things on the floor (perspective surface row)
- The floor's TOP FACE is rows 4-18 of the surface tile row. Put the bottom edge of bottom-anchored
  sprites somewhere inside that band: higher = further back, lower = closer to the front lip. Use y-sort.
- Don't put sprite bottoms on row 19-20 (the lip) or below it.
- Raised banks (slopes atlas) have the same top face one tile higher, so props on a bank sit 32 px higher.
- Anemones, sea stars, tube worms can also be placed on top of boulders (put their base on the boulder's top).
