@icon("res://editor/icons/fish.svg")
class_name Swimmer
extends Creature


## Cá nghiêng khi bơi lệch lên/xuống quá ngưỡng này (0 = ngang, 1 = nghiêng)
@export var tilt_threshold: float = 0.3
## Thời gian dừng lại nghỉ giữa các lần bơi (giây, min-max)
@export var rest_time: Vector2 = Vector2(0.3, 1.5)

var _target: Vector2
var _velocity: Vector2 = Vector2.ZERO
var _rest: float = 0.0
var _facing_right: bool = true


func _ready() -> void:
	super() # Chạy _ready của Creature trước
	position = Vector2(192, 144)
	_pick_target()


func _process(delta: float) -> void:
	if _rest > 0.0:
		_rest -= delta
		# Trôi chậm dần
		_velocity = _velocity.move_toward(Vector2.ZERO, speed * delta)
	else:
		var to_target: Vector2 = _target - position
		if to_target.length() < 3.0:
			_rest = randf_range(rest_time.x, rest_time.y)
			_pick_target()
		else:
			_velocity = _velocity.move_toward(
				to_target.normalized() * speed, 
				speed * 2.0 * delta
			)
	position += _velocity * delta
	_update_animation()


# Cá chủ yếu bơi ngang: Điểm mới chỉ lệch dọc tối đa 30px
func _pick_target() -> void:
	_target.x = randf_range(area.position.x, area.end.x)
	_target.y = clampf(
		position.y + randf_range(-30, 30),
		area.position.y, area.end.y
	)


func _update_animation() -> void:
	sprite.speed_scale = clampf(_velocity.length() / speed, 0.4, 1.5)
	if absf(_velocity.x) > 2.0: # Chỉ quay đầu khi thực sự bơi ngang
		_facing_right = _velocity.x > 0
	var dir_y: float = (
		_velocity.normalized().y if _velocity.length() > 1.0
								 else 0.0
	)
	var animation: String
	if dir_y > tilt_threshold:
		animation = "SE" if _facing_right else "SW"
	elif dir_y < -tilt_threshold:
		animation = "NE" if _facing_right else "NW"
	else:
		animation = "E" if _facing_right else "W"
	play_animation(animation)
