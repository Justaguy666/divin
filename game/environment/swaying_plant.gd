@icon("res://editor/icons/environment_prop.svg")
class_name SwayingPlant
extends Sprite2D
## Cây tự lắc lư theo dòng nước, gốc đứng yên, ngọn nghiêng (skew).


## Góc nghiêng tối đa (radian)
@export var max_angle: float = 0.06
## Tốc độ lắc (rad/s): cây mềm thì chậm, cây cứng thì nhanh
@export var sway_speed: float = 1.5
## Lệch pha theo vị trí ngang, tạo làn sóng lướt qua các cây
## (nên bằng wave_scale trong grass_sway.gdshader để cây và thảm cỏ cùng nhịp)
@export var wave_scale: float = 0.15

var _time: float = 0.0
var _phase: float = 0.0


func _ready() -> void:
	_phase = global_position.x * wave_scale
	# Lệch thời gian ngẫu nhiên nhẹ để các cây cạnh nhau không giống hệt
	_time = randf() * 0.5


func _process(delta: float) -> void:
	_time += delta
	var t: float = _time * sway_speed + _phase
	# Sóng chính + một sóng nhỏ nhanh hơn để chuyển động không đều như con lắc
	var wave: float = sin(t) * 0.8 + sin(t * 2.3 + 1.7) * 0.2
	skew = wave * max_angle
