@icon("res://editor/icons/environment_prop.svg")
class_name SwayingPlant
extends Sprite2D
## Cây tự lắc lư theo dòng nước, gốc đứng yên, ngọn nghiêng (skew).
## Mọi cây dùng chung đồng hồ và tốc độ -> lắc cùng lúc, cùng hướng.


## Tốc độ lắc chung cho mọi cây (rad/s), bằng sway_speed trong grass_sway.gdshader
const SWAY_SPEED: float = 1.5

## Góc nghiêng tối đa (radian): chỉ đổi biên độ, không đổi nhịp
@export var max_angle: float = 0.06


func _process(_delta: float) -> void:
	# Đồng hồ chung của game (không cộng dồn riêng từng cây) -> cây thêm sau vẫn cùng nhịp
	var t: float = Time.get_ticks_msec() / 1000.0 * SWAY_SPEED
	# Sóng chính + một sóng nhỏ nhanh hơn để chuyển động không đều như con lắc
	var wave: float = sin(t) * 0.8 + sin(t * 2.3 + 1.7) * 0.2
	skew = wave * max_angle
