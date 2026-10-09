@icon("res://editor/icons/environment_prop.svg")
class_name SyncedSwayAnim
extends AnimatedSprite2D
## Cây nổi: giữ frame vẽ tay, nhưng chọn frame theo đồng hồ chung
## -> cùng nhịp, cùng hướng với các cây lắc bằng skew (SwayingPlant).
## Sprite sheet là một chu kỳ sin: frame 0 = giữa, 2–3 = lệch phải, 5 = giữa, 7–8 = lệch trái.
## Cả cây nhấp nhô lên xuống theo mặt nước (WaterSurface) tại vị trí của nó.

## Mức nhấp nhô so với mặt nước (1 = theo đúng mặt nước)
@export var bob_amount: float = 0.8

var _base_y: float = 0.0


func _ready() -> void:
	_base_y = position.y


func _process(_delta: float) -> void:
	var t: float = Time.get_ticks_msec() / 1000.0 * SwayingPlant.SWAY_SPEED
	var count: int = sprite_frames.get_frame_count(animation)
	frame = roundi(fposmod(t, TAU) / TAU * count) % count
	# Dời nguyên khối theo số pixel nguyên -> giữ nét pixel
	position.y = _base_y + roundi(WaterSurface.height_at(global_position.x) * bob_amount)
