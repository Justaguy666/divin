@icon("res://editor/icons/environment_prop.svg")
class_name O2Pearling
extends Node2D


## Hiệu ứng thở Oxy / Pearling (Bọt khí li ti quang hợp trên cây thủy sinh và thực vật)
## Tải asset bọt khí riêng của từng biome theo định dạng: <biome_id>_o2_pearling_6f.png

# Static cache để các bọt thở trong cùng biome tái sử dụng sf
static var _cached_frames: Dictionary[String, SpriteFrames] = {}

const PF_TEXTURE_PATH := "res://assets/environments/freshwater/planted_freshwater/effects/bubbles/pf_o2_pearling_6f.png"
const SG_TEXTURE_PATH := "res://assets/environments/marine/seagrass_meadow/effects/bubbles/sg_oxygen_pearling_6x24_6f.png"
const HFRAMES := 6

## Texture tùy biến (nếu để trống sẽ tự động lấy asset tương ứng của biome hiện tại)
@export var custom_texture: Texture2D
## Kích thước 1 frame (px). Nếu là ZERO sẽ tự nhận diện
@export var frame_size: Vector2 = Vector2.ZERO
## Tốc độ khung hình
@export var fps: float = 8.0

## Sủi bọt liên tục (true) hay ngắt quãng theo từng đợt (false)
@export var continous_loop: bool = false
## Khoảng thời gian ngẫu nhiên giữa các đợt sủi (giây: min, max)
@export var burst_interval: Vector2 = Vector2(2.0, 5.0)
## Tạo độ trễ ngẫu nhiên trước đợt sủi đầu tiên
@export var random_start_delay: bool = true

@onready var sprite: AnimatedSprite2D = $Sprite

var _timer := 0.0
var _is_playing_burst := false


func _ready() -> void:
	_setup_sprite_frames()
	sprite.animation_finished.connect(_on_animation_finished)

	if continous_loop:
		_start_continous()
	else:
		sprite.visible = false
		_timer = (
			randf_range(0.2, burst_interval.y)
			if random_start_delay
			else burst_interval.x	
		)


func _process(delta: float) -> void:
	if continous_loop or _is_playing_burst:
		return
		
	_timer -= delta
	if _timer <= 0.0:
		_play_burst()


## Thiết lập sprite frames từ tài nguyên ảnh của biome
func _setup_sprite_frames() -> void:
	var current_biome_id := ""
	if AquariumManager.current:
		current_biome_id = AquariumManager.current.id
	
	# 1. Kiểm tra cache trước (chỉ cache cho texture mặc định theo biome)
	var is_custom := custom_texture != null
	if (
		not is_custom and current_biome_id != ""
		and _cached_frames.has(current_biome_id)
	):
		sprite.sprite_frames = _cached_frames[current_biome_id]
		return
	
	var tex := custom_texture
	var fsize := frame_size
	
	# 2. Tự động nhận diện biome và tải asset file tương ứng
	if not tex:
		if current_biome_id == "sg":
			tex = load(SG_TEXTURE_PATH)
			if fsize == Vector2.ZERO:
				fsize = Vector2(6, 24)
		else:
			tex = _load_biome_pearling_texture(current_biome_id)
			if fsize == Vector2.ZERO:
				fsize = Vector2(8, 8)
	elif fsize == Vector2.ZERO:
		fsize = Vector2(tex.get_width() / float(HFRAMES), tex.get_height())
		
	if not tex:
		return
		
	var sf := SpriteFrames.new()
	sf.remove_animation(&"default")
	sf.add_animation(&"pearling")
	sf.set_animation_speed(&"pearling", fps)
	sf.set_animation_loop(&"pearling", continous_loop)
	
	for i in HFRAMES:
		var atlas := AtlasTexture.new()
		atlas.atlas = tex
		atlas.region = Rect2(
			Vector2(fsize.x * i, 0),
			fsize
		)
		sf.add_frame(&"pearling", atlas)
		
	if not is_custom and current_biome_id != "":
		_cached_frames[current_biome_id] = sf
		
	sprite.sprite_frames = sf


## Tải file asset bọt thở riêng của biome, fallback về pf
func _load_biome_pearling_texture(biome_id: String) -> Texture2D:
	if AquariumManager.current and biome_id != "":
		var info := AquariumManager.current
		var cat_folder := "freshwater"
		match info.category:
			AquariumInfo.Category.MARINE: cat_folder = "marine"
			AquariumInfo.Category.SPECIAL: cat_folder = "special"

		var biome_name: String = info.display_name.to_lower().replace(" ", "_")
		var path := (
			"res://assets/environments/%s/%s/effects/bubbles/%s_o2_pearling_6f.png"
		) % [cat_folder, biome_name, biome_id]
		
		if ResourceLoader.exists(path):
			return load(path)
			
	return load(PF_TEXTURE_PATH)


## Kích hoạt chế độ nhả bọt liên tục
func _start_continous() -> void:
	sprite.visible = true
	sprite.play(&"pearling")


## Kích hoạt hiệu ứng nhả bọt
func _play_burst() -> void:
	_is_playing_burst = true
	sprite.visible = true
	sprite.frame = 0
	sprite.play(&"pearling")


## Xử lý khi chạy hết chuỗi 6 frame của mỗi đợt bọt
func _on_animation_finished() -> void:
	if not continous_loop:
		_is_playing_burst = false
		sprite.visible = false
		_timer = randf_range(burst_interval.x, burst_interval.y)
