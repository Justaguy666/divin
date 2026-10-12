extends Node


signal aquarium_changed(info: AquariumInfo)

const SECTION := "aquarium"
const LAST_KEY := "last"

@export var aquariums: Array[AquariumInfo] = []

var current: AquariumInfo
var is_switching: bool = false
var selector_open: bool = false


func load_last() -> AquariumInfo:
	var last_id := str(Config.get_value(SECTION, LAST_KEY, ""))
		
	for aquarium in aquariums:
		if aquarium.id == last_id and aquarium.available:
			return aquarium
			
	for aquarium in aquariums:
		if aquarium.available: # mặc định: bể cá đầu tiên có asset
			return aquarium
			
	return null
	

func set_current(info: AquariumInfo) -> void:
	current = info
	Config.set_value(SECTION, LAST_KEY, info.id)
	aquarium_changed.emit(info)
