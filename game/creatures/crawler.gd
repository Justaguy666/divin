@icon("res://editor/icons/fish.svg")
class_name Crawler
extends Creature


## Tiền tố animation khi di chuyển (shrimp: walk_, snail: crawl_)
@export var move_prefix: String = "walk_"

## Vùng mặt sàn mà CHÂN của crawler được phép di chuyển
@export var floor_y: float = 196.0
@export var floor_height: float = 16.0

## Chuyển động bob theo trục Y
@export var bob_speed: float = 4.0 # Tần số dao động
@export var bob_amount: float = 2.0 # Biên độ dao động

## Thời gian duy trì trạng thái
@export var move_time: Vector2 = Vector2(1.0, 4.0)
@export var idle_time: Vector2 = Vector2(1.0, 3.0)

## Layer va chạm của footprint vật cản (Layer 2 = floor_obstacle)
@export_flags_2d_physics var obstacle_mask: int = 2

var _dir: int = 1
var _moving: bool = false
var _timer: float = 0.0

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
	super()
	_offset = -frame_size.y / 2.0
	sprite.offset.y = _offset
	_base_y = randf_range(
		floor_y + bob_amount, 
		floor_end - bob_amount
	)
	if position.x == 0:
		position.x = area.get_center().x
	position.y = _base_y
	_switch_state()
	_join_floor_sort.call_deferred()


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
	
	# Di chuyển ngang: phía trước có vật cản thì quay đầu
	var step_x: float = _dir * speed * delta
	if stuck or not _is_blocked(global_position + Vector2(step_x, 0)):
		position.x += step_x
	else:
		_dir = -_dir
	
	# Dao động Y: bị chặn thì giữ nguyên y
	_bob_time += delta
	var bob_y: float = clampf(
		_base_y + sin(_bob_time * bob_speed) * bob_amount,
		floor_y,
		floor_end
	)
	var step_y: float = bob_y - position.y
	if stuck or not _is_blocked(global_position + Vector2(0, step_y)):
		position.y += step_y
	
	# Chạm thành bể thì quay lại
	if position.x < area.position.x or position.x > area.end.x:
		_dir = -_dir
		position.x = clampf(position.x, area.position.x, area.end.x)
	
	side = "R" if _dir > 0 else "L"
	play_animation(move_prefix + side)


# Luận phiên giữa bò và đứng yên
func _switch_state() -> void:
	_moving = not _moving
	if _moving and randf() < 0.2: # Thỉnh thoảng đổi hướng
		_dir = -_dir
	var time_range: Vector2 = move_time if _moving else idle_time
	_timer = randf_range(time_range.x, time_range.y)


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
