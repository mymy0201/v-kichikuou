# Kichikuou Rance (Quỷ Súc Vương Rance) - Dự Án Việt Hóa & Hướng Dẫn Trải Nghiệm

---

## 1. Giới thiệu Game & Dự án Việt Hóa

### 1.1. Giới thiệu về Kichikuou Rance (鬼畜王ランス)
**Kichikuou Rance** (ra mắt năm 1996 bởi hãng **ALICESOFT**) là một trong những tựa game đại chiến thuật kết hợp visual novel/RPG đồ sộ và có tầm ảnh hưởng lớn nhất lịch sử visual novel Nhật Bản. Tác phẩm này đã cứu sống ALICESOFT thời kỳ khủng hoảng và đặt nền móng toàn diện cho toàn bộ thế giới quan Rance Series sau này:
- **Lối chơi chiến lược đỉnh cao**: Người chơi vào vai chiến binh kiêm tướng cướp Rance, từng bước lãnh đạo nghĩa quân giải phóng và thống nhất vương quốc Leazas, bành trướng thế lực đối đầu các đế chế lân cận (Helman, Zeth, JAPAN) và cuối cùng mở chiến dịch chống lại Đội quân Ma tộc khổng lồ do Ma nhân Kayblis cầm đầu.
- **Hệ thống điều binh khiển tướng**: Hơn 50 vị tướng lĩnh, chỉ huy các đạo quân đặc thù từ kỵ sĩ, xạ thủ, ma pháp sư, sát thủ ninja cho tới quái thú và ma thần.
- **Hệ thống cốt truyện & hậu cung (Harem)**: Hàng chục tuyến nhân vật nữ với cốt truyện riêng biệt, hệ thống thẻ bài nhân vật độc đáo, tương tác nhân vật sâu sắc, kèm theo các cảnh ân ái (H-scene) đặc trưng của ALICESOFT.

### 1.2. Mục tiêu & Nền tảng kỹ thuật của Dự án Việt hóa
Dự án được xây dựng với mục tiêu mang lại bản dịch tiếng Việt hoàn chỉnh, chuyên nghiệp và có thể vận hành mượt mà trên cả PC (Windows/Linux) lẫn thiết bị di động (Android):
- **Nền tảng Engine**: Sử dụng mã nguồn mở **xsystem35** – engine System 3.5 hiện đại hỗ trợ Unicode UTF-8 nguyên bản, khử răng cưa chữ (font antialiasing), chạy trực tiếp không cần chuyển mã vùng hệ điều hành (Locale Emulator / AppLocale).
- **Bộ công cụ biên dịch**: Bộ dịch ngược và biên dịch kịch bản chính thức `xsys35c` / `xsys35dc`.
- **Hệ thống hiển thị**: Tích hợp font Unicode `unifont_jp.otf` chuẩn, hiển thị 100% tiếng Việt có dấu sắc nét, đồng bộ hoàn toàn với font ký tự Kanji/Katakana của game.
- **Tối ưu hiển thị**: Thuật toán ngắt dòng cân bằng (**Balanced Wordwrap**) tự động tính toán pixel hiển thị, căn chỉnh ngắt đoạn thẩm mỹ trong hộp thoại 240px–500px, loại bỏ hoàn toàn hiện tượng tràn khung hình hoặc ngắt từ giữa chừng.

---

## 2. Quy mô Game & Khối lượng Công việc Đã Hoàn Thành

Dự án có quy mô văn bản khổng lồ, được thẩm định và hiệu đính qua hàng chục đợt làm việc chuyên sâu:

### 2.1. Thống kê quy mô kịch bản
- **Số lượng script**: **201/201** tập tin kịch bản `.ADV` (100% kịch bản trong `src/`).
- **Tổng lượng từ vựng**: **Hơn 629.500 từ** tiếng Việt đã được biên tập và trau chuốt kỹ lưỡng.
- **Hệ quả kịch bản phân nhánh**: Toàn bộ 7 đại chiến dịch / Arc lớn của cốt truyện:
  1. *Arc 1: Băng sơn tặc Rance (Bandit Arc)*
  2. *Arc 2: Cuộc khởi nghĩa giải phóng Leazas (Leazas Rebellion)*
  3. *Arc 3: Trị vì vương quốc Leazas & Chiêu mộ đồng minh (King of Leazas)*
  4. *Arc 4: Đại chiến Đế quốc Helman (Helman War)*
  5. *Arc 5: Chinh phạt xứ sở JAPAN (JAPAN Campaign)*
  6. *Arc 6: Cuộc chiến Vương quốc Ma pháp Zeth (Zeth War)*
  7. *Arc 7: Đại chiến Ma giới diệt chủng Kayblis (Demon Realm War)*

### 2.2. Giao diện người dùng & Hệ thống chiến thuật (UI/UX)
- Dịch và cân chỉnh toàn bộ **29 file hệ thống & giao diện**: Màn hình menu chính, hệ thống lưu/tải (Save/Load), giao diện tổng hành dinh Leazas, bản đồ tác chiến thế giới, bảng ngân sách/thuế khóa, giao diện xây dựng thành thị và mua sắm thương nhân.
- Hệ thống chiến đấu toàn diện: Quyết đấu quân sự, công thành chiến, thủ thành phản kích, thám hiểm mê cung (tích hợp cụm phím tắt điều hướng nhanh).
- Thống nhất và chuẩn hóa danh xưng, đại từ xưng hô và thuật ngữ theo bộ quy tắc sử thi – kiếm hiệp (`QUY_TAC_XUNG_HO_VA_THUAT_NGU.md`).

### 2.3. Đồ họa thẻ bài nhân vật (ALD & PMS Graphic Reconstruction)
- **108 Thẻ hồ sơ nhân vật & Hậu cung**: 54 thẻ tướng lĩnh quân sự (`CG0601`–`CG0654`) và 54 thẻ nữ nhân hậu cung (`CG0701`–`CG0750`).
- Được tái tạo đồ họa từ gốc: Render font tiếng Việt khử răng cưa sắc nét, quantize chuyển đổi về hệ màu 8-bit palette indexed đúng chuẩn System 3.5, đóng gói trực tiếp vào kho lưu trữ `KICHIKUGA.ALD` mà vẫn giữ nguyên liên kết dữ liệu với `KICHIKUGB.ALD`.

### 2.4. Công cụ hỗ trợ độc quyền đi kèm
- **Rance Save Tool (`rance_save_tool.exe` / `tools/rance_save_tool.py`)**: Công cụ giải mã, phân tích và chỉnh sửa savegame nhị phân System 3.5 độc quyền, hỗ trợ người chơi vượt qua độ khó khắc nghiệt của game.
- Bộ kịch bản biên dịch tự động `build_vietnamese.bat` cho phép người dùng tùy biến và biên dịch lại kịch bản chỉ với 1 cú click.

---

## 3. Hướng Dẫn Sử Dụng Save Tool (`rance_save_tool`)

Game có độ khó và tính ngẫu nhiên rất cao, việc phân chia quân lực hoặc quản lý ngân sách sai lầm có thể dẫn tới thất bại (Game Over). Bộ công cụ Save Tool giúp bạn kiểm tra trạng thái hoặc kích hoạt các tùy chọn hỗ trợ một cách dễ dàng.

### 3.1. Chạy giao diện Menu tương tác (Dành cho người dùng thông thường)
1. Trong thư mục game, nhấp đúp chạy trực tiếp [rance_save_tool.exe](file:///d:/Kichikuou%20Rance/rance_save_tool.exe) (hoặc chạy lệnh `python tools/rance_save_tool.py`).
2. Chương trình sẽ hiện danh sách lựa chọn trực quan bằng tiếng Việt:
   - **Xem thông tin (Inspect)**: Hiển thị chi tiết lượt chơi, ngày tháng LP, số tiền, điểm hành động (CP), số tướng lĩnh, số CG đã mở khóa.
   - **Thêm tiền / Ngân sách**: Tăng ngân quỹ quốc gia để chiêu mộ lính và phát triển thành thị.
   - **Tăng điểm hành động (CP)**: Đặt số lệnh có thể thực hiện trong mỗi lượt (VD: 10–20 lượt hành động thay vì 2–3 lượt mặc định).
   - **Hồi phục & Tăng cường binh lực**: Hồi đầy quân số ngay lập tức hoặc nâng trần quân lực cho toàn bộ tướng lĩnh.
   - **Tăng chỉ số tướng**: Tăng sức tấn công và phòng ngự cho đội ngũ chỉ huy.
   - **Mở khóa 100% Thư viện CG (Full CG Unlock)**: Mở toàn bộ 2.000 CG thưởng thức tại Dinh thự Alice/Menu chính.
   - **Mở khóa Clear Game Flag**: Kích hoạt cờ phá đảo game để mở khóa các tính năng thưởng khi bắt đầu lại.
   - **Tạo sẵn Save Game 7 Arc**: Tự động sinh ra 7 file save tương ứng từ Arc 1 đến Arc 7 với đầy đủ tướng lĩnh và chỉ số tối ưu.

### 3.2. Sử dụng qua dòng lệnh (Command Line Interface - Nhanh & Tự động)
Nếu muốn thực hiện nhanh hoặc lập trình sẵn thông số, bạn có thể gọi từ cửa sổ lệnh Command Prompt hoặc PowerShell:

- **Kiểm tra thông tin file save slot 1 (`KICHIKUSA.asd`)**:
  ```cmd
  rance_save_tool.exe inspect KICHIKUSA.asd
  ```
- **Thêm 50.000 vàng và đặt 10 điểm CP mỗi lượt cho slot 1**:
  ```cmd
  rance_save_tool.exe modify KICHIKUSA.asd --gold 50000 --cp 10
  ```
- **Hồi phục toàn bộ quân đội và nâng giới hạn lính lên 1.000 cho mọi tướng**:
  ```cmd
  rance_save_tool.exe modify KICHIKUSA.asd --heal-troops --boost-troops 1000
  ```
- **Mở khóa toàn bộ CG và Clear Game lưu vào slot 2 (`KICHIKUSB.asd`)**:
  ```cmd
  rance_save_tool.exe modify KICHIKUSA.asd --unlock-cgs --clear-flag --slot 2
  ```
- **Tạo toàn bộ bộ save game cho cả 7 Arc**:
  ```cmd
  rance_save_tool.exe create-all-arcs
  ```

---

## 4. Hướng Dẫn Cài Đặt & Chơi Trên Điện Thoại (Android) qua APK xsystem35

Nhờ engine **xsystem35** có phiên bản tương thích Android (`xsystem35 for Android` / `xsys35-android`), bạn hoàn toàn có thể thưởng thức bản dịch tiếng Việt mượt mà ngay trên smartphone với điều khiển cảm ứng trực quan.

### 4.1. Chuẩn bị tệp tin
1. **Ứng dụng giả lập/engine xsystem35 (APK)**:
   - Tải và cài đặt file cài đặt APK `xsystem35` (hoặc bản build SDL2 xsystem35 cho Android từ cộng đồng GitHub/Release).
   - Cấp đầy đủ quyền truy cập bộ nhớ (**All Files Access / Storage Permission**) cho ứng dụng trong phần Cài đặt của điện thoại.
2. **Dữ liệu game Việt Hóa**:
   - Thư mục game chứa đầy đủ các file dữ liệu:
     - Các tệp nén tài nguyên gốc: `KICHIKUGB.ALD`, `KICHIKUWA.ALD`,...
     - Các tệp tài nguyên Việt hóa: `KICHIKUSA.ALD`, `KICHIKUGA.ALD`, `System39.ain`.
     - Font chữ tiếng Việt: `unifont_jp.otf`.
     - Tệp cấu hình engine: `.xsys35rc`.
     - Các file savegame (nếu có): `KICHIKUSA.asd`,...

### 4.2. Các bước thiết lập thư mục trên điện thoại
1. Kết nối điện thoại với máy tính qua cáp USB (hoặc dùng Google Drive, ZArchiver, v.v.).
2. Tạo một thư mục trò chơi trong bộ nhớ trong điện thoại, ví dụ:
   ```text
   /sdcard/xsystem35/kichikuou/
   ```
   *(Hoặc đường dẫn thư mục mà ứng dụng xsystem35 chỉ định trên máy của bạn, ví dụ: `Android/data/...` hoặc thư mục riêng của app)*.
3. Chép toàn bộ dữ liệu game đã chuẩn bị ở trên vào thư mục này.
4. **Kiểm tra tệp cấu hình `.xsys35rc`**:
   Đảm bảo tệp `.xsys35rc` nằm cùng thư mục chứa game và có nội dung sau để font tiếng Việt hiển thị chính xác:
   ```ini
   ttfont_gothic: unifont_jp.otf
   ttfont_mincho: unifont_jp.otf
   saveformat: xsystem35
   antialias: Yes
   ```

### 4.3. Khởi chạy và trải nghiệm trò chơi
1. Mở ứng dụng **xsystem35** trên điện thoại.
2. Tại màn hình chọn thư mục game, duyệt tìm đến thư mục `/sdcard/xsystem35/kichikuou/` (hoặc nơi bạn vừa chép game vào) và chọn trò chơi.
3. Game sẽ khởi động với màn hình tựa đề tiếng Việt **Kichikuou Rance - Tiếng Việt**.
4. **Cách thao tác cảm ứng trên Android**:
   - **Chạm 1 ngón (Tap)**: Tương đương click chuột trái (chọn lệnh, tiếp tục hội thoại).
   - **Chạm giữ / Chạm 2 ngón (Two-finger tap)**: Tương đương click chuột phải hoặc phím `Esc` (hủy lệnh, mở menu nhanh, đóng bảng).
   - **Vuốt hoặc sử dụng bàn phím ảo**: Dùng phím mũi tên Lên/Xuống để duyệt nhanh các tầng mê cung hoặc duyệt danh sách tướng.

---

## 5. Danh Mục Tệp Tin Đính Kèm Cần Lưu Ý

| Tệp tin / Thư mục | Chức năng |
|---|---|
| [System39.ain](file:///d:/Kichikuou%20Rance/System39.ain) | File nhị phân logic game tiếng Việt đã biên dịch hoàn tất |
| [KICHIKUSA.ALD](file:///d:/Kichikuou%20Rance/KICHIKUSA.ALD) | Gói kịch bản hội thoại tiếng Việt toàn bộ 201 file |
| [KICHIKUGA.ALD](file:///d:/Kichikuou%20Rance/KICHIKUGA.ALD) | Gói đồ họa chứa 108 thẻ bài nhân vật đã Việt hóa 8bpp |
| [unifont_jp.otf](file:///d:/Kichikuou%20Rance/unifont_jp.otf) | Font chữ Unicode hỗ trợ đầy đủ tiếng Việt và tiếng Nhật |
| [.xsys35rc](file:///d:/Kichikuou%20Rance/.xsys35rc) | Tệp cấu hình bắt buộc để engine kích hoạt font và khử răng cưa |
| [rance_save_tool.exe](file:///d:/Kichikuou%20Rance/rance_save_tool.exe) | Bộ công cụ sửa file save, mở khóa CG và hỗ trợ chơi game |
| [play_game.bat](file:///d:/Kichikuou%20Rance/play_game.bat) | Kịch bản khởi động nhanh trên máy tính PC Windows |

---

*Chúc các bạn có những giờ phút trải nghiệm chiến thuật và cốt truyện hào hùng của Quỷ Súc Vương Rance trọn vẹn nhất!*
