class_name AquariumCard
extends Button


@onready var thumb: TextureRect = %Thumb
@onready var name_label: Label = %NameLabel
@onready var here_badge: Control = %HereBadge
@onready var soon_label: Label = %SoonLabel

var info: AquariumInfo


# Gọi sau add_child, vì trước đó các biến @onready vẫn là null
func setup(p_info: AquariumInfo, is_current: bool) -> void:
	info = p_info
	thumb.texture = info.thumbnail
	name_label.text = info.display_name
	here_badge.visible = is_current
	soon_label.visible = not info.available
	disabled = not info.available
	thumb.modulate = Color.WHITE if info.available else Color(0.25, 0.3, 0.4)
