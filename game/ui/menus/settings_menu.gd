class_name SettingsMenu
extends Control


signal closed

const FLAGS := {
	"en": preload("res://assets/ui/flags/ui_flag_en.png"),
	"vi": preload("res://assets/ui/flags/ui_flag_vi.png"),
}

@onready var language_option: OptionButton = %LanguageOption
@onready var tabs: Array[Button] = [%TabGeneral, %TabAudio]
@onready var pages: Array[VBoxContainer] = [%GeneralPage, %AudioPage]

var _tab_group := ButtonGroup.new()
var _current_page := 0

func _ready() -> void:
	hide()
	add_to_group("modal_menu")
	for i in tabs.size():
		tabs[i].toggle_mode = true
		tabs[i].button_group = _tab_group
		tabs[i].pressed.connect(_show_page.bind(i))
	language_option.auto_translate_mode = Node.AUTO_TRANSLATE_MODE_DISABLED
	for language in Localization.SUPPORTED_LANGUAGES:
		language_option.add_icon_item(
			FLAGS[language], 
			Localization.LANGUAGE_NAMES[language]
		)
		language_option.set_item_metadata(
			language_option.item_count - 1,
			language
		)
	language_option.item_selected.connect(_on_language_selected)
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
	show()
	create_tween().tween_property(self, "modulate:a", 1.0, 0.15)
	tabs[_current_page].grab_focus.call_deferred()


# Đóng settings
func close() -> void:
	# không hiện thì không cần đóng
	if not visible:
		return
		
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
	var current_language := Localization.get_language()
	for i in language_option.item_count:
		if language_option.get_item_metadata(i) == current_language:
			language_option.select(i)
			return


# Xử lý sự kiện chọn ngôn ngữ
func _on_language_selected(index: int) -> void:
	Localization.set_language(language_option.get_item_metadata(index))


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
