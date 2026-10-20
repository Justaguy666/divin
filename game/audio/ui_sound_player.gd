class_name UISoundPlayer
extends Node
## Âm giao diện: press, hover, ...

## Meta data đặt trên từng nút để để đổi âm mặc định
## giá trị là tên (vd: &"action_confirm"), hoặc &"" để tắt âm
const META_PRESS := &"ui_press_sound"
const META_HOVER := &"ui_hover_sound"
const META_HOOKED := &"_ui_sfx_hooked"
## Hai tiếng hover cách nhau tối thiêu (giây), tránh rê chuột qua lưới thẻ bể bị lộp độp
const HOVER_GAP := 0.05
const POOL_SIZE := 4

## Gán trong inspector. vd: &"press" -> ui_button_press.wav
@export var sounds: Dictionary[StringName, AudioStream] = {}

# vài player xoay vòng để click nhanh không cắt âm trước
var _pool: Array[AudioStreamPlayer] = []
var _next := 0
var _last_hover_ms := 0.0
var _watched_popup: PopupMenu # PopupMenu đang mở cần theo dõi
var _last_popup_item := -1


func _ready() -> void:
	for i in POOL_SIZE:
		var player := AudioStreamPlayer.new()
		player.bus = &"UI"
		add_child(player)
		_pool.append(player)
	# Node sau này
	get_tree().node_added.connect(_on_node_added)
	# Tất cả các node trước đó
	for node in get_tree().root.find_children("*", "BaseButton", true, false):
		_on_node_added(node)
	set_process(false) # chỉ cần chạy _process khi có PopupMenu đang mở


## Chỉ chạy khi popup đang mở
func _process(_delta: float) -> void:
	var item := _watched_popup.get_focused_item()
	if item == _last_popup_item:
		return
	_last_popup_item = item
	if item >= 0 and not _watched_popup.is_item_disabled(item):
		_play_hover()


## Phát âm theo tên. Tên chưa gán -> im lặng
func play(sound: StringName) -> void:
	var stream: AudioStream = sounds.get(sound)
	if stream == null:
		return
		
	var player := _pool[_next]
	_next = (_next + 1) % POOL_SIZE
	player.stream = stream
	player.pitch_scale = randf_range(0.97, 1.03) # làm lệch quãng
	player.play()


func _on_node_added(node: Node) -> void:
	if not node is BaseButton or node.has_meta(META_HOOKED):
		return
	node.set_meta(META_HOOKED, true)
	node.pressed.connect(_on_button_pressed.bind(node))
	node.mouse_entered.connect(_on_button_hovered.bind(node))
	if node is OptionButton:
		_hook_popup(node.get_popup())
	

func _on_button_pressed(button: BaseButton) -> void:
	play(button.get_meta(META_PRESS, &"button_press"))


func _on_button_hovered(button: BaseButton) -> void:
	if button.disabled:
		return
	_play_hover(button.get_meta(META_HOVER, &"button_hover"))


## Hover sfx dùng chung cho các nút và item trong PopupMenu
func _play_hover(sound: StringName = &"button_hover") -> void:
	var now := Time.get_ticks_msec()
	if now - _last_hover_ms < HOVER_GAP * 1000:
		return
	_last_hover_ms = now
	play(sound)


func _hook_popup(popup: PopupMenu) -> void:
	popup.id_pressed.connect(func(_id: int) -> void: play(&"button_press"))
	popup.visibility_changed.connect(_on_popup_visibility_changed.bind(popup))
	

func _on_popup_visibility_changed(popup: PopupMenu) -> void:
	if popup.visible: # open
		_watched_popup = popup
		_last_popup_item = popup.get_focused_item()
		set_process(true)
	elif popup == _watched_popup: # close
		_watched_popup = null
		set_process(false)
