@tool
extends Parallax2D
## Giữ lớp nền đứng yên trong editor (không trượt theo khung nhìn của editor),
## để vị trí hiển thị khớp với game khi camera ở giữa bể.
## Khi chạy game vẫn parallax theo camera như bình thường.
## Khi khung hình rộng/cao hơn khung gốc (aspect "expand", vd. điện thoại 20:9),
## bù scroll_offset để lớp nền vẫn căn giữa như ở khung gốc, không lệch về một bên.


func _ready() -> void:
	ignore_camera_scroll = Engine.is_editor_hint()
	if Engine.is_editor_hint():
		screen_offset = Vector2.ZERO
		return
	get_viewport().size_changed.connect(_recenter)
	_recenter()


func _recenter() -> void:
	var base := Vector2(
		ProjectSettings.get_setting("display/window/size/viewport_width"),
		ProjectSettings.get_setting("display/window/size/viewport_height")
	)
	var extra: Vector2 = get_viewport_rect().size - base
	# Vị trí lớp = scroll_offset + screen_offset * (1 - scroll_scale);
	# phần khung thêm làm screen_offset lệch -extra/2 khi camera đứng giữa -> bù lại
	scroll_offset = extra / 2.0 * (Vector2.ONE - scroll_scale)
