class_name HUD
extends Control


signal aquarium_pressed
signal settings_pressed

@export var idle_delay := 3.0 # Sau bao nhiêu giây không đụng sẽ mờ
@export var idle_alpha := 0.26 # Độ mờ khi nghỉ
@export var fade_out_time := 0.6 # Tốc độ mờ
@export var fade_in_time := 0.15 # Tốc độ hiện lại

@onready var aquarium_button: TextureButton = %AquariumButton
@onready var settings_button: TextureButton = %SettingsButton
@onready var buttons: Control = %Buttons

var _idle_timer := Timer.new()
var _tween: Tween
var _is_idle := false


func _ready() -> void:
	aquarium_button.pressed.connect(aquarium_pressed.emit)
	settings_button.pressed.connect(settings_pressed.emit)
	
	# Khởi tạo đồng hồ đếm ngược
	_idle_timer.one_shot = true
	_idle_timer.wait_time = idle_delay
	_idle_timer.timeout.connect(_on_idle_timeout)
	add_child(_idle_timer)
	_idle_timer.start()


# Dùng _input để bắt được sự kiện ngay cả khi chuột đang đè lên nút hoặc menu
func _input(event: InputEvent) -> void:
	if event is InputEventMouseMotion:
		_wake()
	elif event is InputEventMouseButton:
		_wake()
	elif event is InputEventKey and event.pressed:
		if not event.is_echo():
			_wake()
	elif event is InputEventJoypadButton and event.pressed:
		_wake()
	elif event is InputEventJoypadMotion:
		if absf(event.axis_value) > 0.2:
			_wake()


# Có thao tác: đếm lại từ đầu, hiện rõ nếu đang mờ
func _wake() -> void:
	_idle_timer.start()
	if _is_idle:
		_is_idle = false
		_fade_to(1.0, fade_in_time)
		Input.mouse_mode = Input.MOUSE_MODE_VISIBLE


# Hết giờ: mờ đi, trừ khi chuột đang đứng yên trên nút
func _on_idle_timeout() -> void:
	if buttons.get_global_rect().has_point(get_global_mouse_position()):
		_idle_timer.start() # làm mới timer liên tục
		return
	_is_idle = true
	_fade_to(idle_alpha, fade_out_time)
	Input.mouse_mode = Input.MOUSE_MODE_HIDDEN

		
func _fade_to(alpha: float, duration: float) -> void:
	if _tween:
		_tween.kill() # Hủy _tween cũ để không giật khi đổi hướng giữ chừng
		
	_tween = create_tween()
	(
		_tween.tween_property(self, "modulate:a", alpha, duration)
		.set_trans(Tween.TRANS_SINE)
	)
