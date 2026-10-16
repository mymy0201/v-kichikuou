# Báo Cáo Xử Lý Tràn Hộp Thoại (Wordwrap & Textbox Overflow Resolution)

## 1. Tổng Quan Vấn Đề (Problem Overview)
Trong *Kichikuou Rance* (chạy trên engine System 3.9), khung thoại màu trắng (speech bubble) hiển thị lời thoại nhân vật có sức chứa tối đa **3 dòng** (với độ rộng chuẩn `width = 32` ký tự/dòng).

- **Hiện tượng**: Các khối thoại dài từ 4 dòng trở lên sẽ bị tràn ra khỏi mép dưới của khung thoại trắng, đè lên ảnh nền hoặc sprite nhân vật phía dưới gây mất thẩm mỹ và khó đọc.
- **Yêu cầu**: Cắt câu thoại sau một số lượng chữ/dòng nhất định và tiếp tục câu thoại ở một hộp thoại mới bằng cách chờ người chơi bấm chuột rồi hiển thị tiếp, đồng thời ngắt câu tự nhiên theo dấu câu/mệnh đề.

---

## 2. Cơ Chế Engine System 3.9 (Engine Mechanism)
Qua phân tích tệp điều khiển hiển thị `WAO_SUB.ADV`:
- Biến cờ `VAR0521` quyết định cách thức đóng/chuyển hộp thoại:
  - `VAR0521 : 0` tương ứng lệnh `\CLOSE:` (đóng hẳn khung thoại).
  - `VAR0521 : 1` tương ứng lệnh `\A:`: thực thi `IK 0:` (chờ người chơi nhấp chuột hoặc bấm phím) rồi gọi `\CLEAR:` (xóa trắng nội dung trong khung nhưng giữ nguyên khung thoại).
- Mỗi tệp kịch bản `.ADV` đều định nghĩa một nhãn phụ (helper label) ở cuối tệp để gọi `!VAR0521 : 1!`, ví dụ:
  - `Cｼｮｳﾆﾝ.ADV`: nhãn `\L_01fde:`
  - `Gｼｨﾙ.ADV`: nhãn `\L_09789:`
  - `Iﾌﾟﾛﾛｰｸﾞ.ADV`: nhãn `\L_00ce1:`
- Khi một nhân vật tiếp tục nói sang hộp thoại kế tiếp, cú pháp chuẩn của engine là:
  ```text
  \L_helper:
  ZH 1:
  ```
  Lệnh `\L_helper:` chờ click và clear khung thoại, lệnh `ZH 1:` bật lại chế độ hiển thị chữ để in tiếp các dòng tiếp theo mà không làm mất sprite hay trạng thái hội thoại.

---

## 3. Thuật Toán Phân Đoạn Thông Minh (Two-Tier Splitting Algorithm)
Để lời thoại ngắt tự nhiên và dễ đọc nhất cho người chơi:
1. **Tầng 1 - Ngắt theo câu hoàn chỉnh**:
   - Tách đoạn văn bản dài thành các câu dựa trên dấu kết thúc câu (`.`, `!`, `?`, `…`).
   - Gom các câu vào cùng một hộp thoại chừng nào tổng số dòng sau khi wrap (chiều rộng 32 ký tự) $\le 3$ dòng.
2. **Tầng 2 - Ngắt theo mệnh đề**:
   - Nếu bản thân một câu riêng lẻ dài hơn 3 dòng, tách câu đó theo các dấu phân tách mệnh đề (`,`, `;`, `:`, `-`, `–`, `—`).
   - Gom các vế câu vào hộp thoại đảm bảo $\le 3$ dòng.
3. **Giới hạn cứng**:
   - Tuyệt đối không có bất kỳ hộp thoại nào vượt quá **3 dòng**.
   - Các khối 4 dòng trước đây được phân bổ thành 2 dòng + 2 dòng (hoặc theo ranh giới câu), tạo khoảng trống cách lề dưới thoải mái, hoàn toàn vừa vặn trong khung thoại trắng.

---

## 4. Kết Quả Xử Lý (Execution Results)
- **Công cụ thực thi**: [tools/fix_wordwrap_overflow.py](file:///d:/Kichikuou%20Rance/tools/fix_wordwrap_overflow.py)
- **Số tệp kịch bản đã điều chỉnh**: 144 tệp `.ADV`
- **Số khối thoại tràn được tách thành nhiều hộp thoại**: 4.952 khối
- **Số khối thoại dài được tinh chỉnh lại dòng vừa vặn ($\le 3$ dòng)**: 1.002 khối
- **Tổng số khối thoại được xử lý**: 5.954 khối

### Bản lưu dự phòng (Backups)
- Toàn bộ 144 tệp nguồn gốc trước khi tách: `editorial_review/wordwrap_fix/backup/src/`
- Bản sao lưu nhị phân game gốc: `editorial_review/wordwrap_fix/backup/game/` (`KICHIKUSA.ALD`, `System39.ain`)

---

## 5. Biên Dịch & Cài Đặt Vào Game (Compilation & Installation)
- Sử dụng trình biên dịch `xsys35c.exe` với tệp cấu hình dự án `src/xsys35c.cfg`.
- **Kết quả biên dịch**: Thành công 100% (mã thoát `0`), không phát sinh lỗi cú pháp hay nhãn nhảy.
- **Tệp nhị phân tạo ra**:
  - `KICHIKUSA.ALD`: 2.488.336 bytes
  - `System39.ain`: 3.534.422 bytes
- **Cài đặt**: Đã sao chép trực tiếp vào thư mục gốc của game `d:\Kichikuou Rance\`.

---

## 6. Kiểm Thử & Xác Minh Độc Lập (Verification)
1. **Decompile kiểm tra ngược**:
   - Sử dụng `xsys35dc.exe` dịch ngược trực tiếp từ `KICHIKUSA.ALD` và `System39.ain` vừa tạo ra thư mục `editorial_review/wordwrap_fix/verified_build/`.
2. **Quét tự động toàn bộ 144 tệp thoại dịch ngược**:
   - Chạy script kiểm tra [tools/verify_verified_build.py](file:///d:/Kichikuou%20Rance/tools/verify_verified_build.py).
   - **Kết quả**: **0 tệp thoại có khối thoại > 3 dòng**. 100% hội thoại trong game tuân thủ nghiêm ngặt giới hạn $\le 3$ dòng.
3. **Kiểm tra ví dụ thực tế (Cảnh Pluepet trong ảnh chụp màn hình)**:
   - Trước:
     ```text
     'Tôi là Pluepet, thương gia của'
     R
     'hoàng gia.Tôi hi vọng chúng ta'
     R
     'sẽ hòa thuận với nhau, vị vua'
     R
     'mới.'
     ```
     *(4 dòng, dòng thứ 4 bị tràn khỏi hộp thoại)*
   - Sau:
     - **Hộp thoại 1**:
       ```text
       'Tôi là Pluepet, thương gia của'
       R
       'hoàng gia.Tôi hi vọng chúng ta'
       ```
     - **Chờ bấm chuột & xóa khung thoại**:
       ```text
       \L_02079:
       ZH 1:
       ```
     - **Hộp thoại 2**:
       ```text
       'sẽ hòa thuận với nhau,'
       R
       'vị vua mới.'
       ```
     Cả hai hộp thoại đều hiển thị gọn gàng, cách đáy hộp thoại an toàn, không còn hiện tượng tràn chữ.

---

## 7. Tinh Chỉnh Wordwrap Cho Toàn Bộ Bản Dịch Tiếng Việt Hiện Có (Existing Translations Wordwrap Refinement)
Theo yêu cầu tập trung tối ưu hóa cho các bản dịch tiếng Việt sẵn có mà không làm ảnh hưởng đến các tệp tiếng Anh/tiếng Nhật gốc:

- **Công cụ thực thi**: [tools/apply_complete_vn_wordwrap.py](file:///d:/Kichikuou%20Rance/tools/apply_complete_vn_wordwrap.py)
- **Phạm vi xử lý**: Quét toàn bộ **39.584 khối thoại tiếng Việt** trong tất cả các tệp .ADV.
- **Các trường hợp đặc biệt đã giải quyết triệt để (65 khối thuộc 13 tệp)**:
  1. **Tệp Mở Đầu (Iﾌﾟﾛﾛｰｸﾞ.ADV)**: 13 khối thoại có dòng đơn lẻ vượt 32 ký tự (33-37 ký tự) hoặc tràn 4 dòng đã được re-wrap và tách theo câu/mệnh đề tự nhiên với nhãn helper \L_00ce1:.
  2. **Kịch bản Chiến Đấu (FIGT_M.ADV, FIGT作.ADV, FIGT表示.ADV, FIGTﾃｷDE.ADV, FIGTﾐｶDE.ADV)**: 40 khối thoại chiến đấu dài 4 dòng được phân tách thành 2 hộp thoại $\\le 3$ dòng bằng nhãn helper chiến đấu tương ứng (\L_0c576:, \L_00a4e:, \L_03a73:, \L_02658:, \L_00ecb:).
  3. **Tệp Hậu Truyện Game Over (OVER.ADV)**: 2 khối tóm tắt nhân vật dài 4 dòng được tinh chỉnh câu chữ vừa vặn $\\le 3$ dòng mà không cần ngắt click.
  4. **Các dòng thoại kéo dài/chấm lửng không có khoảng trắng (Gｱﾘｽ.ADV, Gｼｽﾞｶ.ADV, Gﾁｽﾞｺ.ADV, Gﾏｼﾞｯｸ.ADV, Gﾙｰﾍﾞﾗﾝ.ADV, Iﾏｼﾞﾝ.ADV)**: Tinh gọn các chuỗi chấm lửng/tiếng hét kéo dài để đảm bảo luôn $\\le 32$ ký tự.

### Kết quả xác minh trên bản build game dịch ngược:
- **Tổng số khối thoại tiếng Việt**: 39.584 khối
- **Số khối thoại tiếng Việt > 3 dòng**: **0 khối** (100% tuân thủ nghiêm ngặt $\\le 3$ dòng).
- **Số dòng tiếng Việt > 32 ký tự**: **0 dòng** (100% tuân thủ nghiêm ngặt $\\le 32$ ký tự).
- **Trạng thái game**: Đã biên dịch và cập nhật trực tiếp vào thư mục gốc d:\\Kichikuou Rance\\.
