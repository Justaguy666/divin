extends Camera2D

# Camera được lệch tối đa bao nhiêu pixel
@export var max_left: float = 20.0
@export var max_right: float = 20.0
@export var max_up: float = 10.0
@export var max_down: float = 20.0
# Bật = camera đi ngược hướng chuột
@export var invert: bool = true
# Độ mượt mà (càng lớn camera phản ứng càng nhanh)
@export var smoothing: float = 30.0

var _center: Vector2


func _ready() -> void:
	_center = position


func _process(delta: float) -> void:
	var screen := get_viewport_rect().size
	var mouse := get_viewport().get_mouse_position()
	
	# t chạy từ -1 (chuột sát mép trái/trên) đến 1 (chuột sát mép phải/dưới)
	var t: Vector2 = ((mouse / screen) - Vector2(0.5, 0.5)) * 2.0
	t = t.clamp(Vector2(-1, -1), Vector2(1, 1))
	
	# Hướng camera sẽ đi
	var dir: Vector2 = -t if invert else t
	
	# Độ dời pixel mỗi hướng
	var offset_px: Vector2 = Vector2(
		dir.x * (max_right if dir.x > 0 else max_left),
		dir.y * (max_down if dir.y > 0 else max_up)
	)

	var target: Vector2 = _center + offset_px
	position = position.lerp(target, 1 - exp(-smoothing * delta))
	
