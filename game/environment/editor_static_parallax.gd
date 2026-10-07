@tool
extends Parallax2D
## Giữ lớp nền đứng yên trong editor (không trượt theo khung nhìn của editor),
## để vị trí hiển thị khớp với game khi camera ở góc (0, 0).
## Khi chạy game vẫn parallax theo camera như bình thường.


func _ready() -> void:
	ignore_camera_scroll = Engine.is_editor_hint()
	if Engine.is_editor_hint():
		screen_offset = Vector2.ZERO
