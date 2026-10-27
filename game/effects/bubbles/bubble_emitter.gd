@icon("res://editor/icons/bubble_emitter.svg")
class_name BubbleEmitter
extends Node2D


## Scene của bubble
@export var bubble_scene: PackedScene = preload("res://scenes/effects/bubbles/bubble.tscn")
## Tự động nhả bọt theo chu kỳ
@export var autostart: bool = true
## Thời gian ngẫu nhiên giữa các đợt nhả bọt (giây, min-max)
@export var emit_interval: Vector2 = Vector2(3.0, 8.0)
## Số lượng bọt mỗi đợt
@export var burst_count: Vector2i = Vector2i(1, 3)
## Độ trễ giữa các hạt bọt trong cùng 1 đợt
@export var burst_delay: Vector2 = Vector2(0.12, 0.25)
## Độ lệch vị trí ngẫu nhiên quanh tâm lỗ thoát khí (px)
@export var spawn_jitter: Vector2 = Vector2(2.0, 1.0)

var _timer := 0.0
var _effects_holder: Node2D


func _ready() -> void:
	_find_effects_holder()
	_reset_timer()


func _process(delta: float) -> void:
	if not autostart:
		return
		
	_timer -= delta
	if _timer <= 0.0:
		emit_burst()
		_reset_timer()


## Nhả một đợt bọt khí
func emit_burst(count: int = -1) -> void:
	if not bubble_scene or not _effects_holder:
		return
	
	var total := (
		count if count > 0 
		else randi_range(burst_count.x, burst_count.y)
	)
	for i in total:
		var bubble := bubble_scene.instantiate() as Node2D
		if not bubble:
			return
			
		# Đặt vị trí bọt
		var jitter = Vector2(
			randf_range(-spawn_jitter.x, spawn_jitter.x),
			randf_range(-spawn_jitter.y, spawn_jitter.y)
		)
		bubble.global_position = global_position + jitter
		
		# Thêm vào Effect holder của bể
		_effects_holder.add_child(bubble)
		
		# Nếu đợt bọt có nhiều hơn 1, nhả cách nhau 1 chút
		if total > 1 and i < total - 1:
			await get_tree().create_timer(
				randf_range(burst_delay.x, burst_delay.y),
			).timeout


## Làm mới cooldown của burst
func _reset_timer() -> void:
	_timer = randf_range(emit_interval.x,  emit_interval.y)


## Tìm node Effects của Aquarium hiện tại để chứa bọt
func _find_effects_holder() -> void:
	var aquarium := get_tree().get_first_node_in_group(&"aquarium")
	if aquarium:
		_effects_holder = aquarium.get_node_or_null("Effects")

	# Fallback: tìm toàn cây scene hoặc tự làm cha
	if  not _effects_holder:
		var found := get_tree().current_scene.find_child("Effects", true, false)
		_effects_holder = found if found is Node2D else self
