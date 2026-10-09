@icon("res://editor/icons/environment_prop.svg")
class_name WaterSurface
extends ColorRect
## Mặt nước gợn sóng và nhấp nhô. Phía trên vạch là không khí (cảnh vật được làm sáng/nhạt),
## phía dưới vạch trong suốt.
## Mặt nước lặng nằm cách đáy ColorRect một khoảng SURFACE_FROM_BOTTOM.
## height_at() dùng chung cho cây nổi để nhấp nhô theo đúng mặt nước.

const SHADER := preload("res://shaders/water/water_surface.gdshader")
## Khoảng cách từ mặt nước lặng tới đáy ColorRect (px)
const SURFACE_FROM_BOTTOM: float = 8.0

## Nhấp nhô: sóng dài, chậm
const SWELL_AMP: float = 1.0
const SWELL_LEN: float = 320.0
const SWELL_SPEED: float = 1.2
## Gợn: sóng ngắn, chạy ngược chiều
const RIPPLE_AMP: float = 0.8
const RIPPLE_LEN: float = 52.0
const RIPPLE_SPEED: float = 2.6

## Màu vạch mặt nước (mỗi biome chỉnh trong Inspector cho hợp nền)
@export var line_color: Color = Color8(240, 196, 128)
## Màu dải nhạt ngay dưới vạch
@export var band_color: Color = Color8(222, 170, 104, 160)
## Màu điểm lấp lánh
@export var spark_color: Color = Color8(255, 232, 176)
## Màu không khí phía trên mặt nước
@export var air_color: Color = Color8(250, 226, 180)
## Mức pha màu không khí (0 = cảnh vật giữ nguyên, 1 = chỉ còn màu không khí)
@export_range(0.0, 1.0) var air_mix: float = 0.55

var _mat: ShaderMaterial


## Đồng hồ chung (giống SwayingPlant, SyncedSwayAnim)
static func time_s() -> float:
	return Time.get_ticks_msec() / 1000.0


## Độ lệch mặt nước tại toạ độ x (px, dương = xuống dưới)
static func height_at(x: float) -> float:
	var t: float = time_s()
	return SWELL_AMP * sin(x * TAU / SWELL_LEN - t * SWELL_SPEED) \
		+ RIPPLE_AMP * sin(x * TAU / RIPPLE_LEN + t * RIPPLE_SPEED)


func _ready() -> void:
	mouse_filter = Control.MOUSE_FILTER_IGNORE
	color = Color(0, 0, 0, 0)
	# Tạo material bằng code, không cần file .tres
	_mat = ShaderMaterial.new()
	_mat.shader = SHADER
	_mat.set_shader_parameter("surface_y", global_position.y + size.y - SURFACE_FROM_BOTTOM)
	_mat.set_shader_parameter("swell_amp", SWELL_AMP)
	_mat.set_shader_parameter("swell_len", SWELL_LEN)
	_mat.set_shader_parameter("swell_speed", SWELL_SPEED)
	_mat.set_shader_parameter("ripple_amp", RIPPLE_AMP)
	_mat.set_shader_parameter("ripple_len", RIPPLE_LEN)
	_mat.set_shader_parameter("ripple_speed", RIPPLE_SPEED)
	_mat.set_shader_parameter("line_color", line_color)
	_mat.set_shader_parameter("band_color", band_color)
	_mat.set_shader_parameter("spark_color", spark_color)
	_mat.set_shader_parameter("air_color", air_color)
	_mat.set_shader_parameter("air_mix", air_mix)
	material = _mat


func _process(_delta: float) -> void:
	_mat.set_shader_parameter("time_s", time_s())
