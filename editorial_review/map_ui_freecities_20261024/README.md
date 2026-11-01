# Khung thông tin bản đồ và arc thành bang độc lập — 24/10/2026

126 mục hiệu đính hội thoại và6 nhóm layout UI trong4 script. Bản Nhật gốc là nguồn nghĩa; Anh chỉ tham khảo. Không nhận hoàn tất các script ngoài phạm vi.

## Wordwrap ảnh1–2

- Cﾌﾞｶ: sửa toàn bộ3 trang chỉ số cá nhân/chỉ huy dùng chung cho thuộc hạ. Tên riêng có hàng riêng. Trang1 có tên, cấp/HP, công/thủ, EXP. Trang2 có tên, mưu kế%, ma lực/thủ, lượt đánh. Trang3 có tiêu đề và3 hàng thưởng công/thủ theo tấn công, phòng thủ, mê cung. Giữ trang quân số/trang vật phẩm, điều kiện và nhịp chuyển trang.
- Cｼﾊｲﾄｼ: tên thành phố, phe, kinh tế/phòng thủ, chiến trường thành4 hàng.
- Cﾃｷﾄｼ và Cﾃｷﾄｼ2: cùng mẫu4 hàng cho thành địch, cả nhánh biết/chưa biết thông tin. Không thêm hàng trắng giữa tên và phe.
- Dùng ngoặc vuông ASCII ở3 tiêu đề thành phố; tên dài nhất Thành phố Đấu Thần Toushin với ngoặc Nhật rộng360px, ngoặc ASCII còn336px. Không đổi tên địa danh trong SET_MAP hay sửa SET_CHR.
- Không trông chờ engine tự ngắt chuỗi đã chèn số/tên. Chỉ thêm lệnh xuống dòng R, nhãn ngắn rõ nghĩa, giữ mọi X/H, biến, điều kiện, lệnh gameplay và waits.

## Hiệu đính arc ảnh3

Đã đọc JP13–233 của Cﾃｷﾄｼ, gồm các nhánh chấp nhận/từ chối và đối thoại tiếp nối của Mars, Rockearth/Graco, Ice, Lazeal/Amuro/Raylee, Red/Green, Bồ Đào Nha/Goa và Pluepet xin hòa bình. Các phần ngoài phạm vi còn ghi chưa rà. Không suy nhãn H cho phần chưa đọc.

- Graco xưng tôi, gọi Bệ hạ/ngài; Rance ta/ngươi; Maris thần/Bệ hạ. Sửa Qua Rance thành Bệ hạ Rance, các câu chàng/ngươi của Graco và tôi của Rance. Graco thống nhất theo tên hiển thị portrait GRACO ALCAPONE trong ảnh, không giữ lỗi Gracq.
- Giao dịch là nhắm mắt làm ngơ trước việc Hội DX làm để đổi lấy Rockearth và tài trợ chiến phí. Sửa khoản đặt trước, điều không thể làm công khai nhưng làm được trong giới ngầm; không dịch thành dưới lòng đất.
- トランク là va-li chứa tiền, không cốp xe; おい là gọi thuộc hạ, không chào tạm biệt.
- Sửa cả nhánh Rance từ chối/giết Graco và chấp nhận/sáp nhập. Giữ số hối lộ50.000.000 GOLD cùng toàn bộ lệnh/nhánh.
- Lazeal: lời hứa chờ một tháng, điều kiện giao thành cùng Raylee, lời phàn nàn bị phá hứa và Maris truyền lệnh, không gửi đơn đặt hàng.
- Red: giữ tên thành phố, không dịch thành xứ Đỏ; điều kiện ngài bảo vệ đời sống dân, không phải tôi bảo đảm; lời hứa không cướp bóc và nhánh từ chối.
- Bồ Đào Nha được JAPAN chống lưng, không là lá chắn chống JAPAN. Giữ tên Việt hiện hành để khớp bản đồ. Sửa lời đòi900vạn, hạ xuống5vạn, nhánh trả/không trả; không sửa số liệu hoặc đơn vị hiển thị ngân sách.
- Pluepet không phải con rối. Sửa Vũ Rance, hành động bước tới bóng bẩy thay tập tễnh, lời xin hòa bình vì nhà/tài sản ở đó và khoản quyên góp10.000.000 GOLD.
- Mars/Ice: giữ các sửa tay đã đúng; sửa câu dẫn và phản ứng còn dịch máy. Nhóm25 chứa tên thành phố chèn động được giữ đúng hai cụm trước/sau X.

## Kiểm tra và bằng chứng

inventory.json/provenance.json lưu3 nguồn và hashes. review.json gồm126 mục văn bản và6 nhóm UI có bằng chứng Nhật/Anh. ui_layout_review.json ghi nguyên phần/lệnh. coverage.json ghi phạm vi thực, không toàn file. changes.diff và complete_changes.diff lưu trước–sau.

-126 mục khớp chữ duyệt; measured font actual-size cho hội thoại, giữ số ô và nhịp chờ.
-4.615 ca UI từ bộ phát văn bản theo lệnh nguồn:91 tên bản đồ,11 nhãn phe,2 trạng thái trinh sát,53 tên nhân vật, số0/8/100/65535 và thưởng chỉ huy âm/dương/trung tính. Tối đa336px,4 hàng. B3 gốc376×140 giữ nguyên. dynamic_ui_validation.json lưu từng hàng/số đo.
-ui_layout_preview.png là ảnh mô phỏng bằng font thật đã xem, không phải ảnh chụp game.
-Biên dịch staging, giải biên dịch đủ201 script; literal/MS khớp.349 nhóm không sửa trong4 file giữ nguyên.
-Giữ toàn bộ lệnh thực thi ngoài R, biến/ID/điều kiện/gameplay numbers/X/H, nhịp chờ, font/cấu hình, saves và197 script ngoài phạm vi.
-Chỉ cài archive khớp staging sau kiểm tra. Chưa chạy kiểm tra trực tiếp trong game.

Hai chỉ mục gốc tái tạo sau metadata/validation/hàng đợi. Giữ toàn bộ chỉ số loại trừ lịch sử và provenance; chỉ mục dòng hiện hành1-based được tính lại. Không đoán dòng cho hồ sơ lịch sử unresolved.

Bổ sung cuối cùng: [hai menu](../map_ui_freecities_menus_20261024/README.md) đã sửa, tổng128 mục văn bản/menu và6 nhóm layout. Bản cài mới nhất nằm trong đợt bổ sung đó, giữ nguyên mọi sửa UI ở đây.
