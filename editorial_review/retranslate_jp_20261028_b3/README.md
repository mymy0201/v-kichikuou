# Dịch lại từ tiếng Nhật — đợt 3 (lớn nhất trước), 2026-10-28

Theo yêu cầu: lần này đi từ script lớn nhất trong danh sách Pronoun Studio
chưa đánh dấu hoàn tất. Script lớn nhất là Gｱﾘｽ.ADV (khu Tòa nhà Hanny /
Alice Soft: nhân viên, góc trò chuyện hậu trường, cảnh H người lớn với Mieko).

## Phạm vi

- Gｱﾘｽ.ADV: đọc hết 888 nhóm VI / 900 nhóm JP, viết lại 1.469 khung.
  Bản cũ có nhiều đoạn dịch máy sai nghĩa (vd. 胸 thành “rương”, 狭間 thành
  “Sill”, tên nhân vật, ai nói câu nào); đã sửa theo tiếng Nhật.
- Đoạn VI gộp nhiều câu JP (vùng hội thoại YOK/Con gái số 1, Kuma) được viết
  lại theo đúng thứ tự câu JP; số khung và lệnh chờ giữ nguyên.
- Giữ nguyên, không dịch lại: nhóm VI 255, 257, 264 (đùa về nữ sinh/đồ bơi
  trường học). Menu và chữ cái mật khẩu giữ nguyên nếu đã đúng.
- Cảnh H người lớn (Mieko, nhóm 225, 228) được dịch theo yêu cầu người dùng.

## Kiểm tra

`tools/validate_retranslate_jp.py` (RETRANSLATE_BATCH=retranslate_jp_20261028_b3):
biên dịch đạt, 201 script round-trip khớp, lệnh/chờ y nguyên, mọi khung sửa
≤3 dòng trong 28 ký tự/336 px (unifont_jp.otf), save không đổi. Đã cài; hash
cài khớp staging. Chưa chơi thử trực quan.

Ghi chú công cụ: `<` trong chuỗi bị trình biên dịch hiểu là thẻ; đã thêm kiểm
tra trong `tools/retranslate_jp.py` để từ chối ký tự này.

## Tiếp theo (lớn nhất trước)

Iﾏｼﾞﾝ.ADV, FIGT_M.ADV (còn 44 bản nháp Pronoun Studio chưa build — xử lý
trước), Gｼｨﾙ.ADV, Gｶﾌｪ.ADV, Gﾅｷﾞ.ADV...
