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
	position.x = area.size.x / 2
	position.y = _base_y
	_switch_state()
	_join_floor_sort.call_deferred()


func _process(delta: float) -> void:
	_timer -= delta
	
	if _timer <= 0:
		_switch_state()
	
	var side: String = "R" if _dir > 0 else "L"
	
	if not _moving:
		play_animation("idle_" + side)
		return
	
	# Di chuyển ngang
	position.x += _dir * speed * delta
	
	# Dao động nhẹ theo Y
	_bob_time += delta
	var bob_y: float = (
		_base_y
		+ sin(_bob_time * bob_speed) * bob_amount
	)
	position.y = clampf(bob_y, floor_y, floor_end)
	
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


# Thêm creature vào floor Y sort
func _join_floor_sort() -> void:
	var floor_node: Node = get_tree().get_first_node_in_group("floor_sort")
	if floor_node and get_parent() != floor_node:
		reparent(floor_node) # Chuyển node sang một node cha khác
