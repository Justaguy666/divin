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

@onready var Music: MusicPlayer = $Music
@onready var Ambience: AmbiencePlayer = $Ambience
@onready var UI: UISoundPlayer = $UI

var _volumes: Dictionary[StringName, float] = {}


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS # Phát nhạc kể cả khi pause
	
	AquariumManager.aquarium_changed.connect(_on_aquarium_changed)


# Đổi bể -> đổi nhạc + ambience
func _on_aquarium_changed(info: AquariumInfo) -> void:
	Music.play(info.music)
	Ambience.set_players(info.ambience)


func get_volume(bus: StringName) -> float:
	return _volumes.get(bus, DEFAULT_VOLUME)


## Áp dụng ngay nhưng chưa ghi file
func set_volume(bus: StringName, value: float) -> void:
	_volumes[bus] = value
	var idx := AudioServer.get_bus_index(bus)
	if idx == -1:
		push_warning("Audio bus not found: %s" % String(bus))
		return
	AudioServer.set_bus_volume_db(idx, linear_to_db(value))
	AudioServer.set_bus_mute(idx, value <= 0) # linear_to_db(0) = -inf


## Ghi âm lượng vào settings.cfg (gọi khi đóng settings)
func save_volumes() -> void:
	for bus in _volumes:
		Config.set_value(SECTION, String(bus).to_lower(), _volumes[bus])


func load_volumes() -> void:
	for bus in BUSES:
		set_volume(
			bus, 
			float(Config.get_value(SECTION, String(bus).to_lower(), DEFAULT_VOLUME))
		)
