# Hướng dẫn Bản dịch Tiếng Việt - Kichikuou Rance (xsystem35)

## 1. Giới thiệu & Cấu trúc đã thiết lập

Dự án này sử dụng bộ công cụ dịch mã nguồn và biên dịch chính thức `xsys35c` kết hợp cùng engine mã nguồn mở `xsystem35` (hỗ trợ Unicode UTF-8 nguyên bản).

- **Thư mục mã nguồn kịch bản**: `src/` (chứa toàn bộ 201 file kịch bản `.ADV` đã được trích xuất).
- **Font chữ hỗ trợ**: `unifont_jp.otf` (bao gồm đầy đủ 58.926 ký tự Unicode, hỗ trợ 100% tiếng Việt có dấu và tiếng Nhật/Anh không bị lỗi ô vuông).
- **Cấu hình font & engine**: `.xsys35rc` (đã kích hoạt `ttfont_gothic` và `ttfont_mincho` bằng `unifont_jp.otf` và bật khử răng cưa `antialias: Yes`).
- **Bản sao lưu gốc**: `orig_backup/` (lưu trữ nguyên bản `KICHIKUSA.ALD` và `System39.ain`).

---

## 2. Các phần kịch bản & giao diện đã được dịch sang Tiếng Việt (Tổng cộng: ~560.000 ký tự)

### A. Giao diện & Hệ thống hoàn chỉnh (Toàn bộ 29 file giao diện đã dịch)
1. **Khởi động & Menu chính (`src/ｽﾀMENU.ADV` & `src/ｽﾀｰﾄ.ADV`)**:
   - Tựa đề cửa sổ: *Kichikuou Rance - Tiếng Việt*
   - Mô tả nút bấm Menu: Tiếp tục, Bắt đầu mới, Bói vận mệnh, Dinh thự Alice, Xem CG, Phòng nhạc,...
2. **Giao diện Lưu/Tải (`src/ﾛｰﾄﾞｾｰﾌﾞ.ADV`)**:
   - Tải dữ liệu, Lưu dữ liệu, Tự động lưu, chọn ô lưu trữ.
3. **Giao diện Lệnh & Lượt chơi (`src/COMMAND.ADV` & `src/MAIN.ADV`)**:
   - Menu Hậu cung, Bộ hạ, Sào huyệt sơn tặc, Lâu đài Leazas, Kho báu, Thương nhân, Hết lượt,...
   - Bảng thông số: Ngân sách, Binh lực, Năm LP, Tháng, Tuần,...
   - Thông báo chuyển giao Giai đoạn của tất cả các thế lực.
4. **Hệ thống Chiến đấu & Điều khiển Quân sự (`FIGT.ADV`, `FIGT_M.ADV`, `FIGT_SEL.ADV`, `FIGTATTK.ADV`, `FIGT_A.ADV`, `FIGT_B.ADV`, `FIGT作.ADV`, `FIGT表示.ADV`, `FIGTﾃｷDE.ADV`, `FIGTﾐｶDE.ADV`)**:
   - Các loại trận đánh: Quyết đấu, Công thành chiến, Thủ thành chiến, Trận chiến mê cung.
   - Thao tác chiến đấu: Công trực diện, Bắn cung, Công phép, Kỹ năng đặc biệt (Tia Gian Lận, Rance Đột Kích, Tia Bạch Hủy Diệt,...).
   - Tình huống phòng thủ thành: Đánh chặn, Ninja do thám, Bỏ rơi thành phố.
   - Chiến thuật đặc biệt: Đột kích sau lưng, phục kích, phá vỡ đội hình.
   - Bảng hiển thị thông số: Binh lực hai bên, sĩ khí, ưu thế, thông báo Thắng lợi / Thất bại.
5. **Giao diện Quản lý Thành thị, Cơ sở & Thao lược (`Cﾃｷﾄｼ.ADV`, `Cﾃｷﾄｼ2.ADV`, `Cﾒｲｷｭｳ.ADV`, `Cｼｮｳﾆﾝ.ADV`, `Cﾃｲﾄ.ADV`, `Cｼﾊｲﾄｼ.ADV`, `Cﾆﾝｼﾞｬ.ADV`, `Cﾊｰﾚﾑ.ADV`, `Cﾌﾞｶ.ADV`)**:
   - Quản lý thành thị chiếm đóng: Trưng thu tạm thời, Gia cố phòng thủ, Đào hố bẫy lớn, Đặt thức ăn tẩm độc, Kinh tế, Phòng thủ.
   - Xây dựng Hoàng đô Leazas, Labyrinth/Mê cung thám hiểm, Cửa hàng thương nhân mua bán trang bị.
   - Chiến dịch Ninja trinh sát và do thám các phe phái.
6. **Quản lý Đội hình, Hậu cung, Vật phẩm & Thống kê (`Sﾌﾞﾀｲ.ADV`, `Sﾌﾞｶ.ADV`, `Sﾊｰﾚﾑ.ADV`, `Sｱｲﾃﾑ.ADV`, `各種DATA.ADV`, `CG.ADV`, `OVER.ADV`, `TEST.ADV`)**:
   - Bổ sung binh lực, thêm lính mới, giới hạn xuất trận, chi phí chiến tranh.
   - Quản lý Hậu cung: Số lần ân ái, lần cuối triệu tập, nhận kinh nghiệm.
   - Trang bị & tháo gỡ vật phẩm nhân vật.
   - Bảng tổng kết số liệu quốc gia: Tổng ngân quỹ, Chi phí lặt vặt, Ngân sách quân sự, Tổng thương vong.
   - Bộ sưu tập hình ảnh CG và Màn hình Kết thúc game (Game Over).

### B. Kịch bản cốt truyện & Nữ chính (Đợt 1: ~216.000 ký tự)
1. **`src/Iﾌﾟﾛﾛｰｸﾞ.ADV` (4.484 ký tự)**: Kịch bản mở đầu game (Rance, Sill, Soul Less, Bound Less).
2. **`src/Iﾄｳｿﾞｸ.ADV` (11.246 ký tự)**: Diễn biến băng sơn tặc của Rance, đột kích Golak, chạm trán quân Helman và kết thúc "Vua Trộm".
3. **`src/Iﾊﾝﾗﾝ.ADV` (13.597 ký tự)**: Cuộc biến loạn và khởi nghĩa tại Vương quốc Leazas.
4. **`src/Iｶﾝｶﾞｴ.ADV` (4.095 ký tự)**: Suy ngẫm và quyết sách chiến lược của Rance.
5. **`src/Iｼﾚｲﾌﾞ.ADV` (24.201 ký tự)**: Bộ chỉ huy chiến lược / Phòng hành quân chiến tranh Leazas.
6. **`src/Iｱﾘｽ.ADV` (13.769 ký tự)**: Cốt truyện Dinh thự Alice và các sự kiện Alice.
7. **`src/IMﾗﾝﾄﾞ.ADV` (8.218 ký tự)**: Cốt truyện Vùng đất M-Land kỳ bí.
8. **`src/Iﾏｼﾞﾝ2.ADV` (4.667 ký tự)**: Tuyến cốt truyện Ma nhân (Majin) phần 2.
9. **`src/Iｼｬﾝｸﾞﾘﾗ.ADV` (28.041 ký tự)**: Toàn bộ tuyến kịch bản Shangri-La.
10. **`src/TJAPAN.ADV` (14.714 ký tự)**: Các sự kiện lượt chơi và biến cố tại JAPAN.
11. **`src/Gｼｨﾙ.ADV` (47.286 ký tự)**: Toàn bộ kịch bản và sự kiện của nữ chính Sill (bạn đồng hành của Rance).
12. **`src/Iｾﾞｽ.ADV` (41.404 ký tự)**: Tuyến kịch bản chiến tranh và cốt truyện Vương quốc Ma pháp Zeth.

### C. Đại chiến Ma nhân & Chiến dịch JAPAN (Đợt 2: ~212.000 ký tự)
1. **`src/Iﾏｼﾞﾝ.ADV` (58.544 ký tự)**: Toàn bộ tuyến cốt truyện Đại chiến Ma nhân (Kayblis, Camilla, Satella, Red Eye, Medusa, cuộc xâm lược Lãnh địa Ma vương).
2. **`src/Gｱﾘｽ.ADV` (58.375 ký tự)**: Toàn bộ sự kiện Dinh thự Alice, tác giả Alice và các bí mật của Đấng sáng tạo.
3. **`src/Gｶﾌｪ.ADV` (48.575 ký tự)**: Khu vực Quán rượu / Cafe trung tâm thị trấn, thuê lính đánh thuê và các nhiệm vụ đặc biệt.
4. **`src/IJAPAN.ADV` (46.600 ký tự)**: Toàn bộ chiến dịch chinh phạt JAPAN (chúa quỷ Nobunaga, Kouhime, Isoroku, thành Osaka, mỏ vàng Sado).

### D. Hồ sơ Nhân vật & Kịch bản Chế độ Hậu cung (Harem Mode) (~340.000 ký tự)
1. **Hồ sơ Thẻ nhân vật Chiến đấu & Hậu cung (`KICHIKUGA.ALD`)**:
   - Toàn bộ **54 thẻ hồ sơ nhân vật chiến đấu** (`CG0601`–`CG0654`): Tái thiết kế đồ họa, kết xuất văn bản tiếng Việt khử răng cưa sắc nét trong khung thẻ viền vàng nguyên bản.
   - Toàn bộ **54 thẻ hồ sơ nữ nhân trong Hậu cung** (`CG0701`–`CG0750` và các biến thể trước khi lên ngôi `CG0695`, `CG0697`, `CG0698`, `CG0699`): Văn bản tiếng Việt đồng bộ hoàn toàn với giọng điệu tự sự của Rance.
2. **Việt hóa thuật ngữ quân sự & chiến đấu còn sót lại**:
   - **20 danh hiệu quân chủng đồng minh & 40 chủng loại quân địch** trong `src/SET_CHR.ADV`: Băng trộm, Kỵ sĩ Leazas, Binh sĩ Leazas, Pháp sư Leazas, Cận vệ Hoàng gia, Kỵ sĩ Helman, Ma chiến binh, Võ sĩ, Ảo thú, Cung thủ JAPAN, Hộ vệ, Thánh kỵ sĩ, Kalar, Lính đánh thuê, Ngụy thiên thần,...
   - **Tuyệt kỹ chiến đấu trong `src/FIGT.ADV`**: Rance Đột Kích (Rance Attack), Nhân Tiện (By the Way), Tia Bạch Hủy Diệt (White Destruction Beam), Tốc độ cao (Highspeed), Chu-hai, Bom biến mất (Vanish Bomb), Tia Gian Lận (Cheater Beam), Quân Rance (Rance Army).
   - Nút bấm và danh xưng trong `src/Sﾊｰﾚﾑ.ADV`: Nút "Thoát" (End), Nữ Cận Vệ (Royal Guards), Bò Hồng (Pink Cow).
3. **Toàn bộ Kịch bản Hậu Cung & Cảnh H (Ân ái / CG Sex) của 48 Nữ Nhân (`G*.ADV` - Hơn 930.000 ký tự)**:
   - Dịch hoàn tất 100% mọi phân đoạn ân ái (H-scene), đối thoại phòng the, tương tác thân mật và sự kiện hậu cung khi diện kiến từng cô gái trong chế độ Hậu cung và khi mở khóa CG:
     - `Gｼｨﾙ.ADV` (Sill Plain), `Gｿｳﾙ.ADV` (Soul), `Gｱﾅｾﾙ.ADV` (Anasel), `Gﾘｱ.ADV` (Lia), `Gﾏﾘｽ.ADV` (Maris), `Gｽｽﾞﾒ.ADV` (Suzume), `Gｳｪﾝﾃﾞｨ.ADV` (Wendy), `Gｶﾅﾐ.ADV` (Kanami), `Gﾚｲﾗ.ADV` (Leila), `Gﾒﾅﾄﾞ.ADV` (Menad), `Gﾓｺﾓｺ.ADV` (Mokomoko), `Gﾊｳﾚｰﾝ.ADV` (Haurein), `Gﾒﾙﾌｪｲｽ.ADV` (Melfeis), `Gｳﾝｶﾞ.ADV` (Sayori Unga), `Gﾒﾘﾑ.ADV` (Merim), `Gﾚｨﾘｨ.ADV` (Raylee), `Gｱｵｲ.ADV` (Aoi), `Gｼｬﾘｴﾗ.ADV` (Shariela), `Gｱﾐﾗﾝ.ADV` (Amiran), `Gｶﾁｭｰｼｬ.ADV` (Katyusha), `Gｿﾙﾆｱ.ADV` (Saulnia), `Gﾏﾘｱ.ADV` (Maria), `Gｼｽﾞｶ.ADV` (Shizuka), `Gﾐﾘ.ADV` (Milli), `Gﾐﾙ.ADV` (Mill), `Gﾗﾝ.ADV` (Ran), `Gｻﾃﾗ.ADV` (Satella), `Gｼﾞｭﾘｱ.ADV` (Julia), `Gﾗﾌｧﾘｱ.ADV` (Rafalia), `Gｱｰﾙｺｰﾄ.ADV` (Arlcoate), `Gｸﾘｰﾑ.ADV` (Cream), `Gﾙｰﾍﾞﾗﾝ.ADV` (Ruberan), `Gｼｰﾗ.ADV` (Sheila), `Gﾁｽﾞｺ.ADV` (Chizuko), `Gﾏｼﾞｯｸ.ADV` (Magic), `Gﾅｷﾞ.ADV` (Nagi), `Gﾏｺﾄ.ADV` (Makoto), `Gﾜｰｸﾞ.ADV` (Warg), `Gｶｸｻﾝ.ADV` (Kaoru), `Gｽｹｻﾝ.ADV` (Wichita), `Gｴﾘｻﾞﾍﾞ.ADV` (Elisabeth), `Gｲｿﾛｸ.ADV` (Isoroku), `Gﾒﾙｼｨ.ADV` (Merci), `Gｺｳﾋﾒ.ADV` (Kou), `Gﾚﾍﾞｯｶ.ADV` (Rebecca), `Gｱﾆｽ.ADV` (Annis), `Gｴﾚﾅ.ADV` (Elena), `Gｻｲﾄｳ.ADV` (Saitou).

---

## 3. Cách chạy game & biên dịch

### Chơi game:
- Chạy trực tiếp [play_game.bat](file:///d:/Kichikuou%20Rance/play_game.bat) hoặc nhấp đúp vào [xsystem35.exe](file:///d:/Kichikuou%20Rance/xsystem35.exe).

### Khi bạn chỉnh sửa mã nguồn kịch bản trong `src/*.ADV`:
- Chạy [build_vietnamese.bat](file:///d:/Kichikuou%20Rance/build_vietnamese.bat) để tự động biên dịch kịch bản UTF-8 thành file `KICHIKUSA.ALD` và `System39.ain`.

### Đóng gói lại đồ họa ALD & Thẻ Profile:
- **Lưu ý quan trọng về ALD**: `KICHIKUGA.ALD` chứa bảng chỉ mục (master index) cho cả Volume 1 (`KICHIKUGA.ALD`) lẫn Volume 2 (`KICHIKUGB.ALD`) tổng cộng 1222 mục. Nếu chỉ tạo manifest cho Volume 1, game sẽ mất liên kết tới các CG màn hình Title (`CG0298`, `CG0301`, `CG0302`, `CG0303` nằm ở Volume 2) khiến màn hình bắt đầu bị đen!
- **Lưu ý quan trọng về PMS**: Engine System 3.5 là engine 8-bit palette. Các thẻ profile (`CG0601..CG0654` offset `8,11`, `CG0701..CG0750` offset `8,6`) bắt buộc phải được mã hóa ở định dạng **8bpp indexed** (thông qua quantize palette gốc). Nếu xuất dạng RGB 16bpp (`\x10\x00`), game sẽ không thể render thẻ profile.
- Để tự động kết xuất và đóng gói lại toàn bộ 108 thẻ Profile chuẩn 8bpp cùng bảng liên kết đầy đủ:
  ```cmd
  python tools\rebuild_vietnamese_profiles.py
  ```
