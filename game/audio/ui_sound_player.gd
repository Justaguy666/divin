class_name UISoundPlayer
extends Node
## Âm giao diện: press, hover, ...

 
const POOL_SIZE := 4

## Gán trong inspector. vd: &"press" -> ui_button_press.wav
@export var sounds: Dictionary[StringName, AudioStream] = {}

# vài player xoay vòng để click nhanh không cắt âm trước
var _pool: Array[AudioStreamPlayer] = []
var _next := 0


func _ready() -> void:
	for i in POOL_SIZE:
		var player := AudioStreamPlayer.new()
		player.bus = &"UI"
		add_child(player)
		_pool.append(player)


## Phát âm theo tên. Tên chưa gán -> im lặng
func play(sound: StringName) -> void:
	var stream: AudioStream = sounds.get(sound)
	if stream == null:
		return
		
	var player := _pool[_next]
	_next = (_next + 1) % POOL_SIZE
	player.stream = stream
	player.pitch_scale = randf_range(0.97, 1.03) # làm lệch quãng
	player.play()
