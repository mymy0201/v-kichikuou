# Dịch lại từ tiếng Nhật — đợt 12: Gｱﾋﾞｧﾄｰﾙ.ADV (2026-10-29)

Script: Aviator (cựu đội trưởng Cận vệ, đã có chồng, hơn Rance 7 tuổi) — Maris mời
trở lại, Rance tán tỉnh và hỏi chuyện chồng; các tuyến bổ nhiệm đội trưởng Cận vệ
(Screela bị đuổi); trường sĩ quan nữ Leazas: Rafalia (đại diện khóa 1), Arlcoate
(năm nhất, thiên tài chỉ huy, nhút nhát); kỳ thi chọn học viên xuất sắc (Rafalia
cho Arlcoate uống thuốc lợi tiểu, Arlcoate vẫn thắng rồi ngất); chọn ai nhập ngũ.

## Phạm vi

- Đọc hết 585 nhóm VI / 619 nhóm JP và 4 menu; viết lại 958 khung trong 541 nhóm.
- Bản cũ: phần đầu đã sửa sơ bộ nhưng nhiều câu bị cắt gọn; phần lớn còn lại là
  dịch máy (“Phi công” cho tên Aviator, “Bà Aviator”, “King”, “ngươi/cậu” lẫn
  lộn, “Arcoatat” trong menu, “Sơn phủ” cho Arlcoate). Bộ đếm tuần dùng chữ
  “giây” cho đuôi số nhiều tiếng Anh “s”; nay là chuỗi rỗng, xem coverage.json.
- Xưng hô: Aviator `tôi`, gọi Rance `Vua Rance`/`Bệ hạ`; Rance gọi `cô giáo`/
  `Aviator`. Rafalia `tôi` (quyết định bổ sung 9), gọi `Bệ hạ`; Arlcoate `em`,
  gọi `nhà vua`; Rafalia–Arlcoate `chị`/`em`.

## Loại trừ (giữ nguyên, không tính là hoàn tất)

Tuổi của các học viên (Rafalia, Arlcoate, nữ sinh) không được xác lập; JP gọi
Rafalia là đứa trẻ già trước tuổi, Arlcoate là năm nhất. Theo quy tắc 7, các
nội dung tình dục hoặc lời ám chỉ tình dục liên quan tới học viên được đọc nhưng
giữ nguyên: cảnh H của Rafalia trong lớp (g219–g229), các lần Rafalia gạ gẫm
(g308–g312, g516, g558–g563), lời Rance về việc dùng học viên trên giường/hậu
cung (g101, g156, g232, g239, g241, g268, g270, g314, g336, g416, g432, g481,
g547, các khung g361.b5, g464.b1, g467.b1). 36 nhóm + 3 khung, đã ghi vào chỉ mục.
Cảnh không tình dục với học viên (giới thiệu, ganh đua, bắt nạt bằng thuốc,
Arlcoate tè ra quần và ngất, menu chọn người) được dịch.

## Sửa lỗi đợt 10 (Gﾊﾟﾊﾟｲｱ.ADV)

Công cụ soạn thảo đã cắt dấu cách cuối dòng trong edits.txt đợt 10, nên g12.b0
“Cựu” và g391.b0 “Gandhi cùng” dính liền vào chữ/tên phía sau trong game. Đã
khôi phục dấu cách; không thay đổi gì khác. Từ đợt này, khung cần dấu cách cuối
được ghi bằng ký hiệu tạm rồi thay bằng dấu cách trước khi apply.

## Kiểm tra

Biên dịch đạt, 201 script round-trip khớp (kể cả chuỗi rỗng), lệnh/chờ y nguyên,
mọi khung sửa ≤3 dòng trong giới hạn 28/336 px hoặc 50/600 px, save không đổi.
Đã cài; hash cài khớp staging (installation.json). Chưa chơi thử trực quan.

## Chỉ mục

`update_review_indexes.py` và `--check` đạt. Nhãn lịch sử của Aviator (nhóm
13–16, 37, 52–57; JP 14–19, 40, 55–60) được gạch vì đã dịch lại (người lớn);
nhóm 92/JP99 giữ nhãn. 36 nhóm loại trừ mới được ghi nhận. 12 nhãn nhóm lịch sử
chưa định vị vì khoảng dòng đổi (chỉ số gốc giữ nguyên). Tổng: 12.525 đã định
vị, 834 chưa định vị.

## Tiếp theo (lớn nhất trước)

Gｾﾙ.ADV, Gｲｿﾛｸ.ADV...
