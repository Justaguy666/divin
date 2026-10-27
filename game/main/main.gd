extends Node2D


@onready var holder: Node2D = $AquariumHolder
@onready var fade: ColorRect = $FadeLayer/Fade
@onready var hud: HUD = $UI/HUD
@onready var aquarium_selector: AquariumSelector = $UI/AquariumSelector
@onready var settings_menu: SettingsMenu = $UI/SettingsMenu

var _current_node: Node


func _ready() -> void:
	aquarium_selector.aquarium_chosen.connect(_on_aquarium_chosen)
	hud.aquarium_pressed.connect(aquarium_selector.open)
	hud.settings_pressed.connect(settings_menu.open)
	fade.modulate.a = 1.0 	# Mở game từ màn tối
	switch_to(AquariumManager.load_last())


# Xử lý sự kiện chọn bể
func _on_aquarium_chosen(info: AquariumInfo) -> void:
	aquarium_selector.close()
	if info != AquariumManager.current:
		switch_to(info)


# Chuyển tới bể
func switch_to(info: AquariumInfo) -> void:
	if info == null or AquariumManager.is_switching:
		return
	AquariumManager.is_switching = true
	
	ResourceLoader.load_threaded_request(info.scene_path) # Load song song fade
	await _fade_to(1.0)
	
	while (
		ResourceLoader.load_threaded_get_status(info.scene_path) 
		== ResourceLoader.THREAD_LOAD_IN_PROGRESS
	):
		# tạm dừng while lại 1 frame để không chạy vô hạn quá nhanh
		await get_tree().process_frame
		
	var packed := ResourceLoader.load_threaded_get(info.scene_path) as PackedScene
	if packed == null:
		push_error("Loading fail: " + info.scene_path)
		await _fade_to(0.0)
		AquariumManager.is_switching = false
		return
		
	# Free bể cũ trước khi thêm bể mới
	if _current_node:
		holder.remove_child(_current_node)
		_current_node.queue_free()
	_current_node = packed.instantiate()
	_current_node.add_to_group(&"aquarium")
	holder.add_child(_current_node)
	AquariumManager.set_current(info)
	
	await _fade_to(0.0)
	AquariumManager.is_switching = false


# Hiệu ứng fade
func _fade_to(alpha: float) -> void:
	var tw := create_tween()
	tw.tween_property(fade, "modulate:a", alpha, 0.35).set_trans(Tween.TRANS_SINE)
	await tw.finished
