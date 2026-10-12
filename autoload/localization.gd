extends Node


signal language_changed(locale: String)

const SUPPORTED_LANGUAGES := ["en", "vi"]
const DEFAULT_LANGUAGE := "en"
const LANGUAGE_NAMES := {
	"en": "English",
	"vi": "Tiếng Việt"
}

const SECTION := "localization"
const LANGUAGE_KEY := "language"


func _ready() -> void:
	var language: String = _inittial_language()
	TranslationServer.set_locale(language)
	
	
# Ngôn ngữ đã lưu → ngôn ngữ hệ thống → mặc định
func _inittial_language() -> String:
	if Config.has_value(SECTION, LANGUAGE_KEY):
		var saved := str(Config.get_value(SECTION, LANGUAGE_KEY))
		if saved in SUPPORTED_LANGUAGES:
			return saved
		push_warning("Saved language is unsupported: %s" % saved)

	var system: String = OS.get_locale_language()
	if system in SUPPORTED_LANGUAGES:
		return system
	return DEFAULT_LANGUAGE

	
# Lấy ngôn ngữ hiện tại đang áp dụng
func get_language() -> String:
	return TranslationServer.get_locale().substr(0, 2)
	
	
# Thiết lập ngôn ngữ được áp dụng
func set_language(language: String) -> void:
	if language not in SUPPORTED_LANGUAGES:
		push_warning("Unsupported language: %s" % language)
		return
	
	if get_language() == language:
		return
		
	TranslationServer.set_locale(language)
	Config.set_value(SECTION, LANGUAGE_KEY, language)
	language_changed.emit(language)

	
