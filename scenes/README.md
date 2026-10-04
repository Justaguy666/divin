# scenes/ — cấu trúc

Mỗi file .tscn = một "prefab" có thể instance. Script đi kèm nằm ở game/ theo cùng tên nhánh
(vd. scenes/creatures/_shared/swimmer_base.tscn  <->  game/creatures/swimmer.gd).

```
scenes/
├─ main/                    main.tscn (scene khởi chạy), boot / loading
├─ aquarium/                aquarium.tscn — root của bể: camera cố định 384x216, chứa environment + creatures + food + effects
│  └─ layers/               template các lớp: bg_far, bg_mid, bg_near, fg (TileMapLayer / Sprite2D)
├─ environment/
│  ├─ _shared/              environment_base.tscn — khung chung: 4 lớp + water surface + ambient effects
│  ├─ freshwater/<biome>/   <biome>.tscn kế thừa environment_base (vd. planted_freshwater.tscn)
│  │   └─ props/            (planted_freshwater) prefab cây/đá/lũa riêng của biome, dùng asset pf_*
│  ├─ marine/<biome>/
│  └─ special/<biome>/
├─ creatures/               mọi sinh vật di chuyển trong bể (chủ yếu là cá)
│  ├─ _shared/              creature_base.tscn (phần chung)
│  │                        swimmer_base.tscn (bơi: cá, tôm bơi) · crawler_base.tscn (bò đáy: cua, ốc, sên biển)
│  │                        drifter_base.tscn (trôi: sứa) — đều kế thừa creature_base
│  └─ freshwater|marine|special/<biome>/   mỗi loài một .tscn kế thừa swimmer/crawler/drifter_base
├─ decoration/              decor dùng chung nhiều biome (cây, đá, lũa, vỏ ốc, san hô, khác)
│  └─ _shared/              decoration_base.tscn (Sprite2D + sway shader tuỳ chọn)
├─ effects/                 bubbles, particles, water, lighting (GPUParticles2D / AnimatedSprite2D)
├─ food/                    các loại thức ăn
└─ ui/                      hud, aquarium, environment, creatures, menus, components (nút, panel tái sử dụng)
```

Quy ước
- Tên file snake_case, trùng tên node gốc: planted_freshwater.tscn -> node "PlantedFreshwater".
- Thư mục bắt đầu bằng `_shared` chứa scene gốc để kế thừa (New Inherited Scene).
- Biome mới: tạo <biome>.tscn kế thừa environment/_shared/environment_base.tscn, chỉ thay TileSet, background và props.
- Asset (png) ở assets/, TileSet/Material (.tres) ở resources/, scene (.tscn) ở scenes/, script (.gd) ở game/.
