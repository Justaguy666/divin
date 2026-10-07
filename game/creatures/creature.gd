@icon("res://editor/icons/fish.svg")
class_name Creature
extends Node2D


## Sheet ảnh: Mỗi hàng là một animation, mỗi cột là một frame
@export var sheet: Texture2D
@export var frame_size: Vector2i = Vector2i(32, 28)
## Tỉ lệ vùng Body so với phần thân thật (phần có pixel)
@export var body_fill: Vector2 = Vector2(0.8, 0.6)
## Tên animation theo thứ tự hàng trong sheet
@export var animation_names: PackedStringArray = []
@export var frames_per_animation: int = 4
@export var animation_fps: float = 8.0
## Tốc độ di chuyển (px/s)
@export var speed: float = 20.0
## Vùng được phép hoạt động trong bể
@export var area: Rect2 = Rect2(0, 0, 576, 356)

@onready var sprite: AnimatedSprite2D = $Sprite

## Kích thước thân thật (phần có pixel của frame đầu tiên), đo trong _build_body()
var body_size: Vector2 = Vector2.ZERO


func _ready() -> void:
	sprite.sprite_frames = _build_frames()
	add_to_group("creatures")
	_build_body()


# Đo thân thật và tạo vùng thân (Area2D, layer 4)
func _build_body() -> void:
	# Đo phần không trong suốt của frame đầu tiên trong sheet
	var frame_image: Image = (
		sheet.get_image()
			 .get_region(Rect2i(Vector2i.ZERO, frame_size))
	)
	var used: Rect2i = frame_image.get_used_rect()
	body_size = Vector2(used.size)
	
	var rect: RectangleShape2D = RectangleShape2D.new()
	rect.size = body_size * body_fill
	
	var shape: CollisionShape2D = CollisionShape2D.new()
	shape.shape = rect
	var used_center: Vector2 = Vector2(used.position) + body_size / 2.0
	shape.position = sprite.offset + used_center - Vector2(frame_size) / 2.0
	
	var body: Area2D = Area2D.new()
	body.name = "Body"
	body.collision_layer = 8 # (2^(4-1))
	body.collision_mask = 0
	body.monitoring = false # không cần đi tìm
	body.add_child(shape)
	add_child(body)


# Cắt sheet thành các frame và gom thành SpriteFrames
func _build_frames() -> SpriteFrames:
	var sf: SpriteFrames = SpriteFrames.new()
	sf.remove_animation("default")
	for row in animation_names.size():
		var animation: String = animation_names[row]
		sf.add_animation(animation)
		sf.set_animation_speed(animation, animation_fps)
		for col in frames_per_animation:
			var texture: AtlasTexture = AtlasTexture.new()
			texture.atlas = sheet
			texture.region = Rect2(
				col * frame_size.x, row * frame_size.y,
				frame_size.x, frame_size.y
			)
			sf.add_frame(animation, texture)
	return sf


# Thực hiện animation
func play_animation(animation: String) -> void:
	if sprite.animation == animation and sprite.is_playing():
		return
		
	var f: int = sprite.frame
	sprite.play(animation)
	sprite.frame = f
