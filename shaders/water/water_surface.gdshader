shader_type canvas_item;

// Mặt nước: vạch sáng gợn sóng + dải nhạt + điểm lấp lánh.
// Phía trên vạch: lấy lại đúng cảnh vật phía sau rồi làm sáng/nhạt như không khí
// -> khác hẳn phần dưới nước nhưng vẫn thấy rõ cảnh vật. Phía dưới vạch: trong suốt.
// Công thức độ cao phải giống WaterSurface.height_at() (water_surface.gd).

uniform float time_s = 0.0;       // đồng hồ chung, script gán mỗi frame
uniform float surface_y = 0.0;    // y thế giới của mặt nước khi lặng
uniform float swell_amp = 1.0;    // nhấp nhô: biên độ (px)
uniform float swell_len = 320.0;  // nhấp nhô: bước sóng (px)
uniform float swell_speed = 1.2;
uniform float ripple_amp = 0.8;   // gợn: biên độ (px)
uniform float ripple_len = 52.0;  // gợn: bước sóng (px)
uniform float ripple_speed = 2.6;

uniform vec4 line_color : source_color = vec4(0.941, 0.769, 0.502, 1.0);
uniform vec4 band_color : source_color = vec4(0.871, 0.667, 0.408, 0.63);
uniform vec4 spark_color : source_color = vec4(1.0, 0.910, 0.690, 1.0);
uniform vec4 air_color : source_color = vec4(0.980, 0.886, 0.706, 1.0); // màu không khí phía trên
uniform float air_mix : hint_range(0.0, 1.0) = 0.55;  // mức pha màu không khí (0 = giữ nguyên cảnh)

uniform sampler2D screen_tex : hint_screen_texture, filter_nearest;

varying vec2 world_pos;

void vertex() {
	world_pos = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}

float ripple_wave(float x) {
	return sin(x * TAU / ripple_len + time_s * ripple_speed);
}

float height_at(float x) {
	return swell_amp * sin(x * TAU / swell_len - time_s * swell_speed) + ripple_amp * ripple_wave(x);
}

void fragment() {
	vec2 p = floor(world_pos);         // toạ độ pixel thế giới
	float x = p.x + 0.5;
	float h = height_at(x);
	float s = surface_y + sign(h) * floor(abs(h) + 0.5);   // làm tròn đối xứng -> số pixel nguyên

	vec4 c = vec4(0.0);                // mặc định: trong suốt
	if (p.y < s) {
		// Không khí: giữ chi tiết cảnh vật, chỉ pha sang màu không khí
		vec3 scene = texture(screen_tex, SCREEN_UV).rgb;
		c = vec4(mix(scene, air_color.rgb, air_mix), 1.0);
	} else if (p.y == s) {
		c = ripple_wave(x) < -0.93 ? spark_color : line_color;   // lấp lánh ở đỉnh gợn
	} else if (p.y == s + 1.0 && mod(p.x + floor(time_s * 6.0), 7.0) < 3.0) {
		c = band_color;                // dải nhạt đứt quãng, trôi chậm
	}
	COLOR = c;
}
