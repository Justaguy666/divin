class_name AquariumSelector
extends Control


signal aquarium_chosen(info: AquariumInfo)

const CARD_SCENE := preload("res://scenes/ui/aquarium/aquarium_card.tscn")

@onready var grid: GridContainer = %Grid
@onready var info_label: Label = %InfoLabel
@onready var go_button: Button = %GoButton
@onready var tabs: Array[Button] = [%TabFresh, %TabMarine, %TabSpecial]

var _selected: AquariumInfo
var _tab_group: ButtonGroup = ButtonGroup.new()


func _ready() -> void:
	hide()
	add_to_group("modal_menu")
	for i in tabs.size():
		tabs[i].toggle_mode = true
		tabs[i].button_group = _tab_group
		tabs[i].pressed.connect(_show_category.bind(i))
	%CloseButton.pressed.connect(close)
	go_button.pressed.connect(_confirm)
	%Dim.gui_input.connect(_on_dim_input)


# Xử lý sự kiện
func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("toggle_aquarium_menu"):
		close() if visible else open()
		get_viewport().set_input_as_handled()
	elif visible and event.is_action_pressed("ui_cancel"):
		close()
		get_viewport().set_input_as_handled()


# Mở selector
func open() -> void:
	# Nếu đã mở hoặc đang chuyển cảnh hoặc không có bể nào đang được chọn
	if (
		visible 
		or AquariumManager.is_switching 
		or AquariumManager.current == null
		or _other_menu_open()
	):
		return
		
	var category := AquariumManager.current.category
	tabs[category].button_pressed = true
	_show_category(category)
	AquariumManager.selector_open = true
	modulate.a = 0.0
	show()
	create_tween().tween_property(self, "modulate:a", 1.0, 0.15)


# Đóng selector
func close() -> void:
	# không hiện thì không cần đóng
	if not visible:
		return
		
	AquariumManager.selector_open = false
	var tw := create_tween()
	tw.tween_property(self, "modulate:a", 0.0, 0.12)
	tw.tween_callback(hide)


# Hiện môi trường theo loại
func _show_category(category: int) -> void:
	# Xóa grid cũ
	for child in grid.get_children():
		grid.remove_child(child)
		child.queue_free()
	
	# Làm mới trạng thái
	_selected = null
	var card_group: ButtonGroup = ButtonGroup.new()
	var focus_card: AquariumCard = null
	
	# Nạp grid mới
	for info in AquariumManager.aquariums:
		if info.category != category:
			continue
		
		# Tạo aquarium card
		var card: AquariumCard = CARD_SCENE.instantiate()
		grid.add_child(card)
		var is_current: bool = info == AquariumManager.current
		card.setup(info, is_current)
		card.button_group = card_group
		card.pressed.connect(_select.bind(info))		
		if is_current or (focus_card == null and info.available):
			if is_current:
				card.button_pressed = true
			focus_card = card	

	# Cập nhật footer
	_update_footer(
		AquariumManager.current 
		if AquariumManager.current.category == category
		else null
	)
	# Cho mũi tên / tay cầm
	if focus_card:
		focus_card.grab_focus.call_deferred()
	

# Xử lý chọn môi trường
func _select(info: AquariumInfo) -> void:
	if info == _selected:
		_confirm()
		return
	_update_footer(info)
	

# Chuyển môi trường
func _confirm() -> void:
	if _selected and _selected.available:
		aquarium_chosen.emit(_selected)
		

# Cập nhật mô tả môi trường
func _update_footer(info: AquariumInfo) -> void:
	_selected = info
	if info == null:
		info_label.text = ""
		go_button.disabled = true
		return
	
	info_label.text = (
		"%s - %s" 
		% [tr(info.display_name), tr(info.description)]
	)
	var is_here: bool = AquariumManager.current == info
	go_button.disabled = is_here
	go_button.text = "You're here" if is_here else "Go ›"


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
