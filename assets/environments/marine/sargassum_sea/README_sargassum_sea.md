# Sargassum Sea – asset notes (marine)

Open ocean far from any coast: clear cobalt water with strong sunlight, golden-brown rafts of floating sargassum
weed at the surface with long fronds hanging down, and floating flotsam. Everything stays at the surface —
nothing sinks or drifts through the water column.
NO sea floor — the water just gets darker below. The famous raft fauna (sargassum fish, frogfish, filefish,
baby turtles, flying fish, mahi underneath) is left for the game's own creatures.
Viewport 384x216, filter Nearest. Prefix `sr_`.

## tiles/
- surface/sr_sargassum_mat_atlas.png (5x1 tiles, 160x32) — a floating mat to run ALONG THE WATER SURFACE
  (own TileMapLayer at the top, top-anchored like a ceiling)
  - Cols: 0 left end (rounded), 1 middle (seamless in x), 2 right end (rounded), 3-4 middle variants with longer fronds
  - Leave gaps between end tiles for open water
- water/sr_water_surface_4f.png — surface line (4 frames); sr_water_tint.png = light blue tint
- (no ground / slope tiles — there is no floor)

## decoration/
- rafts/ (TOP-anchored — put their top on the water surface line):
  sargassum raft large / medium / small, drift log with gooseneck barnacles (sessile) hanging under it,
  floating coconut
  - Keep space between rafts so the surface does not get crowded

## background/  (384x216, fixed screen)
- far: bright cobalt under the surface deepening to dark blue, sun shafts, a thin continuous distant mat plus distant rafts on the surface
- mid: continuous sargassum mat covering the WHOLE surface (seamless in x) with long hanging fronds —
  so the surface always looks filled even where tiles/rafts leave gaps (alpha)
- near: dark sargassum masses in the top corners with long fronds (alpha — above fish for depth)

## effects/
- ambient: sr_light_shaft.png (48x216), sr_sun_glints_32x12_6f.png (tileable sparkle strip just under the
  surface), sr_caustics_64_4f.png (on the underside of rafts / upper water), sr_depth_fade_overlay.png
  (384x216 — darkens toward the bottom, the open-ocean depth; above fish)
- bubbles: bladder bubbles (10x50, 6f — tiny bubbles rising from the air bladders), sizes strip (2,3,4,6 px)
- particles: sr_plankton_specks_4.png (4 tiny light specks for ambient plankton)
