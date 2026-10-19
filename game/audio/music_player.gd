class_name MusicPlayer
extends Node
## Nhạc nền: 2 player thay phiên nhau để crossfade khi đổi bài


const FADE_TIME := 1.5

var _player_a := AudioStreamPlayer.new()
var _player_b := AudioStreamPlayer.new()
var _player_current: AudioStreamPlayer


func _ready() -> void:
	for player: AudioStreamPlayer in [_player_a, _player_b]:
		player.bus = &"Music"
		add_child(player)
	_player_current = _player_a
	

## crossfade sang bài mới, stream = null -> tắt nhạc
func play(stream: AudioStream, fade: float = FADE_TIME) -> void:
	# Cùng stream -> giữ nguyên
	if stream == _player_current.stream and _player_current.playing:
		return
		
	var old := _player_current
	var new := _player_b if old == _player_a else _player_a
	_player_current = new
	
	if stream:
		new.stream = stream
		new.volume_db = AudioFade.SILENT_DB
		new.play()
		AudioFade.fade(new, 0.0, fade) # 0.0 -> bật tiếng
	else:
		new.stop()
		new.stream = null
		
	if old.playing:
		AudioFade.fade(old, AudioFade.SILENT_DB, fade).tween_callback(old.stop)


func stop(fade: float = FADE_TIME) -> void:
	play(null, fade)


## Chỉ dùng khi test: nhảy tới gần cuối bài để nghe chỗ nối loop
func debug_seek_to_loop(seconds_before_end: float = 3.0) -> void:
	if _player_current.stream == null or not _player_current.playing:
		return
	var length := _player_current.stream.get_length()
	_player_current.seek(maxf(0.0, length - seconds_before_end))
