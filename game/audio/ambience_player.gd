class_name AmbiencePlayer
extends Node
## Các lớp ambient chồng lên nhau, lớp chung giữa 2 bể phát liên tục không đổi

const FADE_TIME := 1.0

var _players: Dictionary[AudioStream, AudioStreamPlayer] = {}


## Đặt danh sách lớp. lớp đã có thì phát tiếp, lớp mới fade in, lớp cũ fade out
func set_layers(streams: Array[AudioStream], fade: float = FADE_TIME) -> void:
	# Fade out lớp cũ
	for stream: AudioStream in _players.keys():
		if stream not in streams:
			var player := _players[stream]
			_players.erase(stream)
			AudioFade.fade(player, AudioFade.SILENT_DB, fade).tween_callback(player.queue_free)
	
	# Fade in lớp mới		
	for stream in streams:
		# Nếu null hoặc đang phát thì bỏ qua
		if stream == null or _players.has(stream):
			continue
			
		var player := AudioStreamPlayer.new()
		player.stream = stream
		player.bus = &"Ambient"
		player.volume_db = AudioFade.SILENT_DB
		add_child(player)
		player.play()
		_players[stream] = player
		AudioFade.fade(player, 0.0, fade)


## Chỉ dùng khi test: nhảy mọi lớp tới gần cuối của chính nó
func debug_seek_to_loop(seconds_before_end: float = 3.0) -> void:
	for player: AudioStreamPlayer in _players.values():
		var length := player.stream.get_length()
		player.seek(maxf(0.0, length - seconds_before_end))
