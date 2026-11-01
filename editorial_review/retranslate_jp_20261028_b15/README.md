# Dịch lại từ tiếng Nhật — đợt 15: Gﾏﾘｱ.ADV (2026-10-29)

Script: Maria Custard, nhà phát minh Tulip — ngắm mục tiêu pháo Tulip 2 Goliath
ở thành phố North; lỗ nhìn trộm phòng thay đồ và chuyện phiếm của các nữ nghiên
cứu viên; Rance trêu Maria đọc chữ Hán tục; Maria hỏi vì sao Rance cưới Lia;
trò giả cướp trong phòng tối; Tháp Khoa học Kỹ thuật (Rance xé bản thiết kế rồi
vẫn cho xây); Tulip 1 Cải, Goliath, mạch tăng sinh tốc độ cao (vụ nổ, vết sẹo ở
ngực, nhánh chết/nằm viện), Tulip 100 bay vào vũ trụ (kết GAME OVER) hoặc bị
Rance ra lệnh hủy.

## Phạm vi

- Đọc hết 476 nhóm VI / 485 nhóm JP và 3 menu; viết lại 1.012 khung trong 440
  nhóm (36 nhóm đọc xong giữ nguyên: tiêu đề, “...”, câu đã đúng).
- Bản cũ phần lớn là dịch máy: “Khập khiễng” cho つまらん, Rance xưng `tôi`
  gọi `ngươi`, “Maris” thay cho Maria (g97), “lò phản ứng”, “King Rance”,
  menu hủy dự án dịch sai (“Công việc cuối cùng của lò phản ứng”).
- Xưng hô: Maria `tôi`, gọi `Rance`/`cậu` (bạn cũ từ Custom); trong độc thoại và
  lời tỏ tình (g162, g362, g414; 貴方/好き) chuyển `em`/`anh`. Rance `ta`, gọi
  `cô` (`em` trong cảnh H). Maria gọi `Nữ hoàng Lia`, `Sill`. Maris `thần`,
  `Bệ hạ Rance`, `cô Maria`. Nữ nghiên cứu viên `tớ`/`cậu`, `Tiến sĩ Maria`.
- Chữ Hán tục (痴漢/小陰唇/官能/膣/亀頭): giữ âm Nhật kèm nghĩa để giữ trò đùa.
- Cảnh người lớn (trêu chữ, trò giả cướp, các cảnh H, vết sẹo, kết vũ trụ) dịch
  lại theo JP, trung thành, không tô vẽ. Maria là người lớn; không có nội dung
  liên quan trẻ vị thành niên. 122 nhãn nhóm + 123 nhãn JP lịch sử
  (size_order_181_185_tail_20261024) được gạch, chỉ số gốc giữ nguyên.
- Kỹ thuật: g8.b0 giữ dấu cách cuối trước biến tên thành phố (viết `~SP`, sed
  khôi phục); g7 giữ bố cục quanh biến. Khung gộp tiêu đề + lời thoại (g18,
  g115, g164, g191, g226, g437, g455) ngắt dòng tường minh; khung đếm ngược
  (g370–g375) ghi `Rance「...」` cho người nói thứ hai.

## Kiểm tra

Biên dịch đạt, 201 script round-trip khớp, lệnh/chờ y nguyên, mọi khung sửa
≤3 dòng trong giới hạn 28/336 px hoặc 50/600 px, save không đổi. Đã cài; hash
cài khớp staging (installation.json). Chưa chơi thử trực quan.

## Tiếp theo (lớn nhất trước)

Gﾁｽﾞｺ.ADV, Gｶﾗｰ.ADV, Gﾊﾟｯﾄﾝ.ADV, Gﾐｷ.ADV (kiểm tra tuổi/nội dung trước khi sửa
cảnh tình dục), Gｻﾃﾗ.ADV.

## Chỉ mục

`update_review_indexes.py` và `--check` đạt. 128 bản ghi định vị và đã gạch; 117
nhãn nhóm VI đã gạch nhưng chưa định vị vì khoảng dòng đổi (chỉ số gốc giữ
nguyên, không đoán dòng mới). Tổng: 12.357 đã định vị, 1.002 chưa định vị.
