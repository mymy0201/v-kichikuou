# Kichikuou Rance - Bản Dịch Tiếng Việt (Vietnamese Localization)

Dự án bản dịch Tiếng Việt toàn diện và hoàn chỉnh 100% cho tựa game chiến thuật kinh điển **Kichikuou Rance (Rance Bạo Chúa - 鬼畜王ランス)** của hãng ALICESOFT trên nền tảng engine `xsystem35` (hỗ trợ Unicode UTF-8 nguyên bản).

---

## 🌟 Tổng Quan Dự Án

- **Tiến độ kịch bản**: **100%** (201/201 tập tin kịch bản `.ADV` trong `src/`).
- **Tổng số lượng từ thoại**: **629,589 từ** đã được biên tập, trau chuốt và chuẩn hóa.
- **Văn phong & Đại từ xưng hô**: Chuẩn hóa nghiêm ngặt theo phong cách kiếm hiệp – sử thi, bám sát tính cách nhân vật (xem chi tiết tại [`QUY_TAC_XUNG_HO_VA_THUAT_NGU.md`](QUY_TAC_XUNG_HO_VA_THUAT_NGU.md)).
- **Ngắt dòng cân bằng (Balanced Wordwrap)**: Tối ưu hóa hiển thị hộp thoại, căn chỉnh thẩm mỹ, không tràn khung hình hay lỗi ngắt từ.
- **Việt hóa đồ họa thẻ bài & nhân vật**: 108 thẻ nhân vật và hậu cung trong `ald_ga_files/` (`KICHIKUGA.ALD`) được tái thiết kế đồ họa tiếng Việt sắc nét.
- **Hỗ trợ Unicode toàn diện**: Sử dụng font TrueType `unifont_jp.otf` kết hợp cấu hình `.xsys35rc`, hiển thị đầy đủ dấu tiếng Việt có khử răng cưa (Antialiasing).

---

## 📁 Cấu Trúc Thư Mục Repository

```text
├── src/                               # Toàn bộ 201 file kịch bản nguồn (.ADV) & cấu hình xsys35c
│   ├── *.ADV                          # Các tệp kịch bản thoại tiếng Việt
│   ├── variables.txt                  # Định nghĩa biến kịch bản
│   ├── xsys35c.cfg                    # Cấu hình biên dịch xsys35c
│   └── xsys35dc.hed                   # Header decompile xsys35dc
├── ald_ga_files/                      # Tệp đồ họa thẻ nhân vật & hậu cung Việt hóa (.PMS)
├── ald_ga_manifest.txt                # Danh sách ánh xạ tệp đồ họa ALD-GA
├── full_ga_manifest.txt               # Manifest đầy đủ cho bộ nén đồ họa
├── editorial_review/                  # Tài liệu theo dõi tiến độ biên tập, audit & đối chiếu 4 đợt
├── KICHIKUSA.ALD                      # Bản nén kịch bản nhị phân đã biên dịch sẵn
├── System39.ain                       # Mã nhị phân logic game đã biên dịch sẵn
├── KICHIKUGA.ALD                      # Kho lưu trữ đồ họa thẻ nhân vật đã Việt hóa sẵn
├── unifont_jp.otf                     # Font chữ Unicode tiếng Việt & tiếng Nhật đầy đủ
├── arial.ttf / tahoma.ttf             # Font phụ trợ đồ họa thẻ bài
├── .xsys35rc                          # Tệp cấu hình engine xsystem35 (font, hiển thị, khử răng cưa)
├── build_vietnamese.bat               # Kịch bản lệnh biên dịch nhanh từ src/ sang .ALD và .ain
├── HUONG_DAN_TIENG_VIET.md            # Hướng dẫn chi tiết cài đặt và trải nghiệm
├── QUY_TAC_XUNG_HO_VA_THUAT_NGU.md    # Bộ quy tắc đại từ xưng hô và thuật ngữ toàn diện
└── game_compatibility.md             # Tài liệu tương thích kỹ thuật xsystem35
```

---

## 🚀 Hướng Dẫn Cài Đặt Bản Dịch (Dành Cho Người Chơi)

1. **Chuẩn bị game gốc**: Cài đặt game *Kichikuou Rance* kèm engine `xsystem35`.
2. **Áp dụng bản dịch**:
   - Sao chép 3 tệp nhị phân đã Việt hóa:
     - `KICHIKUSA.ALD`
     - `System39.ain`
     - `KICHIKUGA.ALD`
   - Sao chép font chữ `unifont_jp.otf` và tệp cấu hình `.xsys35rc` vào thư mục gốc của game (ghi đè nếu được hỏi).
3. **Chạy game**: Khởi động game thông qua `xsystem35.exe`. Toàn bộ giao diện, thoại nhân vật, thẻ bài và hậu cung sẽ hiển thị tiếng Việt hoàn chỉnh.

---

## 🛠️ Biên Dịch Lại Từ Mã Nguồn (`src/`)

Nếu bạn chỉnh sửa kịch bản trong `src/*.ADV`, bạn có thể tự biên dịch lại thành tệp game nhị phân:

1. Đặt bộ công cụ biên dịch `xsys35c` vào thư mục `xsys35c_tools/` (hoặc cài đặt vào biến môi trường PATH).
2. Chạy lệnh:
   ```cmd
   build_vietnamese.bat
   ```
   Hoặc gọi trực tiếp:
   ```cmd
   xsys35c --project=src/xsys35c.cfg --outdir=.
   ```
3. Bộ biên dịch sẽ tự động tạo ra `KICHIKUSA.ALD` và `System39.ain` mới nhất.

---

## 📖 Tham Khảo Tài Liệu Biên Dịch

- [Hướng dẫn trải nghiệm Tiếng Việt chi tiết](HUONG_DAN_TIENG_VIET.md)
- [Quy tắc đại từ xưng hô & Thuật ngữ thế giới Rance](QUY_TAC_XUNG_HO_VA_THUAT_NGU.md)
- [Báo cáo tiến độ biên tập 4 đợt & Audit](editorial_review/README.md)
- [Tương thích kỹ thuật Engine xsystem35](game_compatibility.md)

---

## ⚖️ Tuyên Bố Bản Quyền & Giấy Phép

- Trò chơi gốc **Kichikuou Rance (鬼畜王ランス)** thuộc bản quyền của **ALICESOFT**.
- Bản dịch Tiếng Việt được thực hiện phi thương mại bởi cộng đồng người hâm mộ, phục vụ mục đích trải nghiệm ngôn ngữ và lưu trữ kịch bản.
