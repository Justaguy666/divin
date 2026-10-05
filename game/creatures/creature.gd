@icon("res://editor/icons/fish.svg")
class_name Creature
extends Node2D

## Sheet ảnh: Mỗi hàng là một animation, mỗi cột là một frame
@export var sheet: Texture2D
@export var frame_size: Vector2i = Vector2i(32, 28)
## Tên animation theo thứ tự hàng trong sheet
@export var animation_names: PackedStringArray = []
@export var frames_per_animation: int = 4
@export var animation_fps: float = 8.0
## Tốc độ di chuyển (px/s)
@export var speed: float = 20.0
## Vùng được phép hoạt động trong bể
@export var area: Rect2 = Rect2(0, 0, 384, 212)

@onready var sprite: AnimatedSprite2D = $Sprite


func _ready() -> void:
	sprite.sprite_frames = _build_frames()


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
