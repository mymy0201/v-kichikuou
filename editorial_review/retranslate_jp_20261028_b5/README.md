# Dịch lại từ tiếng Nhật — đợt 5: FIGT_M.ADV (2026-10-28)

1. Gộp trước 44 bản nháp Pronoun Studio chưa build vào `src/FIGT_M.ADV` bằng
   chính `render_adv` của studio. 1 dòng (L_000b5:608) phải chỉnh: dấu nháy đơn
   không hợp lệ trong chuỗi ADV và vượt khung 3×28. Bản nháp đã được lưu trữ
   (`*.merged.backup.json`) nên studio tải lại không bị xung đột. Chi tiết:
   `draft_merge/merged_rows.json`, bản nguồn trước khi gộp ở `draft_merge/`.
2. Dịch lại toàn file từ tiếng Nhật: lời thoại xuất trận của mọi nhân vật
   (19 nhóm, ~990 khung). Viết lại 859 khung; các khung VI thừa là câu JP dài
   bị chia 2–3 khung, đã ghép theo đúng thứ tự câu JP.
3. Giữ nguyên: g12.b31 (nữ sinh), g12.b42 (nhận xét dâm về cô bé nhỏ tuổi).

Công cụ: FIGT_M dùng khung thoại 28 ký tự (không phải khung chiến đấu 20);
`tools/retranslate_jp.py` giờ chỉ áp 20 ký tự cho FIGT* có mọi dòng ≤20.

Kiểm tra: biên dịch đạt, 201 script round-trip khớp, lệnh/chờ y nguyên, khung
sửa ≤3 dòng trong giới hạn pixel, save không đổi; đã cài, hash khớp staging.
Chưa chơi thử trực quan.

Tiếp theo (lớn nhất trước): Gｼｨﾙ, Gｶﾌｪ, Gﾅｷﾞ, Gﾏｼﾞｯｸ, Gﾊﾟﾊﾟｲｱ.
