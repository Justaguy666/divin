class_name AmbiencePlayer
extends Node
## Các lớp ambient chồng lên nhau, lớp chung giữa 2 bể phát liên tục không đổi

const FADE_TIME := 1.0

var _players: Dictionary[AudioStream, AudioStreamPlayer] = {}


## Đặt danh sách lớp. lớp đã có thì phát tiếp, lớp mới fade in, lớp cũ fade out
func set_players(streams: Array[AudioStream], fade: float = FADE_TIME) -> void:
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
