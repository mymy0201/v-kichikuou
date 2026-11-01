# Dịch lại từ tiếng Nhật — đợt 10: Gﾊﾟﾊﾟｲｱ.ADV (2026-10-29)

Script: Papaya và Nomicon ở tháp Papaya (xúc xắc ra trận, chờ quân Leazas với
Pika); Rance tìm Pika ở cung điện Zeth; các lần tra khảo Papaya trong ngục ngầm
(dây thừng/kẹp phơi đồ, tất ủ 5 ngày, Papaya khai chỗ giấu Pika); làm tình trong
ngục; Papaya làm đồ mua vui cho lính; cung điện Zeth bị Pika phá hủy; menu xử trí
(nghiên cứu viên không lương / đồ mua vui cho lính / thả đi); Papaya nhảy tháp
(chết năm 21 tuổi); hồi sinh và di thư; tháp Papaya bị đột nhập; Chizuko/Anis/
Nagi tìm pháp sư LV30; Anis và Shizuka bị rút máu làm Pika; Pika diệt quân
Leazas (Miki sống sót); Gandhi lộ thân phận, menu xem hành động/giết, Gandhi
tuyên chiến với Zeth trước cung điện.

## Phạm vi

- Đọc hết 447 nhóm VI / 474 nhóm JP và cả hai menu (g114, g373); viết lại
  1.012 khung trong 385 nhóm. 62 nhóm còn lại đã đọc và giữ nguyên vì đã đúng
  nghĩa (phần lớn do đợt size_order_193_195_197_20261023 sửa trước đó).
- Bản cũ phần lớn là dịch máy từ tiếng Anh: Pika thành “Flash/Đèn Flash”,
  “KEKEKEKEH”, “Sis”, “Lord Papaya”, “Chúa Papaya”, “Tia Chớp”, “đu đủ”,
  “Rance đạt cực khoái… thiếp ra rồi”, “Tứ Thiên Vương”, sai người nói/nghe.
- Xưng hô: Papaya `tôi`, gọi Rance `Vua Leazas`/`cậu` (theo リーザス王/あなた);
  Rance `ta`, gọi Papaya `cô`/`ả`; Nomicon gọi Papaya `chị đại`, tự xưng `ta`;
  đệ tử gọi `đại sư Papaya`; Gandhi với Rance xưng `thần`, gọi `Vua Rance`/
  `ngài`/`Bệ hạ`; Chizuko xưng `ta`, gọi Anis `em`; Anis xưng `em`. Tên/thuật
  ngữ: Pika (ma pháp tối thượng), Nomicon (ma đạo thư), ngục ngầm, Phòng yết kiến,
  Phòng Cán Bộ Tối Cao, Tứ Đại Lãnh Chúa, Hắc Ba Động, Snow Laser, Lightning
  Laser, petit hanny, thị trấn Poor, Ragnarokarc Super Gandhi.
- Chơi chữ tiếng Nhật (Nomicon) được chuyển thành chơi chữ tiếng Việt tương
  đương, không dịch từng chữ (vd. よく柿食う客 → “khách khứa khề khà”).
- Cảnh người lớn dịch lại theo JP (Papaya 21 tuổi, JP168): xem coverage.json.
  Không có nội dung tình dục liên quan trẻ vị thành niên. Cảnh rút máu Anis/
  Shizuka và cảnh Miki sống sót không mang tính tình dục. 64 nhãn nhóm + 68 nhãn
  JP lịch sử (size_order_193_195_197_20261023) được gạch, chỉ số gốc giữ nguyên.
- Khung ghép người nói (giới hạn lệnh portrait cũ): người nói thứ hai được đánh
  dấu `Tên「...」` ở g84.b3, g177.b0, g243.b0, g282.b0, g291.b0, g409.b0,
  g438.b7. Chi tiết trong coverage.json.
- Khung cạnh biến số: g12.b0 (điều kiện 元) là “Cựu ” có dấu cách cuối;
  g304.b0–b3, g345.b0–b1 bắt đầu bằng dấu cách sau tên đội quân `X 1`;
  g391.b0 kết thúc bằng dấu cách trước tên Wichita/Kaoru có điều kiện.

## Kiểm tra

Biên dịch đạt, 201 script round-trip khớp, lệnh/chờ y nguyên, mọi khung sửa
≤3 dòng trong giới hạn 28/336 px hoặc 50/600 px (unifont_jp.otf), save không
đổi. Đã cài; hash cài khớp staging (installation.json). Chưa chơi thử trực quan.

## Tiếp theo (lớn nhất trước)

Gﾚｲﾗ.ADV, Gｱﾋﾞｧﾄｰﾙ.ADV, Gｾﾙ.ADV, Gｲｿﾛｸ.ADV...

## Chỉ mục

`update_review_indexes.py` và `--check` đạt. 132 nhãn lịch sử của Gﾊﾟﾊﾟｲｱ đều đã
gạch (69 định vị: 68 JP + 1 nhóm VI; 63 nhóm VI chưa định vị vì khoảng dòng đã
đổi do đợt này; chỉ số gốc giữ nguyên, không đoán số dòng). Tổng: 12.502 đã
định vị, 821 chưa định vị (758 trước đợt + 63).
