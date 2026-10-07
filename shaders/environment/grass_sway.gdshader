shader_type canvas_item;

// Thảm cỏ tự lắc lư theo dòng nước (không còn phụ thuộc creature)

uniform float wind = 1.0;        // độ lệch tối đa của ngọn cỏ (px)
uniform float sway_speed = 1.5;  // tốc độ lắc
uniform float wave_scale = 0.15; // lệch pha theo phương ngang (càng lớn sóng càng ngắn)
uniform float tile_height = 32.0; // chiều cao một tile (px)

varying vec2 world_pos;

void vertex() {
	// Chuyển tọa độ của node sang tọa độ thế giới
	world_pos = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}

void fragment() {
	// Vị trí trong tile: 0 ở đỉnh, 1 ở đáy (đúng cả khi atlas có nhiều hàng)
	float y_in_tile = fract(UV.y / (tile_height * TEXTURE_PIXEL_SIZE.y));
	float h = 1.0 - y_in_tile; // 1 ở ngọn, 0 ở gốc

	// Lệch pha theo TỪNG TILE (không theo từng pixel), để cả tile lệch cùng nhau.
	// Nếu tính theo từng pixel, hai cột kề nhau lệch khác nhau sẽ làm lặp/mất cột -> vỡ ảnh.
	float tile_x = (floor(world_pos.x / tile_height) + 0.5) * tile_height;
	// Dao động -wind -> wind, các tile lệch pha nhau tạo thành làn sóng
	float sway = sin(TIME * sway_speed + tile_x * wave_scale) * wind;

	float off = round(sway * h); // làm tròn để giữ nét pixel
	COLOR = texture(TEXTURE, UV - vec2(off * TEXTURE_PIXEL_SIZE.x, 0.0));
}
