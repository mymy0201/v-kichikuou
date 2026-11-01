# Các dòng đã bị loại trừ vì H/cận H/nhóm trộn

Cập nhật: 2026-11-01 (Asia/Bangkok). Đợt hiện hành: `retranslate_jp_20261030_b63`.

**“Loại trừ” nghĩa là không biên tập trong đợt có nhãn, không phải đã xóa khỏi script.** Danh sách tổng hợp nhãn đã ghi, không phân loại thêm bằng từ khóa và không xác nhận toàn bộ khoảng đều là H. Nhiều nhóm có cả thoại thường, cận H và H nên đã giữ nguyên cả nhóm.

Số dòng bắt đầu–kết thúc là **1-based, bao gồm hai đầu**. Cột VI trỏ vào `src` hiện hành; JP trỏ bản Nhật đã kiểm chứng. Chỉ số nhóm/chunk là **0-based**. Không trộn hai hệ chỉ số. Khoảng là biên của đơn vị văn bản đã bị gắn nhãn, có thể chứa lệnh xen giữa; không được xóa lệnh hoặc coi đó là biên đầy đủ của cả cảnh.

Các nhãn lịch sử có thể chồng lấp hoặc chỉ là phần đã hoãn ở đợt trước. Đợt mới hơn có thể đã sửa một phần thường trong nhóm trộn. Dùng nguồn đợt và coverage hiện hành để xác định phạm vi; không suy ra rằng mọi nhóm không có trong danh sách đều đã được rà hoặc an toàn để edit.

JP không ánh xạ được chắc chắn sang VI vẫn có tọa độ Nhật chính xác; không tự lấy cùng ordinal. Mục chỉ có dòng cũ chưa đủ căn cứ nằm ở phần cuối. Các chỉ số loại trừ liên tiếp cùng nguồn được gộp thành một khoảng dòng trong bảng; báo cáo JSON giữ từng đơn vị riêng. Nhãn legacy_label khôi phục từ đúng nhãn phân đoạn của bản sao lưu cũ, không chạy lại bộ lọc hay pipeline sửa cũ.

15275 bản ghi đã định vị; 368 bản ghi cần đối chiếu thêm. Không gồm phần chỉ ghi “chưa đọc” mà chưa có nhãn H/cận H.

## Khoảng dòng theo từng script

### 45. Gﾊﾞｳﾝﾄﾞ.ADV

VI SHA-256: `05fcadda45d28cb98729e2cf65732a78fa90b20c2ef4564812dcd643f94dfafe`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾞｳﾝﾄﾞ.ADV:30>)~~ | ~~30~~ | ~~432~~ | ~~chunk 0–58~~ | ~~[editorial_review\size_order_46_50_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_46_50_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾞｳﾝﾄﾞ.ADV:453>)~~ | ~~453~~ | ~~453~~ | ~~chunk 59~~ | ~~[editorial_review\size_order_41_45_20261023\scope.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_41_45_20261023/scope.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾞｳﾝﾄﾞ.ADV:496>)~~ | ~~496~~ | ~~503~~ | ~~chunk 66–67~~ | ~~[editorial_review\size_order_46_50_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_46_50_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾞｳﾝﾄﾞ.ADV:522>)~~ | ~~522~~ | ~~527~~ | ~~chunk 71–72~~ | ~~[editorial_review\size_order_46_50_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_46_50_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾞｳﾝﾄﾞ.ADV:769>)~~ | ~~769~~ | ~~771~~ | ~~chunk 110~~ | ~~[editorial_review\size_order_41_45_20261023\scope.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_41_45_20261023/scope.json>)~~ |

### 50. Iﾌﾟﾛﾛｰｸﾞ.ADV

VI SHA-256: `3eec8e989d9286859426447a70b0ca745d0b8fa753495f788edf8c726e5069d0`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾌﾟﾛﾛｰｸﾞ.ADV:17>)~~ | ~~17~~ | ~~160~~ | ~~chunk 0–25~~ | ~~[editorial_review\size_order_46_50_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_46_50_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾌﾟﾛﾛｰｸﾞ.ADV:341>)~~ | ~~341~~ | ~~429~~ | ~~chunk 56–70~~ | ~~[editorial_review\size_order_46_50_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_46_50_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾌﾟﾛﾛｰｸﾞ.ADV:482>)~~ | ~~482~~ | ~~549~~ | ~~chunk 79–89~~ | ~~[editorial_review\size_order_46_50_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_46_50_20261023/coverage.json>)~~ |

### 52. Iｶﾝｶﾞｴ.ADV

VI SHA-256: `229e3bf3bc9ad5ca0929c7f950353afc23d6312ff17041d987f3a3255e3337e3`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:23>)~~ | ~~23~~ | ~~32~~ | ~~chunk 3–4~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:48>)~~ | ~~48~~ | ~~93~~ | ~~chunk 6–11~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:112>)~~ | ~~112~~ | ~~138~~ | ~~chunk 14–16~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:156>)~~ | ~~156~~ | ~~184~~ | ~~chunk 18–21~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:234>)~~ | ~~234~~ | ~~269~~ | ~~chunk 28–32~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:325>)~~ | ~~325~~ | ~~329~~ | ~~chunk 42~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:421>)~~ | ~~421~~ | ~~435~~ | ~~chunk 53–55~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:465>)~~ | ~~465~~ | ~~490~~ | ~~chunk 59–60~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:512>)~~ | ~~512~~ | ~~580~~ | ~~chunk 64–73~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:602>)~~ | ~~602~~ | ~~613~~ | ~~chunk 76–77~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｶﾝｶﾞｴ.ADV:702>)~~ | ~~702~~ | ~~704~~ | ~~chunk 90~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |

### 53. Gｵｳｼﾞ.ADV

VI SHA-256: `1af81a8664e2d833926233f15f1ee92d046b8489842000d4c14be6470b886415`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｵｳｼﾞ.ADV:101>)~~ | ~~101~~ | ~~189~~ | ~~chunk 12–25~~ | ~~[editorial_review\size_order_51_55_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_51_55_20261023/coverage.json>)~~ |

### 58. Gﾊﾝﾃｨ.ADV

VI SHA-256: `3d1fc5eb7bdaeae0039ef76ed3a000cbfc806c2c1c71c909123a3eb38db0f001`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾝﾃｨ.ADV:84>)~~ | ~~84~~ | ~~115~~ | ~~chunk 10–15~~ | ~~[editorial_review\size_order_56_60_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_56_60_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾝﾃｨ.ADV:273>)~~ | ~~273~~ | ~~429~~ | ~~chunk 38–63~~ | ~~[editorial_review\size_order_56_60_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_56_60_20261023/coverage.json>)~~ |

### 60. Gﾋｭｰﾊﾞｰﾄ.ADV

VI SHA-256: `e9cbf95b120400d2684e525ca09f1b2b1135192d473e47a76d3b01f7a28e80d0`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾋｭｰﾊﾞｰﾄ.ADV:195>)~~ | ~~195~~ | ~~219~~ | ~~jp 30–34~~ | ~~[editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾋｭｰﾊﾞｰﾄ.ADV:18>)~~ | ~~18~~ | ~~290~~ | ~~chunk 0–46~~ | ~~[editorial_review\size_order_56_60_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_56_60_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾋｭｰﾊﾞｰﾄ.ADV:321>)~~ | ~~321~~ | ~~321~~ | ~~chunk 49~~ | ~~[editorial_review\size_order_56_60_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_56_60_20261023/coverage.json>)~~ |

### 64. Gｳﾝｶﾞ.ADV

VI SHA-256: `9ee1bb4e277664e0c4e7b22890d20671a0f940bfa797670b985b4509699a6c60`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｳﾝｶﾞ.ADV:24>)~~ | ~~24~~ | ~~960~~ | ~~chunk 0–197~~ | ~~[editorial_review\size_order_61_65_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_61_65_20261023/coverage.json>)~~ |

### 65. Gｷﾝｹｰﾄﾞ.ADV

VI SHA-256: `ad941aba1ef7c81866b3ba9f37b44e6c6c5dacf1232122870a2bec1d6f9484b7`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｷﾝｹｰﾄﾞ.ADV:334>) | 334 | 458 | jp 42 | [editorial_review\retranslate_jp_20261030_b41\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b41/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｷﾝｹｰﾄﾞ.ADV:261>)~~ | ~~261~~ | ~~951~~ | ~~chunk 33–161~~ | ~~[editorial_review\size_order_61_65_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_61_65_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｷﾝｹｰﾄﾞ.ADV:460>) | 460 | 722 | group 42 | [editorial_review\retranslate_jp_20261030_b41\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b41/coverage.json>) |

### 67. Gﾜｵ.ADV

VI SHA-256: `c7ea7b47c92326aab810e0b9fefb4cbc9c63f00119ab946b69f7ea649b664864`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾜｵ.ADV:802>)~~ | ~~802~~ | ~~844~~ | ~~chunk 104–111~~ | ~~[editorial_review\size_order_66_70_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_66_70_20261023/coverage.json>)~~ |

### 68. Cﾆﾝｼﾞｬ.ADV

VI SHA-256: `21770c3aaec7f2829f4b5daa68d45dca0bbe641070ef5ce22e874b7b6fdbf0da`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Cﾆﾝｼﾞｬ.ADV:675>)~~ | ~~675~~ | ~~687~~ | ~~chunk 79–81~~ | ~~[editorial_review\size_order_66_70_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_66_70_20261023/coverage.json>)~~ |

### 70. Gｻｲﾄｳ.ADV

VI SHA-256: `f28f374642fbca9e0a087767d30d7bc04f0c5b6f9e8f6751f166e7b6470e53ea`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻｲﾄｳ.ADV:618>)~~ | ~~618~~ | ~~1097~~ | ~~chunk 107–186~~ | ~~[editorial_review\size_order_66_70_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_66_70_20261023/coverage.json>)~~ |

### 71. Gﾄｸﾍﾞﾂ.ADV

VI SHA-256: `9d271e261de32774fcf1c577020b10f6ba6f6115df024ca1f50c1686597beb81`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾄｸﾍﾞﾂ.ADV:27>)~~ | ~~27~~ | ~~1063~~ | ~~chunk 0–215~~ | ~~[editorial_review\size_order_71_75_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_71_75_20261023/coverage.json>)~~ |

### 72. Gｴﾘｻﾞﾍﾞ.ADV

VI SHA-256: `660c2343943b34c9eb1c2ec74185f9336a16d67bd8eeeb5c6844b67cf3362788`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｴﾘｻﾞﾍﾞ.ADV:21>)~~ | ~~21~~ | ~~1112~~ | ~~chunk 0–229~~ | ~~[editorial_review\size_order_71_75_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_71_75_20261023/coverage.json>)~~ |

### 73. Gﾊﾆｰ.ADV

VI SHA-256: `e783e7de48bfd4d6bd8bb2ed71ba8c63115e86771f071442860ee6a2470ecff3`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾆｰ.ADV:1056>)~~ | ~~1056~~ | ~~1063~~ | ~~chunk 147–148~~ | ~~[editorial_review\size_order_71_75_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_71_75_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾆｰ.ADV:1236>)~~ | ~~1236~~ | ~~1265~~ | ~~chunk 169–174~~ | ~~[editorial_review\size_order_71_75_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_71_75_20261023/coverage.json>)~~ |

### 74. Gﾘｯｸ.ADV

VI SHA-256: `645b2d00c2cfa74cdd3232e0631d9aca0aac7db6df2c55e1f064bc29b19c1da5`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾘｯｸ.ADV:169>)~~ | ~~169~~ | ~~229~~ | ~~chunk 21–31~~ | ~~[editorial_review\size_order_71_75_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_71_75_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾘｯｸ.ADV:357>)~~ | ~~357~~ | ~~371~~ | ~~chunk 48–50~~ | ~~[editorial_review\size_order_71_75_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_71_75_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾘｯｸ.ADV:1254>)~~ | ~~1254~~ | ~~1256~~ | ~~chunk 184~~ | ~~[editorial_review\size_order_71_75_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_71_75_20261023/coverage.json>)~~ |

### 77. Gﾒﾙｼｨ.ADV

VI SHA-256: `84d1d98d7d2104bf57e74b064e6522919906ddbe47354d40c437aec1d92eaf02`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾒﾙｼｨ.ADV:268>)~~ | ~~268~~ | ~~1397~~ | ~~chunk 37–299~~ | ~~[editorial_review\size_order_76_80_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_76_80_20261023/coverage.json>)~~ |

### 79. Gｶﾞﾙﾃｨｱ.ADV

VI SHA-256: `dcf0f9cd6dbbef666f2e0a072978a96548c3ff0981f4806c2207e9f7bf605536`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾞﾙﾃｨｱ.ADV:989>)~~ | ~~989~~ | ~~991~~ | ~~chunk 154~~ | ~~[editorial_review\size_order_76_80_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_76_80_20261023/coverage.json>)~~ |

### 80. Gｹｲﾌﾞﾆｬﾝ.ADV

VI SHA-256: `1396b09ad634ff7d5e66268424c4330865194a6aa269c9f09908e6fc33c48db0`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾆｬﾝ.ADV:25>)~~ | ~~25~~ | ~~90~~ | ~~chunk 0–10~~ | ~~[editorial_review\size_order_76_80_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_76_80_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾆｬﾝ.ADV:472>)~~ | ~~472~~ | ~~501~~ | ~~chunk 69–74~~ | ~~[editorial_review\size_order_76_80_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_76_80_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾆｬﾝ.ADV:597>)~~ | ~~597~~ | ~~601~~ | ~~chunk 87~~ | ~~[editorial_review\size_order_76_80_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_76_80_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾆｬﾝ.ADV:871>)~~ | ~~871~~ | ~~1522~~ | ~~chunk 127–257~~ | ~~[editorial_review\size_order_76_80_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_76_80_20261023/coverage.json>)~~ |

### 81. Gｶｸｻﾝ.ADV

VI SHA-256: `e5cfe51bc1d7fd2d356dac218bc5553323f54edb95716e5cf35a7906291434c6`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶｸｻﾝ.ADV:70>)~~ | ~~70~~ | ~~1127~~ | ~~chunk 5–231~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶｸｻﾝ.ADV:1230>)~~ | ~~1230~~ | ~~1303~~ | ~~chunk 246–254~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶｸｻﾝ.ADV:1351>)~~ | ~~1351~~ | ~~1358~~ | ~~chunk 262–263~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶｸｻﾝ.ADV:1443>)~~ | ~~1443~~ | ~~1461~~ | ~~chunk 277–279~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |

### 82. GDX.ADV

VI SHA-256: `015955002a42580258238ac1e806042eaf0a8638d59543c103f3f5d4f95bc3c3`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:125>)~~ | ~~125~~ | ~~161~~ | ~~chunk 17–23~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:362>)~~ | ~~362~~ | ~~394~~ | ~~chunk 48–54~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:657>)~~ | ~~657~~ | ~~678~~ | ~~chunk 97–100~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:781>)~~ | ~~781~~ | ~~826~~ | ~~chunk 115–121~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:846>)~~ | ~~846~~ | ~~863~~ | ~~chunk 124–126~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:875>)~~ | ~~875~~ | ~~917~~ | ~~chunk 128–133~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:932>)~~ | ~~932~~ | ~~932~~ | ~~chunk 136~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:947>)~~ | ~~947~~ | ~~999~~ | ~~chunk 138–145~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:1012>)~~ | ~~1012~~ | ~~1051~~ | ~~chunk 149–154~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:1059>)~~ | ~~1059~~ | ~~1075~~ | ~~chunk 156–158~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/GDX.ADV:1244>)~~ | ~~1244~~ | ~~1258~~ | ~~chunk 185–187~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |

### 83. Gｻｰﾅｷｱ.ADV

VI SHA-256: `3771efa1b3ef6541c83ab5698bd43c1b6eedd91b6bd72bb2145165917be12e0f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻｰﾅｷｱ.ADV:86>)~~ | ~~86~~ | ~~90~~ | ~~chunk 12~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻｰﾅｷｱ.ADV:110>)~~ | ~~110~~ | ~~120~~ | ~~chunk 16–18~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻｰﾅｷｱ.ADV:756>)~~ | ~~756~~ | ~~1309~~ | ~~chunk 118–262~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |

### 84. IMﾗﾝﾄﾞ.ADV

VI SHA-256: `d815c580e2e93f49b1956dac8c253a3aa7bce00073048e4b2403a776b8a7db38`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/IMﾗﾝﾄﾞ.ADV:917>)~~ | ~~917~~ | ~~931~~ | ~~chunk 147–149~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/IMﾗﾝﾄﾞ.ADV:1690>)~~ | ~~1690~~ | ~~1694~~ | ~~chunk 271~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/IMﾗﾝﾄﾞ.ADV:1728>)~~ | ~~1728~~ | ~~1751~~ | ~~chunk 276–279~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |

### 85. Gﾏｺﾄ.ADV

VI SHA-256: `f7eb6dd5d82a2e5f898bfac4698c1af59cc75761211861d95c65c61d8eba16e7`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｺﾄ.ADV:17>)~~ | ~~17~~ | ~~22~~ | ~~chunk 0–1~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｺﾄ.ADV:198>)~~ | ~~198~~ | ~~200~~ | ~~chunk 27~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｺﾄ.ADV:210>)~~ | ~~210~~ | ~~212~~ | ~~chunk 29~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｺﾄ.ADV:222>)~~ | ~~222~~ | ~~224~~ | ~~chunk 31~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｺﾄ.ADV:433>)~~ | ~~433~~ | ~~1550~~ | ~~chunk 65–293~~ | ~~[editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>)~~ |

### 86. Cｼｮｳﾆﾝ.ADV

VI SHA-256: `ab010b106b2e900fbada272f85c646dcf637e16d135cca64457459a432b69acb`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Cｼｮｳﾆﾝ.ADV:101>)~~ | ~~101~~ | ~~101~~ | ~~chunk 9~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Cｼｮｳﾆﾝ.ADV:655>)~~ | ~~655~~ | ~~679~~ | ~~chunk 97–101~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Cｼｮｳﾆﾝ.ADV:766>)~~ | ~~766~~ | ~~1082~~ | ~~chunk 114–161~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Cｼｮｳﾆﾝ.ADV:1524>)~~ | ~~1524~~ | ~~1584~~ | ~~chunk 223–233~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Cｼｮｳﾆﾝ.ADV:1642>)~~ | ~~1642~~ | ~~1659~~ | ~~chunk 244–247~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |

### 87. Iｱﾘｽ.ADV

VI SHA-256: `3c854ec25149a12a3d847b14c8919236111ae0e40934d72dcd188cdf9776af0f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iｱﾘｽ.ADV:423>)~~ | ~~423~~ | ~~425~~ | ~~chunk 76~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |

### 88. Gｶﾄﾞﾐｭｳﾑ.ADV

VI SHA-256: `7e4306ec0d8842638d48ad2b1031e740987417e9b6b3edee79d721bff2396adc`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾄﾞﾐｭｳﾑ.ADV:543>)~~ | ~~543~~ | ~~688~~ | ~~chunk 82–107~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾄﾞﾐｭｳﾑ.ADV:1027>)~~ | ~~1027~~ | ~~1029~~ | ~~chunk 158~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾄﾞﾐｭｳﾑ.ADV:1980>)~~ | ~~1980~~ | ~~2005~~ | ~~chunk 310–315~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |

### 89. Gｼﾉﾀﾞ.ADV

VI SHA-256: `12b215558857e17b1c6240b0ed4c0cac1b2d735451e7b9574cfcad04af2ed14d`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼﾉﾀﾞ.ADV:1646>)~~ | ~~1646~~ | ~~1716~~ | ~~chunk 241–252~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼﾉﾀﾞ.ADV:1933>)~~ | ~~1933~~ | ~~1948~~ | ~~chunk 287–290~~ | ~~[editorial_review\size_order_86_90_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_86_90_20261023/coverage.json>)~~ |

### 91. Cｼﾊｲﾄｼ.ADV

VI SHA-256: `c46dfda7ebfa19ae21a197e7d9296c5f2b8c3ef2830b86db7847bb2fdd48db83`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Cｼﾊｲﾄｼ.ADV:1072>)~~ | ~~1072~~ | ~~1169~~ | ~~chunk 102–122~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |

### 92. Gﾛﾚｯｸｽ.ADV

VI SHA-256: `a7c6019b8003f68cfed4ad4f0fbbf66cde5cc7ae55a46b75073f8379003a7c34`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾛﾚｯｸｽ.ADV:1238>)~~ | ~~1238~~ | ~~1283~~ | ~~jp 163~~ | ~~[editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾛﾚｯｸｽ.ADV:1627>)~~ | ~~1627~~ | ~~1627~~ | ~~chunk 253~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾛﾚｯｸｽ.ADV:1728>)~~ | ~~1728~~ | ~~1728~~ | ~~chunk 271~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |

### 93. Gｱｵｲ.ADV

VI SHA-256: `f819777f1ec3062fec956333d212019a60eb55f681f3dde1fd5624a33fddf267`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱｵｲ.ADV:30>)~~ | ~~30~~ | ~~1543~~ | ~~chunk 0–307~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱｵｲ.ADV:1617>)~~ | ~~1617~~ | ~~1651~~ | ~~chunk 327–337~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |

### 94. Gｹｲﾌﾞﾜﾝ.ADV

VI SHA-256: `77848c574d9a8fadfa6416b92436c4c9326658418a2db643a227611489f791a4`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾜﾝ.ADV:125>)~~ | ~~125~~ | ~~173~~ | ~~chunk 19–29~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾜﾝ.ADV:972>)~~ | ~~972~~ | ~~981~~ | ~~chunk 161–162~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾜﾝ.ADV:1303>)~~ | ~~1303~~ | ~~1811~~ | ~~chunk 220–320~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |

### 95. Gｹﾝﾀﾛｳ.ADV

VI SHA-256: `268d8c79eb1c527bef2fa8893c3ee37897b9d55b7d1324dadb7be56719ab6e91`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:32>)~~ | ~~32~~ | ~~55~~ | ~~chunk 0–3~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:101>)~~ | ~~101~~ | ~~218~~ | ~~chunk 11–27~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:262>)~~ | ~~262~~ | ~~266~~ | ~~chunk 33~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:312>)~~ | ~~312~~ | ~~316~~ | ~~chunk 39~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:385>)~~ | ~~385~~ | ~~392~~ | ~~chunk 50–51~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:917>)~~ | ~~917~~ | ~~985~~ | ~~chunk 132–142~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:1091>)~~ | ~~1091~~ | ~~1096~~ | ~~chunk 156–157~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:1154>)~~ | ~~1154~~ | ~~1156~~ | ~~chunk 165~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:1251>)~~ | ~~1251~~ | ~~1256~~ | ~~chunk 178–179~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:1328>)~~ | ~~1328~~ | ~~1337~~ | ~~chunk 190–191~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｹﾝﾀﾛｳ.ADV:1397>)~~ | ~~1397~~ | ~~1402~~ | ~~chunk 201–202~~ | ~~[editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>)~~ |

### 96. Gｿﾙﾆｱ.ADV

VI SHA-256: `221f49fb80e3b7e3ef1650da9210a0cfa7b199f0d5013810a3741afd1384d8c7`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｿﾙﾆｱ.ADV:56>)~~ | ~~56~~ | ~~1541~~ | ~~chunk 4–287~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｿﾙﾆｱ.ADV:1689>)~~ | ~~1689~~ | ~~1718~~ | ~~chunk 309–314~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |

### 98. Gｼｨﾙ2.ADV

VI SHA-256: `9e41d1fd28c8f16b1fce44cecf169cb528741d46121c9601600daa1bdc389465`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ2.ADV:229>)~~ | ~~229~~ | ~~1244~~ | ~~chunk 29–263~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ2.ADV:1456>)~~ | ~~1456~~ | ~~1760~~ | ~~chunk 296–355~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |

### 99. OVER.ADV

VI SHA-256: `83d6f2a10806c03af6df5174109616c6a938377b7e1ce1f1eebb8022c13ecaed`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:291>)~~ | ~~291~~ | ~~310~~ | ~~chunk 8–9~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:424>)~~ | ~~424~~ | ~~426~~ | ~~chunk 18~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:546>)~~ | ~~546~~ | ~~566~~ | ~~chunk 28–29~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:611>)~~ | ~~611~~ | ~~626~~ | ~~chunk 33–34~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:760>)~~ | ~~760~~ | ~~762~~ | ~~chunk 46~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:855>)~~ | ~~855~~ | ~~857~~ | ~~chunk 54~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:901>)~~ | ~~901~~ | ~~903~~ | ~~chunk 58~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1002>)~~ | ~~1002~~ | ~~1006~~ | ~~chunk 66~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1162>)~~ | ~~1162~~ | ~~1166~~ | ~~chunk 79~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1310>)~~ | ~~1310~~ | ~~1340~~ | ~~chunk 92–94~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1386>)~~ | ~~1386~~ | ~~1388~~ | ~~chunk 98~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1408>)~~ | ~~1408~~ | ~~1410~~ | ~~chunk 100~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1482>)~~ | ~~1482~~ | ~~1486~~ | ~~chunk 106~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1546>)~~ | ~~1546~~ | ~~1550~~ | ~~chunk 111~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1582>)~~ | ~~1582~~ | ~~1586~~ | ~~chunk 114~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1633>)~~ | ~~1633~~ | ~~1637~~ | ~~chunk 118~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/OVER.ADV:1684>)~~ | ~~1684~~ | ~~1686~~ | ~~chunk 122~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |

### 100. Gｼｬﾘｴﾗ.ADV

VI SHA-256: `545f172d7c81a828b4ab935d8af2692a3155520a8bc95db41ce1984d11305486`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｬﾘｴﾗ.ADV:619>)~~ | ~~619~~ | ~~641~~ | ~~chunk 89–92~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｬﾘｴﾗ.ADV:798>)~~ | ~~798~~ | ~~1750~~ | ~~chunk 118–315~~ | ~~[editorial_review\size_order_96_100_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_96_100_20261023/coverage.json>)~~ |

### 101. Gｼﾞｰｸ.ADV

VI SHA-256: `290f7853b3af4d77fcf80593210138367af12f8c3b3bb9dfd305399496eefe37`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼﾞｰｸ.ADV:567>) | 567 | 660 | jp 74–89 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼﾞｰｸ.ADV:847>) | 847 | 899 | jp 114–124 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼﾞｰｸ.ADV:1223>) | 1223 | 1259 | jp 177–182 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |

### 102. Gｱﾐﾗﾝ.ADV

VI SHA-256: `f427656fcff1e2b4c0352b343991128dca74488cd7dc2806ca250d27e4302eb0`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾐﾗﾝ.ADV:311>) | 311 | 1071 | jp 49–126 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾐﾗﾝ.ADV:1214>) | 1214 | 1224 | jp 146 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾐﾗﾝ.ADV:1259>) | 1259 | 1310 | jp 153–162 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |

### 104. Gﾄｳｹﾞﾝ.ADV

VI SHA-256: `9d1888a45699a928ca1d2722e7e95d3a047a4fdbc18c533111745d7d3a3a10e6`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾄｳｹﾞﾝ.ADV:293>) | 293 | 1347 | jp 27–96 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |

### 105. Gｺｰﾄﾞ.ADV

VI SHA-256: `a324039ca16d227352d86bb22acd440502d44550fda88499f8d05e8bef10cf5d`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺｰﾄﾞ.ADV:974>) | 974 | 1020 | jp 166–167 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺｰﾄﾞ.ADV:1509>) | 1509 | 1512 | jp 246 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) |

### 106. Gﾌﾞﾘﾃｨ.ADV

VI SHA-256: `30be138ab81244e48ba7330256d30418c4834f2a11665f71bab9538777e1600f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌﾞﾘﾃｨ.ADV:424>)~~ | ~~424~~ | ~~424~~ | ~~jp 52~~ | ~~[editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾌﾞﾘﾃｨ.ADV:523>)~~ | ~~523~~ | ~~523~~ | ~~group 45~~ | ~~[editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>)~~ |

### 107. Gｷｬﾛﾘ.ADV

VI SHA-256: `d81d192a3e9da557df5a5ed0c269cc7efcefb79ed4a0239e2b64cff4dbc0acff`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｷｬﾛﾘ.ADV:132>) | 132 | 214 | jp 12–20 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｷｬﾛﾘ.ADV:301>) | 301 | 1074 | jp 37–134 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｷｬﾛﾘ.ADV:1370>) | 1370 | 1372 | jp 183 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |

### 108. Gｱﾘｽﾄﾚｽ.ADV

VI SHA-256: `4d4dccd72dfe71dd1513c3c1948b3c8eea460e76dea282f7a173800486cea152`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽﾄﾚｽ.ADV:262>) | 262 | 274 | jp 34 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽﾄﾚｽ.ADV:800>) | 800 | 842 | jp 84 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽﾄﾚｽ.ADV:973>) | 973 | 975 | jp 96 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽﾄﾚｽ.ADV:1172>) | 1172 | 1177 | jp 120 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽﾄﾚｽ.ADV:1206>) | 1206 | 1216 | jp 126–127 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽﾄﾚｽ.ADV:343>) | 343 | 369 | group 32 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |

### 109. Gｺﾙﾄﾞﾊﾞ.ADV

VI SHA-256: `5a280290dab4976cfbddab7bc7fad64df573f7cf07b47f30f80eef0892909654`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺﾙﾄﾞﾊﾞ.ADV:195>) | 195 | 198 | jp 23 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺﾙﾄﾞﾊﾞ.ADV:276>) | 276 | 284 | jp 32 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺﾙﾄﾞﾊﾞ.ADV:563>) | 563 | 839 | jp 70–82 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺﾙﾄﾞﾊﾞ.ADV:882>) | 882 | 915 | jp 88–93 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺﾙﾄﾞﾊﾞ.ADV:1196>) | 1196 | 1208 | jp 134 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺﾙﾄﾞﾊﾞ.ADV:1236>) | 1236 | 1381 | jp 137–161 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｺﾙﾄﾞﾊﾞ.ADV:260>) | 260 | 271 | group 22 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｺﾙﾄﾞﾊﾞ.ADV:373>) | 373 | 390 | group 30 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｺﾙﾄﾞﾊﾞ.ADV:784>) | 784 | 1290 | group 64–75 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｺﾙﾄﾞﾊﾞ.ADV:1347>) | 1347 | 1394 | group 81–85 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｺﾙﾄﾞﾊﾞ.ADV:1766>) | 1766 | 1787 | group 124 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｺﾙﾄﾞﾊﾞ.ADV:1819>) | 1819 | 2045 | group 127–146 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |

### 110. Iﾄｳｿﾞｸ.ADV

VI SHA-256: `adfe4393ee277d2de434ee256a5127e40a353dc7367732bd171d02547079ab71`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾄｳｿﾞｸ.ADV:255>)~~ | ~~255~~ | ~~262~~ | ~~jp 29~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾄｳｿﾞｸ.ADV:483>)~~ | ~~483~~ | ~~485~~ | ~~jp 61~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾄｳｿﾞｸ.ADV:886>)~~ | ~~886~~ | ~~902~~ | ~~jp 126–127~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾄｳｿﾞｸ.ADV:1423>)~~ | ~~1423~~ | ~~1426~~ | ~~jp 181~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾄｳｿﾞｸ.ADV:1540>)~~ | ~~1540~~ | ~~1569~~ | ~~jp 198–203~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:321>)~~ | ~~321~~ | ~~340~~ | ~~group 27~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:321>) | 321 | 435 | group 27–38 | [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:610>) | 610 | 668 | group 55–62 | [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:638>)~~ | ~~638~~ | ~~647~~ | ~~group 59~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:889>) | 889 | 941 | group 90–94 | [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:1166>)~~ | ~~1166~~ | ~~1199~~ | ~~group 123–124~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:1166>) | 1166 | 1214 | group 123–126 | [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:1892>)~~ | ~~1892~~ | ~~1901~~ | ~~group 178~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Iﾄｳｿﾞｸ.ADV:2043>)~~ | ~~2043~~ | ~~2085~~ | ~~group 195–199~~ | ~~[editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>)~~ |

### 111. Gｿﾐｰﾀ.ADV

VI SHA-256: `ef0c344fe8c9e2f1c66cd6d222cebc18f9687e41d59e2238514af07850d4414b`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｿﾐｰﾀ.ADV:35>) | 35 | 44 | jp 1–2 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｿﾐｰﾀ.ADV:67>) | 67 | 158 | jp 6–18 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｿﾐｰﾀ.ADV:296>) | 296 | 316 | jp 41–45 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｿﾐｰﾀ.ADV:365>) | 365 | 628 | jp 52–98 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｿﾐｰﾀ.ADV:838>) | 838 | 846 | jp 131 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｿﾐｰﾀ.ADV:1021>) | 1021 | 1373 | jp 160–185 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｿﾐｰﾀ.ADV:40>) | 40 | 54 | group 1 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｿﾐｰﾀ.ADV:90>) | 90 | 254 | group 5–16 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｿﾐｰﾀ.ADV:457>) | 457 | 484 | group 39–43 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｿﾐｰﾀ.ADV:544>) | 544 | 973 | group 49–93 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｿﾐｰﾀ.ADV:1274>) | 1274 | 1289 | group 125 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｿﾐｰﾀ.ADV:1521>) | 1521 | 2114 | group 153–174 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) |

### 112. Gｽｹｻﾝ.ADV

VI SHA-256: `de0559fcabadfbab38dd14c1674bac1da9058be16b8a0325705a84e52cadb6b0`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:60>) | 60 | 72 | jp 4–5 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:88>) | 88 | 88 | jp 8 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:186>) | 186 | 216 | jp 26–29 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:237>) | 237 | 542 | jp 33–49 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:586>) | 586 | 743 | jp 55–77 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:761>) | 761 | 848 | jp 79–93 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:864>) | 864 | 866 | jp 96 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:876>) | 876 | 876 | jp 98 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:905>) | 905 | 906 | jp 103 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:978>) | 978 | 984 | jp 113 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｹｻﾝ.ADV:1002>) | 1002 | 1292 | jp 117–120 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:69>) | 69 | 88 | group 3 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:109>) | 109 | 111 | group 6 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:252>) | 252 | 295 | group 24–26 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:323>) | 323 | 846 | group 30–46 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:902>) | 902 | 1160 | group 51–72 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:1183>) | 1183 | 1311 | group 74–88 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:1330>) | 1330 | 1339 | group 91 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:1358>) | 1358 | 1358 | group 93 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:1401>) | 1401 | 1408 | group 98 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:1516>) | 1516 | 1527 | group 108 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｹｻﾝ.ADV:1551>) | 1551 | 2072 | group 112–115 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |

### 113. Gｱﾅｾﾙ.ADV

VI SHA-256: `cab5a97c1365edd13b11c82c7a71361876efc8245d001c75e751f48bd188106f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾅｾﾙ.ADV:147>) | 147 | 148 | jp 19 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾅｾﾙ.ADV:194>) | 194 | 234 | jp 25–31 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾅｾﾙ.ADV:319>) | 319 | 1139 | jp 44–99 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾅｾﾙ.ADV:1317>) | 1317 | 1457 | jp 123–136 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾅｾﾙ.ADV:194>) | 194 | 196 | group 19 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾅｾﾙ.ADV:259>) | 259 | 325 | group 25–31 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾅｾﾙ.ADV:434>) | 434 | 1701 | group 44–98 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾅｾﾙ.ADV:1962>) | 1962 | 2160 | group 122–134 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |

### 114. Gﾒﾃﾞｨｳｻ.ADV

VI SHA-256: `c6725b0c217dd2abfc2a3a4904fe271fe91682fa36f256ee189630d4222c2b29`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾃﾞｨｳｻ.ADV:495>) | 495 | 546 | jp 74–83 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾃﾞｨｳｻ.ADV:817>) | 817 | 1649 | jp 122–210 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾃﾞｨｳｻ.ADV:599>) | 599 | 674 | group 68–75 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾃﾞｨｳｻ.ADV:1025>) | 1025 | 2258 | group 112–192 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |

### 115. Gﾓｺﾓｺ.ADV

VI SHA-256: `f885970efb8c8158320b3fb3deaa7741c90c67a3fe843f16df299041414c9314`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾓｺﾓｺ.ADV:382>) | 382 | 494 | jp 56–79 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾓｺﾓｺ.ADV:535>) | 535 | 1097 | jp 86–134 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾓｺﾓｺ.ADV:1131>) | 1131 | 1133 | jp 140 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾓｺﾓｺ.ADV:1179>) | 1179 | 1180 | jp 150 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾓｺﾓｺ.ADV:1309>) | 1309 | 1316 | jp 172–173 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾓｺﾓｺ.ADV:1338>) | 1338 | 1601 | jp 176–203 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾓｺﾓｺ.ADV:533>) | 533 | 699 | group 56–79 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾓｺﾓｺ.ADV:755>) | 755 | 1613 | group 86–134 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾓｺﾓｺ.ADV:1662>) | 1662 | 1666 | group 140 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾓｺﾓｺ.ADV:1730>) | 1730 | 1734 | group 150 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾓｺﾓｺ.ADV:1902>) | 1902 | 1918 | group 171–172 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾓｺﾓｺ.ADV:1945>) | 1945 | 2338 | group 175–202 | [editorial_review\size_order_112_116_plus170_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_112_116_plus170_20261023/coverage.json>) |

### 118. Gｸﾘｰﾑ.ADV

VI SHA-256: `6d1b799d294b9df23a24febec1af0213d082695c1ab2bc960b544cbe451edbf8`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｸﾘｰﾑ.ADV:272>) | 272 | 987 | jp 31–95 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｸﾘｰﾑ.ADV:272>) | 272 | 1033 | jp 31–97 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｸﾘｰﾑ.ADV:1168>) | 1168 | 1362 | jp 111–148 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｸﾘｰﾑ.ADV:1172>) | 1172 | 1264 | jp 112–128 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｸﾘｰﾑ.ADV:1324>) | 1324 | 1338 | jp 142–144 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｸﾘｰﾑ.ADV:1406>) | 1406 | 1417 | jp 155–156 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｸﾘｰﾑ.ADV:1441>) | 1441 | 1443 | jp 160 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｸﾘｰﾑ.ADV:371>) | 371 | 1596 | group 29–95 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｸﾘｰﾑ.ADV:1782>) | 1782 | 1916 | group 111–127 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｸﾘｰﾑ.ADV:2000>) | 2000 | 2028 | group 141–143 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｸﾘｰﾑ.ADV:2119>) | 2119 | 2143 | group 154–155 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｸﾘｰﾑ.ADV:2177>) | 2177 | 2187 | group 159 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |

### 119. Iﾊﾝﾗﾝ.ADV

VI SHA-256: `f92dc8aca65f13b258d7361306e88368e0a9bea38c74a61f5584b3ff2c554a46`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾊﾝﾗﾝ.ADV:278>) | 278 | 294 | jp 26 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾊﾝﾗﾝ.ADV:1055>) | 1055 | 1257 | jp 122–136 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾊﾝﾗﾝ.ADV:380>) | 380 | 411 | group 26 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾊﾝﾗﾝ.ADV:1509>) | 1509 | 1825 | group 122–136 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾊﾝﾗﾝ.ADV:1590>) | 1590 | 1825 | group 132–136 | [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |

### 120. Gﾏｹﾝ.ADV

VI SHA-256: `19f2f6afddb8d599c4bd8a5ba92f3f7f5d18dc1e6ac7c184a1f1079801d244c9`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:279>) | 279 | 281 | jp 22 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:307>) | 307 | 313 | jp 26 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:718>) | 718 | 719 | jp 85 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:728>) | 728 | 742 | jp 87–90 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:780>) | 780 | 781 | jp 96 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:973>) | 973 | 976 | jp 128 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1020>) | 1020 | 1056 | jp 135–139 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1173>) | 1173 | 1185 | jp 157–159 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1386>) | 1386 | 1389 | jp 192 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1423>) | 1423 | 1425 | jp 198 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1486>) | 1486 | 1493 | jp 207 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1517>) | 1517 | 1517 | jp 211 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1543>) | 1543 | 1551 | jp 215 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1562>) | 1562 | 1578 | jp 217–218 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1595>) | 1595 | 1595 | jp 221 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1688>) | 1688 | 1740 | jp 235–243 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｹﾝ.ADV:1787>) | 1787 | 1789 | jp 249 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:363>) | 363 | 365 | group 24 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:402>) | 402 | 419 | group 28 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:984>) | 984 | 988 | group 88 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:1000>) | 1000 | 1019 | group 90–93 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:1068>) | 1068 | 1070 | group 99 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:1341>) | 1341 | 1348 | group 129 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:1407>) | 1407 | 1465 | group 136–140 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:1622>) | 1622 | 1635 | group 158–159 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:1892>) | 1892 | 1903 | group 188 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:1947>) | 1947 | 1951 | group 194 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:2028>) | 2028 | 2040 | group 203 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:2079>) | 2079 | 2081 | group 207 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:2116>) | 2116 | 2136 | group 211 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:2149>) | 2149 | 2179 | group 213–214 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:2199>) | 2199 | 2199 | group 217 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:2313>) | 2313 | 2393 | group 230–238 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏｹﾝ.ADV:2463>) | 2463 | 2470 | group 244 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |

### 121. Gﾕｳﾚｲ.ADV

VI SHA-256: `1cb226494dc33079aa9647183d488dadd2bda2bbbd896ad86b32a120ef3460d4`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:35>) | 35 | 48 | jp 0–1 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:111>) | 111 | 113 | jp 13 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:128>) | 128 | 171 | jp 15–19 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:247>) | 247 | 261 | jp 30–31 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:475>) | 475 | 485 | jp 69–70 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:531>) | 531 | 537 | jp 75 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:675>) | 675 | 717 | jp 91–93 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:828>) | 828 | 840 | jp 113 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:992>) | 992 | 994 | jp 135 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:1119>) | 1119 | 1121 | jp 151 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:1253>) | 1253 | 1295 | jp 167–174 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:1334>) | 1334 | 1648 | jp 180–206 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾕｳﾚｲ.ADV:1697>) | 1697 | 1708 | jp 212–214 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:36>) | 36 | 58 | group 0 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:142>) | 142 | 146 | group 10 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:164>) | 164 | 232 | group 12–14 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:337>) | 337 | 363 | group 25 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:653>) | 653 | 671 | group 61–62 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:727>) | 727 | 744 | group 66 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:936>) | 936 | 1018 | group 82–84 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:1160>) | 1160 | 1190 | group 100 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:1381>) | 1381 | 1388 | group 120 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:1567>) | 1567 | 1571 | group 134 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:1735>) | 1735 | 1794 | group 147–153 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:1853>) | 1853 | 2422 | group 159–184 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾕｳﾚｲ.ADV:2476>) | 2476 | 2490 | group 189–191 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |

### 122. Gﾐﾙ.ADV

VI SHA-256: `f84a3b46504f01530a70e0c925cf1a484846ed494e2b52792066be7ccbc6a3da`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾙ.ADV:166>) | 166 | 177 | jp 22–24 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾙ.ADV:211>) | 211 | 397 | jp 28–57 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾙ.ADV:514>) | 514 | 1877 | jp 77–246 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾙ.ADV:211>) | 211 | 228 | group 22–24 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾙ.ADV:271>) | 271 | 541 | group 28–57 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾙ.ADV:693>) | 693 | 981 | group 77–108 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾙ.ADV:1012>) | 1012 | 2653 | group 110–243 | [editorial_review\size_order_117_122_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_117_122_20261023/coverage.json>) |

### 123. Gﾗﾝ.ADV

VI SHA-256: `f8f245ccb95367b8faf5c9d35655ad5cb07d19a1abff3f4c4db7343fdbc97079`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:85>) | 85 | 93 | jp 7 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:148>) | 148 | 183 | jp 15–22 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:277>) | 277 | 281 | jp 37 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:335>) | 335 | 339 | jp 47 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:377>) | 377 | 391 | jp 52–53 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:497>) | 497 | 604 | jp 71 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:625>) | 625 | 641 | jp 73 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:718>) | 718 | 734 | jp 84–87 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:886>) | 886 | 1617 | jp 112–169 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾝ.ADV:1637>) | 1637 | 1648 | jp 174 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:107>) | 107 | 130 | group 6 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:200>) | 200 | 250 | group 13–20 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:377>) | 377 | 384 | group 35 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:460>) | 460 | 469 | group 45 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:514>) | 514 | 535 | group 49–50 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:671>) | 671 | 867 | group 68 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:891>) | 891 | 921 | group 70 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:1009>) | 1009 | 1030 | group 81–84 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:1227>) | 1227 | 2375 | group 109–164 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾝ.ADV:2400>) | 2400 | 2429 | group 169 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |

### 124. Gｼﾞｭﾘｱ.ADV

VI SHA-256: `7708669ce1bc53bff29212710e15579dd8cd96cb8bb98a69204e45f400a97406`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼﾞｭﾘｱ.ADV:134>) | 134 | 1015 | jp 14–64 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼﾞｭﾘｱ.ADV:1363>) | 1363 | 1424 | jp 116–125 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼﾞｭﾘｱ.ADV:1465>) | 1465 | 1501 | jp 131–138 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｼﾞｭﾘｱ.ADV:153>) | 153 | 1492 | group 13–62 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｼﾞｭﾘｱ.ADV:1953>) | 1953 | 2051 | group 114–123 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｼﾞｭﾘｱ.ADV:2098>) | 2098 | 2151 | group 129–136 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |

### 125. Gｶﾊﾟｰﾗ.ADV

VI SHA-256: `2915c316e466fd5eaf31e0bbec290a477e46adce6df0a114d08f99ace68b043a`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾊﾟｰﾗ.ADV:248>) | 248 | 260 | jp 30–31 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾊﾟｰﾗ.ADV:495>) | 495 | 1367 | jp 66–114 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾊﾟｰﾗ.ADV:1669>) | 1669 | 1683 | jp 151 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾊﾟｰﾗ.ADV:1699>) | 1699 | 1706 | jp 155 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾊﾟｰﾗ.ADV:339>) | 339 | 367 | group 28 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾊﾟｰﾗ.ADV:679>) | 679 | 2028 | group 62–107 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾊﾟｰﾗ.ADV:2422>) | 2422 | 2453 | group 144 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾊﾟｰﾗ.ADV:2473>) | 2473 | 2487 | group 148 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |

### 126. Gﾌﾘｰｸ.ADV

VI SHA-256: `9024f7392f01f305fc0c511df83ee895890c5dde4eee7430234a1246acc1aff6`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌﾘｰｸ.ADV:367>) | 367 | 414 | jp 51–59 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌﾘｰｸ.ADV:1718>) | 1718 | 1736 | jp 237 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌﾘｰｸ.ADV:461>) | 461 | 523 | group 46–52 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌﾘｰｸ.ADV:2174>) | 2174 | 2209 | group 218 | [editorial_review\size_order_123_127_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_123_127_20261023/coverage.json>) |

### 128. TJAPAN.ADV

VI SHA-256: `8e905e4b68236bd03b94d872b96872dfc852163f058ed3e0fd18b77dd370e4c5`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/TJAPAN.ADV:1102>) | 1102 | 1139 | jp 113–119 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/TJAPAN.ADV:1485>) | 1485 | 1972 | jp 169–224 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/TJAPAN.ADV:1433>) | 1433 | 1490 | group 111–117 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/TJAPAN.ADV:1966>) | 1966 | 2412 | group 166–191 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/TJAPAN.ADV:1978>) | 1978 | 2797 | group 167–222 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |

### 129. Gｳｪﾝﾃﾞｨ.ADV

VI SHA-256: `9fef7a2be8572372cab204fd3bd9bce56b55d36effafb79b75c788f5f084e6c0`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｳｪﾝﾃﾞｨ.ADV:25>) | 25 | 605 | jp 0–59 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｳｪﾝﾃﾞｨ.ADV:647>) | 647 | 674 | jp 63–65 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｳｪﾝﾃﾞｨ.ADV:765>) | 765 | 1215 | jp 80–132 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｳｪﾝﾃﾞｨ.ADV:1406>) | 1406 | 1419 | jp 161–163 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｳｪﾝﾃﾞｨ.ADV:1567>) | 1567 | 1827 | jp 189–210 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｳｪﾝﾃﾞｨ.ADV:26>) | 26 | 921 | group 0–59 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｳｪﾝﾃﾞｨ.ADV:987>) | 987 | 1035 | group 63–65 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｳｪﾝﾃﾞｨ.ADV:1156>) | 1156 | 1868 | group 80–133 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｳｪﾝﾃﾞｨ.ADV:2109>) | 2109 | 2130 | group 160–161 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｳｪﾝﾃﾞｨ.ADV:2327>) | 2327 | 2744 | group 187–208 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |

### 130. FIGT表示.ADV

VI SHA-256: `2b7eb2ad8bd89046725abf1608b749b961180b6845ea8821736215556491b608`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/FIGT表示.ADV:329>) | 329 | 386 | jp 5 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/FIGT表示.ADV:517>) | 517 | 616 | jp 9 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/FIGT表示.ADV:936>) | 936 | 1095 | jp 13 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/FIGT表示.ADV:1773>) | 1773 | 2086 | jp 18 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/FIGT表示.ADV:402>) | 402 | 468 | group 5 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/FIGT表示.ADV:616>) | 616 | 764 | group 9 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/FIGT表示.ADV:1172>) | 1172 | 1380 | group 13 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/FIGT表示.ADV:2249>) | 2249 | 2627 | group 20 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |

### 131. Gﾚﾍﾞｯｶ.ADV

VI SHA-256: `2775f4935e4714f8e3c45157a4c95c2cbc9ed394b85e7d8b072c2623e637032e`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾚﾍﾞｯｶ.ADV:22>) | 22 | 612 | jp 0–42 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾚﾍﾞｯｶ.ADV:735>) | 735 | 1429 | jp 59–143 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾚﾍﾞｯｶ.ADV:1478>) | 1478 | 1734 | jp 150–162 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾚﾍﾞｯｶ.ADV:23>) | 23 | 55 | group 0–2 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾚﾍﾞｯｶ.ADV:75>) | 75 | 957 | group 4–43 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾚﾍﾞｯｶ.ADV:1131>) | 1131 | 2245 | group 59–143 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾚﾍﾞｯｶ.ADV:2310>) | 2310 | 2728 | group 150–162 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |

### 132. Gｶﾁｭｰｼｬ.ADV

VI SHA-256: `88f6b210c9d173fd2d137a5b6917271286c6802d3ca893a56c534ff6b84084f4`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾁｭｰｼｬ.ADV:35>) | 35 | 1595 | jp 0–133 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾁｭｰｼｬ.ADV:1657>) | 1657 | 1664 | jp 141–142 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾁｭｰｼｬ.ADV:1748>) | 1748 | 1787 | jp 157–162 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾁｭｰｼｬ.ADV:36>) | 36 | 1550 | group 0–91 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾁｭｰｼｬ.ADV:1571>) | 1571 | 2528 | group 93–133 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾁｭｰｼｬ.ADV:2606>) | 2606 | 2618 | group 141–142 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾁｭｰｼｬ.ADV:2743>) | 2743 | 2801 | group 157–162 | [editorial_review\size_order_128_132_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_128_132_20261023/coverage.json>) |

### 133. Gﾐﾈﾊﾞ.ADV

VI SHA-256: `18b1e91ec766af6cbc5e510d997aaf52b0ca49398ff7824d0e16fd79b0ca4616`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾈﾊﾞ.ADV:759>) | 759 | 850 | jp 101–114 | [editorial_review\retranslate_jp_20261030_b48\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b48/coverage.json>); [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾈﾊﾞ.ADV:984>) | 984 | 1001 | jp 130–133 | [editorial_review\retranslate_jp_20261030_b48\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b48/coverage.json>); [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾈﾊﾞ.ADV:1133>) | 1133 | 1136 | jp 157 | [editorial_review\retranslate_jp_20261030_b48\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b48/coverage.json>); [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾈﾊﾞ.ADV:1061>) | 1061 | 1203 | group 95–108 | [editorial_review\retranslate_jp_20261030_b48\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b48/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾈﾊﾞ.ADV:1383>) | 1383 | 1416 | group 122–125 | [editorial_review\retranslate_jp_20261030_b48\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b48/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾈﾊﾞ.ADV:1583>) | 1583 | 1595 | group 145 | [editorial_review\retranslate_jp_20261030_b48\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b48/coverage.json>) |

### 134. Gﾌﾚｲｱ.ADV

VI SHA-256: `d1ad14fe70103ec5eb425dd37184a664b81408ba23306b456a2b93dca106dd9e`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌﾚｲｱ.ADV:1025>) | 1025 | 1373 | jp 145–169 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |

### 137. Gｶﾅﾐ.ADV

VI SHA-256: `592dbbcb377a388753ae0b6f48db92f071833d3793dcc13387534c7ee8dc63fb`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾅﾐ.ADV:192>) | 192 | 2034 | group 17–148 | [editorial_review\retranslate_jp_20261030_b54\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b54/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾅﾐ.ADV:2615>) | 2615 | 2920 | group 216–238 | [editorial_review\retranslate_jp_20261030_b54\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b54/coverage.json>) |

### 138. Gｼﾙｷｨ.ADV

VI SHA-256: `587bc991f9b7c312ce7e643ed46ceaebaeda3446fab5e02a5aac681091045789`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [VI](<D:/Download/Kichikuou Rance/src/Gｼﾙｷｨ.ADV:1630>) | 1630 | 1862 | group 135–137 | [editorial_review\retranslate_jp_20261030_b54\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b54/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｼﾙｷｨ.ADV:2995>) | 2995 | 3126 | group 241–256 | [editorial_review\retranslate_jp_20261030_b54\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b54/coverage.json>) |

### 139. Gｱｰﾔ.ADV

VI SHA-256: `9e43a28eefaad82df1f1d92f64451ab25e10f299b1689ab1982af511886a9495`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [VI](<D:/Download/Kichikuou Rance/src/Gｱｰﾔ.ADV:2491>) | 2491 | 2876 | group 243–244 | [editorial_review\retranslate_jp_20261030_b54\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b54/coverage.json>) |

### 140. Gｽｽﾞﾒ.ADV

VI SHA-256: `59d13f7a389e271fbf00b92651b887e20588c83efc3c31838b8dd0b8151c1236`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｽﾞﾒ.ADV:49>)~~ | ~~49~~ | ~~139~~ | ~~jp 0–15~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｽﾞﾒ.ADV:802>)~~ | ~~802~~ | ~~804~~ | ~~jp 70~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｽﾞﾒ.ADV:823>)~~ | ~~823~~ | ~~826~~ | ~~jp 74~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽｽﾞﾒ.ADV:847>)~~ | ~~847~~ | ~~918~~ | ~~jp 77–86~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｽｽﾞﾒ.ADV:50>)~~ | ~~50~~ | ~~174~~ | ~~group 0–15~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｽｽﾞﾒ.ADV:50>) | 50 | 2890 | group 0–195 | [editorial_review\retranslate_jp_20261030_b54\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b54/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｽｽﾞﾒ.ADV:1104>)~~ | ~~1104~~ | ~~1113~~ | ~~group 67~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｽｽﾞﾒ.ADV:1138>)~~ | ~~1138~~ | ~~1142~~ | ~~group 71~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｽｽﾞﾒ.ADV:1172>)~~ | ~~1172~~ | ~~1291~~ | ~~group 74–83~~ | ~~[editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>)~~ |

### 141. Gｹｲﾌﾞﾘｽ.ADV

VI SHA-256: `01fe8e7a37ac1325b9ed8cb81274cf5300603943c11e683d920c33dd0a4c9639`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｹｲﾌﾞﾘｽ.ADV:583>) | 583 | 978 | jp 55–115 | [editorial_review\retranslate_jp_20261030_b55\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b55/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｹｲﾌﾞﾘｽ.ADV:1954>) | 1954 | 1962 | jp 245 | [editorial_review\retranslate_jp_20261030_b55\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b55/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾘｽ.ADV:751>) | 751 | 1376 | group 51–105 | [editorial_review\retranslate_jp_20261030_b55\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b55/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｹｲﾌﾞﾘｽ.ADV:2814>) | 2814 | 2833 | group 228 | [editorial_review\retranslate_jp_20261030_b55\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b55/coverage.json>) |

### 142. Gｴﾚﾅ.ADV

VI SHA-256: `3ec5612ae27de72d4eb3c00651f1ce1f280b09384817ec6dbfec01df10ce731f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｴﾚﾅ.ADV:44>) | 44 | 150 | jp 0–15 | [editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｴﾚﾅ.ADV:45>) | 45 | 206 | group 0–15 | [editorial_review\size_order_133_142_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_133_142_tail_20261024/coverage.json>) |

### 144. Gﾒﾘﾑ.ADV

VI SHA-256: `b1c1e71b85091229d3cbb6e36f2f0aa2089be9d101732c6b1169da65aed47907`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾘﾑ.ADV:37>) | 37 | 113 | jp 0–13 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾘﾑ.ADV:335>) | 335 | 361 | jp 40–45 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾘﾑ.ADV:438>) | 438 | 485 | jp 58 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾘﾑ.ADV:38>) | 38 | 161 | group 0–13 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾘﾑ.ADV:492>) | 492 | 531 | group 40–45 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾘﾑ.ADV:639>) | 639 | 713 | group 57 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |

### 145. Gﾊﾟｲｱｰﾙ.ADV

VI SHA-256: `58f51e6a83763d1abb4189031163831682256d19cef9e428ae809d4e20b93c8a`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟｲｱｰﾙ.ADV:133>) | 133 | 134 | jp 14 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟｲｱｰﾙ.ADV:168>) | 168 | 169 | jp 18 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |

### 146. Gｱﾆｽ.ADV

VI SHA-256: `3efcbafeb52aff99b12791bbbe8edad492403209a3336f57dd3b5f14e3948c2c`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾆｽ.ADV:39>) | 39 | 54 | jp 0–1 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾆｽ.ADV:188>) | 188 | 190 | jp 23 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾆｽ.ADV:40>) | 40 | 66 | group 0 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾆｽ.ADV:272>) | 272 | 279 | group 22 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |

### 147. Gｼｰﾗ.ADV

VI SHA-256: `8e075bde0c78661053867e74d06383bf97bf0373d1dab6f6f1539943e2f4fc69`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｰﾗ.ADV:166>) | 166 | 203 | jp 12 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>); [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｰﾗ.ADV:314>) | 314 | 1030 | jp 26–94 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｰﾗ.ADV:1280>) | 1280 | 1986 | jp 136–202 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｼｰﾗ.ADV:230>) | 230 | 294 | group 11 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |

### 148. Gﾗﾌｧﾘｱ.ADV

VI SHA-256: `d7861dd5fbb7085d58c27d5a9822e921f91d2c69fcac3b4626bba5616c537b4f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾌｧﾘｱ.ADV:31>) | 31 | 257 | jp 0–13 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾗﾌｧﾘｱ.ADV:297>) | 297 | 326 | jp 19–22 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾌｧﾘｱ.ADV:32>) | 32 | 433 | group 0–13 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾗﾌｧﾘｱ.ADV:491>) | 491 | 545 | group 19–21 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) |

### 149. CG.ADV

VI SHA-256: `98af0f585b14eadc482841e90267d7f8cf1a01d0d6c4ba36d12bd1b10aae3185`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/CG.ADV:2342>)~~ | ~~2342~~ | ~~2551~~ | ~~jp 8–10~~ | ~~[editorial_review\retranslate_jp_20261030_b58\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b58/coverage.json>); [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/CG.ADV:2352>)~~ | ~~2352~~ | ~~2938~~ | ~~group 8–10~~ | ~~[editorial_review\retranslate_jp_20261030_b58\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b58/coverage.json>); [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>)~~ |

### 150. Gｽﾃｯｾﾙ.ADV

VI SHA-256: `87f8368b4e377687c2c6d3d3b8ef314640bb1dfc3a83c05423245423abd7ba4c`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽﾃｯｾﾙ.ADV:1134>) | 1134 | 1287 | jp 135 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽﾃｯｾﾙ.ADV:1380>) | 1380 | 2131 | jp 145–243 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｽﾃｯｾﾙ.ADV:2231>) | 2231 | 2240 | jp 255 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |

### 151. Gｻｲｾﾞﾙ.ADV

VI SHA-256: `f320b2459d10f6373457aa038ee3c1840fea688c0075360bd61f1731df0bf74c`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:109>) | 109 | 112 | jp 10 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:146>) | 146 | 152 | jp 17–18 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:503>) | 503 | 514 | jp 65–66 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:554>) | 554 | 560 | jp 73–74 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:766>) | 766 | 772 | jp 106 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:801>) | 801 | 806 | jp 112 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:963>) | 963 | 1064 | jp 134–152 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:1130>) | 1130 | 1155 | jp 162–165 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:1206>) | 1206 | 1281 | jp 168–176 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:1366>) | 1366 | 1398 | jp 180–186 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:1735>) | 1735 | 1931 | jp 244–264 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:2092>) | 2092 | 2118 | jp 277 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻｲｾﾞﾙ.ADV:2143>) | 2143 | 2155 | jp 280–281 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:120>) | 120 | 124 | group 8 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:168>) | 168 | 177 | group 15–16 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:606>) | 606 | 632 | group 58–59 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:676>) | 676 | 685 | group 64–65 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:971>) | 971 | 993 | group 93 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:1035>) | 1035 | 1044 | group 99 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:1249>) | 1249 | 1417 | group 118–133 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:1496>) | 1496 | 1541 | group 141–144 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:1602>) | 1602 | 1706 | group 147–155 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:1826>) | 1826 | 1869 | group 158–163 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:2315>) | 2315 | 2568 | group 217–231 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:2800>) | 2800 | 2841 | group 243 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｻｲｾﾞﾙ.ADV:2873>) | 2873 | 2889 | group 246 | [editorial_review\retranslate_jp_20261030_b59\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b59/coverage.json>) |

### 152. Gﾏﾘｽ.ADV

VI SHA-256: `187b24c1e8488f37b2d69480920cecf8dc9794dfa39529187a1e84f5bd23450c`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏﾘｽ.ADV:2152>) | 2152 | 2358 | group 199 | [editorial_review\adult_hscenes_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/adult_hscenes_20261022/scope.json>) |

### 153. Gｶｾｲ.ADV

VI SHA-256: `9bc4d55ebc4a2ae63faaf9e0166eedc2c9f59b822b8ca793340ea90eb0cdc537`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶｾｲ.ADV:951>) | 951 | 953 | jp 154 | [editorial_review\retranslate_jp_20261030_b60\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b60/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶｾｲ.ADV:985>) | 985 | 992 | jp 160 | [editorial_review\retranslate_jp_20261030_b60\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b60/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶｾｲ.ADV:1802>) | 1802 | 1810 | jp 269–270 | [editorial_review\retranslate_jp_20261030_b60\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b60/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶｾｲ.ADV:1329>) | 1329 | 1333 | group 148 | [editorial_review\retranslate_jp_20261030_b60\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b60/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶｾｲ.ADV:1377>) | 1377 | 1396 | group 154 | [editorial_review\retranslate_jp_20261030_b60\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b60/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶｾｲ.ADV:2448>) | 2448 | 2469 | group 244–245 | [editorial_review\retranslate_jp_20261030_b60\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b60/coverage.json>) |

### 154. Gﾎﾗｶﾞ.ADV

VI SHA-256: `a9d3e03e49cdb4c84dbe766d248b7368ac58dbe576a10a3a2475f0fd9ce09dd3`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾎﾗｶﾞ.ADV:32>) | 32 | 72 | jp 0–2 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾎﾗｶﾞ.ADV:320>) | 320 | 346 | jp 26–30 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾎﾗｶﾞ.ADV:33>) | 33 | 102 | group 0–2 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾎﾗｶﾞ.ADV:461>) | 461 | 505 | group 25–29 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |

### 155. G2.ADV

VI SHA-256: `31f79e49eb338c1c8b553c2573c764a625cf111d16a3b35dec08a0d93f4b82ae`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/G2.ADV:59>) | 59 | 529 | jp 0–44 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/G2.ADV:743>) | 743 | 1144 | jp 50–70 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/G2.ADV:60>) | 60 | 791 | group 0–39 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/G2.ADV:1173>) | 1173 | 1857 | group 45–61 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |

### 156. Gｿｳﾙ.ADV

VI SHA-256: `c5546391b00783526b46a5eb656028152ff86e99188a1c21c3c3a3fdab15648c`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｿｳﾙ.ADV:147>)~~ | ~~147~~ | ~~296~~ | ~~jp 8–32~~ | ~~[editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｿｳﾙ.ADV:178>)~~ | ~~178~~ | ~~393~~ | ~~group 8–31~~ | ~~[editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>)~~ |

### 157. Gﾐﾘ.ADV

VI SHA-256: `224c89529fd81062696429cedae752b73fdcad1dedf84e654a8304a28e70f8f1`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾘ.ADV:54>) | 54 | 589 | jp 0–37 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾘ.ADV:1040>) | 1040 | 1041 | jp 107 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾘ.ADV:1129>) | 1129 | 1130 | jp 120 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐﾘ.ADV:1193>) | 1193 | 1196 | jp 129 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾘ.ADV:55>) | 55 | 870 | group 0–36 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾘ.ADV:1491>) | 1491 | 1493 | group 106 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾘ.ADV:1612>) | 1612 | 1614 | group 119 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐﾘ.ADV:1703>) | 1703 | 1708 | group 128 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |

### 158. Gﾏﾙﾁﾅ.ADV

VI SHA-256: `bbab3dc7251fefaa2ca2c967fff06d2a72ce4a22477936df9c71e67ff5a69e4b`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏﾙﾁﾅ.ADV:28>) | 28 | 356 | jp 0–49 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏﾙﾁﾅ.ADV:488>) | 488 | 695 | jp 69–94 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏﾙﾁﾅ.ADV:29>) | 29 | 530 | group 0–42 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾏﾙﾁﾅ.ADV:717>) | 717 | 992 | group 62–85 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |

### 159. Gﾚｨﾘｨ.ADV

VI SHA-256: `9818862dfca91629b4e252c61c05098a24a6805bdf2a5afacfd4955233aa8f2e`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾚｨﾘｨ.ADV:34>) | 34 | 336 | jp 0–44 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾚｨﾘｨ.ADV:35>) | 35 | 473 | group 0–44 | [editorial_review\size_order_153_162_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_153_162_tail_20261024/coverage.json>) |

### 161. Gﾙｰﾍﾞﾗﾝ.ADV

VI SHA-256: `6c2e1661c126bd31ac8bfc8a417a0a6e94167120caf2e1462571f3b4754497e3`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾙｰﾍﾞﾗﾝ.ADV:345>) | 345 | 562 | jp 47–76 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾙｰﾍﾞﾗﾝ.ADV:750>) | 750 | 2138 | jp 94–185 | [editorial_review\through_helman_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/through_helman_20261022/scope.json>) |

### 163. Gｼｽﾞｶ.ADV

VI SHA-256: `9b5f1ffed7f1ce3810fa82eaac11a0cb0c292baa5120c880e8a581454ad78277`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｽﾞｶ.ADV:56>) | 56 | 683 | jp 0–54 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｼｽﾞｶ.ADV:57>) | 57 | 1129 | group 0–51 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |

### 164. Gﾘｱ.ADV

VI SHA-256: `4753cf09efb382f1a149e48a8889eaf8cf3ec0425ce032799a4aeb68f15df678`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾘｱ.ADV:45>) | 45 | 893 | jp 0–54 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾘｱ.ADV:46>) | 46 | 1313 | group 0–54 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |

### 165. Cﾃｷﾄｼ.ADV

VI SHA-256: `263faa3cb0e6d663a2515956d3f4b9a423612ceec5f6401a2b2a83e749ac0bc3`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [VI](<D:/Download/Kichikuou Rance/src/Cﾃｷﾄｼ.ADV:2683>) | 2683 | 2692 | group 242 | [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Cﾃｷﾄｼ.ADV:3218>) | 3218 | 3260 | group 299–305 | [editorial_review\retranslate_priority_20261029_b32\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b32/coverage.json>) |

### 166. Gｱｰﾙｺｰﾄ.ADV

VI SHA-256: `1e88329e1ac1f9b4316d733ed0cfe83e461b923aab89df2af068283f90589ff6`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱｰﾙｺｰﾄ.ADV:57>) | 57 | 583 | jp 0–54 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱｰﾙｺｰﾄ.ADV:58>) | 58 | 885 | group 0–53 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |

### 167. Gﾒﾙﾌｪｲｽ.ADV

VI SHA-256: `a670c82c444836d0821075e18c459fae42385b8e640d0037b3a155e49b5fab2a`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾙﾌｪｲｽ.ADV:210>) | 210 | 337 | jp 26–48 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾙﾌｪｲｽ.ADV:271>) | 271 | 469 | group 26–48 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |

### 168. Gﾊｳﾚｰﾝ.ADV

VI SHA-256: `fae1c14486251729c5b287087e21b3d01c789881e68ac947d82f00fecc9d3136`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊｳﾚｰﾝ.ADV:1200>)~~ | ~~1200~~ | ~~1215~~ | ~~group 112~~ | ~~[editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊｳﾚｰﾝ.ADV:1408>)~~ | ~~1408~~ | ~~2201~~ | ~~group 132–187~~ | ~~[editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊｳﾚｰﾝ.ADV:2518>)~~ | ~~2518~~ | ~~2537~~ | ~~group 221–222~~ | ~~[editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊｳﾚｰﾝ.ADV:2751>)~~ | ~~2751~~ | ~~4220~~ | ~~group 238–323~~ | ~~[editorial_review\retranslate_jp_20261030_b36\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b36/coverage.json>)~~ |

### 169. Gｺｳﾋﾒ.ADV

VI SHA-256: `15e57b3e8dfb08a2df70aa80a531d17e6c2cda2712d17cbfdc4c21fdff5f21ef`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｺｳﾋﾒ.ADV:232>) | 232 | 332 | jp 30–44 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｺｳﾋﾒ.ADV:319>) | 319 | 501 | group 30–44 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |

### 171. Gﾜｰｸﾞ.ADV

VI SHA-256: `d3d43c720caebdd1b6f5654f50c2cf8f709ee35d9c79207fb1c073e0d882ed31`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾜｰｸﾞ.ADV:249>) | 249 | 407 | jp 16–44 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾜｰｸﾞ.ADV:335>) | 335 | 570 | group 16–44 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |

### 172. Iｼﾚｲﾌﾞ.ADV

VI SHA-256: `49c8a65c5444bd51c5a95be378dc3aad66ca6f55b716c7cf0d70bfdd4da1abd9`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:108>) | 108 | 116 | jp 8 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:778>) | 778 | 785 | jp 84 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\main_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/main_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:1197>) | 1197 | 1251 | jp 144–153 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:1220>) | 1220 | 1225 | jp 148–149 | [editorial_review\main_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/main_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:1461>) | 1461 | 1467 | jp 174 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\main_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/main_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:2312>) | 2312 | 2397 | jp 270–283 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:2443>) | 2443 | 2444 | jp 289 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:2649>) | 2649 | 2788 | jp 322–339 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:2730>) | 2730 | 2788 | jp 332–339 | [editorial_review\main_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/main_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:2983>) | 2983 | 3025 | jp 367–375 | [editorial_review\main_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/main_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:3006>) | 3006 | 3025 | jp 372–375 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:3151>) | 3151 | 3160 | jp 390–391 | [editorial_review\main_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/main_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼﾚｲﾌﾞ.ADV:3151>) | 3151 | 3164 | jp 390–392 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:121>) | 121 | 139 | group 7 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:1076>) | 1076 | 1097 | group 82 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:1654>) | 1654 | 1727 | group 140–149 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:2061>) | 2061 | 2070 | group 170 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:3307>) | 3307 | 3429 | group 265–278 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:3393>) | 3393 | 3429 | group 274–278 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:3488>) | 3488 | 3490 | group 284 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:3776>) | 3776 | 3990 | group 317–334 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:3950>) | 3950 | 3990 | group 330–334 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:4292>) | 4292 | 4326 | group 367–370 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:4509>) | 4509 | 4529 | group 385–387 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼﾚｲﾌﾞ.ADV:4592>) | 4592 | 4612 | group 393–395 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |

### 173. Gﾌｳｶ.ADV

VI SHA-256: `e2d2f31d32b6c0d63b718995d575f3bf6ab8926053d456e8140c57279202f087`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:84>) | 84 | 85 | jp 2 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:156>) | 156 | 412 | jp 12–54 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:244>) | 244 | 253 | jp 28 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:369>) | 369 | 374 | jp 46 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:513>) | 513 | 515 | jp 69 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:569>) | 569 | 581 | jp 80–83 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:629>) | 629 | 656 | jp 92–96 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:669>) | 669 | 675 | jp 99 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:872>) | 872 | 882 | jp 130 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:1064>) | 1064 | 1525 | jp 156–229 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:1756>) | 1756 | 1761 | jp 265 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾌｳｶ.ADV:2753>) | 2753 | 3110 | jp 409–455 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:85>) | 85 | 89 | group 1 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b29\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b29/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:195>) | 195 | 591 | group 11–50 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:319>) | 319 | 346 | group 26 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b29\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b29/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:534>) | 534 | 543 | group 44 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b29\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b29/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:716>) | 716 | 726 | group 64 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b30\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b30/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:814>) | 814 | 831 | group 75–78 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b30\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b30/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:898>) | 898 | 937 | group 87–90 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b30\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b30/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:956>) | 956 | 967 | group 93 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b30\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b30/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:1256>) | 1256 | 1275 | group 123 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b30\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b30/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:1514>) | 1514 | 2160 | group 146–213 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:2476>) | 2476 | 2485 | group 248 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾌｳｶ.ADV:3877>) | 3877 | 4430 | group 365–410 | [editorial_review\fuuka_full_ordinary_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/fuuka_full_ordinary_20261024/coverage.json>); [editorial_review\retranslate_jp_20261030_b35\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b35/coverage.json>) |

### 174. Gﾒﾅﾄﾞ.ADV

VI SHA-256: `3bde7ed35306a634bb7d8c82e39ae8c47da7e7eb4bf1fc4d94cc46fae17e267f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾅﾄﾞ.ADV:67>) | 67 | 629 | jp 0–67 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾒﾅﾄﾞ.ADV:683>) | 683 | 688 | jp 73 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:68>) | 68 | 935 | group 0–66 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:194>) | 194 | 520 | group 14–39 | [editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:711>) | 711 | 935 | group 63–66 | [editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:1005>) | 1005 | 1014 | group 72 | [editorial_review\size_order_163_174_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_163_174_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:1229>) | 1229 | 1245 | group 96 | [editorial_review\retranslate_jp_20261029_b28\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b28/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:1726>) | 1726 | 1911 | group 156–174 | [editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:2296>) | 2296 | 2305 | group 217 | [editorial_review\retranslate_jp_20261029_b29\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b29/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:2334>) | 2334 | 2336 | group 221 | [editorial_review\retranslate_jp_20261029_b29\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b29/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:2346>) | 2346 | 2360 | group 223 | [editorial_review\retranslate_jp_20261029_b29\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b29/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:2861>) | 2861 | 2872 | group 282–283 | [editorial_review\retranslate_jp_20261029_b29\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b29/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:3330>) | 3330 | 3428 | group 337–347 | [editorial_review\retranslate_jp_20261029_b30\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b30/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:3641>) | 3641 | 3668 | group 372–375 | [editorial_review\retranslate_jp_20261029_b30\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b30/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾒﾅﾄﾞ.ADV:3730>) | 3730 | 5340 | group 380–482 | [editorial_review\retranslate_jp_20261029_b31\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b31/coverage.json>) |

### 175. Gｶﾞﾝｼﾞｰ.ADV

VI SHA-256: `529aee4837f7f1a6d76fd3a8b671f791b85c156b783b388ea90dadb1164066ff`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾞﾝｼﾞｰ.ADV:191>)~~ | ~~191~~ | ~~317~~ | ~~jp 24–43~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾞﾝｼﾞｰ.ADV:388>)~~ | ~~388~~ | ~~500~~ | ~~jp 52–69~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾞﾝｼﾞｰ.ADV:242>)~~ | ~~242~~ | ~~423~~ | ~~group 23–41~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾞﾝｼﾞｰ.ADV:546>)~~ | ~~546~~ | ~~711~~ | ~~group 50–65~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |

### 176. Iｼｬﾝｸﾞﾘﾗ.ADV

VI SHA-256: `6f72fc2764859bc7cf48cbe0addb2d77319786f124f2f4a59b7de5d7b79e5107`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:147>) | 147 | 259 | jp 17–28 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\shangrila_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/shangrila_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:414>) | 414 | 435 | jp 50–54 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\shangrila_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/shangrila_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:1477>) | 1477 | 1508 | jp 187–193 | [editorial_review\shangrila_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/shangrila_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:1477>) | 1477 | 1527 | jp 187–195 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:1550>) | 1550 | 1555 | jp 199 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:1550>) | 1550 | 1607 | jp 199–202 | [editorial_review\shangrila_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/shangrila_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:1570>) | 1570 | 1607 | jp 201–202 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:1757>) | 1757 | 1806 | jp 219–228 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\shangrila_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/shangrila_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:2294>) | 2294 | 2368 | jp 264–277 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｼｬﾝｸﾞﾘﾗ.ADV:2299>) | 2299 | 2345 | jp 265–272 | [editorial_review\shangrila_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/shangrila_20261022/scope.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼｬﾝｸﾞﾘﾗ.ADV:198>) | 198 | 366 | group 17–28 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼｬﾝｸﾞﾘﾗ.ADV:576>) | 576 | 609 | group 50–54 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼｬﾝｸﾞﾘﾗ.ADV:2049>) | 2049 | 2116 | group 187–195 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼｬﾝｸﾞﾘﾗ.ADV:2146>) | 2146 | 2153 | group 199 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼｬﾝｸﾞﾘﾗ.ADV:2173>) | 2173 | 2237 | group 201–202 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼｬﾝｸﾞﾘﾗ.ADV:2435>) | 2435 | 2500 | group 219–228 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｼｬﾝｸﾞﾘﾗ.ADV:3133>) | 3133 | 3248 | group 263–276 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |

### 177. Gｱﾘｽ2.ADV

VI SHA-256: `fc65c7ac7924bc28b592b3beb6667335c0262109abacdf236eb3a6a355032fff`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ2.ADV:1874>) | 1874 | 1887 | group 194–195 | [editorial_review\retranslate_jp_20261029_b25\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b25/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ2.ADV:2131>) | 2131 | 2861 | group 219–253 | [editorial_review\retranslate_jp_20261029_b25\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b25/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ2.ADV:3047>)~~ | ~~3047~~ | ~~3906~~ | ~~group 276–332~~ | ~~[editorial_review\retranslate_jp_20261029_b27\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b27/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ2.ADV:4258>)~~ | ~~4258~~ | ~~4888~~ | ~~group 375–400~~ | ~~[editorial_review\retranslate_jp_20261029_b27\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b27/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ2.ADV:5133>)~~ | ~~5133~~ | ~~5177~~ | ~~group 430–431~~ | ~~[editorial_review\retranslate_jp_20261029_b27\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b27/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ2.ADV:5239>)~~ | ~~5239~~ | ~~5272~~ | ~~group 437–438~~ | ~~[editorial_review\retranslate_jp_20261029_b27\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b27/coverage.json>)~~ |

### 179. Gｶﾐｰﾗ.ADV

VI SHA-256: `5358c2a68d53440f5d890a6e7a74a37be30ff250c7b876ee6f02f1ff60a54f4d`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾐｰﾗ.ADV:42>) | 42 | 828 | jp 0–82 | [editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾐｰﾗ.ADV:185>) | 185 | 207 | jp 23–25 | [editorial_review\retranslate_jp_20261030_b46\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b46/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾐｰﾗ.ADV:359>) | 359 | 596 | jp 47 | [editorial_review\retranslate_jp_20261030_b46\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b46/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾐｰﾗ.ADV:43>) | 43 | 1190 | group 0–78 | [editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾐｰﾗ.ADV:112>)~~ | ~~112~~ | ~~233~~ | ~~group 7–21~~ | ~~[editorial_review\retranslate_jp_20261029_b20\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b20/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾐｰﾗ.ADV:238>) | 238 | 275 | group 22–24 | [editorial_review\retranslate_jp_20261029_b20\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b20/coverage.json>); [editorial_review\retranslate_jp_20261030_b46\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b46/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾐｰﾗ.ADV:280>)~~ | ~~280~~ | ~~466~~ | ~~group 25–44~~ | ~~[editorial_review\retranslate_jp_20261029_b20\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b20/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾐｰﾗ.ADV:471>) | 471 | 880 | group 45 | [editorial_review\retranslate_jp_20261029_b20\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b20/coverage.json>); [editorial_review\retranslate_jp_20261030_b46\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b46/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾐｰﾗ.ADV:896>)~~ | ~~896~~ | ~~1190~~ | ~~group 46–78~~ | ~~[editorial_review\retranslate_jp_20261029_b20\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b20/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾐｰﾗ.ADV:3159>) | 3159 | 3761 | group 251–263 | [editorial_review\retranslate_jp_20261029_b20\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b20/coverage.json>) |

### 180. Gｻﾃﾗ.ADV

VI SHA-256: `19fdc0a721e828e930d5574099784eacc2671bf3f48d1b4e566d4b398a3debea`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻﾃﾗ.ADV:183>)~~ | ~~183~~ | ~~1470~~ | ~~jp 14–104~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｻﾃﾗ.ADV:1932>)~~ | ~~1932~~ | ~~2108~~ | ~~jp 165–192~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:227>)~~ | ~~227~~ | ~~1941~~ | ~~group 14–98~~ | ~~[editorial_review\retranslate_jp_20261029_b19\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b19/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:227>)~~ | ~~227~~ | ~~2115~~ | ~~group 14–102~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:2720>)~~ | ~~2720~~ | ~~2962~~ | ~~group 160–185~~ | ~~[editorial_review\size_order_175_180_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_175_180_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:2852>)~~ | ~~2852~~ | ~~2908~~ | ~~group 172–178~~ | ~~[editorial_review\retranslate_jp_20261029_b19\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b19/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:3091>)~~ | ~~3091~~ | ~~3637~~ | ~~group 199–253~~ | ~~[editorial_review\retranslate_jp_20261029_b19\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b19/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:3807>)~~ | ~~3807~~ | ~~3829~~ | ~~group 271–273~~ | ~~[editorial_review\retranslate_jp_20261029_b19\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b19/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:4318>)~~ | ~~4318~~ | ~~4322~~ | ~~group 318~~ | ~~[editorial_review\retranslate_jp_20261029_b19\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b19/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｻﾃﾗ.ADV:5254>)~~ | ~~5254~~ | ~~5371~~ | ~~group 416~~ | ~~[editorial_review\retranslate_jp_20261029_b19\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261029_b19/coverage.json>)~~ |

### 181. Gﾐｷ.ADV

VI SHA-256: `b623927030cad9ce71747d410a290afd7a7179aa33cceb5ca9f88a4f7b38a5eb`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐｷ.ADV:735>) | 735 | 882 | jp 94–115 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐｷ.ADV:735>) | 735 | 1455 | jp 94–190 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐｷ.ADV:1543>) | 1543 | 1590 | jp 203–210 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐｷ.ADV:2705>) | 2705 | 3571 | jp 354–458 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐｷ.ADV:3947>) | 3947 | 3971 | jp 515–519 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐｷ.ADV:4078>) | 4078 | 4081 | jp 535 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾐｷ.ADV:4243>) | 4243 | 4310 | jp 558–569 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐｷ.ADV:982>) | 982 | 1962 | group 88–174 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐｷ.ADV:2074>) | 2074 | 2146 | group 186–193 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐｷ.ADV:3649>) | 3649 | 4900 | group 322–418 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐｷ.ADV:5399>) | 5399 | 5434 | group 471–475 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐｷ.ADV:5559>) | 5559 | 5564 | group 490 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾐｷ.ADV:5754>) | 5754 | 5848 | group 512–520 | [editorial_review\retranslate_jp_20261030_b63\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261030_b63/coverage.json>) |

### 183. Gｶﾗｰ.ADV

VI SHA-256: `3d9c94ad66856e2a35591f396dc10b6c8f57b44d3c0b58c17a02ecfc3fc63558`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾗｰ.ADV:870>) | 870 | 962 | jp 132–146 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:277>) | 277 | 303 | group 21–24 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:348>) | 348 | 361 | group 28 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>); [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:1143>) | 1143 | 1324 | group 125–138 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:1143>) | 1143 | 1949 | group 125–175 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:2120>) | 2120 | 2141 | group 201–203 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:2321>) | 2321 | 2422 | group 221–231 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:2491>) | 2491 | 2495 | group 240 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:3055>) | 3055 | 3064 | group 297 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:3108>) | 3108 | 3381 | group 301–326 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:3417>)~~ | ~~3417~~ | ~~3483~~ | ~~group 331–336~~ | ~~[editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:3547>) | 3547 | 3946 | group 345–361 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:4029>)~~ | ~~4029~~ | ~~4170~~ | ~~group 371–381~~ | ~~[editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｶﾗｰ.ADV:4319>) | 4319 | 5809 | group 399–490 | [editorial_review\retranslate_jp_20261028_b17\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b17/coverage.json>) |

### 184. Gﾁｽﾞｺ.ADV

VI SHA-256: `b46818c8b496a8fd8fd69d763b103ff8f498d98875d466e805d0fca35d13efb1`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾁｽﾞｺ.ADV:496>)~~ | ~~496~~ | ~~754~~ | ~~jp 58–98~~ | ~~[editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾁｽﾞｺ.ADV:717>)~~ | ~~717~~ | ~~1115~~ | ~~group 58–98~~ | ~~[editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>)~~ |

### 185. Gﾏﾘｱ.ADV

VI SHA-256: `c06e005da89dbd06db3525f1b814459b43d67ee675bb7a9989638fa529163c1f`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏﾘｱ.ADV:172>)~~ | ~~172~~ | ~~261~~ | ~~jp 13–23~~ | ~~[editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏﾘｱ.ADV:441>)~~ | ~~441~~ | ~~1282~~ | ~~jp 53–164~~ | ~~[editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏﾘｱ.ADV:204>)~~ | ~~204~~ | ~~334~~ | ~~group 13–23~~ | ~~[editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏﾘｱ.ADV:569>)~~ | ~~569~~ | ~~1784~~ | ~~group 53–163~~ | ~~[editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>)~~ |

### 186. Gｲｿﾛｸ.ADV

VI SHA-256: `67964b455979bbef75eff722750d67fb179bbed8757ef8bf03b078c0e210f7fe`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｲｿﾛｸ.ADV:670>)~~ | ~~670~~ | ~~674~~ | ~~jp 112–113~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｲｿﾛｸ.ADV:989>)~~ | ~~989~~ | ~~998~~ | ~~group 112–113~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |

### 187. Gｾﾙ.ADV

VI SHA-256: `cf518c46f3a39860193819f87109341ec89c155f84121406d058d9382f247443`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｾﾙ.ADV:325>)~~ | ~~325~~ | ~~641~~ | ~~jp 43–83~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｾﾙ.ADV:674>)~~ | ~~674~~ | ~~676~~ | ~~jp 87~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｾﾙ.ADV:719>)~~ | ~~719~~ | ~~731~~ | ~~jp 95–96~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｾﾙ.ADV:839>)~~ | ~~839~~ | ~~846~~ | ~~jp 112~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｾﾙ.ADV:999>)~~ | ~~999~~ | ~~1001~~ | ~~jp 138~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｾﾙ.ADV:1080>)~~ | ~~1080~~ | ~~1128~~ | ~~jp 149–159~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｾﾙ.ADV:404>)~~ | ~~404~~ | ~~834~~ | ~~group 36–68~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｾﾙ.ADV:875>)~~ | ~~875~~ | ~~879~~ | ~~group 72~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｾﾙ.ADV:937>)~~ | ~~937~~ | ~~953~~ | ~~group 80–81~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｾﾙ.ADV:1096>)~~ | ~~1096~~ | ~~1109~~ | ~~group 96~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｾﾙ.ADV:1300>)~~ | ~~1300~~ | ~~1304~~ | ~~group 119~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｾﾙ.ADV:1426>)~~ | ~~1426~~ | ~~1528~~ | ~~group 128–138~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |

### 188. Iｶﾐ.ADV

VI SHA-256: `b2241a15f650b2c0cf6a46c36e00d2494874c9683a7d609e1ea79dd8c33c4ce0`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｶﾐ.ADV:768>) | 768 | 908 | jp 96 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｶﾐ.ADV:1140>) | 1140 | 1270 | jp 99 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｶﾐ.ADV:2255>) | 2255 | 2268 | jp 195 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｶﾐ.ADV:2871>) | 2871 | 2922 | jp 285 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｶﾐ.ADV:3837>) | 3837 | 3839 | jp 370 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｶﾐ.ADV:1025>) | 1025 | 1266 | group 91 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｶﾐ.ADV:1609>) | 1609 | 1919 | group 95 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｶﾐ.ADV:3278>) | 3278 | 3304 | group 184 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｶﾐ.ADV:4106>) | 4106 | 4195 | group 266 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｶﾐ.ADV:5341>) | 5341 | 5350 | group 347 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |

### 189. Gｱﾋﾞｧﾄｰﾙ.ADV

VI SHA-256: `9ac2e2cb497d0950710fe9177d063031e8e1b9e6e1e580420e1105f18b7bdddf`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾋﾞｧﾄｰﾙ.ADV:134>)~~ | ~~134~~ | ~~176~~ | ~~jp 14–19~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾋﾞｧﾄｰﾙ.ADV:330>)~~ | ~~330~~ | ~~332~~ | ~~jp 40~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾋﾞｧﾄｰﾙ.ADV:451>)~~ | ~~451~~ | ~~485~~ | ~~jp 55–60~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾋﾞｧﾄｰﾙ.ADV:747>) | 747 | 756 | jp 99 | [editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:183>)~~ | ~~183~~ | ~~255~~ | ~~group 13–16~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:469>)~~ | ~~469~~ | ~~473~~ | ~~group 37~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:673>)~~ | ~~673~~ | ~~731~~ | ~~group 52–57~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:1085>) | 1085 | 1100 | group 92 | [editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:1225>) | 1225 | 1245 | group 101 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:1976>) | 1976 | 1980 | group 156 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:2747>) | 2747 | 3084 | group 219–229 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:3111>) | 3111 | 3115 | group 232 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:3190>) | 3190 | 3192 | group 239 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:3216>) | 3216 | 3225 | group 241 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:3556>) | 3556 | 3563 | group 268 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:3587>) | 3587 | 3596 | group 270 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:4001>) | 4001 | 4062 | group 308–312 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:4077>) | 4077 | 4081 | group 314 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:4323>) | 4323 | 4333 | group 336 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:5313>) | 5313 | 5326 | group 416 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:5490>) | 5490 | 5494 | group 432 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:5982>) | 5982 | 5984 | group 481 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:6405>) | 6405 | 6409 | group 516 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:6786>) | 6786 | 6800 | group 547 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾋﾞｧﾄｰﾙ.ADV:6910>) | 6910 | 6949 | group 558–563 | [editorial_review\retranslate_jp_20261028_b12\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b12/coverage.json>) |

### 190. Iｾﾞｽ.ADV

VI SHA-256: `c7a9f4d7e3d8ffdad41137ea9b318e34f5d08e1d9f85572d4c92a83d7c649eb8`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iｾﾞｽ.ADV:4184>) | 4184 | 4787 | jp 510–578 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｾﾞｽ.ADV:5869>) | 5869 | 6336 | group 500–522 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｾﾞｽ.ADV:5906>) | 5906 | 6832 | group 504–572 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｾﾞｽ.ADV:6473>) | 6473 | 6489 | group 535 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｾﾞｽ.ADV:6636>) | 6636 | 6685 | group 552–554 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iｾﾞｽ.ADV:6808>) | 6808 | 6815 | group 569 | [editorial_review\retranslate_priority_20261029_b33\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_priority_20261029_b33/coverage.json>) |

### 191. Gﾚｲﾗ.ADV

VI SHA-256: `ee8529d94825798642d3ca4803fd6ea7ced0987075cb8f9527c13005c5fc8b4a`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾚｲﾗ.ADV:1001>)~~ | ~~1001~~ | ~~1131~~ | ~~jp 151–174~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾚｲﾗ.ADV:1437>)~~ | ~~1437~~ | ~~1644~~ | ~~group 150–173~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |

### 192. Gﾏｼﾞｯｸ.ADV

VI SHA-256: `b26f5ce10f3f44f76fc8aa6f6ff4fca35ede967919e43e4fa6f114c3910a99d9`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｼﾞｯｸ.ADV:123>)~~ | ~~123~~ | ~~126~~ | ~~jp 6~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｼﾞｯｸ.ADV:175>)~~ | ~~175~~ | ~~178~~ | ~~jp 10~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｼﾞｯｸ.ADV:307>)~~ | ~~307~~ | ~~310~~ | ~~jp 20~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｼﾞｯｸ.ADV:396>)~~ | ~~396~~ | ~~399~~ | ~~jp 27~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｼﾞｯｸ.ADV:437>)~~ | ~~437~~ | ~~440~~ | ~~jp 30~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｼﾞｯｸ.ADV:622>)~~ | ~~622~~ | ~~644~~ | ~~jp 54–56~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾏｼﾞｯｸ.ADV:776>)~~ | ~~776~~ | ~~961~~ | ~~jp 74–102~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｼﾞｯｸ.ADV:149>)~~ | ~~149~~ | ~~159~~ | ~~group 5~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｼﾞｯｸ.ADV:213>)~~ | ~~213~~ | ~~217~~ | ~~group 9~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｼﾞｯｸ.ADV:378>)~~ | ~~378~~ | ~~388~~ | ~~group 19~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｼﾞｯｸ.ADV:504>)~~ | ~~504~~ | ~~513~~ | ~~group 26~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｼﾞｯｸ.ADV:557>)~~ | ~~557~~ | ~~567~~ | ~~group 29~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｼﾞｯｸ.ADV:836>)~~ | ~~836~~ | ~~866~~ | ~~group 53–55~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾏｼﾞｯｸ.ADV:1045>)~~ | ~~1045~~ | ~~1317~~ | ~~group 72–99~~ | ~~[editorial_review\size_order_186_192_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_186_192_tail_20261024/coverage.json>)~~ |

### 193. Gﾊﾟﾊﾟｲｱ.ADV

VI SHA-256: `cfedc2a3f907bd0f4ed4cffc039b609bad16da18784430dddc282abdf064133d`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:70>)~~ | ~~70~~ | ~~131~~ | ~~jp 3–10~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:517>)~~ | ~~517~~ | ~~1191~~ | ~~jp 51–97~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:1471>)~~ | ~~1471~~ | ~~1485~~ | ~~jp 127–129~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:1511>)~~ | ~~1511~~ | ~~1517~~ | ~~jp 134~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:1532>)~~ | ~~1532~~ | ~~1561~~ | ~~jp 136–141~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:1634>)~~ | ~~1634~~ | ~~1637~~ | ~~jp 151~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:2903>)~~ | ~~2903~~ | ~~2988~~ | ~~jp 296~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾊﾟﾊﾟｲｱ.ADV:3176>)~~ | ~~3176~~ | ~~3183~~ | ~~jp 321~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:77>)~~ | ~~77~~ | ~~171~~ | ~~group 2–7~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:724>)~~ | ~~724~~ | ~~1881~~ | ~~group 43–88~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:2298>)~~ | ~~2298~~ | ~~2315~~ | ~~group 119–120~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:2350>)~~ | ~~2350~~ | ~~2361~~ | ~~group 125~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:2383>)~~ | ~~2383~~ | ~~2435~~ | ~~group 127–132~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:2542>)~~ | ~~2542~~ | ~~2547~~ | ~~group 142~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:4547>)~~ | ~~4547~~ | ~~4726~~ | ~~group 277~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾊﾟﾊﾟｲｱ.ADV:4998>)~~ | ~~4998~~ | ~~5012~~ | ~~group 299~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |

### 194. IJAPAN.ADV

VI SHA-256: `021e5d08c02085c12c79cb0aa9e57ef0b49b3663d5955a7decbe95c948737e3d`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:419>) | 419 | 430 | jp 53–54 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:792>) | 792 | 833 | jp 106–111 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:1472>) | 1472 | 1495 | jp 209–213 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:1547>) | 1547 | 1595 | jp 220–227 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:1610>) | 1610 | 1635 | jp 230–234 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:2266>) | 2266 | 2403 | jp 335–352 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:2514>) | 2514 | 2523 | jp 362 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:2601>) | 2601 | 2607 | jp 374 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:2872>) | 2872 | 2881 | jp 416 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:2907>) | 2907 | 3018 | jp 421–434 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:3408>) | 3408 | 3569 | jp 489–514 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:3831>) | 3831 | 3843 | jp 562–563 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:3858>) | 3858 | 3858 | jp 566 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:3902>) | 3902 | 3904 | jp 575 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:4022>) | 4022 | 4027 | jp 596 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:4042>) | 4042 | 4043 | jp 599 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/IJAPAN.ADV:4149>) | 4149 | 4163 | jp 612–615 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:616>) | 616 | 634 | group 51–52 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:1259>) | 1259 | 1329 | group 105–110 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:2362>) | 2362 | 2406 | group 208–212 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:2511>) | 2511 | 2598 | group 219–226 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:2622>) | 2622 | 2662 | group 229–233 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:3741>) | 3741 | 4010 | group 333–350 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:4210>) | 4210 | 4238 | group 359 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:4378>) | 4378 | 4405 | group 371 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:4810>) | 4810 | 4841 | group 412 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:4879>) | 4879 | 5079 | group 417–430 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:5697>) | 5697 | 5968 | group 483–508 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:6395>) | 6395 | 6418 | group 556–557 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:6444>) | 6444 | 6446 | group 560 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:6504>) | 6504 | 6513 | group 569 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:6693>) | 6693 | 6707 | group 590 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:6731>) | 6731 | 6733 | group 593 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/IJAPAN.ADV:6892>) | 6892 | 6913 | group 606–609 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |

### 195. Gﾅｷﾞ.ADV

VI SHA-256: `abd3f7288ccb781e14847e93ab85487a427e8c774c6f0ee58a43774561e858d4`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:301>)~~ | ~~301~~ | ~~389~~ | ~~jp 17–31~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:393>) | 393 | 405 | jp 32–34 | [editorial_review\retranslate_jp_20261028_b8\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b8/coverage.json>); [editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>) |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:409>)~~ | ~~409~~ | ~~459~~ | ~~jp 35–42~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:463>) | 463 | 618 | jp 43 | [editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>) |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:636>)~~ | ~~636~~ | ~~791~~ | ~~jp 44–68~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:800>) | 800 | 955 | jp 69 | [editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>) |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:970>)~~ | ~~970~~ | ~~1224~~ | ~~jp 70–106~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:2410>)~~ | ~~2410~~ | ~~2743~~ | ~~jp 248–274~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:4811>) | 4811 | 4887 | jp 553–564 | [editorial_review\retranslate_jp_20261028_b8\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b8/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gﾅｷﾞ.ADV:4945>) | 4945 | 4958 | jp 574–576 | [editorial_review\retranslate_jp_20261028_b8\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b8/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:434>)~~ | ~~434~~ | ~~577~~ | ~~group 17–30~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:582>) | 582 | 605 | group 31–33 | [editorial_review\retranslate_jp_20261028_b8\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b8/coverage.json>); [editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:610>)~~ | ~~610~~ | ~~682~~ | ~~group 34–41~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:687>) | 687 | 980 | group 42 | [editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:999>)~~ | ~~999~~ | ~~1236~~ | ~~group 43–66~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:1246>) | 1246 | 1558 | group 67 | [editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>) |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:1574>)~~ | ~~1574~~ | ~~1952~~ | ~~group 68–103~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:3681>)~~ | ~~3681~~ | ~~4264~~ | ~~group 244–270~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:7326>) | 7326 | 7436 | group 547–558 | [editorial_review\retranslate_jp_20261028_b8\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b8/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gﾅｷﾞ.ADV:7519>) | 7519 | 7539 | group 568–570 | [editorial_review\retranslate_jp_20261028_b8\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/retranslate_jp_20261028_b8/coverage.json>) |

### 197. Gｶﾌｪ.ADV

VI SHA-256: `dc2f44f14fa8b8d08ed5f0789c4c2a0bc79afcabbe875066e3cb23c17d6e9031`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:115>)~~ | ~~115~~ | ~~141~~ | ~~jp 13–16~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:213>)~~ | ~~213~~ | ~~238~~ | ~~jp 27–32~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:261>)~~ | ~~261~~ | ~~263~~ | ~~jp 37~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:386>)~~ | ~~386~~ | ~~398~~ | ~~jp 53–55~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:528>)~~ | ~~528~~ | ~~537~~ | ~~jp 73–74~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:670>)~~ | ~~670~~ | ~~683~~ | ~~jp 93–96~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:769>)~~ | ~~769~~ | ~~780~~ | ~~jp 110–112~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:820>)~~ | ~~820~~ | ~~834~~ | ~~jp 118~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1096>)~~ | ~~1096~~ | ~~1131~~ | ~~jp 158–163~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1154>)~~ | ~~1154~~ | ~~1162~~ | ~~jp 166~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1196>)~~ | ~~1196~~ | ~~1207~~ | ~~jp 172~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1234>)~~ | ~~1234~~ | ~~1330~~ | ~~jp 177–189~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1549>)~~ | ~~1549~~ | ~~1556~~ | ~~jp 212~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1590>)~~ | ~~1590~~ | ~~1610~~ | ~~jp 215–219~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1631>)~~ | ~~1631~~ | ~~1631~~ | ~~jp 223~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1671>)~~ | ~~1671~~ | ~~1690~~ | ~~jp 229–232~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｶﾌｪ.ADV:1783>)~~ | ~~1783~~ | ~~2720~~ | ~~jp 246–305~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:144>)~~ | ~~144~~ | ~~188~~ | ~~group 13–16~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:279>)~~ | ~~279~~ | ~~315~~ | ~~group 26–31~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:348>)~~ | ~~348~~ | ~~353~~ | ~~group 36~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:522>)~~ | ~~522~~ | ~~539~~ | ~~group 51–53~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:707>)~~ | ~~707~~ | ~~722~~ | ~~group 70~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:897>)~~ | ~~897~~ | ~~914~~ | ~~group 89–92~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:1038>)~~ | ~~1038~~ | ~~1059~~ | ~~group 106–108~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:1122>)~~ | ~~1122~~ | ~~1149~~ | ~~group 114~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:1565>)~~ | ~~1565~~ | ~~1620~~ | ~~group 155–160~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:1646>)~~ | ~~1646~~ | ~~1661~~ | ~~group 163~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:1707>)~~ | ~~1707~~ | ~~1732~~ | ~~group 169~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:1771>)~~ | ~~1771~~ | ~~1832~~ | ~~group 174–177~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:1853>)~~ | ~~1853~~ | ~~1924~~ | ~~group 179–187~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:2177>)~~ | ~~2177~~ | ~~2194~~ | ~~group 207~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:2245>)~~ | ~~2245~~ | ~~2272~~ | ~~group 210–214~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:2302>)~~ | ~~2302~~ | ~~2304~~ | ~~group 218~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:2355>)~~ | ~~2355~~ | ~~2389~~ | ~~group 224–227~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｶﾌｪ.ADV:2513>)~~ | ~~2513~~ | ~~4031~~ | ~~group 241–298~~ | ~~[editorial_review\size_order_193_195_197_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_193_195_197_20261023/coverage.json>)~~ |

### 198. Gｼｨﾙ.ADV

VI SHA-256: `075473637367f469494a04e5e199c2fbd309a8c7eb2cb890123e38a943e0f125`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:111>)~~ | ~~111~~ | ~~217~~ | ~~jp 0–17~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:492>)~~ | ~~492~~ | ~~507~~ | ~~jp 56–59~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:540>)~~ | ~~540~~ | ~~596~~ | ~~jp 66–78~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:658>)~~ | ~~658~~ | ~~664~~ | ~~jp 90–91~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:746>)~~ | ~~746~~ | ~~753~~ | ~~jp 104~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:922>)~~ | ~~922~~ | ~~1736~~ | ~~jp 128–201~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:1890>)~~ | ~~1890~~ | ~~2162~~ | ~~jp 227–248~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:2867>)~~ | ~~2867~~ | ~~3938~~ | ~~jp 342–446~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:4355>)~~ | ~~4355~~ | ~~4378~~ | ~~jp 519–523~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:4484>)~~ | ~~4484~~ | ~~4489~~ | ~~jp 541–542~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:4863>)~~ | ~~4863~~ | ~~4874~~ | ~~jp 594~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:5714>)~~ | ~~5714~~ | ~~5739~~ | ~~jp 733–738~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:5920>)~~ | ~~5920~~ | ~~5946~~ | ~~jp 772–775~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:5972>)~~ | ~~5972~~ | ~~5978~~ | ~~jp 778~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｼｨﾙ.ADV:6016>)~~ | ~~6016~~ | ~~6030~~ | ~~jp 786~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:112>)~~ | ~~112~~ | ~~258~~ | ~~group 0–17~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:650>)~~ | ~~650~~ | ~~671~~ | ~~group 55–58~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:712>)~~ | ~~712~~ | ~~787~~ | ~~group 65–77~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:868>)~~ | ~~868~~ | ~~877~~ | ~~group 89–90~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:984>)~~ | ~~984~~ | ~~1001~~ | ~~group 102~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:1218>)~~ | ~~1218~~ | ~~1223~~ | ~~group 125~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:1259>)~~ | ~~1259~~ | ~~2578~~ | ~~group 128–199~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:2786>)~~ | ~~2786~~ | ~~3261~~ | ~~group 225–246~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:4248>)~~ | ~~4248~~ | ~~5999~~ | ~~group 340–443~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:6555>)~~ | ~~6555~~ | ~~6585~~ | ~~group 516–520~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:6725>)~~ | ~~6725~~ | ~~6737~~ | ~~group 538–539~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:8396>)~~ | ~~8396~~ | ~~8431~~ | ~~group 726–731~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:8661>)~~ | ~~8661~~ | ~~8698~~ | ~~group 764–767~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:8730>)~~ | ~~8730~~ | ~~8743~~ | ~~group 770~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |
| ~~[VI](<D:/Download/Kichikuou Rance/src/Gｼｨﾙ.ADV:8798>)~~ | ~~8798~~ | ~~8822~~ | ~~group 778~~ | ~~[editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>)~~ |

### 199. FIGT_M.ADV

VI SHA-256: `51549865fd11dbf278f062f7b3a13731b00e67a84e0580fa9d3b7b0f42fa9769`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/FIGT_M.ADV:6586>) | 6586 | 7069 | jp 12 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/FIGT_M.ADV:7396>) | 7396 | 7506 | jp 18 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |

### 200. Gｱﾘｽ.ADV

VI SHA-256: `ec932c5d6fb7b3a861926fe832b48b6c110492716cd7d2ad217f2d61f7bec2b3`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:315>) | 315 | 315 | jp 36 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:717>) | 717 | 1005 | jp 100–133 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:1042>) | 1042 | 1069 | jp 140 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:1166>) | 1166 | 1169 | jp 149 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:1268>) | 1268 | 1311 | jp 164–170 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:1629>) | 1629 | 2011 | jp 215–271 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:2047>) | 2047 | 2049 | jp 276 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:2133>) | 2133 | 2180 | jp 282–287 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Gｱﾘｽ.ADV:4169>) | 4169 | 4182 | jp 586 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:478>) | 478 | 480 | group 37 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:1014>) | 1014 | 1197 | group 102–132 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:1362>) | 1362 | 1381 | group 135–136 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:1429>) | 1429 | 1465 | group 143 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:1584>) | 1584 | 1592 | group 152 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:1741>) | 1741 | 1797 | group 168–174 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:2243>) | 2243 | 2406 | group 221–233 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:2433>) | 2433 | 2491 | group 236–242 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:2506>) | 2506 | 2638 | group 244–259 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:2655>) | 2655 | 2702 | group 261–267 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:2717>) | 2717 | 2786 | group 269–276 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:2829>) | 2829 | 2833 | group 281 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:2988>) | 2988 | 3059 | group 287–292 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Gｱﾘｽ.ADV:6154>) | 6154 | 6186 | group 584 | [editorial_review\size_order_198_200_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_198_200_20261023/coverage.json>) |

### 201. Iﾏｼﾞﾝ.ADV

VI SHA-256: `30f766a3f6db3b10062becb97fb73816e7a3538c75a7fd71f621365c306322b6`.

| Nguồn | Dòng từ | Đến | Chỉ số loại trừ | Căn cứ/đợt |
|---|---:|---:|---|---|
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:735>) | 735 | 739 | jp 87 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:798>) | 798 | 801 | jp 97 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:817>) | 817 | 820 | jp 100 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:817>) | 817 | 831 | jp 100–102 | [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:964>) | 964 | 970 | jp 118 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:1037>) | 1037 | 1045 | jp 128–129 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:1149>) | 1149 | 1158 | jp 143–144 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:1391>) | 1391 | 1394 | jp 164 | [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:1856>) | 1856 | 2138 | jp 223–239 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:2194>) | 2194 | 2195 | jp 248 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:3072>) | 3072 | 4081 | jp 343–443 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:3099>) | 3099 | 3487 | jp 348–389 | [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:3519>) | 3519 | 4081 | jp 391–443 | [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:4133>) | 4133 | 4243 | jp 445–456 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:4467>) | 4467 | 4477 | jp 489 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:4599>) | 4599 | 4773 | jp 504–514 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>); [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:5427>) | 5427 | 5680 | jp 592–609 | [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:5568>) | 5568 | 5680 | jp 607–609 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:5807>) | 5807 | 5929 | jp 618–619 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:5818>) | 5818 | 5929 | jp 619 | [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:6235>) | 6235 | 6515 | jp 643–685 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [JP](<D:/Download/Kichikuou Rance/editorial_review/japanese_base_20261022/reference/japanese/Iﾏｼﾞﾝ.ADV:6255>) | 6255 | 6515 | jp 646–685 | [editorial_review\remaining_story_20261022\scope.json](<D:/Download/Kichikuou Rance/editorial_review/remaining_story_20261022/scope.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:995>) | 995 | 1006 | group 84 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:1087>) | 1087 | 1094 | group 94 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:1119>) | 1119 | 1128 | group 97 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:1328>) | 1328 | 1339 | group 114 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:1440>) | 1440 | 1451 | group 124–125 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:1584>) | 1584 | 1600 | group 139–140 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:2603>) | 2603 | 3051 | group 219–235 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:3121>) | 3121 | 3125 | group 244 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:4368>) | 4368 | 5846 | group 338–436 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:5907>) | 5907 | 6072 | group 438–448 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:6366>) | 6366 | 6386 | group 481 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:6537>) | 6537 | 6803 | group 496–505 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:7907>) | 7907 | 8105 | group 598–600 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:8279>) | 8279 | 8499 | group 609–610 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |
| [VI](<D:/Download/Kichikuou Rance/src/Iﾏｼﾞﾝ.ADV:8903>) | 8903 | 9317 | group 634–674 | [editorial_review\i_descending_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/i_descending_20261023/coverage.json>) |

## Chưa đủ căn cứ ánh xạ — không dùng như dòng VI hiện hành

| Script | Loại/chỉ số hoặc dòng cũ | Nguồn | Thiếu dữ liệu |
|---|---|---|---|
| COMMAND.ADV | old_line 173 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Cｼｮｳﾆﾝ.ADV | old_line 616 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Cｼｮｳﾆﾝ.ADV | old_line 899 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Cｼｮｳﾆﾝ.ADV | old_line 1359 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Cｼﾊｲﾄｼ.ADV | old_line 806 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Cﾃｷﾄｼ.ADV | old_line 2632 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Cﾃｷﾄｼ.ADV | old_line 3007 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Cﾒｲｷｭｳ.ADV | old_line 1890 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| FIGT_M.ADV | old_line 2306 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| FIGT_M.ADV | old_line 7400 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| FIGT_M.ADV | old_line 8306 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| FIGT表示.ADV | old_line 577 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| FIGT表示.ADV | old_line 1062 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| FIGT表示.ADV | old_line 2023 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｼﾚｲﾌﾞ.ADV | old_line 235 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｼﾚｲﾌﾞ.ADV | old_line 1696 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｼﾚｲﾌﾞ.ADV | old_line 2102 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｼﾚｲﾌﾞ.ADV | old_line 2669 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｼﾚｲﾌﾞ.ADV | old_line 3018 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｾﾞｽ.ADV | old_line 2196 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｾﾞｽ.ADV | old_line 5583 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｾﾞｽ.ADV | old_line 5792 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iｾﾞｽ.ADV | old_line 6194 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾄｳｿﾞｸ.ADV | old_line 1044 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾄｳｿﾞｸ.ADV | old_line 1824 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾊﾝﾗﾝ.ADV | old_line 10 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾊﾝﾗﾝ.ADV | old_line 1148 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾊﾝﾗﾝ.ADV | old_line 1608 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 1666 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 1974 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 2031 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 2589 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 4129 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 4535 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 4913 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 5676 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 5955 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 6651 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 7116 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 7867 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 8201 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Iﾏｼﾞﾝ.ADV | old_line 8822 | [editorial_review\excluded_sections.json](<D:/Download/Kichikuou Rance/editorial_review/excluded_sections.json>) | historical start has no verified original label/backup; current end unknown |
| Gｼﾞｰｸ.ADV | group 69 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 70 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 71 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 72 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 73 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 74 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 75 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 78 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 79 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 80 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 81 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 105 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 106 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 107 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 108 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 109 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 110 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 111 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 112 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 113 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 114 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 115 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 162 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 163 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 164 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 165 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 166 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｼﾞｰｸ.ADV | group 167 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 49 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 50 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 51 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 52 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 53 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 54 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 55 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 56 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 57 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 58 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 59 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 60 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 61 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 62 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 63 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 64 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 65 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 66 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 67 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 68 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 69 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 70 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 71 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 72 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 73 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 74 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 75 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 76 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 77 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 78 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 79 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 80 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 81 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 82 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 83 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 84 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 85 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 86 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 87 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 88 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 89 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 90 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 91 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 92 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 93 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 94 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 95 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 96 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 97 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 98 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 99 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 100 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 101 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 102 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 103 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 104 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 105 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 106 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 107 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 108 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 109 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 110 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 111 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 112 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 113 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 114 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 115 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 116 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 117 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 118 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 119 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 120 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 121 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 122 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 123 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 124 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 125 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 146 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 153 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 154 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 155 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 156 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 157 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 158 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 159 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 160 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 161 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｱﾐﾗﾝ.ADV | group 162 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 27 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 28 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 29 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 30 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 31 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 32 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 33 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 34 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 35 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 36 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 37 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 38 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 39 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 40 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 41 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 42 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 43 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 44 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 45 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 46 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 47 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 48 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 49 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 50 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 51 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 52 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 53 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 56 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 57 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 58 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 59 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 60 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 72 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 73 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 74 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 75 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 76 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 77 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 78 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 79 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 80 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 81 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 82 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 83 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 84 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 85 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 86 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 87 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 88 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 89 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 90 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 91 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 92 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 93 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾄｳｹﾞﾝ.ADV | group 94 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｺｰﾄﾞ.ADV | group 146 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｺｰﾄﾞ.ADV | group 147 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｺｰﾄﾞ.ADV | group 218 | [editorial_review\size_order_101_105_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_101_105_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 10 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 11 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 12 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 13 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 14 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 15 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 16 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 33 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 34 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 35 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 36 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 37 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 38 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 39 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 40 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 41 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 42 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 43 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 44 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 45 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 46 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 47 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 48 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 49 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 50 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 51 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 52 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 53 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 54 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 55 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 56 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 57 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 58 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 59 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 60 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 61 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 62 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 63 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 64 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 65 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 66 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 67 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 68 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 69 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 70 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 71 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 72 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 73 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 74 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 75 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 76 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 77 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 78 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 79 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 80 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 81 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 82 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 83 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 84 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 85 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 86 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 87 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 88 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 89 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 90 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 91 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 92 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 93 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 94 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 95 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 96 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 97 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 98 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 99 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 100 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 101 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 102 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 103 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 104 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 105 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 106 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 107 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 108 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 109 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 110 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 111 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 112 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 113 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 114 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 115 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 116 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 117 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 118 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 119 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 120 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 121 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 122 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 123 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 124 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gｷｬﾛﾘ.ADV | group 172 | [editorial_review\size_order_106_111_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_106_111_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾊﾟｲｱｰﾙ.ADV | group 14 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾊﾟｲｱｰﾙ.ADV | group 18 | [editorial_review\size_order_143_152_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_143_152_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 88 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 89 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 90 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 91 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 92 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 93 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 94 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 95 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 96 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 97 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 98 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 99 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 100 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 101 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 102 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 103 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 104 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 105 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 106 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾐｷ.ADV | group 107 | [editorial_review\size_order_181_185_tail_20261024\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_181_185_tail_20261024/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾋｭｰﾊﾞｰﾄ.ADV | chunk 47 | [editorial_review\size_order_56_60_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_56_60_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| Gﾋｭｰﾊﾞｰﾄ.ADV | chunk 48 | [editorial_review\size_order_56_60_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_56_60_20261023/coverage.json>) | frozen historical range changed or no hash-verified backup; current position unresolved |
| GDX.ADV | chunk 122 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 123 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 127 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 134 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 135 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 137 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 146 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 147 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 148 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| GDX.ADV | chunk 155 | [editorial_review\size_order_81_85_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_81_85_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 252 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 254 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 255 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 256 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 257 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 258 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 259 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 260 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 261 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 262 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 263 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 264 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 265 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 266 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 267 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 268 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 269 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |
| Gﾛﾚｯｸｽ.ADV | chunk 270 | [editorial_review\size_order_91_95_20261023\coverage.json](<D:/Download/Kichikuou Rance/editorial_review/size_order_91_95_20261023/coverage.json>) | cannot verify current position; no ordinal guess |

## Làm mới và kiểm tra

Chạy cùng lệnh ở scripts_by_size.md sau mỗi lần edit. `--check` trả mã lỗi nếu chỉ mục cũ so với nguồn/metadata hiện hành. Báo cáo máy đọc và hash đầu vào: [review_indexes.generated.json](<D:/Download/Kichikuou Rance/editorial_review/review_indexes.generated.json>). Không trích nội dung cảnh nhạy cảm vào chỉ mục này.
