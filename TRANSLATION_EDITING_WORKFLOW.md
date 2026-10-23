# Quy trình hiệu đính: đối chiếu Nhật–Anh–Việt

Nhập và điều chỉnh từ `D:\Vestaria\TRANSLATION_EDITING_WORKFLOW.md` ngày
22/10/2026 theo yêu cầu người dùng. Bản sao nguyên trạng và hash của quy trình
nguồn được lưu trong `editorial_review/japanese_base_20261022/`.

## Nguồn và thứ tự ưu tiên

1. Tiếp tục từ `src/` hiện hành; đọc `editorial_review/README-current.txt` và
   kiểm tra archive đang cài. Không dùng bản dịch giai đoạn đầu để xây bản mới.
   Không chạy lại bộ dịch máy, cache dịch cũ hoặc bộ thay đại từ hàng loạt.
2. **Tiếng Nhật gốc là nguồn nghĩa chính. Tiếng Anh chỉ là tham khảo.** Ghi rõ
   xuất xứ, phiên bản và hash của từng nguồn. Không coi file mang tên
   `orig_backup` là tiếng Nhật nếu chưa kiểm chứng nội dung. Nếu thiếu nguồn Nhật,
   ghi phần đó là chờ đối chiếu, không nhận đã hiệu đính theo tiếng Nhật.
3. Ghép đúng cảnh bằng thứ tự sự kiện, nhân vật và lệnh điều khiển. File/nhãn/ID
   giữa các bản có thể khác. Không ghép chỉ theo số dòng hoặc chỉ số chuỗi.
   Khi Anh và Nhật khác nhau, ưu tiên Nhật; không nhập tình tiết riêng của bản Anh.

## Đọc và sửa theo cảnh

4. Đọc từng cảnh và mọi nhánh liên quan, xác định người nói, người nghe, tuổi,
   quan hệ, địa vị và hoàn cảnh. Đặc biệt phân biệt Rance trước/sau khi lên ngôi;
   không gọi mọi nhân vật hoặc mọi người nghe là Bệ hạ. Portrait đang hiện không
   đủ để khẳng định người nghe nếu nhân vật đang nói với đám đông hoặc người thứ ba.
5. Viết lại trực tiếp bằng tiếng Việt: nghĩa, chủ thể, quan hệ, giới tính, sắc
   thái, lời đùa, hướng dẫn chơi. Một cách xưng hô phù hợp trong từng câu; không
   dùng phương án ghép. Không lấy đầu ra dịch máy mới làm bản hiệu đính cuối.
6. Dùng `QUY_TAC_XUNG_HO_VA_THUAT_NGU.md` hiện hành, kể cả quyết định bổ sung.
   Giữ tên hiển thị đã thống nhất. Không nhập tên, xưng hô, thuật ngữ hay số đo
   layout của Vestaria sang Rance. Yêu cầu trực tiếp và nghĩa nguyên tác được
   ưu tiên khi bảng hướng dẫn mâu thuẫn; ghi lại trường hợp cần quyết định mới.
7. Phạm vi gồm mở đầu, băng sơn tặc, lên ngôi/nội chiến Leazas, các sự kiện
   lãnh thổ và nhân vật Leazas, lựa chọn, thất bại và sự kiện chung được gọi tới.
   Ghi từng nhánh đã đọc/chưa đọc/loại trừ. Cờ reviewed chỉ đánh dấu đã đọc,
   không chứng minh bản dịch chắc chắn đúng. Không sửa nội dung tình dục có trẻ
   vị thành niên; ghi rõ phần loại trừ, không tính là đã hoàn tất.

## Giữ kỹ thuật và giao diện

8. Bảo toàn ID, lệnh, điều kiện, biến, số liệu gameplay, placeholder, mã chờ và
   thứ tự sự kiện. Không thêm nhịp chờ để chữa chữ dài. Giữ các sửa combat UI,
   font Unicode và layout hiện hành. Chỉ thay cách xuống dòng khi cần và phải
   ghi tách khỏi sửa nội dung.
9. Ngắt theo từ và theo khung thực tế của cảnh. Khung thoại thường dùng giới
   hạn hiện hành 28/28/28 ký tự; khung rộng tối đa 50 ký tự/dòng. Với font
   `unifont_jp.otf` hiện hành, đo tối đa 336 px ở khung thường và 600 px ở khung
   rộng; tiêu đề cỡ 32 phải đo riêng, không áp chiều ngang của cỡ 24. Kiểm tra font và
   bề rộng thực khi có thể; không áp mốc 42 ký tự/Arial 17 của Vestaria vào đây.
   Giữ đoạn văn chủ ý, không phá câu do bê nguyên xuống dòng Nhật/Anh.
10. Ghi đối chiếu Nhật–Anh–Việt trước/sau, file/cảnh/nhánh và lý do sửa. Ghi rõ
    trường hợp chưa ghép chắc, bản sao liên quan và đoạn chỉ sửa layout.

## Xây và kiểm tra

11. Sao lưu bản mới nhất trước khi sửa. Biên dịch vào thư mục staging riêng,
    giải biên dịch lại và đối chiếu nội dung; so lệnh điều khiển, placeholder,
    thuật ngữ, bề rộng và các file không thuộc phạm vi.
12. Chỉ cài build sau khi kiểm tra thành công. Sao lưu archive đang dùng và so
    hash save trước/sau; không sửa save. Ghi hash build và archive đã cài.
    Báo đúng số cảnh đã đọc, phần còn lại và giới hạn kiểm tra trực quan.

Quy trình này thay thế phương pháp thay đại từ hàng loạt cho các đợt hiệu đính
mới; các script cũ chỉ là lịch sử, không phải quy trình đang dùng.
