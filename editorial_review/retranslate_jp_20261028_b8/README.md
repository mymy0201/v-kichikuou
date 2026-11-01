# Dịch lại từ tiếng Nhật — đợt 8: Gﾅｷﾞ.ADV (2026-10-29)

Script: Nagi và Ragarl ở tháp Nagi (Zeth); nhánh Nagi làm hầu gái của
Kesselring; Nagi hầu Rance ban đêm (“giặt giũ tâm hồn”); Wendy; ước mơ của Nagi;
Ragarl triệu Shizuka, trận ở bình nguyên Parapara, Ragarl cưỡng hiếp Shizuka,
Rance cứu; các nhánh tấn công tháp (Ragarl chết, Nagi giết Ragarl, chọn
Shizuka/Nagi), Nagi chết hoặc đến lâu đài Kesselring.

## Phạm vi

- Đọc hết 571 nhóm VI / 577 nhóm JP và mọi nhánh (menu g459); viết lại 942 khung.
- Bản cũ phần lớn là dịch máy: “Sau 10 giờ tối” cho １０の時から, xưng hô
  cậu/ngươi/anh/em lẫn lộn, “Chủ nhân/Thầy” cho 師匠 (nay `sư phụ`), lời dẫn
  ghi nhầm người nói (“Rance” trong lời Ragarl ở g259), “（đổ lỗi）”, “Quá tuyệt vời!!”
  cho ラガーール！！, menu “Xuka”.
- Xưng hô: Nagi `tôi`, gọi Rance `Vua Leazas`/`ngài` (lúc cự tuyệt: `ngươi`),
  gọi Shizuka `con gái Masou`; Nagi–Ragarl `con`–`sư phụ`/`cha`; Ragarl `ta`, gọi
  Shizuka `ngươi`; Shizuka gọi Ragarl `ngươi`, gọi Rance `anh`; Rance gọi Nagi/Shizuka `cô`.
- Cảnh H người lớn dịch lại theo JP: Rance/Nagi g42, g67; Ragarl/Shizuka g259.

## Loại trừ (liên quan trẻ vị thành niên) — giữ nguyên, không tính là đã dịch lại

- g31: Nagi nói đã làm “nghi lễ” với sư phụ (cha) từ năm 10 tuổi.
- g32–g33 (phản ứng/tiếp nối trực tiếp), các khung g42.b8–b9, g42.b50,
  g67.b69–b71 (nhắc lại quan hệ tình dục với sư phụ/cha).
- g547–g558, g568–g570: Ragarl thực hiện phòng trung thuật với Nagi.
- Ghi vào coverage.json (`excluded_vi_command_aligned`, `excluded_jp`,
  `minor_related_left_unchanged_boxes`). Nhãn lịch sử của nhóm 31–33, 42, 67
  (JP 32–34, 43, 69) không gạch; 109 nhãn nhóm + 112 nhãn JP còn lại được gạch.

## Kiểm tra

Biên dịch đạt, 201 script round-trip khớp, lệnh/chờ y nguyên, mọi khung sửa
≤3 dòng trong giới hạn 28/336 px hoặc 50/600 px (unifont_jp.otf), save không
đổi. Đã cài; hash cài khớp staging (installation.json). Chưa chơi thử trực quan.
Quy tắc thuật ngữ đổi hash so với đợt 7 do người dùng sửa mục Uspira; không ảnh hưởng file này.

## Tiếp theo (lớn nhất trước)

Gﾏｼﾞｯｸ.ADV, Gﾊﾟﾊﾟｲｱ.ADV...

## Chỉ mục

`update_review_indexes.py` và `--check` đạt. 18 nhóm VI + 18 nhóm JP loại trừ mới
của đợt này đều định vị được. Nhãn lịch sử của Gﾅｷﾞ: 109 nhóm + 112 JP gạch;
giữ không gạch nhóm 31–33, 42, 67 và JP 32–34, 43, 69. 103 bản ghi lịch sử
(101 đã gạch, 2 chưa gạch: nhóm 42, 67) chuyển sang “cần đối chiếu thêm” vì
khoảng dòng đã đổi; chỉ số gốc giữ nguyên, không đoán số dòng. Tổng: 12.597 đã
định vị, 726 chưa định vị (623 trước đợt + 103).
