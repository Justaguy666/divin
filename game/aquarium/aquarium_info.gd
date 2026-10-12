class_name AquariumInfo
extends Resource


enum Category {
	FRESHWATER,
	MARINE,
	SPECIAL
}


@export var id: String = "" # "pf", "bw"
@export var display_name: String = "" # Có thể là key dịch
@export var category: Category = Category.FRESHWATER
@export_file("*.tscn") var scene_path: String = "" # Lưu đường dẫn, không preload
@export var thumbnail: Texture2D
@export var available: bool = true # false = sắp có
@export_multiline var description: String = ""
