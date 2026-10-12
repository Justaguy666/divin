extends Node

const PATH := "user://settings.cfg"

var _config := ConfigFile.new()


# Chạy ngay khi được tạo instance, trước khi đưa vào scene tree
func _init() -> void:
	var err := _config.load(PATH)
	if err != OK and err != ERR_FILE_NOT_FOUND:
		push_warning("Failed to load settings: %s" % error_string(err))
		
		
# Kiểm tra xem section, key có tồn tại không
func has_value(section: String, key: String) -> bool:
	return _config.has_section_key(section, key)
	
	
# Lấy giá trị
func get_value(section: String, key: String, default: Variant = null) -> Variant:
	return _config.get_value(section, key, default)


# Thiết lập giá trị
func set_value(section: String, key: String, value: Variant) -> bool:
	_config.set_value(section, key, value)
	var err := _config.save(PATH)
	if err != OK:
		push_warning("Failed to save settings: %s" % error_string(err))
		return false
	return true
