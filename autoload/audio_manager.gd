extends Node
## Tùy chỉnh âm lượng cho các bus và nối sự kiện đổi bể tới Music/Ambience


const SECTION := "audio"
## Các bus có slider trong settings
const BUSES: Array[StringName] = [
	&"Master",
	&"Music",
	&"Ambient",
	&"SFX",
	&"UI",
]
const DEFAULT_VOLUME := 0.8

@export_group("Category music")
@export var freshwater_music: AudioStream
@export var marine_music: AudioStream
@export var special_music: AudioStream
@export var default_music: AudioStream

@onready var Music: MusicPlayer = $Music
@onready var Ambience: AmbiencePlayer = $Ambience
@onready var UI: UISoundPlayer = $UI

var _volumes: Dictionary[StringName, float] = {}
var _dirty := false


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS # Phát nhạc kể cả khi pause
	_load_volumes()
	AquariumManager.aquarium_changed.connect(_on_aquarium_changed)


# Đổi bể -> đổi nhạc + ambience
func _on_aquarium_changed(info: AquariumInfo) -> void:
	Music.play(_music_for(info))
	Ambience.set_layers(info.ambience)


# Nhạc riêng > Nhạc chung > Nhạc mặc định (cho môi trường)
func _music_for(info: AquariumInfo) -> AudioStream:
	if info.music:
		return info.music
	var by_category: AudioStream
	match info.category:
		AquariumInfo.Category.FRESHWATER: by_category = freshwater_music
		AquariumInfo.Category.MARINE: by_category = marine_music
		AquariumInfo.Category.SPECIAL: by_category = special_music
	return by_category if by_category else default_music


func get_volume(bus: StringName) -> float:
	return _volumes.get(bus, DEFAULT_VOLUME)


## Áp dụng ngay nhưng chưa ghi file
func set_volume(bus: StringName, value: float) -> void:
	_volumes[bus] = value
	_dirty = true
	var idx := AudioServer.get_bus_index(bus)
	if idx == -1:
		push_warning("Audio bus not found: %s" % String(bus))
		return
	AudioServer.set_bus_volume_db(idx, linear_to_db(value))
	AudioServer.set_bus_mute(idx, value <= 0) # linear_to_db(0) = -inf


## Ghi âm lượng vào settings.cfg (gọi khi đóng settings)
func save_volumes() -> void:
	if not _dirty:
		return
	for bus in _volumes:
		Config.set_value(SECTION, String(bus).to_lower(), _volumes[bus])
	_dirty = false


func _load_volumes() -> void:
	for bus in BUSES:
		set_volume(
			bus, 
			float(Config.get_value(SECTION, String(bus).to_lower(), DEFAULT_VOLUME))
		)
	_dirty = false


# F9: nghe thử chỗ nối loop (chỉ hoạt động khi chạy từ editor, bản export tự bỏ qua)
func _unhandled_input(event: InputEvent) -> void:
	if not OS.is_debug_build():
		return
	if event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_F9:
		Music.debug_seek_to_loop()
		Ambience.debug_seek_to_loop()
