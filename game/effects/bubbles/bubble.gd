@icon("res://editor/icons/environment_prop.svg")
class_name Bubble
extends Node2D


enum State { RISING, POPPING, FADING }

# Static cache để các bọt khí trong cùng 1 biome tải chung tài nguyên
static var _cached_frames: Dictionary[String, SpriteFrames] = {}
static var _cached_has_pop: Dictionary[String, bool] = {}

@export var rising_speed: float = 24.0 # tốc độ bay lên (px/s)
@export var wobble_amplitude: float = 2.0 # Biên độ lắc lư ngang (px)
@export var wobble_frequency: float = 4.0 # Tần số lắc lư

@onready var sprite: AnimatedSprite2D = $Sprite

var _state := State.RISING
var _time := 0.0
var _base_x := 0.0
var _has_pop_effect := true


func _ready() -> void:
	if AquariumManager.current:
		_auto_setup_from_current_biome()
	
	_base_x = position.x
	_time = randf() * TAU # Random pha lắc lư, TAU = 360 độ
	sprite.animation_finished.connect(_on_animation_finished)


func _process(delta: float) -> void:
	if _state != State.RISING:
		return
		
	_time += delta
	# Bay lên và lắc lư nhẹ nhàng
	position.y -= delta * rising_speed
	position.x = _base_x + sin(_time * wobble_frequency) * wobble_amplitude
	
	# Kiểm tra vị trí chạm mặt nước
	var water_line = 0.0
	if ClassDB.class_exists(&"WaterSurface"):
		water_line = WaterSurface.height_at(global_position.x)
		
	if global_position.y <= water_line:
		_pop()
	elif global_position.y < -32.0: # Fallback chống rò rỉ bộ nhớ
		queue_free()


func _auto_setup_from_current_biome() -> void:
	var info := AquariumManager.current
	var biome_id := info.id
	
	var cat_folder := "freshwater"
	match info.category:
		AquariumInfo.Category.MARINE: cat_folder = "marine"
		AquariumInfo.Category.SPECIAL: cat_folder = "special"

	var biome_name: String = info.display_name.to_lower().replace(" ", "_")
	var biome_path: String = (
		"res://assets/environments/%s/%s"
	) % [cat_folder, biome_name]
	
	setup_for_biome(biome_id, biome_path)

	
# Setup texture và animation theo biome
func setup_for_biome(biome_id: String, biome_path: String) ->  void:
	# 1. Kiểm tra cache trước để tránh phân tích lại texture nhiều lần
	if _cached_frames.has(biome_id):
		sprite.sprite_frames = _cached_frames[biome_id]
		_has_pop_effect = _cached_has_pop.get(biome_id, false)
		_pick_random_bubble_size()
		return
		
	var sizes_path := (
		"%s/effects/bubbles/%s_bubbles_sizes.png"
	) % [biome_path, biome_id]
	var pop_path := (
		"%s/effects/bubbles/%s_bubble_pop_4f.png"
	) % [biome_path, biome_id]
	
	var sf := SpriteFrames.new()
	sf.remove_animation(&"default")
	
	# 2. Xử lý các kích cỡ bọt (animation "float")
	if ResourceLoader.exists(sizes_path):
		var tex_sizes: Texture2D = load(sizes_path)
		var bubble_rects  := _extract_bubble_rect(tex_sizes.get_image())
		sf.add_animation(&"float")
		sf.set_animation_loop(&"float", false)
		for rect in bubble_rects:
			var atlas := AtlasTexture.new()
			atlas.atlas = tex_sizes
			atlas.region = Rect2(rect)
			sf.add_frame(&"float", atlas)
	
	# 3. Xử lý hiệu ứng nổ (animation "pop")
	if ResourceLoader.exists(pop_path):
		var tex_pop: Texture2D = load(pop_path)
		_has_pop_effect = true
		sf.add_animation(&"pop")
		sf.set_animation_speed(&"pop", 12.0)
		sf.set_animation_loop(&"pop", false)
		
		# pop sheet luôn là 40x10 gồm 4 frame (mỗi frame 10x10)
		const POP_FRAME_SIZE := Vector2(10, 10)
		for col in 4:
			var atlas = AtlasTexture.new()
			atlas.atlas = tex_pop
			atlas.region = Rect2(
				Vector2(col * POP_FRAME_SIZE.x, 0), 
				POP_FRAME_SIZE
			)
			sf.add_frame(&"pop", atlas)
	else:
		_has_pop_effect = false
		
	_cached_frames[biome_id] = sf
	_cached_has_pop[biome_id] = _has_pop_effect
	
	sprite.sprite_frames = sf
	_pick_random_bubble_size()
	

func _pick_random_bubble_size() -> void:
	if (
		not sprite.sprite_frames 
		or not sprite.sprite_frames.has_animation(&"float")
	):
		return
	var count: int = sprite.sprite_frames.get_frame_count(&"float")
	if count > 0:
		sprite.play(&"float")
		sprite.frame = randi() % count
		sprite.pause()
	

## Tự động quét và tách các bounding box của từng hạt bọt trong ảnh
func _extract_bubble_rect(img: Image, max_gap: int = 1) -> Array[Rect2i]:
	var rects: Array[Rect2i] = []
	var w := img.get_width()
	var h := img.get_height()
	var in_col := false
	var col_start := 0
	var empty_count := 0
	
	for x in w:
		var has_opaque := false
		for y in h:
			if img.get_pixel(x, y).a > 0.01:
				has_opaque = true
				break
		
		if has_opaque:
			if not in_col:
				in_col = true
				col_start = x
			empty_count = 0
		else:
			if in_col:
				empty_count += 1
				if empty_count > max_gap:
					in_col = false
					var col_end := x - empty_count
					rects.append(_get_sub_rect(img, col_start, col_end, h))
					empty_count = 0
	
	# Xử lý hạt bọt cuối cùng nếu chạm sát cạnh phải của ảnh
	if in_col:
		var col_end := w - 1 - empty_count
		rects.append(_get_sub_rect(img, col_start, col_end, h))	
	
	return rects


## Lấy phần texture đúng chứa sprite
func _get_sub_rect(img: Image, x1: int, x2: int, h: int) -> Rect2i:
	var y_min = h
	var y_max = 0
	for x in range(x1, x2 + 1):
		for y in h:
			if img.get_pixel(x, y).a > 0.01:
				y_min = mini(y_min, y)
				y_max = maxi(y_max, y)
	return Rect2i(x1, y_min, x2 - x1 + 1, y_max - y_min + 1)

	
func _pop() -> void:
	if _has_pop_effect and sprite.sprite_frames.has_animation(&"pop"):
		_state = State.POPPING
		sprite.play(&"pop")
	else:
		# biome không có pop: fade out rồi tự hủy
		_state = State.FADING
		var tw := create_tween()
		tw.tween_property(self, "modulate:a", 0.0, 0.2)
		tw.tween_callback(queue_free)
	
	
func _on_animation_finished() ->  void:
	if _state == State.POPPING:
		queue_free()
