class_name AudioFade
extends RefCounted
## Tiện ích fade âm lượng, dùng chung cho nhạc và ambience


## Mức âm lượng coi như im lặng (dB)
const SILENT_DB := -40.0


## Fade volume của player, nếu fade cũ chưa xong thì sẽ bị hủy
static func fade(player: AudioStreamPlayer, to_db: float, duration: float) -> Tween:
	if player.has_meta(&"fade_tween"):
		var old_tween: Tween = player.get_meta(&"fade_tween", null)
		if old_tween and old_tween.is_valid():
			old_tween.kill()
		
	# Tween gắn với player -> player bị free thì tween cũng ngừng
	var tween := player.create_tween().set_trans(Tween.TRANS_SINE)
	tween.tween_property(player, "volume_db", to_db, duration)
	player.set_meta(&"fade_tween", tween)
	return tween
	
