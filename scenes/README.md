# Scene Architecture & Structure (`scenes/`)

Every `.tscn` file is an instantiable scene or prefab. Matching GDScript files reside under `game/` with parallel directory naming (e.g. `scenes/creatures/_shared/swimmer_base.tscn` <-> `game/creatures/swimmer.gd`).

Viewport resolution: **640x360** (rendered 1:1, pixel snap enabled; default window 1280x720, stretch mode `viewport` with aspect `expand`).

```
scenes/
├─ main/
│  └─ main.tscn                     Startup scene: manages AquariumHolder, FadeLayer, and CanvasLayer UI
├─ aquarium/
│  └─ <id>_aquarium.tscn            36 biome aquarium scenes (e.g. pf_aquarium.tscn, cs_aquarium.tscn):
│                                   holds Environment instance + Creatures + Food + Effects
├─ environment/
│  ├─ _shared/
│  │  └─ environment_base.tscn      Base parallax tank template:
│  │                                BgFar / BgMid / BgNear (Parallax2D)
│  │                                WaterSurface (ColorRect with shader)
│  │                                Ground + FloorOverlay (TileMapLayer)
│  │                                Props (Node2D, group "floor_sort")
│  │                                Fg (Parallax2D)
│  └─ <category>/<biome>/
│     ├─ <biome>.tscn               Inherited scene from environment_base.tscn with biome TileSet & backgrounds
│     └─ props/                     Biome-specific prop scenes (rocks, plants, wood, shells)
├─ creatures/
│  ├─ _shared/
│  │  ├─ swimmer_base.tscn          Base swimmer scene (Swimmer script, 6 swimming directions, crowd avoidance)
│  │  └─ crawler_base.tscn          Base crawler scene (Crawler script, 4 walk/idle directions, floor tracking)
│  └─ <category>/<biome>/
│     └─ <pre>_<species>.tscn       Per-species inherited scene from swimmer_base or crawler_base
├─ ui/
│  ├─ hud/                          hud.tscn (bottom drawer buttons for AquariumSelector & Settings)
│  ├─ aquarium/                     aquarium_selector.tscn, aquarium_card.tscn (biome switching grid)
│  └─ menus/                        settings_menu.tscn (audio sliders, locale switcher)
├─ effects/                         (Future expansion) Bubbles, particles, water, lighting
└─ food/                            (Future expansion) Fish food pellets & flakes
```

## Conventions

- **File naming**: `snake_case` matching the root node name (e.g. `planted_freshwater.tscn` -> node `PlantedFreshwater`).
- **Inherited scenes**: Folders named `_shared` contain the template scenes meant for inheritance (`New Inherited Scene`).
- **Asset / Scene separation**:
  - Raw visual assets (`.png`, `.aseprite`) live under `assets/`.
  - Resources (`.tres`, `TileSet`, Materials) live under `resources/` or `data/`.
  - Scene definitions (`.tscn`) live under `scenes/`.
  - Scripts (`.gd`) live under `game/` or `autoload/`.
- **New biomes**: Create `<biome>.tscn` inheriting `environment/_shared/environment_base.tscn`, configure the TileSet, background textures, and local props under `props/`.
