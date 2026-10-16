# Báo Cáo Dịch Thuật Đợt 200k Từ & Tối Ưu Hóa Wordwrap (Batch 200k Translation Report)

## 1. Tổng Quan Nhiệm Vụ (Task Overview)
- **Mục tiêu**: Dịch thuật toàn bộ lượng nội dung tiếng Anh chưa dịch còn lại trong game (~194.249 từ / ~29.284 đoạn văn trên 157 tệp kịch bản `.ADV`).
- **Quy tắc dịch thuật**: Tuân thủ triệt để [QUY_TAC_XUNG_HO_VA_THUAT_NGU.md](file:///d:/Kichikuou%20Rance/QUY_TAC_XUNG_HO_VA_THUAT_NGU.md).
- **Quy chuẩn Wordwrap & Hộp thoại**:
  - Chiều rộng dòng tối đa: **32 ký tự/dòng** (ngắt dòng bằng lệnh `R`).
  - Số dòng tối đa mỗi hộp thoại: **3 dòng/hộp thoại** (vừa vặn hoàn hảo trong khung thoại trắng).
  - Tự động phân tách các khối thoại dài sang hộp thoại kế tiếp bằng nhãn helper engine (`\L_helper: \n ZH 1:`).

---

## 2. Thống Kê Dịch Thuật & Kịch Bản (Translation Statistics)

- **Số tệp kịch bản được dịch và cập nhật**: **157 tệp `.ADV`**
- **Tổng số từ tiếng Anh đã dịch sang tiếng Việt**: **194.249 từ**
- **Tổng số đoạn thoại tiếng Anh đã xử lý**: **29.284 đoạn**
- **Số khối thoại được phân tách sang hộp thoại mới để chống tràn**: **1.663 khối**
- **Bộ nhớ cache dịch thuật ([tools/translation_cache.json](file:///d:/Kichikuou%20Rance/tools/translation_cache.json))**: Đã lưu trữ hơn **33.000 mục** dịch thuật với cơ chế khóa đa luồng (thread-safe lock) và ghi tệp nguyên tử (atomic write).

### Các tuyến kịch bản trọng tâm được hoàn thiện:
1. **Tuyến Ma Nhân & Đại Chiến Ma Giới**: `Gｱﾋﾞｧﾄｰﾙ.ADV` (Aviator - 7.7k từ), `Gｶﾐｰﾗ.ADV` (Camilla - 5.8k từ), `Gｹｯｾﾙ.ADV` (Kesselring - 3.8k từ), `Gﾚｯﾄﾞｱｲ.ADV` (Redeye - 3.5k từ), `Gｻｲｾﾞﾙ.ADV` (Saizel - 3.3k từ), `Gｹｲﾌﾞﾘｽ.ADV` (Kayblis - 3.2k từ), `Gｼﾙｷｨ.ADV` (Silky - 3.1k từ), `Gｶﾊﾟｰﾗ.ADV` (Kapala - 2.7k từ).
2. **Tuyến Thần Thánh & Thế Giới**: `Iｶﾐ.ADV` (Thần Sáng Thế Rudrasaum / Rance - 5.9k từ), `Gｱﾘｽ2.ADV` (Alice & Megalopolis - 6.1k từ), `Gﾐｷ.ADV` (Ma Vương Miki - 5.9k từ).
3. **Tuyến Nữ Hoàng, Heroine & Vương Quốc**: `Gﾊﾟﾊﾟｲｱ.ADV` (Papaya - 7.6k từ), `Gｾﾙ.ADV` (Sel - 7.0k từ), `Gｶﾗｰ.ADV` (Pastel Kalar / Tộc Kalar - 6.5k từ), `Gﾊﾟｯﾄﾝ.ADV` (Patton Misurugi - 6.1k từ), `Gﾌｳｶ.ADV` (Fuuka - 5.4k từ), `Gｶﾞﾝｼﾞｰ.ADV` (Gandhi Zeth - 5.1k từ), `G1.ADV` & `G2.ADV` (Sự kiện dã ngoại Sill, Lia, Maris), `GAL.ADV` (Sự kiện tương tác toàn bộ nhân vật).

---

## 3. Tuân Thủ Quy Chuẩn Xưng Hô & Thuật Ngữ

- **Bản sắc Rance**:
  - Triệt tiêu hoàn toàn xưng hô "tôi - bạn" của Rance. Rance tự xưng là `Ta` (khi giận dữ: `Tao` / `Bố mày`).
  - Tiếng cười bạo chúa chuẩn hóa: `Gahahahaha!`.
  - Gọi phi tần, thuộc hạ nữ sủng ái là `Em`, phụ nữ hoàng tộc là `Nàng`, địch thủ/quái vật là `Ngươi`/`Mày`.
- **Quan hệ nhân vật đặc thù**:
  - **Sill Plain**: Tuyệt đối gọi `Chủ nhân Rance`, tự xưng `em`.
  - **Lia Parapara Leazas**: Gọi `Chàng Rance` / `Chàng` / `Chàng yêu`, tự xưng `thiếp` / `em`.
  - **Patton Misurugi**: Xưng `ta` / `tôi`, gọi `Rance`.
  - **Tướng lĩnh (Rick, Barres, Cordoba, Ex)**: Tôn xưng Rance là `Bệ hạ`, tự xưng `thần` / `lão thần`.
  - **Miki**: Xưng hô trìu mến `Bé Miki` / `Nhóc Miki`.
- **Hệ thống thuật ngữ quân sự & thế giới**:
  - Factions: `Xích Quân`, `Hắc Quân`, `Bạch Quân`, `Thanh Quân`, `Cận vệ Hoàng gia`.
  - Địa danh: `Phòng yết kiến`, `Vương quốc Leazas`, `Đế chế Helman`, `Vương quốc Ma pháp Zeth`, `Quần đảo JAPAN`, `Ma Giới`, `Thánh Pháp Giáo`.
  - Khái niệm: `Ma Nhân`, `Ma Vương`, `Thần Sáng Thế`, `Á Nhân`, `Siêu vũ khí`, `Rance Đột Kích`, `Tia Bạch Hủy Diệt`, `Tia Hắc Hủy Diệt`, `Tia Gian Lận`, `Sĩ khí`, `Độ ưu thế`.

---

## 4. Biên Dịch & Cài Đặt Vào Game (Compilation & Installation)

- **Trình biên dịch**: `xsys35c_tools/xsys35c.exe` với cấu hình `src/xsys35c.cfg`.
- **Kết quả biên dịch**: **Thành công 100% trên cả 201 tệp kịch bản** (mã thoát `0`), không phát sinh bất kỳ lỗi cú pháp, lệnh lạ hay xung đột nhãn.
- **Tệp nhị phân đã cài đặt vào thư mục gốc (`d:\Kichikuou Rance\`)**:
  - [KICHIKUSA.ALD](file:///d:/Kichikuou%20Rance/KICHIKUSA.ALD): **2.507.280 bytes**
  - [System39.ain](file:///d:/Kichikuou%20Rance/System39.ain): **3.910.984 bytes**
- **Bản lưu dự phòng (Backups)**:
  - Bản lưu mã nguồn trước đợt dịch: `editorial_review/batch_200k/backup/src/`
  - Bản lưu file nhị phân game trước khi cài: `editorial_review/batch_200k/backup/game/`

---

## 5. Kiểm Tra & Xác Minh Độc Lập (Verification)

- **Dịch ngược kiểm chứng**: Dịch ngược toàn bộ file game vừa biên dịch ra thư mục [editorial_review/batch_200k/verified_build/](file:///d:/Kichikuou%20Rance/editorial_review/batch_200k/verified_build/) bằng `xsys35dc.exe`.
- **Kết quả kiểm toán tự động trên bản dịch ngược**:
  - Tổng số khối thoại tiếng Việt trong game: **66.038 khối**
  - Số khối thoại vượt quá 3 dòng: **0 khối** (100% đạt chuẩn $\le 3$ dòng).
  - Số dòng thoại tiếng Việt vượt quá 32 ký tự: **0 dòng** (100% đạt chuẩn $\le 32$ ký tự).
