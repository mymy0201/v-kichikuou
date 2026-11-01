# Dịch lại từ tiếng Nhật — đợt 7: Gｶﾌｪ.ADV (2026-10-29)

Script: đội trưởng Carfeknight; Café ở Leazas (Jill, thêu khăn, tượng vàng);
Lady Caravan (gặp Lady, menu mua/nói chuyện/nhận tượng/biến lại/cưỡng bức/rời đi);
nhánh chiến tranh và bắt Lady; gói King; Lady trong ngục; Chaos nhận ra Café,
chuyện 1500 năm (British, Ho Raga, Nikkou, Planner); Suối giải nguyền; Café
trở lại cơ thể cũ, từ chối hậu cung và gia nhập cùng Carfeknight.

## Phạm vi

- Đọc hết 546 nhóm VI / 555 nhóm JP và mọi nhánh (menu g149, g178); viết lại
  1.126 khung. Không có bản nháp Pronoun Studio chờ cho file này.
- Bản cũ phần lớn là dịch máy: “người Anh” cho British, “Mùa xuân” cho 泉,
  “Đoàn lữ hành quý bà”, “Quý cô/Phu nhân” cho Lady, “đụ”, tôi/ngươi lẫn lộn
  trong thoại Rance, “chụp ảnh”, “Thanh kiếm hỏng”, lời Café/Chaos sai người nói.
- Xưng hô: Café/Lady `tôi`, gọi Rance `Vua Leazas`/`ngài`, gọi Chaos `ông`;
  Chaos `ta`, gọi Café `cô`/`nhóc kính cận`, gọi Rance `cậu`; Rance gọi Lady/Café
  `cô`, gọi Chaos `mày`; Carfeknight `tôi`; tên tổ chức giữ `Lady Caravan`,
  `Madam Lady`; tiền `VÀNG`.
- Cảnh H người lớn trước đây bị loại trừ và còn dịch máy (gói King g268, Lady
  trong ngục g288/g298, Café ở suối g528) được dịch lại từng khung theo JP. Mọi
  nhân vật đều là người lớn (Café 1500 tuổi). 113 nhãn nhóm VI + 116 nhãn JP lịch
  sử (size_order_193_195_197_20261023) được gạch qua `exclusion_tracking_overrides.json`,
  chỉ số gốc giữ nguyên.
- VI cũ gộp vài câu JP vào khung tiêu đề/lời dẫn bên cạnh (g19, g42, g54, g70.b3,
  g188, g200, g201, g269, g275, g299, g460); không đổi lệnh, giữ thứ tự trong khung.

## Kiểm tra

Biên dịch đạt, 201 script round-trip khớp, lệnh/chờ y nguyên, mọi khung sửa
≤3 dòng trong giới hạn 28/336 px hoặc 50/600 px (unifont_jp.otf), save không
đổi. Đã cài; hash cài khớp staging (installation.json). Chưa chơi thử trực quan.

## Tiếp theo (lớn nhất trước)

Gﾅｷﾞ.ADV, Gﾏｼﾞｯｸ.ADV, Gﾊﾟﾊﾟｲｱ.ADV...

## Chỉ mục

`tools/update_review_indexes.py`: phần khôi phục từ chỉ mục lịch sử đóng băng nay
cũng áp `exclusion_tracking_overrides.json` (trước đây chỉ áp cho bản ghi có thư
mục nguồn). Chỉ Gｶﾌｪ thay đổi: 136 bản ghi định vị + 93 chưa định vị đều chuyển
sang gạch. 93 bản ghi chưa định vị vì khoảng dòng lịch sử đã đổi do đợt này; chỉ
số gốc giữ nguyên, không đoán số dòng. `update_review_indexes.py --check` đạt.
Tổng: 12.664 đã định vị, 623 chưa định vị (530 trước đợt + 93).
