class_name SettingsMenu
extends Control


signal closed

## Flag dùng trong chuyển đổi ngôn ngữ
const FLAGS: Dictionary[String, Texture2D] = {
	"en": preload("res://assets/ui/flags/ui_flag_en.png"),
	"vi": preload("res://assets/ui/flags/ui_flag_vi.png"),
}
## Label cho bus
const VOLUME_LABELS: Dictionary[StringName, String] = {
	&"Master": "Master Volume",
	&"Music": "Music",
	&"Ambient": "Ambience",
	&"SFX": "Sound Effects",
	&"UI": "Interface",
}
## Icon loa theo mức âm lượng: mute, 1 vạch, 2 vạch, 3 vạch
const VOLUME_ICONS: Array[Texture2D] = [
	preload("res://assets/ui/ui_icon_volume_mute.png"),
	preload("res://assets/ui/ui_icon_volume_1.png"),
	preload("res://assets/ui/ui_icon_volume_2.png"),
	preload("res://assets/ui/ui_icon_volume_3.png"),	
]

@onready var general_page: VBoxContainer = %GeneralPage
@onready var audio_page: VBoxContainer = %AudioPage
@onready var tabs: Array[Button] = [%TabGeneral, %TabAudio]
@onready var pages: Array[VBoxContainer] = [general_page, audio_page]

var _language_option: OptionButton
var _tab_group := ButtonGroup.new()
var _current_page := 0


func _ready() -> void:
	hide()
	add_to_group("modal_menu")
	_build_general_page()
	_build_audio_page()
	for i in tabs.size():
		tabs[i].toggle_mode = true
		tabs[i].button_group = _tab_group
		tabs[i].pressed.connect(_show_page.bind(i))
	%CloseButton.pressed.connect(close)
	%Dim.gui_input.connect(_on_dim_input)


# Xử lý sự kiện
func _unhandled_input(event: InputEvent) -> void:
	if not event.is_action_pressed("ui_cancel"):
		return
	if visible:
		close()
	elif not AquariumManager.is_switching or not _other_menu_open():
		open()
	else:
		return
	get_viewport().set_input_as_handled()


# Mở settings
func open() -> void:
	# Nếu đã mở hoặc đang chuyển cảnh hoặc không có bể nào đang được chọn
	if (
		visible
		or AquariumManager.is_switching
		or _other_menu_open()
	):
		return
		
	_select_current_language()
	_show_page(_current_page)
	modulate.a = 0.0
	AudioManager.UI.play(&"button_press")
	show()
	create_tween().tween_property(self, "modulate:a", 1.0, 0.15)
	tabs[_current_page].grab_focus.call_deferred()


# Đóng settings
func close() -> void:
	# không hiện thì không cần đóng
	if not visible:
		return
	AudioManager.UI.play(&"action_cancel")
	AudioManager.save_volumes()
		
	var tw := create_tween()
	tw.tween_property(self, "modulate:a", 0.0, 0.12)
	tw.tween_callback(hide)
	closed.emit()


# Hiện trang settings hiện tại
func _show_page(index: int) -> void:
	_current_page = index
	tabs[index].button_pressed = true
	for i in tabs.size():
		pages[i].visible = i == _current_page
	

# Tự động select theo ngôn ngữ hiện tại
func _select_current_language() -> void:
	var current_language := LocalizationManager.get_language()
	for i in _language_option.item_count:
		if _language_option.get_item_metadata(i) == current_language:
			_language_option.select(i)
			return


# Xử lý sự kiện chọn ngôn ngữ
func _on_language_selected(index: int) -> void:
	LocalizationManager.set_language(_language_option.get_item_metadata(index))


# Click ra ngoài tự động close
func _on_dim_input(event: InputEvent) -> void:
	if (
		event is InputEventMouseButton 
		and event.pressed
		and event.button_index == MOUSE_BUTTON_LEFT
	):
		close()


# Kiểm tra xem có menu nào đang mở không
func _other_menu_open() -> bool:
	for menu in get_tree().get_nodes_in_group("modal_menu"):
		if menu != self and menu.visible:
			return true
	return false

#region Build page

# Trang general
func _build_general_page() -> void:
	_language_option = OptionButton.new()
	_language_option.auto_translate_mode = Node.AUTO_TRANSLATE_MODE_DISABLED
	for language in LocalizationManager.SUPPORTED_LANGUAGES:
		_language_option.add_icon_item(
			FLAGS[language], 
			LocalizationManager.LANGUAGE_NAMES[language]
		)
		_language_option.set_item_metadata(
			_language_option.item_count - 1,
			language
		)
	_language_option.item_selected.connect(_on_language_selected)
	_add_row(general_page, "Language", _language_option)


# Trang audio
func _build_audio_page() -> void:
	for bus in VOLUME_LABELS:
		var value = AudioManager.get_volume(bus)	
	
		var icon = TextureRect.new()
		icon.texture = _volume_icon(value)
		icon.stretch_mode = TextureRect.STRETCH_KEEP_CENTERED
		
		var slider := HSlider.new()
		slider.custom_minimum_size.x = 120
		slider.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
		slider.min_value = 0.0
		slider.max_value = 1.0
		slider.step = 0.01
		slider.value = value
		
		var percent := Label.new()
		percent.auto_translate_mode = Node.AUTO_TRANSLATE_MODE_DISABLED
		percent.custom_minimum_size.x = 32
		percent.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
		percent.text = "%d%%" % roundi(value * 100)
		
		slider.value_changed.connect(func(v: float) -> void:
			AudioManager.set_volume(bus, v)
			icon.texture = _volume_icon(v)
			percent.text = "%d%%" % roundi(v * 100)
		)
		
		slider.drag_ended.connect(func(_change: bool) -> void:
			AudioManager.UI.play(&"button_press")
		)
		
		var box := HBoxContainer.new()
		box.add_theme_constant_override(&"separation", 6)
		box.add_child(icon)
		box.add_child(slider)
		box.add_child(percent)
		_add_row(audio_page, VOLUME_LABELS[bus], box)


# 0 -> mute, (0, 1/3] -> 1 vạch, (1/3, 2/3] -> 2 vạch, (2/3, 1] -> 3 vạch
func _volume_icon(value: float) -> Texture2D:
	if value <= 0:
		return VOLUME_ICONS[0]
	return VOLUME_ICONS[clampi(ceili(value * 3.0), 1, 3)]
	

func _add_row(page: VBoxContainer, label_text: String, control: Control) -> void:
	var row := HBoxContainer.new()
	row.custom_minimum_size.y = 24
	
	var label = Label.new()
	label.text = label_text
	label.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	label.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	control.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	
	row.add_child(label)
	row.add_child(control)
	page.add_child(row)
	
	var divider := HSeparator.new()
	divider.theme_type_variation = &"RowSeparator"
	page.add_child(divider)

#endregion
