@icon("res://editor/icons/fish.svg")
class_name Crawler
extends Creature


## Độ ngẫu nhiên khi chọn đích (càng lớn càng ít "khôn")
const RANDOMNESS: float = 0.3
## Trọng số của vị trí hướng tới của other trong đánh giá crowding
const NEXT_POSITION_WEIGHT: float = 0.5
## Trọng số của kích thước của other trong đánh giá crowding
const SIZE_WEIGHT: Vector2 = Vector2(0.5, 0.0)
## Kích thước sinh vật mẫu
const REF_SIZE: Vector2 = Vector2(30, 16)

## Tiền tố animation khi di chuyển (shrimp: walk_, snail: crawl_)
@export var move_prefix: String = "walk_"

## Vùng mặt sàn mà CHÂN của crawler được phép di chuyển
@export var floor_y: float = 340.0
@export var floor_height: float = 16.0

## Chuyển động bob theo trục Y
@export var bob_speed: float = 4.0 # Tần số dao động
@export var bob_amount: float = 2.0 # Biên độ dao động

## Thời gian duy trì trạng thái
@export var move_time: Vector2 = Vector2(1.0, 4.0)
@export var idle_time: Vector2 = Vector2(1.0, 3.0)

## Layer va chạm của footprint vật cản (Layer 2 = floor_obstacle)
@export_flags_2d_physics var obstacle_mask: int = 2

## Bán kính ảnh hưởng: rộng theo x, rất hẹp theo y (độ sâu)
@export var crowd_radius: Vector2 = Vector2(50, 8)
## Khoảng nhìn trước mỗi bên để so độ đông (px)
@export var look_ahead: float = 80.0

## Số độ sâu bốc thứ khi lập kế hoạch
@export var lane_samples: int = 5
## Tốc độ chuyển làn
@export var lane_speed: float = 6.0


var _dir: int = 1
var _moving: bool = false
var _timer: float = 0.0
var _lane_y: float
# Số lần lập kế hoạch lại liên tiếp khi bị chặn
var _replans: int = 0

# Độ dời cho chân
var _offset: float

# Tọa độ chân cơ sở của crawler
var _base_y: float

# Thời gian cho chuyển động sin
var _bob_time: float = 0.0

var floor_end: float:
	get:
		return floor_y + floor_height


func _ready() -> void:
	_offset = -frame_size.y / 2.0
	sprite.offset.y = _offset
	
	if animation_names.is_empty():
		animation_names = [
			move_prefix + "R", move_prefix + "L", "idle_R", "idle_L"
		]
	
	super()
	
	_base_y = randf_range(
		floor_y + bob_amount, 
		floor_end - bob_amount
	)
	_lane_y = _base_y
	if position.x == 0:
		position.x = _rand_free_x()
	position.y = _base_y
	
	_switch_state()
	_join_floor_sort.call_deferred()

# Chọn x ngẫu nhiên không nằm trong vật cản
func _rand_free_x() -> float:
	var try_time: int = 20
	var default_x: float = area.get_center().x
	for i in try_time:
		var x: float = randf_range(
			area.position.x + 8,
			area.end.x - 8
		)
		if not _is_blocked(Vector2(x, position.y)):
			return x
	return default_x


# Thêm creature vào floor Y sort
func _join_floor_sort() -> void:
	var floor_node: Node = get_tree().get_first_node_in_group("floor_sort")
	if floor_node and get_parent() != floor_node:
		reparent(floor_node) # Chuyển node sang một node cha khác


func _process(delta: float) -> void:
	_timer -= delta
	if _timer <= 0:
		_switch_state()

	var side: String = "R" if _dir > 0 else "L"
	if not _moving:
		play_animation("idle_" + side)
		return

	# Đang kẹt sẵn trong vật cản (vd. lúc spawn) 
	# thì cho di chuyển tự do để thoát ra
	var stuck: bool = _is_blocked(global_position)

	# Di chuyển ngang
	var step_x: float = _dir * speed * delta
	# Nửa thân
	var probe: float = frame_size.x * 0.4 * _dir
	var blocked: bool = (
		not stuck
		and _is_blocked(global_position + Vector2(step_x + probe, 0))
	)
	if not blocked:
		position.x += step_x
		_replans = 0
	elif is_equal_approx(_lane_y, _base_y):
		# Đã ở đúng làn mục tiêu mà vẫn bị chặn -> lập kế hoạch lại
		_replans += 1
		if _replans > 3:
			# Thử nhiều lần không được -> nghỉ một lúc
			_replans = 0
			_moving = false
			_timer = randf_range(idle_time.x, idle_time.y)
			return
		_plan_move()
	# (đang trên đường sang làn mới thì đứng chờ trôi làn)

	# Trôi dần sang làn mục tiêu + bob (luôn chạy, kể cả khi bị chặn)
	_lane_y = move_toward(_lane_y, _base_y, lane_speed * delta)
	_bob_time += delta
	position.y = _lane_y + sin(_bob_time * bob_speed) * bob_amount

	# Chạm thành bể thì quay lại
	if position.x < area.position.x or position.x > area.end.x:
		_dir = -_dir
		position.x = clampf(position.x, area.position.x, area.end.x)

	side = "R" if _dir > 0 else "L"
	play_animation(move_prefix + side)


# Chọn cùng lúc hướng + độ sâu tốt nhất
func _plan_move() -> void:
	var best: float = INF
	for i in lane_samples:
		var y: float = _lane_y if i == 0 else randf_range(
			floor_y + bob_amount, floor_end - bob_amount
		)
		if not _lane_reachable(y):
			continue
		for side in [-1, 1]:
			# ưu tiên nhẹ làn hiện tại để không đổi làn vô cớ
			var score: float = _side_score(side, y) + absf(y - _lane_y) * 0.03
			if score < best:
				best = score
				_dir = side
				_base_y = y


# Từ chỗ đang đứng có đi thẳng lên/xuống tới làn y được hay không
func _lane_reachable(y: float) -> bool:
	var steps: int = maxi(1, int(absf(y - _lane_y) / 2.0))
	for k in range(1, steps + 1):
		var point_y: float = lerpf(_lane_y, y, float(k) / steps)
		if _is_blocked(Vector2(global_position.x, point_y)):
			return false
	return true


# Luận phiên giữa bò và đứng yên
func _switch_state() -> void:
	_moving = not _moving
	if _moving:
		_plan_move()
	var time_range: Vector2 = move_time if _moving else idle_time
	_timer = randf_range(time_range.x, time_range.y)



# Điểm khó đi của một bên: càng lớn càng không nên đi
func _side_score(side: int, y: float) -> float:
	var point: Vector2 = Vector2(global_position.x + side * look_ahead, y)
	point.x = clampf(point.x, area.position.x, area.end.x)
	var score: float = _evaluate_crowding(point) + randf() * RANDOMNESS
	var reach: float = look_ahead - frame_size.x * 0.4
	score += 2.0 * (1.0 - _free_distance(side, y) / reach)
	return score


# Khoảng trống phía trước theo hướng side, tối đa look_ahead
func _free_distance(side: int, y: float) -> float:
	var start: float = frame_size.x * 0.4
	var distance: float = start
	while distance <= look_ahead:
		var point: Vector2 = Vector2(
			global_position.x + side * distance, 
			y
		)
		if _is_blocked(point):
			return distance - start
		distance += 4.0
	return look_ahead - start


func _evaluate_crowding(point: Vector2) -> float:
	var total: float = 0.0
	for other in get_tree().get_nodes_in_group("creatures"):
		if (
			other == self
			or not (other is Crawler)
			or not (other.is_node_ready())
		):
			continue
		
		var other_size: Vector2 = other.body_size
		if other_size == Vector2.ZERO:
			other_size = other.frame_size
		var size_ratio: Vector2 = other_size / REF_SIZE
		var radius: Vector2 = crowd_radius * (
			Vector2.ONE + SIZE_WEIGHT * (size_ratio - Vector2.ONE)
		)
		
		# Vị trí hiện tại
		var dist_now: Vector2 = (other.global_position - point) / radius
		total += maxf(0.0, 1.0 - dist_now.length())
	
		# Đang bò tới
		if other._moving:
			var ahead: Vector2 = (
				other.global_position + Vector2(other._dir * look_ahead, 0)
			)
			var dist_next: Vector2 = (ahead - point) / radius
			total += NEXT_POSITION_WEIGHT * maxf(0.0, 1.0 - dist_next.length())
	return total


# Điểm p (tọa độ toàn cục) có nằm trong footprint vật cản nào không
func _is_blocked(p: Vector2) -> bool:
	var query: PhysicsPointQueryParameters2D = PhysicsPointQueryParameters2D.new()
	query.position = p
	query.collision_mask = obstacle_mask
	return (
		not get_world_2d()
			.direct_space_state
			.intersect_point(query, 1)
			.is_empty()
	)
