shader_type canvas_item;

// Thảm cỏ tự lắc lư theo dòng nước: mọi tile lắc cùng lúc, cùng hướng

uniform float wind = 1.0;        // độ lệch tối đa của ngọn cỏ (px)
uniform float sway_speed = 1.5;  // tốc độ lắc, bằng SWAY_SPEED trong swaying_plant.gd
uniform float tile_height = 32.0; // chiều cao một tile (px)

void fragment() {
	// Vị trí trong tile: 0 ở đỉnh, 1 ở đáy (đúng cả khi atlas có nhiều hàng)
	float y_in_tile = fract(UV.y / (tile_height * TEXTURE_PIXEL_SIZE.y));
	float h = 1.0 - y_in_tile; // 1 ở ngọn, 0 ở gốc

	// Cùng dạng sóng với cây (sóng chính + sóng nhỏ), không lệch pha theo vị trí
	float t = TIME * sway_speed;
	float sway = (sin(t) * 0.8 + sin(t * 2.3 + 1.7) * 0.2) * wind;

	float off = round(sway * h); // làm tròn để giữ nét pixel
	COLOR = texture(TEXTURE, UV - vec2(off * TEXTURE_PIXEL_SIZE.x, 0.0));
}
