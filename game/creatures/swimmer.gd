@icon("res://editor/icons/fish.svg")
class_name Swimmer
extends Creature

## Độ ngẫu nhiên khi chọn đích (càng lớn càng ít "khôn")
const RANDOMNESS: float = 0.3
## Trọng số của vị trí của other trong đánh giá crowding
const CURRENT_POSITION_WEIGHT: float = 1.0
## Trọng số của vị trí hướng tới của other trong đánh giá crowding
const NEXT_POSITION_WEIGHT: float = 0.5
## Trọng số của kích thước của other trong đánh giá crowding
const SIZE_WEIGHT: Vector2 = Vector2(0.3, 0.5)
## Kích thước sinh vật mẫu
const REF_SIZE: Vector2 = Vector2(30, 14)

## Cá nghiêng khi bơi lệch lên/xuống quá ngưỡng này (0 = ngang, 1 = nghiêng)
@export var tilt_threshold: float = 0.3
## Thời gian dừng lại nghỉ giữa các lần bơi (giây, min-max)
@export var rest_time: Vector2 = Vector2(0.3, 1.5)

## Số điểm bốc thử mỗi lần chọn đích
@export var target_samples: int = 6
## Bán kính ảnh hưởng của 1 con cá chuẩn khi tính độ đông (px)
@export var crowd_radius: float = 60.0
## Layer của vật cản cá không chọn làm đích (Layer 5 = swim_obstacle, vd. lá frogbit)
@export_flags_2d_physics var swim_obstacle_mask: int = 16

var _target: Vector2
var _velocity: Vector2 = Vector2.ZERO
var _rest: float = 0.0
var _facing_right: bool = true


func _ready() -> void:
	if animation_names.is_empty():
		animation_names = ["E", "SE", "SW", "W", "NW", "NE"]
	
	super() # Chạy _ready của Creature trước
	position = _rand_position()
	_pick_target()


func _rand_position() -> Vector2:
	return Vector2(
		randf_range(area.position.x + 16.0, area.end.x - 16.0),
		randf_range(area.position.y + 32.0, area.end.y - 32.0)
	)

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
	var best: Vector2 = position
	var best_score: float = INF
	for i in target_samples:
		var candidate_x: float = randf_range(area.position.x, area.end.x)
		var candidate_y: float = clampf(
			position.y + randf_range(-30, 30),
			area.position.y, area.end.y
		)
		var candidate: Vector2 = Vector2(candidate_x, candidate_y)
		# Bỏ qua điểm nằm trong vật cản (vd. lá frogbit trên mặt nước)
		if _is_swim_blocked(candidate) or _is_path_blocked(position, candidate):
			continue
		# Thêm một chút ngẫu nhiên để cá không luôn chọn đúng 1 góc vắng nhất
		var score: float = _evaluate_crowding(candidate) + randf() * RANDOMNESS
		if score < best_score:
			best_score = score
			best = candidate
	_target = best


# Thân cá (kích thước body_size) đặt tại point có chạm vật cản không
func _is_swim_blocked(point: Vector2) -> bool:
	var shape: RectangleShape2D = RectangleShape2D.new()
	shape.size = body_size if body_size != Vector2.ZERO else Vector2(frame_size)
	var query: PhysicsShapeQueryParameters2D = PhysicsShapeQueryParameters2D.new()
	query.shape = shape
	query.transform = Transform2D(0.0, get_parent().to_global(point))
	query.collision_mask = swim_obstacle_mask
	return not get_world_2d().direct_space_state.intersect_shape(query, 1).is_empty()


# Đi thẳng từ from tới to có lúc nào thân cá chạm vật cản không
func _is_path_blocked(from: Vector2, to: Vector2) -> bool:
	var steps: int = maxi(1, int(from.distance_to(to) / 6.0))
	for k in range(1, steps + 1):
		if _is_swim_blocked(from.lerp(to, float(k) / steps)):
			return true
	return false


# Đánh giá mức độ đông đúc quanh 1 điểm
func _evaluate_crowding(point: Vector2) -> float:
	var total: float = 0.0
	for other in get_tree().get_nodes_in_group("creatures"):
		if (
			other == self 
			or not (other is Swimmer)
			or not other.is_node_ready()
		):
			continue
		
		# Cá to hơn chiếm vùng rộng hơn
		var other_size: Vector2 = other.body_size
		if other_size == Vector2.ZERO:
			other_size = Vector2(other.frame_size)
		var size_ratio: Vector2 = other_size / REF_SIZE
		var radius: Vector2 = Vector2(crowd_radius, crowd_radius) * (
			Vector2.ONE + SIZE_WEIGHT * (size_ratio - Vector2.ONE)
		)
		
		# Vị trí hiện tại của other
		var dist_now: Vector2 = (other.position - point) / radius
		total += (CURRENT_POSITION_WEIGHT * maxf(0.0, 1.0 - dist_now.length()))
		# Vị trí other hướng đến
		var dist_next: Vector2 = (other._target - point) / radius
		total += (NEXT_POSITION_WEIGHT * maxf(0.0, 1.0 - dist_next.length()))
		
	return total


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
