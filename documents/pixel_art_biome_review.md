# Đánh giá pixel art: AC/BW/PF so với MS/FS/CS

**Ngày:** 23-10-2026  
**Branch:** `codex`  
**Phạm vi:** 240 PNG sheets của sáu freshwater biome: 30 swimmers và 10 crawlers mỗi biome. Phân tích sheet, frame, palette, độ sáng, hue/chroma, alpha và quan hệ màu trung bình với far-background; đối chiếu `.agents/rules/pixel_art_guidelines.md` và `.agents/tools/creature_audit.py`.

Bảng “biome hiện tại” phản ánh working tree sau khi hoàn tất batch trên 120 loài MS/FS/CS. Ba pilot được tính là đã hoàn tất từ lượt trước; 117 loài còn lại được chỉnh qua Aseprite MCP. Ảnh zoom pilot ở [pixel_art_pilot_comparison.png](pixel_art_pilot_comparison.png), còn so sánh toàn roster ở [pixel_art_batch_preview.png](pixel_art_batch_preview.png).

Montage chọn mẫu swimmer/crawler, với ba dải reference PF/BW/AC ở trên và biome đích trên nền riêng: [MS](pixel_art_montage_ms.png), [FS](pixel_art_montage_fs.png), [CS](pixel_art_montage_cs.png).

## Kết luận chính

PF, BW và AC có bản sắc sinh vật rõ, nhưng khác nhau đáng kể về tỷ lệ thân, mức tối, chroma và hue. Vì AC vẫn là chuẩn được hài lòng dù thân dài và muted hơn PF/BW, một chỉ tiêu như “cá phải thân sâu”, “ít nhất 75% cùng một hue” hay “dark mass 17–35%” không thể làm thang chất lượng dùng chung.

MS, FS và CS đều có màu biome nhất quán. Hue cohesion của chúng cao hơn PF/BW; vì vậy thiếu sót chính không phải là “sai hue”. Cảm giác ít cuốn hút đến từ sự lặp lại của mảng lưng tối, mặt hông khá đều và cách chia back/flank/belly giống nhau giữa nhiều loài. CS có L* range cao nhất nhóm nhưng vẫn có thể đọc như hai mảng lớn—range tổng thể không cho biết các bậc sáng tối nằm đúng trên khối cơ thể hay không.

Palette RGB của MS/CS nhỏ hơn PF/BW/AC, nhưng color count không tự chứng minh hình bị phẳng. Nó tăng mạnh khi alpha được tính theo RGBA; marking, silhouette và vị trí các cụm pixel giải thích chất lượng tốt hơn số màu thô. Alpha 1–254 cũng không cho biết bao nhiêu pixel thuộc vây.

## Cách đo và giới hạn

- Mỗi PNG được đo ở frame đầu, hàng đầu tiên. Nhóm swimmer có 30 loài; nhóm crawler được tách riêng và không ảnh hưởng summary swimmer. RGB palette bỏ alpha; RGBA palette tính cả alpha; cả hai đếm mọi pixel nhìn thấy trong sprite.
- **Body aspect** là ước tính hộp bao sau phép mở hình thái 3×3 cross để loại bớt phần phụ hẹp. Nó có thể giữ lại vây rộng hoặc loại nhầm phần thân mảnh; cột silhouette aspect gốc giúp đối chiếu. Đây không phải phân đoạn giải phẫu.
- **Deep share** là tỷ lệ swimmer có body-aspect ước tính < 2.0. **Alpha share** là tỷ lệ pixel nhìn thấy có alpha 1–254, không phải tỷ lệ diện tích vây.
- **L range** là L* P95–P5, lấy trung bình từng loài; dùng pixel opaque khi có ít nhất 10 pixel opaque, nếu không dùng toàn bộ pixel nhìn thấy. Dark share, hue family và C90 dùng OKLab. Hue family là cửa sổ trượt 31° lớn nhất trong pixel có chroma ≥ 0.02.
- **Blend share** là tỷ lệ swimmer có màu Lab trung bình cách màu Lab trung bình của file far-background đầu tiên dưới ΔE 20. Nó không kiểm tra marking nhỏ hay tương phản ở nền mid/foreground. `hard_step` là heuristic để tìm cạnh cần nhìn lại, không phải điểm chất lượng.
- Audit hiện đo PNG raster, không tự nhận diện mắt, vây, marking, giải phẫu hay ý đồ animation. Chi tiết định nghĩa và các giới hạn được cập nhật trong `.agents/rules/pixel_art_guidelines.md`.

## So sánh sáu biome

| Biome | RGB median | RGBA median | Alpha 1–254 mean | Body aspect mean | Deep share | L range mean | Dark mass median | Hue family median | C90 median | Blend share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PF | 59.5 | 89.0 | 34.8% | 1.71 | 76.7% | 68.0 | 17.3% | 71.0% | 0.172 | 0.0% |
| BW | 47.0 | 83.0 | 29.6% | 2.03 | 50.0% | 71.5 | 21.1% | 82.4% | 0.078 | 33.3% |
| AC | 62.5 | 88.0 | 29.0% | 2.41 | 26.7% | 65.5 | 10.2% | 86.8% | 0.037 | 6.7% |
| MS | 35.5 | 37.5 | 24.0% | 2.49 | 36.7% | 72.1 | 34.1% | 98.1% | 0.073 | 30.0% |
| FS | 43.0 | 46.0 | 23.3% | 2.22 | 46.7% | 68.3 | 37.9% | 99.8% | 0.067 | 3.3% |
| CS | 33.0 | 35.5 | 29.4% | 2.15 | 46.7% | 77.7 | 36.9% | 83.6% | 0.042 | 0.0% |

### Snapshot của các reference được duyệt

Các số sau lấy trực tiếp từ PF/BW commit đã pin và AC baseline trước pilot, cùng định nghĩa audit hiện tại:

| Reference | RGB median | Body aspect | Deep share | Alpha share | L range | Dark mass | Hue family | C90 | Blend share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PF (`5547197`) | 46.5 | 1.71 | 76.7% | 34.8% | 72.3 | 18.9% | 68.4% | 0.172 | 0.0% |
| BW (`72167f7`) | 34.0 | 2.03 | 50.0% | 29.6% | 74.2 | 21.1% | 71.7% | 0.078 | 36.7% |
| AC (`f755afe3`) | 62.5 | 2.41 | 26.7% | 29.0% | 65.5 | 10.2% | 86.8% | 0.037 | 6.7% |

## Các điểm rút ra khi đối chiếu

1. **Body ratio là đặc điểm roster.** MS có mean 2.49, AC 2.41; cả hai vượt 2.25 nhưng AC được chấp nhận. Deep share AC chỉ 26.7%, PF là 76.7%. Vì vậy quota 40% deep-bodied cá được guideline cũ nêu sẽ ép sai một số roster.
2. **Palette RGB cần tách khỏi alpha.** Reference BW có RGB median 34 nhưng RGBA median 83; AC lần lượt 62.5 và 88. Chỉ đếm RGBA sẽ phóng đại lượng hue thực sự. CS/Pacu pilot tăng 41→45 RGB mà alpha share không đổi.
3. **Không thiếu hue cohesion.** Sau batch, MS 98.1%, FS 99.8%, CS 83.6% trong khi PF 71.0%, BW 82.4%. Hue family cao không tự làm cá thú vị; vị trí marking và chia mặt giải phẫu quan trọng hơn.
4. **Dark mass lớn ở MS/FS/CS, nhưng không có ngưỡng chuẩn chung.** Sau batch, MS 34.1%, FS 37.9%, CS 36.9%; reference AC chỉ 10.2%. Đây là dấu hiệu cần xem mảng tối có quá rộng/đều hay không, không phải lý do để tăng sáng outline toàn bộ.
5. **L range không chấm được phân bố mặt.** CS đạt 77.7, cao nhất; dù vậy mặt thân có thể trông phẳng nếu phần lớn chênh lệch chỉ nằm giữa lưng và bụng. Nên kiểm tra vị trí bậc chuyển, cụm pixel và silhouette ở native scale.
6. **Chroma khác nhau theo biome.** CS C90 0.042, gần AC 0.037 và thấp hơn PF/BW; có thể là chủ ý của suối trong. Không nên tăng saturation đồng loạt chỉ để đạt band 0.07–0.17 như guideline cũ.
7. **Blend share không giải thích hết cảm giác hòa nền.** BW và MS đều khoảng một phần ba swimmer có mean màu gần background; FS chỉ 3.3% dù cảm giác roster vẫn đồng dạng. Cần so từng loài trên composite thực tế.
8. **Palette ít màu là manh mối phụ.** Median RGB của MS/CS thấp, nhưng mỗi pilot sau chỉnh vẫn nằm trong một nhóm khác nhau; count tăng không đảm bảo đẹp. Cần tránh biến count 45–110 thành gate.
9. **Các khác biệt roster nên được giữ.** PF có palette rộng và nhiều điểm nóng; BW dùng pattern/tông ấm; AC dùng thân dài và chroma thấp. Tạo chuẩn chung bằng cách ép cả ba vào một ramp/hình thể sẽ xóa mất lý do người dùng hài lòng.

## Sheet, animation và advisory flags

Tất cả 240 sheet hiện khớp kích thước trong tên file; không có dimension mismatch. Kiểm tra exact pixel A=C trên 180 swimmer rows mỗi biome cho kết quả:

| Biome | A=C mismatch | Hàng chạm biên | Sprite có advisory flag |
|---|---:|---:|---:|
| PF | 6/180 | 22/180 | 10/40 |
| BW | 0/180 | 48/180 | 26/40 |
| AC | 0/180 | 104/180 | 10/40 |
| MS | 12/180 | 10/180 | 23/40 |
| FS | 0/180 | 0/180 | 23/40 |
| CS | 6/180 | 0/180 | 21/40 |

- PF mismatch nằm ở `pf_pea_puffer`; MS ở `ms_chinese_softshell_turtle`, `ms_frog_tadpole`; CS ở `cs_banded_knifefish`. Xem từng clip để xác định lỗi hay chuyển động có chủ ý.
- AC có 104 hàng chạm biên, phần lớn trên nhiều swimmer; BW có 48. PF 22. Do reference cũng có chạm biên, đây là danh sách review theo pixel/tank clipping, không phải auto-fail.
- Flags 26/40 ở BW và 23/40 ở FS không xếp hạng biome: chúng gộp `dE_bg` và `hard_step`, vốn cũng báo trên sprite reference. Đây là lý do audit để advisory mặc định.

## Những điểm guideline cũ cần sửa

1. Gọi PF/BW/AC là cùng một “quality bar” rồi áp ngưỡng tỷ lệ thân duy nhất mâu thuẫn với AC đã được chấp nhận; thay bằng snapshots và nguyên tắc so sánh.
2. Quota 40% deep-bodied không khớp AC 26.7%; đổi thành gợi ý đa dạng roster theo loài.
3. Yêu cầu 45–110 màu nhưng phần mô tả đếm pixel alpha khác nhau như màu riêng; audit mới báo RGB và RGBA riêng. Color count giờ là chỉ báo, không gate.
4. Alpha 1–254 được gọi là “fin share”; phép đo này cũng đếm thân bán trong suốt và biên mềm. Đã đổi thành alpha proxy.
5. Ngưỡng L*≥68, dark mass 17–35%, hue-family≥75% và C90 0.07–0.17 loại sai một hoặc nhiều reference (đặc biệt AC). Đã đổi thành snapshot không bắt buộc.
6. Tỷ lệ aspect trước đây lấy cả vây nhưng được gọi body aspect; audit đã thêm ước tính 3×3 opening và giữ silhouette aspect cạnh đó, đồng thời ghi rõ đây chỉ là gần đúng.
7. Hue family, palette count và màu trung bình không chứng minh từng marking có tương phản; blend-share được ghi rõ là heuristic, cần composite và xem từng species.
8. Hard-step flags có cả trên reference; chỉ dùng để khoanh vùng xem lại, không tự động chạy sửa/đánh rớt.
9. “Luôn để 1 px margin” xung đột với hàng accepted chạm viền: PF 22, BW 48, AC 104. Guideline nay yêu cầu kiểm tra clipping trong viewport thay vì loại sprite tự động.
10. Các lệnh tuyệt đối như cấm pure black/flat region/biên màu cứng quá rộng với pixel art. PF reference có 32 visible `#000000` pixels; outline và mảng phẳng được đánh giá theo nhiệm vụ của pixel ở native scale.
11. `.agents/rules/refs/style_reference.png` có PF, BW rồi lặp PF; không có hình AC dù AC được gọi là một trong ba chuẩn. Guideline nay chỉ sang các asset AC được duyệt ở baseline.

## Pilot đã chỉnh bằng Aseprite MCP

Giữ ba pass tonal trước đó và thêm một bậc sáng upper-shoulder theo từng palette biome. MCP chỉ chỉnh pixel xanh/teal/xanh lam trong dải thân cạnh lưng tối, bỏ qua vùng lân cận marking hue khác và chỉ sửa những vị trí ổn định giữa bốn frame. Alpha, silhouette, marking cam/nâu/đỏ và dữ liệu animation được giữ.

| Pilot | RGB distinct (hiện tại → pilot) | Alpha share | L* range | Số pixel cel đã đổi | Mục tiêu |
|---|---:|---:|---:|---:|---|
| MS pumpkinseed | 43 → 49 | 31.9% → 31.9% | 67.66 → 67.14 | 424 | Bậc sage nhẹ dưới mảng lưng; giữ sọc cam. |
| FS longear sunfish | 34 → 42 | 33.6% → 33.6% | 61.65 → 61.65 | 816 | Chuyển sắc moss sáng theo vai; giữ bụng nâu và vệt sáng. |
| CS pacu | 41 → 45 | 27.4% → 27.4% | 57.59 → 57.59 | 544 | Bậc silver-blue dịu sát lưng; giữ mắt đỏ và chấm sáng. |

L* ở đây là số đo frame E đầu tiên của từng pilot; MS giảm 0.52 điểm, FS/CS không đổi. Các thay đổi lặp cùng tọa độ qua 4 frame nên không tạo shimmer; MCP xác nhận A=C ở cả sáu hướng trên từng pilot, 24 frame và 120 ms mỗi frame, tag E/SE/SW/W/NW/NE còn nguyên. PNG sheet xuất từ các `.aseprite` có kích thước chính xác 4×6 cell.

## Batch đã áp dụng cho 120 loài MS/FS/CS

Batch dùng mask riêng cho từng cel: lấy màu thân chủ đạo ở mặt lưng/vỏ, chọn cụm pixel opaque ngay dưới cạnh tối, bỏ pixel lệch hue và chỉ chấp nhận tọa độ có cùng màu qua cả 4 frame của một tag. Mỗi loài giữ nguyên hue riêng; bậc sáng được nâng nhẹ và chỉ dịch hue rất ít khi màu đó vốn đã gần tint của biome. Hai silhouette hẹp (`ms_stone_loach`, `cs_tidewater_silverside`) có một pixel vai ổn định mỗi hướng nên được giữ làm điểm nhấn đơn pixel, không bị loại như một đốm chớp.

| Biome | Loài trong roster | Pilot đã có | Loài mới qua MCP | Số pixel cel được ghi |
|---|---:|---:|---:|---:|
| MS | 40 | 1 | 39 | 37,756 |
| FS | 40 | 1 | 39 | 40,604 |
| CS | 40 | 1 | 39 | 31,936 |
| **Tổng** | **120** | **3** | **117** | **110,296** |

Số pixel cel là số lần ghi trên từng frame; cùng một tọa độ ổn định được ghi lại ở 4 frame để giữ animation. Cả 117 file nguồn mới đều được sửa và xuất PNG qua Aseprite MCP. Ba pilot trước đó được giữ nguyên, không chạy lại thêm một pass.

**Đối chiếu sau batch:** 120/120 sheet vẫn đúng kích thước theo tên file; so với baseline, số pixel alpha thay đổi là 0. Các mismatch A=C tồn tại trước batch giữ nguyên: MS 12/180 hàng, FS 0/180, CS 6/180; không phát sinh hàng mismatch mới. Boundary-touch rows cũng giữ nguyên ở 10/180, 0/180 và 0/180. MCP xác nhận sau chỉnh sửa các mẫu swimmer vẫn có 24 frame, crawler 16 frame, thời lượng 120 ms và các tag hướng/di chuyển không đổi.

Ảnh spot-check cận cảnh ở [pixel_art_batch_edge_review.png](pixel_art_batch_edge_review.png); danh sách trạng thái từng loài ở [pixel_art_batch_manifest.json](pixel_art_batch_manifest.json). Có thể xem toàn bộ trước/sau ở [pixel_art_batch_preview.png](pixel_art_batch_preview.png).

## Hướng đánh giá tiếp theo

- Xem roster đã chỉnh ở native scale trên far và mid background, sau đó xem các tag chuyển động trong game để đánh giá tương phản ở kích thước chơi thực tế.
- Xem riêng các hàng A=C mismatch có sẵn ở MS và CS cùng các advisory flags; chúng cần được quyết định theo chuyển động và composite, không dựa vào điểm palette đơn lẻ.
- Giữ pass chỉnh sửa tiếp theo theo từng loài khi cần: mở rộng hoặc chia nhỏ mặt sáng theo giải phẫu, giữ marking đặc trưng và biến đổi diện tích mảng tối giữa các species.
