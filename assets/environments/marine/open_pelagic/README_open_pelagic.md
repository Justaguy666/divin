# Open Pelagic – asset notes (marine)

The blue open ocean, far from land and far above the floor: bright ultramarine water, fanned sun rays,
breaking-wave foam and bubble clouds at the surface. NO sea floor and nothing grows here — the only "structure"
is flotsam at the surface (buoy, bamboo FAD raft, ghost net, fishing floats, a lost container) that pelagic fish
gather under. Fauna (tuna, mahi-mahi, oceanic whitetip, sailfish, ocean sunfish, flying fish...) is left for the
game's own creatures; only sessile gooseneck barnacles are drawn on the flotsam.
Different from sargassum_sea (golden weed rafts, cobalt) and twilight_zone (dark, bioluminescent, deep).
Viewport 384x216, filter Nearest. Prefix `op_`.

## tiles/
- water/op_water_surface_4f.png — choppy surface line with foam flecks on high crests (4 frames, tileable)
- water/op_water_tint.png — light ultramarine tint
- (no ground / slope tiles — there is no floor)

## decoration/flotsam/  (all TOP-anchored — put the sprite's top on the water-surface line)
- op_mooring_buoy.png — yellow disc buoy, gooseneck barnacles, long mooring rope ending in a loop
- op_bamboo_fad_raft.png — lashed bamboo FAD with hanging dry palm fronds and frayed ropes
- op_ghost_net.png — lost drift net: float line on top, torn diamond mesh hanging down (keep away from rafts)
- op_glass_fishing_float.png — green glass float in rope netting, short rope tail
- op_trawl_floats.png — three orange trawl floats tied together, gooseneck barnacles
- op_container_adrift.png — lost shipping container floating just under the surface, slight tilt, barnacles
- Spread them out along the surface; leave open water between pieces

## background/  (384x216, fixed screen)
- far: ultramarine gradient (bright near the surface → deep indigo below) with sun rays fanning out — nothing else
- mid: soft light curtains (sway them slowly), faint plankton haze, two distant buoys with mooring lines (alpha)
- near: clouds of tiny bubbles driven down by breaking waves in the top corners (alpha — above fish)

## effects/
- ambient: op_god_rays_overlay.png (384x216, fade/sway), op_light_shaft.png (48x216),
  op_snells_window_glow.png (384x40 bright glow just under the surface), op_caustics_64_4f.png,
  op_depth_fade_overlay.png (384x216 — darkens toward the bottom; above fish)
- surface: op_whitecap_foam_64x20_6f.png — breaking-wave foam on the surface line (tileable in x)
- bubbles: op_wave_bubble_plume_32x64_6f.png (bubbles pushed down by a breaking wave), sizes strip (2,3,4,6 px)
- particles: op_plankton_specks_5.png (5 tiny specks for ambient plankton)
