class_name CreatureVoice
extends AudioStreamPlayer2D
## Gắn vào scene của creature để nó thỉnh thoảng phát ra âm thanh
## Mọi sinh vật trong bể có chung khoảng nghỉ


## Khoảng nghỉ tối thiểu giữa 2 voice được phát
const GLOBAL_GAP := 2.0

## Âm phát ngẫu nhiên
@export var sounds: Array[AudioStream] = []
## Thời gian phát ngẫu nhiên giữa 2 lần kêu (giây): x = min, y = max
@export var interval: Vector2 = Vector2(20.0, 60.0)
## Độ lệch cao độ, 0.1 = ±10%
@export_range(0.0, 0.5, 0.01) var pitch_variation: float = 0.1

# static: thuộc về class, mọi CreatureVoice cùng đọc/ghi một biến
static var _next_allowed_ms: int = 0

var _timer := Timer.new()


func _ready() -> void:
	bus = &"SFX"
	max_polyphony = 1 # số âm tối đa 1 lúc
	if sounds.is_empty():
		return
	_timer.one_shot = true
	_timer.timeout.connect(_on_timer_timeout)
	add_child(_timer)
	# Hẹn giờ chạy lần đầu
	_timer.start(randf_range(interval.x, interval.y))


func _on_timer_timeout() -> void:
	speak()
	_timer.start(randf_range(interval.x, interval.y))
	
## Phát 1 âm ngay lập tức
func speak() -> void:
	if sounds.is_empty() or not _claim_slot():
		return
	stream = sounds.pick_random()
	pitch_scale = randf_range(1.0 - pitch_variation, 1.0 + pitch_variation)
	play()
		
		
# Trả về false nếu vừa có con khác kêu chưa đủ GLOBAL_GAP giây
static func _claim_slot() -> bool:
	var now := Time.get_ticks_msec()
	if now < _next_allowed_ms:
		return false
	_next_allowed_ms = now + int(GLOBAL_GAP * 1000.0)
	return true
