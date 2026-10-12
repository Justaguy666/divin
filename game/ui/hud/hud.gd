class_name HUD
extends Control


signal aquarium_pressed
signal settings_pressed

@onready var aquarium_button: TextureButton = %AquariumButton
@onready var settings_button: TextureButton = %SettingsButton


func _ready() -> void:
	aquarium_button.pressed.connect(aquarium_pressed.emit)
	settings_button.pressed.connect(settings_pressed.emit)
