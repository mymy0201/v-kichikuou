# BẢNG QUY TẮC THUẬT NGỮ, QUAN HỆ & ĐẠI TỪ XƯNG HÔ TOÀN DIỆN - KICHIKUOU RANCE (RANCE BẠO CHÚA)

Tài liệu này là quy chuẩn dịch thuật, biên tập kịch bản và chuẩn hóa văn phong tiếng Việt toàn diện nhất cho toàn bộ tựa game **Kichikuou Rance (Rance Bạo Chúa - 鬼畜王ランス)**.

Tài liệu được cấu trúc chuyên sâu để:
1. Đảm bảo tính nhất quán 100% trong toàn bộ kịch bản 201 file `.ADV`, từ lời dẫn người kể chuyện (storyteller/narration), hội thoại thường nhật, chiến trường công thành, đấu trí chính trị cho tới các phân cảnh ân ái hậu cung 18+.
2. Quy định rõ ràng hệ thống đại từ cho **người kể chuyện (ngôi thứ ba)** khi miêu tả từng nhân vật, tránh lỗi dịch máy cơ học (như lạm dụng "nó", "anh ta", "cô ta").
3. Thiết lập chi tiết cách **xã hội xung quanh (quân sĩ, triều đình, bạn bè, dân chúng, kẻ thù)** gọi từng nhân vật.
4. Cung cấp **ma trận xưng hô chéo đa chiều** giữa toàn bộ các cặp nhân vật chủ chốt trong game.
5. Khắc phục triệt để mọi lỗi máy dịch thảm họa (*came* thành *"tôi đến"*, *Darling* thành *"em yêu"*, *Sill* thành *"ngưỡng cửa"*, *Magic* thành *"phép thuật"*, v.v.).
6. Dùng làm **Prompt Chỉ Thị Cốt Lõi (System Instruction)** nạp trực tiếp vào các mô hình AI dịch thuật tiên tiến (Gemini, Claude, GPT) hoặc script biên tập tự động.

---

## MỤC LỤC
1. [Nguyên Tắc Cốt Lõi Về Giọng Điệu & Bản Chất Của Rance](#1-nguyên-tắc-cốt-lõi-về-giọng-điệu--bản-chất-của-rance)
2. [Quy Chuẩn Đại Từ Cho Lời Dẫn & Người Kể Chuyện (General Storytelling / Third-Person Narration)](#2-quy-chuẩn-đại-từ-cho-lời-dẫn--người-kể-chuyện-general-storytelling--third-person-narration)
   - [2.1. Bản Chất Của Ngôi Kể Thứ Ba Trong Kichikuou Rance](#21-bản-chất-của-ngôi-kể-thứ-ba-trong-kichikuou-rance)
   - [2.2. Đại Từ Người Kể Chuyện Dành Cho Nhân Vật Chính (Rance)](#22-đại-từ-người-kể-chuyện-dành-cho-nhân-vật-chính-rance)
   - [2.3. Đại Từ Người Kể Chuyện Dành Cho Nữ Nhân & Hậu Cung](#23-đại-từ-người-kể-chuyện-dành-cho-nữ-nhân--hậu-cung)
   - [2.4. Đại Từ Người Kể Chuyện Dành Cho Tướng Lĩnh & Hiệp Sĩ](#24-đại-từ-người-kể-chuyện-dành-cho-tướng-lĩnh--hiệp-sĩ)
   - [2.5. Đại Từ Người Kể Chuyện Dành Cho Bậc Tiền Bối, Lão Tướng & Quốc Vương](#25-đại-từ-người-kể-chuyện-dành-cho-bậc-tiền-bối-lão-tướng--quốc-vương)
   - [2.6. Đại Từ Người Kể Chuyện Dành Cho Kẻ Thù, Quái Vật & Ma Nhân](#26-đại-từ-người-kể-chuyện-dành-cho-kẻ-thù-quái-vật--ma-nhân)
   - [2.7. Quy Tắc Chuyển Đổi Nhịp Nhàng Giữa Lời Dẫn Và Thoại Trực Tiếp](#27-quy-tắc-chuyển-đổi-nhịp-nhàng-giữa-lời-dẫn-và-thoại-trực-tiếp)
3. [Hệ Thống Đại Từ Xưng Hô Đối Thoại Của Rance](#3-hệ-thống-đại-từ-xưng-hô-đối-thoại-của-rance)
4. [Bảng Tra Cứu Toàn Diện Mọi Nhân Vật Trong Game](#4-bảng-tra-cứu-toàn-diện-mọi-nhân-vật-trong-game)
5. [Hồ Sơ Nhân Vật Chi Tiết: Người Kể Chuyện, Xã Hội & Rance](#5-hồ-sơ-nhân-vật-chi-tiết-người-kể-chuyện-xã-hội--rance)
   - [5.1. Băng Cướp Rance & Nhóm Đồng Hành Cốt Lõi](#51-băng-cướp-rance--nhóm-đồng-hành-cốt-lõi)
   - [5.2. Vương Quốc Leazas (Hoàng Gia, Tướng Lĩnh, Cận Vệ & Cung Đình)](#52-vương-quốc-leazas-hoàng-gia-tướng-lĩnh-cận-vệ--cung-đình)
   - [5.3. Ninja & Lực Lượng Điệp Báo](#53-ninja--lực-lượng-điệp-báo)
   - [5.4. Thành Phố Tự Do Custom & Toushin City](#54-thành-phố-tự-do-custom--toushin-city)
   - [5.5. Đế Chế Quân Sự Helman](#55-đế-chế-quân-sự-helman)
   - [5.6. Vương Quốc Ma Pháp Zeth](#56-vương-quốc-ma-pháp-zeth)
   - [5.7. Quần Đảo Phong Kiến JAPAN](#57-quần-đảo-phong-kiến-japan)
   - [5.8. Ma Giới, Ma Nhân & Ma Vương](#58-ma-giới-ma-nhân--ma-vương)
   - [5.9. Các Chủng Tộc Bí Ẩn: Tộc Nữ Tiên Kalar & Tộc Đất Nung Haniwa](#59-các-chủng-tộc-bí-ẩn-tộc-nữ-tiên-kalar--tộc-đất-nung-haniwa)
   - [5.10. Đấng Sáng Tạo, Thần Linh & Mascots](#510-đấng-sáng-tạo-thần-linh--mascots)
   - [5.11. Các Nữ Nhân & Nhân Vật Phụ Đặc Biệt Khác](#511-các-nữ-nhân--nhân-vật-phụ-đặc-biệt-khác)
6. [Ma Trận Quan Hệ & Xưng Hô Chéo Giữa Các Nhân Vật Chủ Chốt](#6-ma-trận-quan-hệ--xưng-hô-chéo-giữa-các-nhân-vật-chủ-chốt)
7. [Quy Chuẩn Phân Cảnh Hậu Cung & Ngôn Ngữ Phòng The (H-Scenes)](#7-quy-chuẩn-phân-cảnh-hậu-cung--ngôn-ngữ-phòng-the-h-scenes)
8. [Hệ Thống Thuật Ngữ Chuẩn (Terminology Glossary)](#8-hệ-thống-thuật-ngữ-chuẩn-terminology-glossary)
   - [8.1. Địa Danh, Bản Đồ Chiến Lược & Mê Cung](#81-địa-danh-bản-đồ-chiến-lược--mê-cung)
   - [8.2. Quân Chủng & Binh Chủng Tác Chiến](#82-quân-chủng--binh-chủng-tác-chiến)
   - [8.3. Chiêu Thức, Tuyệt Kỹ & Ma Pháp](#83-chiêu-thức-tuyệt-kỹ--ma-pháp)
   - [8.4. Bảo Bối, Cổ Vật & Trang Bị (50 Items Trong SET_ITEM)](#84-bảo-bối-cổ-vật--trang-bị-50-items-trong-set_item)
   - [8.5. Cơ Chế Ma Thuật, Thần Thánh & Thế Giới](#85-cơ-chế-ma-thuật-thần-thánh--thế-giới)
   - [8.6. Giao Diện & Chỉ Số Vận Hành Game](#86-giao-diện--chỉ-số-vận-hành-game)
9. [Mẫu Prompt Chỉ Thị Cho AI Dịch Thuật & Regex Hậu Xử Lý](#9-mẫu-prompt-chỉ-thị-cho-ai-dịch-thuật--regex-hậu-xử-lý)

---

## 1. NGUYÊN TẮC CỐT LÕI VỀ GIỌNG ĐIỆU & BẢN CHẤT CỦA RANCE

1. **Tuyệt đối không bao giờ dùng "tôi - bạn" cho Rance!**
   - Rance là kẻ ích kỷ cực đoan, ngạo mạn, bạo ngược, dâm loạn vô độ nhưng thẳng thắn như một đứa trẻ hư không bị bất kỳ đạo đức xã hội nào ước thúc.
   - Hắn luôn xem bản thân là trung tâm của vũ trụ, vĩ đại nhất, mạnh mẽ nhất và sở hữu "siêu vũ khí" lợi hại nhất trần đời.
2. **Khẩu khí & Cách xưng hô tự nhiên của Rance**:
   - Khi bình thường / chỉ huy quân đội / nói chuyện với thuộc hạ: **"Ta"** (ngôi thứ nhất).
   - Khi nóng giận, cãi lộn, khinh bỉ kẻ thù nam, đe dọa hoặc đắc thắng: **"Tao"** hoặc **"Bố mày" / "Lão gia đây"**.
   - Với phụ nữ: Luôn nhìn nhận phụ nữ đẹp là chiến lợi phẩm, mục tiêu đè ra giường thị tẩm hoặc thành viên của hậu cung.
3. **Tiếng cười thương hiệu**:
   - Luôn là **`Gahahahaha!`** (hoặc `Ga ha ha ha!`). Tuyệt đối không dịch thành "Haha" hay "Hì hì".
4. **Thán từ & Khẩu ngữ cửa miệng**:
   - `Khốn kiếp!`, `Chết tiệt!`, `Đệt!`, `Mẹ kiếp!`, `Bố mày chém chết giờ!`
   - `Đại pháo của ta`, `Siêu vũ khí của ta` (Hyper Weapon).
   - `Ngoan ngoãn nằm xuống cho ta thị tẩm!`

---

## 2. QUY CHUẨN ĐẠI TỪ CHO LỜI DẪN & NGƯỜI KỂ CHUYỆN (GENERAL STORYTELLING / THIRD-PERSON NARRATION)

Trong Visual Novel, ngoài lời thoại trực tiếp nằm trong ngoặc `「...」` hoặc suy nghĩ trong `（...）`, hơn 50% dung lượng kịch bản là **lời dẫn của người kể chuyện (narration / third-person prose)**. Người kể chuyện đóng vai trò là một người quan sát sắc sảo, hóm hỉnh, mang văn phong kiếm hiệp - sử thi pha lẫn châm biếm đen tối đặc trưng của AliceSoft.

### 2.1. Bản Chất Của Ngôi Kể Thứ Ba Trong Kichikuou Rance
* **Không máy móc, không dịch thô chữ `he/she/it`**: Trong tiếng Anh, `he` và `she` lặp lại liên tục; nếu dịch máy thành `"anh ấy"`, `"cô ấy"`, `"nó"` thì câu văn sẽ cực kỳ nghèo nàn, khô khốc và mất đi khí chất truyện.
* **Nguyên tắc "Đa dạng hóa danh xưng theo ngữ cảnh"**: Kết hợp linh hoạt giữa tên riêng, đại từ chỉ ngôi (`hắn`, `nàng`, `chàng`, `cô`, `ông`), danh phận xã hội (`tên bạo chúa`, `nữ hoàng`, `vị kiếm sĩ`, `cô bé`) và hành động đang diễn ra.

---

### 2.2. Đại Từ Người Kể Chuyện Dành Cho Nhân Vật Chính (Rance)
Tùy vào hoàn cảnh phân cảnh, người kể chuyện sẽ luân chuyển các cách gọi sau:

| Ngữ Cảnh Tình Huống | Đại Từ / Danh Xưng Chuẩn Của Lời Dẫn | Ví Dụ Minh Họa | Cấm Tuyệt Đối |
| :--- | :--- | :--- | :--- |
| **Mặc định / Thường nhật / Chỉ huy** | `Hắn`, `Rance`, `gã` | *Rance khoanh tay cười lớn, ánh mắt hắn quét qua cả căn phòng.* | ❌ Không dùng `nó` (nghe như con vật/vô học). |
| **Hành vi biến thái / Háo sắc / Bắt nạt** | `Tên bạo chúa`, `gã dâm tặc`, `tên vô lại`, `hắn` | *Không để nàng kịp phản ứng, tên bạo chúa liền lao tới đè nghiến đối phương xuống giường.* | ❌ Không dùng `anh ta`, `chàng hiệp sĩ` khi đang làm trò đồi bại. |
| **Chiến trường / Uy lực / Oai phong** | `Hắn`, `Rance`, `gã hiệp sĩ ngông cuồng` | *Đao phong quét qua, Rance xé toạc phòng tuyến địch nhân bằng một cú Rance Attack sấm sét.* | ❌ Không dùng từ ngữ hạ thấp làm mất tính dũng mãnh. |
| **Phòng the / Âu yếm / Trữ tình (H-scenes)** | `Chàng`, `hắn`, `anh` (tiết chế), `Rance` | *Bàn tay thô bạo của chàng vuốt ve dọc tấm lưng trần, khiến nàng khẽ run rẩy.* | ❌ Không dùng `nó`, hạn chế dùng `anh ấy` khô cứng. |

---

### 2.3. Đại Từ Người Kể Chuyện Dành Cho Nữ Nhân & Hậu Cung

| Nhóm Nhân Vật Nữ | Đại Từ Chuẩn Của Lời Dẫn | Danh Xưng Kèm Theo Theo Ngữ Cảnh | Ví Dụ Lời Dẫn Chuẩn |
| :--- | :--- | :--- | :--- |
| **Nữ chính nhu mì / Nô lệ (Sill)** | `Nàng`, `cô bé`, `Sill` | `Tiểu nữ nô lệ`, `cô gái tóc hồng` | *Nàng khẽ cúi đầu, đôi mắt ngấn lệ nép sát sau lưng Rance.* |
| **Nữ hoàng / Vương giả (Lia, Sheila)** | `Nàng`, `Lia` / `Sheila` | `Nữ hoàng`, `nàng nữ hoàng cuồng si`, `nữ hoàng đế nhỏ` | *Nàng mỉm cười rạng rỡ, ánh mắt đong đầy tình si nhìn về phía người tình.* |
| **Nữ quan / Cận thần (Maris, Leila)** | `Nàng`, `cô`, [Tên] | `Thị nữ trưởng`, `nữ đội trưởng`, `nữ kiếm sĩ` | *Maris khẽ thở dài, nàng nhanh chóng ghi chép lại mệnh lệnh của Rance.* |
| **Tsundere / Kiêu kỳ (Shizuka, Kanami)** | `Nàng`, `cô`, [Tên] | `Nữ pháp sư kiêu kỳ`, `nữ ninja`, `cô nàng cứng đầu` | *Khuôn mặt Shizuka đỏ bừng vì uất nghẹn, nàng căm phẫn quay mặt đi.* |
| **Bé gái / Thiếu nữ ngây thơ (Miki, Kou)** | `Cô bé`, `em`, [Tên] | `Tiểu cô nương`, `cô bé ngây thơ`, `tiểu Ma Vương` | *Cô bé ngơ ngác chớp mắt, ôm chặt lấy chú gấu bông của mình.* |
| **Chiến binh nữ / Hiệp sĩ (Menad, Isoroku)** | `Nàng`, `cô`, [Tên] | `Nữ samurai`, `nữ dũng tướng`, `cô nàng tomboy` | *Isoroku siết chặt trường cung, ánh mắt nàng tập trung cao độ.* |

> [!IMPORTANT]
> **Quy Tắc Vàng Với Phụ Nữ:**
> - Tuyệt đối **KHÔNG dùng "nó"** cho bất kỳ nữ nhân nào trong hậu cung hoặc phe người!
> - Từ **"ả"** chỉ được người kể chuyện dùng cho kẻ thù, ma nhân tàn độc hoặc khi đứng từ góc nhìn ghét bỏ của Rance.

---

### 2.4. Đại Từ Người Kể Chuyện Dành Cho Tướng Lĩnh & Hiệp Sĩ
* **Rick, Cordoba, Hubert, Rolex, Aristoles**:
  - Dùng: `chàng`, `anh`, `vị hiệp sĩ`, `vị dũng tướng`, `Rick`, `Cordoba`.
  - Giọng điệu hào hiệp, tôn trọng tư cách hiệp sĩ và lòng trung kiên của họ.
  - Ví dụ: *Vung thanh bảo kiếm rực lửa, Rick lao thẳng vào vòng vây quân địch như một mũi tên xé gió.*

### 2.5. Đại Từ Người Kể Chuyện Dành Cho Bậc Tiền Bối, Lão Tướng & Quốc Vương
* **Barres, Lelyukov, Gandhi, Papaya Server**:
  - Dùng: `ông`, `lão tướng`, `lão tướng quân`, `vị tướng già`, `lão vương` (Gandhi).
  - Giọng điệu kính cẩn trước kinh nghiệm sa trường của các bậc lão trượng.
  - Ví dụ: *Lão tướng Barres vuốt chòm râu bạc, đôi mắt già nua trầm ngâm nhìn lên bản đồ chiến sự.*

### 2.6. Đại Từ Người Kể Chuyện Dành Cho Kẻ Thù, Quái Vật & Ma Nhân
* **Kayblis, Camilla, Nobunaga (bị tha hóa), Redeye, Megalas**:
  - Dùng: `hắn`, `gã`, `tên ma nhân`, `ác quỷ`, `con quái vật`, `quân xâm lược`.
  - Với nữ ma nhân kiêu hãnh (Camilla, Satella, Silky): Dùng `nữ ma nhân`, `nàng`, `ả` (khi cuồng sát).
  - Ví dụ: *Kayblis cười sằng sặc, móng vuốt đen đúa của hắn vung lên tạo thành một luồng ma khí đen ngòm.*

---

### 2.7. Quy Tắc Chuyển Đổi Nhịp Nhàng Giữa Lời Dẫn Và Thoại Trực Tiếp
Khi dịch, phải đảm bảo đại từ trong lời dẫn ăn khớp với đại từ xưng hô trong lời thoại:
* **Hội thoại**:
  ```text
  'Chàng Rance ơi, thiếp nhớ chàng lắm!'
  R
  'Lia lao vào lòng Rance, ôm chặt lấy hắn như không muốn rời.'
  ```
  *(Lời thoại Lia xưng "thiếp - chàng", lời dẫn gọi Rance là "hắn" hoặc "chàng", gọi Lia là "Lia" hoặc "nàng" - ăn khớp tự nhiên).*

---

## 3. HỆ THỐNG ĐẠI TỪ XƯNG HÔ ĐỐI THOẠI CỦA RANCE

| Đối Tượng Giao Tiếp | Rance Tự Xưng | Rance Gọi Đối Phương | Sắc Thái & Ngữ Cảnh Điển Hình |
| :--- | :--- | :--- | :--- |
| **Phụ nữ hậu cung / người tình yêu dấu** | `Ta` (khi dỗ dành: `Anh`) | `Em` | Chiếm hữu, âu yếm, khi thị tẩm hoặc ve vãn. |
| **Phụ nữ quý tộc / vương giả (Lia, Sheila...)** | `Ta` | `Nàng` / `Em` | Tự tôn quân vương, vừa tán tỉnh vừa thuần phục. |
| **Phụ nữ bướng bỉnh / chống đối (Shizuka, Kanami)** | `Ta` (nóng giận: `Tao` / `Bố mày`) | `Cô` / `Ả` / `Con ranh` / `Mày` | Trêu tức, dọa nạt, đè bẹp sự kiêu ngạo. |
| **Phụ nữ bạo dâm / cứng đầu (Milli...)** | `Ta` / `Bố mày` | `Bà cô` / `Mụ điên` / `Ả` | Cay cú, ăn miếng trả miếng, đấu khẩu ngang tàng. |
| **Bé gái / Thiếu nữ ngây thơ (Miki, Kouhime...)** | `Ta` / `Chú` / `Anh` | `Nhóc` / `Em` / `Bé con` | Bề trên cưng chiều, trêu ghẹo nhưng bao bọc. |
| **Thuộc hạ nam trung thành (Rick, Barres, Cordoba)** | `Ta` | `Ngươi` / `Các ngươi` / [Tên] | Bậc quân vương ra lệnh, hào sảng tin cậy. |
| **Đàn em sơn tặc thân cận (Bound, Soul)** | `Ta` / `Đại ca` | `Chú mày` / `Soul` / `Bound` | Huynh đệ giang hồ, đại ca bảo ban lâu la. |
| **Nam nhân kình địch (Kentarou, Patton)** | `Tao` / `Bố mày` / `Ta` | `Mày` / `Thằng ranh` / `Patton` | Khiêu khích, tranh giành gái, đọ sức. |
| **Kẻ thù / Quái vật / Ma nhân xâm lược** | `Tao` / `Bố mày` / `Ta` | `Lũ rác rưởi` / `Mày` / `Bọn bay` | Sát khí ngút trời, tiêu diệt không thương tiếc. |

---

## 4. BẢNG TRA CỨU TOÀN DIỆN MỌI NHÂN VẬT TRONG GAME

Bảng dưới đây tổng hợp toàn diện đại từ của **Người kể chuyện**, **Rance**, và **Xã hội xung quanh** cho toàn bộ ~85 nhân vật:

| STT | Tên Nhân Vật (JP / EN) | Phe Phái / Thân Phận | Người Kể Chuyện Gọi | Mọi Người Xung Quanh Gọi | Rance Gọi - Xưng | Nhân Vật Gọi Rance - Xưng |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Sill Plain** (シィル) | Nô lệ độc quyền / Trị liệu | `Nàng`, `cô bé`, `tiểu nô lệ`, `Sill` | Thuộc hạ: `Tiểu thư Sill`, `Nương nương Sill`; Lia: `Con bé nô lệ` | `Sill` / `Em` (quát: `Mày`) - `Ta` | `Chủ nhân Rance` / `Ngài` - `Em` |
| **2** | **Lia Parapara Leazas** (リア) | Nữ hoàng Leazas (Yandere) | `Nàng`, `Nữ hoàng`, `Lia` | Triều thần: `Bệ hạ`, `Nữ hoàng Bệ hạ`; Dân chúng: `Nữ hoàng Lia` | `Lia` / `Nàng` / `Em` - `Ta` | `Chàng Rance` / `Chàng yêu` - `Thiếp`/`Em` |
| **3** | **Maris Amaryllis** (マリス) | Thị nữ trưởng / Tể tướng thực quyền | `Nàng`, `Maris`, `nữ quan thanh lịch` | Triều đình: `Quan tổng quản Maris`; Lia: `Maris` | `Maris` / `Cô` - `Ta` | `Bệ hạ Rance` / `Bệ hạ` - `Tôi`/`Thần` |
| **4** | **Leila Glaster** (レイラ) | Đội trưởng Cận vệ Hoàng gia | `Nàng`, `Leila`, `nữ đội trưởng` | Cận vệ: `Đội trưởng Leila`; Rick: `Cô Leila` | `Leila` / `Cô` / `Nàng` - `Ta` | `Ngài Rance` / `Bệ hạ` - `Tôi` |
| **5** | **Rick Addison** (リック) | Xích Quỷ / Thống lĩnh Xích Quân | `Chàng`, `Rick`, `vị kiếm sĩ`, `Xích Quỷ` | Binh sĩ: `Tướng quân Rick`, `Đại tướng`; Menad: `Đại nhân Rick` | `Rick` / `Ngươi` - `Ta` | `Bệ hạ` / `Ngài Rance` - `Thần`/`Tôi` |
| **6** | **Barres Provence** (バレス) | Tổng tư lệnh lão tướng quân | `Lão tướng`, `ông`, `Barres`, `lão tướng râu bạc` | Binh sĩ: `Đại tướng quân Barres`; Haurein: `Cha`/`Phụ thân` | `Lão già Barres` / `Ngươi` - `Ta` | `Bệ hạ` - `Lão thần`/`Thần` |
| **7** | **Cordoba** (コルドバ) | Tướng Hắc Giáp / Bức tường sắt | `Cordoba`, `vị tướng thiết giáp` | Binh sĩ: `Tướng quân Cordoba`; Rick: `Tướng quân Cordoba` | `Cordoba` / `Ngươi` - `Ta` | `Bệ hạ` - `Thần` |
| **8** | **Ex Van** (エクス) | Quân sư thiên tài Leazas | `Ex Van`, `chàng`, `vị quân sư trẻ` | Triều đình: `Quân sư Ex`, `Đại nhân Ex` | `Ex` / `Ngươi` - `Ta` | `Bệ hạ` - `Thần` |
| **9** | **Menad** (メナド) | Phó tướng Xích Quân (Tomboy) | `Cô`, `Menad`, `nữ phó tướng dũng cảm` | Binh sĩ: `Phó tướng Menad`; Rick: `Menad` | `Menad` / `Cô bé` / `Em` - `Ta` | `Ngài Rance` - `Em`/`Tôi` |
| **10** | **Haurein** (ハウレーン) | Nữ kiếm sĩ, ái nữ của Barres | `Cô`, `nàng`, `Haurein` | Binh sĩ: `Tiểu thư Haurein`; Barres: `Con gái`, `Haurein` | `Haurein` / `Cô em` - `Ta` | `Bệ hạ` / `Ngài Rance` - `Tôi` |
| **11** | **Melfeis** (メルフェイス) | Nữ pháp sư nhân từ Leazas | `Nàng`, `cô`, `Melfeis` | Thương binh: `Thiên sứ Melfeis`, `Tiểu thư Melfeis` | `Melfeis` / `Em` - `Ta` | `Ngài Rance` - `Em` |
| **12** | **Julia Lindom** (ジュリア) | Tân Đội trưởng Cận vệ tóc vàng | `Cô bé`, `Julia`, `nàng cận vệ trẻ` | Cận vệ: `Đội trưởng Julia`; Leila: `Julia` | `Julia` / `Nhóc con` / `Em` - `Ta` | `Bệ hạ Rance` - `Em` |
| **13** | **Rafalia** (ラファリア) | Học viện Kỵ sĩ hiếu chiến | `Cô`, `Rafalia`, `nữ kỵ sĩ trẻ` | Bạn học: `Rafalia`; Anaseru: `Học viên Rafalia` | `Rafalia` / `Cô em` - `Ta` | `Bệ hạ` - `Tôi` |
| **14** | **Arlcoate** (アールコート) | Học viện Kỵ sĩ rụt rè | `Cô bé`, `Arlcoate`, `cô nhóc nhút nhát` | Bạn bè: `Arlcoate-chan` | `Arlcoate` / `Nhóc nhút nhát` - `Ta` | `Ngài Rance` - `Em` |
| **15** | **Anaseru** (アナセル) | Giáo quan Kỵ sĩ nghiêm nghị | `Nàng`, `cô`, `Anaseru` | Học viên: `Giáo quan Anaseru` | `Anaseru` / `Cô` - `Ta` | `Bệ hạ` - `Tôi` |
| **16** | **Wendy** (ウェンディ) | Hầu gái hoàng cung tươi tắn | `Cô bé`, `Wendy`, `cô hầu gái nhỏ` | Maris: `Wendy`; Đồng nghiệp: `Wendy-chan` | `Wendy` / `Em` - `Ta` | `Chủ nhân Rance` - `Em` |
| **17** | **Elisabeth** (エリザベス) | Cựu công chúa quý tộc Leazas | `Nàng`, `Elisabeth`, `nàng cựu công chúa` | Quý tộc: `Điện hạ Elisabeth`, `Công chúa` | `Elisabeth` / `Nàng` - `Ta` | `Ngài Rance` - `Tôi` |
| **18** | **Kinkaid** (キンケード) | Tướng sĩ thăng tiến Leazas | `Kinkaid`, `anh`, `viên sĩ quan trẻ` | Binh sĩ: `Chỉ huy Kinkaid` | `Kinkaid` / `Ngươi` - `Ta` | `Bệ hạ` - `Thần`/`Tôi` |
| **19** | **Gengorou** (ゲンゴロウ) | Kỳ tài chiến thuật mê bóng đá | `Lão`, `Gengorou`, `kỳ nhân bóng đá` | Mọi người: `Lão dị hợm Gengorou` | `Lão mê bóng đá` / `Ngươi` - `Ta` | `Bệ hạ` / `Cậu Rance` - `Tôi` |
| **20** | **Soul Less** (ソウル) | Nữ sơn tặc phó tướng | `Nàng`, `Soul`, `nữ tặc hoang dã` | Băng cướp: `Đại tỷ Soul`, `Phó tướng Soul` | `Soul` / `Em` - `Ta`/`Đại ca` | `Đại ca Rance` - `Em`/`Tôi` |
| **21** | **Bound Less** (バウンド) | Đô vật sơn tặc to lớn | `Gã`, `Bound`, `gã đô vật khổng lồ` | Băng cướp: `Anh Bound` | `Bound` / `Chú mày` - `Ta`/`Đại ca` | `Đại ca Rance` - `Tôi`/`Em` |
| **22** | **Kentou Kanami** (見当かなみ) | Ninja thân cận Leazas | `Nàng`, `cô`, `Kanami`, `nữ ninja` | Lia: `Kanami`; Suzume: `Kanami-chan` | `Kanami` / `Con nhóc ninja` - `Ta`/`Bố mày` | `Tên Rance khốn khiếp!` - `Tôi` |
| **23** | **Suzume** (鈴女) | Ninja tự do tinh quái dâm đãng | `Nàng`, `Suzume`, `cô nhóc ninja` | Đồng nghiệp: `Suzume`; Kanami: `Con điên Suzume` | `Suzume` / `Con nhóc ranh` - `Ta` | `Rance` / `Chàng Rance` - `Bé Suzume`/`Em` |
| **24** | **Maria Custard** (マリア) | Nhà phát minh phái Tulip (Tsundere) | `Nàng`, `cô`, `Maria`, `nữ phát minh` | Binh sĩ Tulip: `Đại nhân Maria`; Shizuka: `Maria` | `Maria` - `Ta`/`Anh` | `Rance` - `Tôi` |
| **25** | **Shizuka Masou** (魔想志津香) | Thiên tài ma pháp số 1 lục địa | `Nàng`, `Shizuka`, `nữ pháp sư kiêu kỳ` | Giới ma pháp: `Đại pháp sư Shizuka`; Maria: `Shizuka` | `Shizuka` / `Ả kiêu kỳ` - `Ta` | `Tên khốn Rance`/`Tên dâm tặc` - `Tôi` |
| **26** | **Milli Walkers** (ミリ) | Nữ thủ lĩnh bạo dâm phái Walkers | `Ả`, `Milli`, `nữ chúa bạo dâm` | Thuộc hạ: `Nữ vương Milli`; Mill: `Chị Milli` | `Milli` / `Mụ điên` - `Ta`/`Bố mày` | `Cậu em Rance` - `Chị đây`/`Bà` |
| **27** | **Mill Walkers** (ミル) | Em gái Milli, thuần dưỡng ảo thú | `Cô bé`, `Mill`, `cô bé thuần thú` | Milli: `Mill`, `em gái bé nhỏ` | `Mill` / `Bé con` / `Em` - `Ta` | `Anh Rance` - `Em` |
| **28** | **Ran** (ラン) | Nữ thám hiểm Toushin xui xẻo | `Cô`, `Ran`, `cô nhóc xui xẻo` | Bạn thám hiểm: `Ran` | `Ran` / `Nhóc xui xẻo` - `Ta` | `Ngài Rance` - `Em`/`Tôi` |
| **29** | **Merim** (メリム) | Tiếp tân ngân hàng Custom | `Cô`, `Merim`, `cô thủ quỹ dịu dàng` | Đồng nghiệp: `Merim-san` | `Merim` / `Em` - `Ta` | `Ngài Rance` - `Em`/`Tôi` |
| **30** | **Merci** (メルシィ) | Nữ nhân viên Custom lanh lợi | `Cô`, `Merci`, `cô nàng tiếp tân` | Khách hàng: `Cô Merci` | `Merci` / `Em` - `Ta` | `Ngài Rance` - `Em` |
| **31** | **Sheila Helman** (シーラ) | Hoàng đế bù nhìn Helman | `Nàng`, `Sheila`, `nữ hoàng đế nhỏ` | Triều thần Helman: `Bệ hạ`, `Nữ hoàng đế Bệ hạ` | `Sheila` / `Hoàng đế bé nhỏ` / `Em` - `Ta` | `Ngài Rance` - `Tôi`/`Ta` |
| **32** | **Patton Misurugi** (パットン) | Cựu Hoàng thái tử / Quyền vương | `Chàng`, `Patton`, `gã võ sĩ quyền cước` | Hubert: `Điện hạ Patton`; Sheila: `Huynh trưởng` | `Patton` / `Tên cơ bắp` - `Ta`/`Tao` | `Rance` - `Ta`/`Tôi` |
| **33** | **Hubert Lipton** (ヒューバート)| Hiệp sĩ danh dự Helman | `Chàng`, `Hubert`, `người hiệp sĩ mẫu mực`| Binh sĩ: `Hiệp sĩ Hubert`, `Đại nhân Hubert` | `Hubert` / `Ngươi` - `Ta` | `Ngài Rance` - `Tôi` |
| **34** | **Lelyukov** (レリューコフ) | Lão tướng kiên trung Helman | `Lão tướng`, `ông`, `Lelyukov` | Binh sĩ: `Tướng quân Lelyukov` | `Lão tướng` / `Ngươi` - `Ta` | `Ngài Rance` - `Lão phu`/`Tôi` |
| **35** | **Aristoles** (アリストレス) | Sát thủ / Mưu lược gia Helman | `Chàng`, `Aristoles`, `kỳ tài mưu lược` | Binh sĩ: `Quân sư Aristoles` | `Aristoles` / `Ngươi` - `Ta` | `Ngài Rance` - `Tôi` |
| **36** | **Cream** (クリーム) | Nữ quân sư sắc sảo Helman | `Nàng`, `Cream`, `nữ quân sư tài ba` | Đồng minh: `Quân sư Cream` | `Cream` / `Cô ả sắc sảo` - `Ta` | `Ngài Rance` - `Tôi` |
| **37** | **Sayori Unga** (サヨリ) | Tiểu thư quý tộc kiêu kỳ Unga | `Nàng`, `Sayori`, `tiểu thư kiêu kỳ` | Gia nhân: `Tiểu thư Sayori` | `Sayori` / `Tiểu thư` - `Ta` | `Tên cướp vô lại!` / `Ngài Rance` - `Tôi` |
| **38** | **Rolex** (ロレックス) | Song đao phái Baiibahal | `Chàng`, `Rolex`, `kiếm khách song đao` | Binh sĩ: `Đại nhân Rolex` | `Rolex` / `Ngươi` - `Ta` | `Ngài Rance` - `Tôi` |
| **39** | **Ragarl** (ラガール) | Tướng thiết kỵ Helman | `Gã`, `Ragarl`, `viên tướng thiết kỵ` | Binh sĩ: `Tướng quân Ragarl` | `Ragarl` / `Ngươi` - `Ta` | `Ngài Rance` - `Tôi` |
| **40** | **Raylee** (レィリィ) | Nữ chiến binh phương Bắc Helman | `Nàng`, `Raylee`, `nữ chiến binh` | Binh sĩ: `Đại tỷ Raylee` | `Raylee` / `Em` - `Ta` | `Ngài Rance` - `Em`/`Tôi` |
| **41** | **Gandhi The Zeth** (ガンジー)| Quốc vương Zeth / Hộ pháp khổng lồ | `Ông`, `Gandhi`, `lão vương khổng lồ` | Triều thần Zeth: `Bệ hạ`, `Quốc vương Bệ hạ`; Magic: `Phụ vương` | `Lão già Gandhi` / `Ngươi` - `Ta` | `Rance` - `Ta` |
| **42** | **Magic The Gandhi** (マジック)| Công chúa Zeth / Tứ Đại Lãnh Chúa | `Nàng`, `Magic`, `cô công chúa quý phái` | Thần dân Zeth: `Công chúa Magic`, `Điện hạ`; Gandhi: `Con gái rượu` | `Magic` / `Cô công chúa` - `Ta` | `Ngài Rance` / `Tên thô bỉ` - `Tôi` |
| **43** | **Yamada Chizuko** (チズコ) | Tứ Đại Lãnh Chúa váy dạ hội | `Nàng`, `Chizuko`, `cô ả lập dị` | Binh sĩ Zeth: `Lãnh chúa Chizuko` | `Chizuko` / `Cô ả dị hợm` - `Ta` | `Ngài Rance` - `Tôi` |
| **44** | **Nagi Raghav** (ナギ) | Tứ Đại Lãnh Chúa lơ đễnh | `Nàng`, `Nagi`, `pháp sư độc hành` | Giới pháp sư: `Lãnh chúa Nagi` | `Nagi` / `Cô ả lơ đễnh` - `Ta` | `Rance` - `Tôi` |
| **45** | **Uspira** (ウスピラ) | Tứ Đại Lãnh Chúa Băng/Đất | `Bà`, `nàng`, `Uspira` | Triều thần: `Đại pháp sư Uspira` | `Uspira` / `Bà cô ma pháp` - `Ta` | `Ngài Rance` - `Tôi` |
| **46** | **Café Artful** (カフェ) | Nữ quý tộc pháp sư sành điệu | `Nàng`, `Café`, `quý cô sành điệu` | Quý tộc Zeth: `Tiểu thư Café` | `Café` / `Cô ả đỏng đảnh` - `Ta` | `Ngài Rance` - `Tôi` |
| **47** | **Papaya Server** (パパイヤ) | Trưởng lão ma pháp tếu táo | `Lão`, `ông`, `Papaya`, `lão pháp sư già` | Đệ tử: `Đại sư Papaya` | `Lão già Papaya` / `Ngươi` - `Ta` | `Cậu Rance` - `Lão già này`/`Tôi` |
| **48** | **Amira** (アミラン) | Nữ pháp sư quyến rũ chết người | `Nàng`, `Amira`, `nữ pháp sư gợi cảm` | Đồng môn: `Amira` | `Amira` / `Em` - `Ta` | `Ngài Rance` - `Em`/`Tôi` |
| **49** | **Anis** (アニス) | Pháp sư tham tiền siêu cấp | `Cô bé`, `Anis`, `con nhóc hám tiền` | Khách hàng: `Pháp sư Anis` | `Anis` / `Con nhóc hám tiền` - `Ta` | `Đại gia Rance` / `Ngài Rance` - `Em` |
| **50** | **Eleanor** (エレノア) | Nữ ma chiến binh Zeth | `Nàng`, `Eleanor`, `nữ kiếm sĩ phép` | Binh sĩ: `Đội trưởng Eleanor` | `Eleanor` / `Cô` - `Ta` | `Ngài Rance` - `Tôi` |
| **51** | **Oda Nobunaga** (織田信長) | Lãnh chúa JAPAN (Bị quỷ nhập) | `Hắn`, `Nobunaga`, `tên quỷ vương` | Gia thần: `Chúa công`, `Đại nhân Nobunaga`; Kou: `Huynh trưởng` | `Nobunaga` / `Tên quỷ` - `Tao`/`Ta` | `Tên sâu bọ Rance` - `Ta` |
| **52** | **Oda Kouhime** (香姫) | Tiểu công chúa ngây thơ JAPAN | `Cô bé`, `Kouhime`, `tiểu công chúa` | Gia thần: `Công chúa Kou`, `Tiểu thư Kou`; Isoroku: `Kou-chan` | `Kou` / `Kouhime` / `Em` - `Ta` | `Chủ nhân Rance` - `Kou`/`Em` |
| **53** | **Yamamoto Isoroku** (五十六)| Đệ nhất nữ cung thủ samurai | `Nàng`, `Isoroku`, `nữ dũng tướng samurai`| Cung thủ: `Tướng quân Yamamoto`; Kou: `Chị Isoroku` | `Isoroku` / `Em` - `Ta`/`Anh` | `Tướng quân Rance` / `Chàng` - `Thiếp`/`Tôi` |
| **54** | **Makoto** (マコト) | Thiếu nữ tiệm dango tinh nghịch | `Cô bé`, `Makoto`, `cô bé dango` | Khách làng: `Bé Makoto` | `Makoto` / `Con nhóc dango` - `Ta` | `Ngài Rance` - `Em` |
| **55** | **Torako** (虎子) | Nữ kiếm sĩ cọp con Mikawa | `Cô`, `Torako`, `cô nàng hổ báo` | Đồng đội: `Torako` | `Torako` / `Cô em hổ báo` - `Ta` | `Ngài Rance` - `Tôi` |
| **56** | **Kurusu Miki** (美樹) | Ma Vương định mệnh (Little Princess) | `Cô bé`, `Miki`, `tiểu Ma Vương` | Kentarou: `Miki`; Sill: `Miki-chan`; Ma nhân: `Ma Vương Bệ hạ` | `Miki` / `Nhóc Ma Vương` - `Ta` | `Chú Rance` / `Anh Rance` - `Em`/`Miki` |
| **57** | **Ogawa Kentarou** (健太郎) | Dũng sĩ mang thánh đao / Bạn Miki | `Chàng trai`, `cậu ta`, `Kentarou` | Miki: `Kentarou-kun`; Nikkou: `Chủ nhân Kentarou` | `Kentarou` / `Thằng ranh` - `Tao`/`Bố mày` | `Mày` / `Tên Rance chết tiệt` - `Tao` |
| **58** | **Thánh Đao Nikkou** (日光) | Thánh đao cổ đại diệt Ma Nhân | `Nó`, `thanh thánh đao`, `Nikkou` | Kentarou: `Đao Nikkou`; Chaos: `Thanh sắt cổ hủ` | `Cây đao khó tính` / `Mày` - `Tao` | `Kẻ dâm đãng Rance` - `Ta`/`Bản đao` |
| **59** | **Ma Kiếm Chaos** (カオス) | Ma kiếm tà dâm chém rách kết giới | `Nó`, `thanh ma kiếm`, `Chaos` | Rance: `Lão kiếm dâm`; Nikkou: `Thanh kiếm đồi trụy` | `Lão kiếm dâm` / `Chaos` - `Tao`/`Ta` | `Thằng nhóc dâm tặc` - `Bản kiếm`/`Ta` |
| **60** | **Kayblis** (ケイブリス) | Đệ Nhất Ma Nhân (Phe xâm lược) | `Hắn`, `gã`, `Kayblis`, `tên trùm ma nhân`| Thuộc hạ: `Đại nhân Kayblis`; Phe Hornet: `Tên phản đồ Kayblis` | `Kayblis` / `Tên khốn` - `Tao`/`Bố mày` | `Tên người hạ đẳng` - `Bản tọa`/`Ta` |
| **61** | **Camilla** (カミーラ) | Nữ Ma Nhân Long Tộc kiêu hãnh | `Nàng`, `Camilla`, `nữ ma nhân rồng` | Ma quân: `Đại nhân Camilla`; Kayblis: `Camilla` | `Camilla` / `Con rồng cái` - `Ta`/`Tao` | `Tên người ngông cuồng` - `Ta` |
| **62** | **Hornet** (ホーネット) | Nữ Ma Nhân lãnh tụ phe ôn hòa | `Nàng`, `Hornet`, `nữ chúa ma nhân` | Thuộc hạ: `Ngài Hornet`, `Hornet-sama`; Kayblis: `Con tiện nhân` | `Hornet` / `Nữ chúa ong` - `Ta` | `Rance` / `Con người` - `Ta` |
| **63** | **Satella** (サテラ) | Nữ Ma Nhân Hộ Vệ cao ngạo | `Nàng`, `Satella`, `ả ma nhân hộ vệ` | Hornet: `Satella`; Ma quân: `Đại nhân Satella` | `Satella` / `Ả ma nhân` - `Ta` | `Tên con người hạ đẳng` / `Rance` - `Ta` |
| **64** | **Silky** (シルキィ) | Nữ Ma Nhân Băng Giá trầm lặng | `Nàng`, `Silky`, `ả ma nhân băng giá` | Hornet: `Silky`; Đồng minh: `Silky` | `Silky` / `Ả băng tuyết` - `Ta` | `Rance` - `Ta` |
| **65** | **Saizel & Hawzel** (サイゼル＆ハウゼル)| Cặp Ma Nhân Ngụy Thiên Thần | `Hai ả`, `chị em thiên thần giả` | Ma quân: `Đại nhân Saizel/Hawzel` | `Hai đứa bay` / `Thiên thần giả` - `Ta` | `Rance` / `Tên người` - `Bọn ta` |
| **66** | **Warg** (ワーグ) | Ma Nhân Mộng Giới bé gái | `Nó`, `ả`, `Warg`, `nhóc ma quái` | Đồng minh: `Warg` | `Warg` / `Nhóc ma quái` - `Ta` | `Rance` - `Ta`/`Em` |
| **67** | **Galtia** (ガルティア) | Ma Nhân Háu Ăn khổng lồ | `Gã`, `Galtia`, `tên ma nhân háu ăn` | Ma quân: `Đại nhân Galtia` | `Galtia` / `Tên tham ăn` - `Ta` | `Rance` - `Ta` |
| **68** | **Megalas** (メガラス) | Ma Nhân Tộc Horus bay lượn | `Hắn`, `Megalas`, `tên chimera bay` | Binh đoàn bay: `Chủ tướng Megalas` | `Megalas` / `Tên chimera bay` - `Ta` | `Rance` - `Ta` |
| **69** | **Medusa** (メデューサ) | Ma Nhân Xà Nữ hóa đá | `Ả`, `Medusa`, `ả rắn độc ma nhân` | Thuộc hạ rắn: `Nữ chúa Medusa` | `Medusa` / `Ả rắn độc` - `Ta` | `Con người ti tiện` - `Ta` |
| **70** | **Redeye** (レッドアイ) | Ma Nhân Độc Nhãn sát thủ | `Hắn`, `Redeye`, `tên sát thủ chột mắt` | Kayblis: `Redeye` | `Redeye` / `Tên chột` - `Tao`/`Ta` | `Rance` - `Ta` |
| **71** | **Kesselring** (ケッセルリンク)| Ma Nhân Huyết Tộc ma cà rồng | `Hắn`, `Kesselring`, `bá tước bóng đêm`| Tộc nhân ma cà rồng: `Chúa tể Kesselring` | `Kessel` / `Tên ma cà rồng` - `Ta` | `Rance` - `Ta` |
| **72** | **Babora** (バボラ) | Ma Nhân Cự Thạch khổng lồ | `Nó`, `Babora`, `tên cự thạch ma nhân` | Ma nhân: `Babora` | `Babora` / `Tên núi đá` - `Ta` | `Rwoooaar!` |
| **73** | **Pastel Kalar** (パステル) | Nữ hoàng Tộc Kalar căm thù đàn ông | `Nàng`, `Pastel`, `Nữ hoàng Kalar` | Tộc nhân Kalar: `Nữ hoàng Bệ hạ`, `Đại nhân Pastel` | `Pastel` / `Nữ hoàng Kalar` - `Ta` | `Tên người thô bỉ` / `Rance` - `Ta` |
| **74** | **Somita** (ソミタ) | Nữ tiên chiến binh Kalar | `Nàng`, `cô`, `Somita` | Pastel: `Somita`; Đồng đội: `Somita` | `Somita` / `Cô nàng Kalar` - `Ta` | `Ngài Rance` - `Tôi` |
| **75** | **Đại vương Mars** (マーズ) | Vua Tộc Đất Nung Haniwa | `Lão`, `ông`, `Đại vương Mars` | Thần dân Haniwa: `Đại vương Mars (Haniwa~)` | `Lão tượng đất` / `Ngươi` - `Ta` | `Rance (Haniwa~)` - `Ta` |
| **76** | **Elena** (エレーナ) | Nữ tu sĩ AL Giáo hoàn lương | `Nàng`, `cô`, `Elena`, `nữ tu sĩ dịu hiền`| Tín đồ: `Nữ tu Elena` | `Elena` / `Cô tu sĩ` - `Ta` | `Ngài Rance` - `Em`/`Tôi` |
| **77** | **Saitou** (サイトウ) | Búp bê cơ khí sống Shangri-La | `Cô bé`, `Saitou`, `cô búp bê nhỏ` | Mọi người: `Bé búp bê Saitou` | `Saitou` / `Búp bê nhỏ` - `Ta` | `Chủ nhân Rance` - `Em` |
| **78** | **Saulnia** (ソルニア) | Thiếu nữ Kogal da nâu ngổ ngáo | `Cô bé`, `Saulnia`, `cô nhóc da nâu` | Bạn bè: `Saulnia` | `Saulnia` / `Cô bé da nâu` - `Ta` | `Anh Rance` - `Em`/`Tôi` |
| **79** | **Martina** (マルチナ) | Nữ quý tộc thương nhân sắc sảo | `Nàng`, `Martina`, `nữ quý tộc buôn bán` | Gia nhân: `Tiểu thư Martina` | `Martina` / `Cô em kiêu kỳ` - `Ta` | `Ngài Rance` - `Tôi` |
| **80** | **Katyusha** (カチューシャ) | Nữ học giả thông thái cổ vật | `Nàng`, `cô`, `Katyusha`, `nữ học giả` | Viện nghiên cứu: `Tiến sĩ Katyusha` | `Katyusha` / `Bà tiến sĩ nhỏ` - `Ta` | `Ngài Rance` - `Tôi` |
| **81** | **Shariella** (シャリエラ) | Tiểu thư đài các đoan trang | `Nàng`, `cô`, `Shariella` | Gia nhân: `Tiểu thư Shariella` | `Shariella` / `Em` - `Ta` | `Ngài Rance` - `Em` |
| **82** | **Aya** (アーヤ) | Nữ y tá dịu hiền tận tụy | `Cô`, `Aya`, `cô y tá hiền lành` | Thương binh: `Y tá Aya` | `Aya` / `Cô y tá ngoan` - `Ta` | `Ngài Rance` - `Em` |
| **83** | **Mokomoko** (モコモコ) | Thú nhân lông xù đáng yêu | `Nó`, `bé con`, `Mokomoko` | Mọi người: `Mokomoko` | `Mokomoko` / `Cục bông` - `Ta` | `Ngài Rance` - `Moko~`/`Em` |
| **84** | **Rudrasaum** (ルドラサウム)| Đấng Sáng Tạo vũ trụ Tối Cao | `Đấng Sáng Tạo`, `Rudra`, `thực thể tối cao`| Thần thánh: `Đấng Sáng Tạo Rudrasaum` | `Lão rùa già` / `Rudra` - `Ta`/`Tao` | `Rance` - `Trẫm`/`Ta` |
| **85** | **Alice** (アリス) | Mascot sáng tạo của AliceSoft | `Nàng`, `Alice`, `nàng thỏ sáng tạo` | Chúng thần: `Thần Alice` | `Ả tác giả` / `Con thỏ Alice` - `Ta` | `Rance-san` - `Bổn thần`/`Alice` |

---

## 5. HỒ SƠ NHÂN VẬT CHI TIẾT: NGƯỜI KỂ CHUYỆN, XÃ HỘI & RANCE

### 5.1. Băng Cướp Rance & Nhóm Đồng Hành Cốt Lõi

#### 1. Sill Plain (シィル・プライン)
* **Thân phận & Bản chất**: Nô lệ độc quyền được Rance mua từ chợ nô lệ với giá rẻ mạt. Dịu dàng, nhẫn nhịn, hy sinh tuyệt đối, xem niềm vui của Rance là lẽ sống duy nhất của đời mình. Dù bị Rance bắt nạt, cốc đầu hay đòi quan hệ bất thình lình, Sill vẫn yêu Rance hơn cả sinh mạng.
* **Người kể chuyện / Lời dẫn (Storyteller Narration)**:
  - Danh xưng chuẩn: `Nàng`, `cô bé`, `Sill`, `tiểu nữ nô lệ`.
  - Tuyệt đối **KHÔNG dùng**: `nó`, `cô ta`, `ả`.
  - Khí chất dẫn: Luôn miêu tả nét dịu hiền, cam chịu nhưng ngập tràn tình yêu thương chân thành.
* **Mọi người xung quanh gọi Sill**:
  - Tướng lĩnh & Quân sĩ Leazas (Rick, Barres, Leila): Gọi là `Tiểu thư Sill` hoặc `Nương nương Sill` (họ tôn trọng vì biết Sill là người duy nhất kiềm chế được Rance).
  - Nữ hoàng Lia: Gọi là `Sill` hoặc ghen tuông gọi `con bé nô lệ của chàng`.
  - Maris, Shizuka, Maria: Gọi thân thiện là `Sill` hoặc `em Sill`.
  - Dân chúng / Người ngoài: Gọi là `Cô gái hầu cận tóc hồng`, `Tiểu thư đi cùng Rance`.
  - Kẻ thù: Gọi là `Con tin`, `Ả nô lệ`.
* **Xưng hô với Rance**:
  - Sill gọi Rance: `Chủ nhân Rance` (khi nói với người khác về ngài: `ngài Rance` / `ngài`), tự xưng `em`.
  - Rance gọi Sill: `Sill` / `Em` (khi gắt gỏng: `mày` / `con ngốc này`), tự xưng `ta` (hoặc `bố mày`).
* **Lỗi máy dịch cấm tuyệt đối**: Từ `Sill` trong tiếng Anh thường bị máy dịch nhầm thành *"ngưỡng cửa"* hoặc *"bệ cửa"* (window sill). Khi gặp phải sửa ngay thành tên riêng **Sill**!

#### 2. Soul Less (ソウル・レス)
* **Thân phận**: Nữ sơn tặc phó tướng trong băng cướp Rance. Hoang dã, ngổ ngáo, cuồng sát, thích bạo lực và đam mê tình dục phóng túng với Rance.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Soul`, `nữ tặc hoang dã`.
* **Mọi người xung quanh gọi Soul**: Băng cướp gọi là `Đại tỷ Soul` / `Phó tướng Soul`; lính đối phương gọi là `Ả nữ tặc điên loạn`.
* **Xưng hô với Rance**: Soul gọi Rance là `Đại ca Rance` / `Đại ca`, tự xưng `em` (khi bàn việc băng đảng: `tôi`). Rance xưng `ta` / `đại ca`, gọi `Soul` / `em` (hoặc `mày`).

#### 3. Bound Less (バウンド・レス)
* **Thân phận**: Đô vật khổng lồ, tay chân trung thành của Rance từ thuở hàn vi trong băng sơn tặc. Thẳng tính, ít suy nghĩ, bảo gì làm nấy.
* **Người kể chuyện / Lời dẫn**: `Gã`, `Bound`, `gã đô vật khổng lồ`.
* **Mọi người xung quanh gọi Bound**: Sơn tặc gọi là `Anh Bound`; binh lính gọi là `Tên hộ pháp cơ bắp`.
* **Xưng hô với Rance**: Bound gọi Rance là `Đại ca Rance` / `Đại ca`, tự xưng `tôi` / `em`. Rance xưng `ta` / `đại ca`, gọi `Bound` / `chú mày` / `ngươi`.

#### 4. Ma Kiếm Chaos (魔剣カオス)
* **Thân phận**: Thánh kiếm cổ đại bị phong ấn linh hồn biến thành ma kiếm tà dâm. Cực kỳ háo sắc, thích ngắm phụ nữ khỏa thân và cùng chí hướng dâm dật với Rance. Vũ khí duy nhất có thể chém rách Kết giới Bất tử của Ma Nhân.
* **Người kể chuyện / Lời dẫn**: `Nó`, `thanh ma kiếm`, `Chaos`, `thanh kiếm tà dâm`.
* **Mọi người xung quanh gọi Chaos**: Nikkou gọi là `Thanh kiếm đồi trụy` / `Kẻ sa đọa`; người khác gọi là `Thanh ma kiếm kỳ quái`.
* **Xưng hô với Rance**: Chaos xưng `bản kiếm` / `ta`, gọi Rance là `thằng nhãi dâm tặc` / `Rance`. Rance xưng `bố mày` / `ta`, gọi Chaos là `lão kiếm dâm` / `cây sắt vụn`.

---

### 5.2. Vương Quốc Leazas (Hoàng Gia, Tướng Lĩnh, Cận Vệ & Cung Đình)

#### 5. Lia Parapara Leazas (リア・パラパラ・リーザス)
* **Thân phận & Bản chất**: Nữ hoàng độc tôn của Vương quốc Leazas. Một yandere siêu cấp bạo liệt, cuồng si Rance đến độ sẵn sàng sát hại triệu người hoặc dâng cả vương quốc cho Rance chỉ để được hắn ôm vào lòng.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Nữ hoàng`, `Lia`, `nàng nữ hoàng cuồng si`. Tránh dùng `ả` trừ khi đứng từ góc nhìn của nạn nhân bị nàng tra tấn.
* **Mọi người xung quanh gọi Lia**:
  - Triều thần, tướng lĩnh Leazas (Barres, Rick, Leila): Gọi là `Bệ hạ`, `Nữ hoàng Bệ hạ`, `Nữ vương`.
  - Maris (tri kỷ): Gọi là `Nữ hoàng Lia`, `Bệ hạ` (khi chỉ có hai người: `Lia`).
  - Kanami: Gọi là `Bệ hạ` / `Nữ hoàng Lia`.
  - Dân chúng Leazas: Gọi tôn kính là `Nữ hoàng Lia`, `Bệ hạ anh minh`.
  - Nguyên thủ ngoại bang (Sheila, Gandhi): Gọi là `Nữ hoàng Leazas`, `Lia Parapara`.
  - Kẻ thù / Ma nhân: Gọi là `Ả nữ hoàng loài người`.
* **Xưng hô với Rance**:
  - Lia gọi Rance: `Chàng Rance` / `Chàng` / `Chàng yêu` (khi nũng nịu: `Anh yêu` / `Darling`), tự xưng `thiếp` / `em` / `Lia`.
  - Rance gọi Lia: `Lia` / `Nàng` / `Em` (khi rùng mình trước sự điên tình: `ả điên này`), tự xưng `ta`.
* **Lỗi máy dịch cấm tuyệt đối**:
  - *Darling* -> Bắt buộc: **`Chàng`** hoặc **`Chàng yêu`** (CẤM: "Em yêu").
  - *I love you* -> Bắt buộc: **`Thiếp yêu chàng`** hoặc **`Lia yêu chàng nhất trên đời`** (CẤM: "Anh yêu em").
  - *I came* -> Bắt buộc: **`Thiếp... ra rồi...`** (CẤM: "Tôi đến").

#### 6. Maris Amaryllis (マリス・アマリリス)
* **Thân phận**: Thị nữ trưởng thân cận của Lia, người thực tế nắm giữ toàn bộ công việc triều chính và điều hành ngân sách Leazas. Thanh lịch, điềm đạm, trí tuệ kiệt xuất.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Maris`, `nữ quan thanh lịch`, `thị nữ trưởng`.
* **Mọi người xung quanh gọi Maris**:
  - Lia: Gọi thân mật là `Maris`.
  - Triều đình & Tướng lĩnh (Barres, Rick, Ex): Gọi là `Quan tổng quản Maris`, `Thị nữ trưởng Maris`, `Cô Maris`.
  - Binh sĩ / Dân chúng: Gọi là `Quan lớn Maris`.
* **Xưng hô với Rance**: Maris gọi Rance là `Bệ hạ Rance` / `Ngài Rance` / `Bệ hạ`, tự xưng `tôi` / `thần`. Rance xưng `ta`, gọi `Maris` / `cô`.

#### 7. Leila Glaster (レイラ・グレクニィ)
* **Thân phận**: Đội trưởng Cận vệ Hoàng gia Leazas, nữ kiếm sĩ mạnh thứ hai vương quốc. Cực kỳ nghiêm cẩn, tôn trọng danh dự hiệp sĩ, lớn tuổi hơn Rance.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Leila`, `nữ đội trưởng`, `nữ hiệp sĩ`.
* **Mọi người xung quanh gọi Leila**: Cận vệ gọi là `Đội trưởng Leila`; Rick gọi là `Cô Leila`; Julia gọi là `Tiền bối Leila`.
* **Xưng hô với Rance**: Leila gọi Rance là `Ngài Rance` / `Bệ hạ`, tự xưng `tôi`. Rance xưng `ta`, gọi `Leila` / `cô` / `nàng`.

#### 8. Rick Addison (リック・アディスン)
* **Thân phận**: "Xích Quỷ" (Red Reaper), Đội trưởng Xích Quân, hiệp sĩ mạnh nhất Leazas. Cương trực, quả cảm, trung dũng vô song.
* **Người kể chuyện / Lời dẫn**: `Chàng`, `Rick`, `vị kiếm sĩ`, `Xích Quỷ`, `vị đại tướng trẻ`.
* **Mọi người xung quanh gọi Rick**: Binh sĩ gọi là `Tướng quân Rick`, `Đại tướng`; Menad gọi là `Đại nhân Rick` / `Anh Rick`; Kẻ thù gọi là `Xích Quỷ của Leazas`.
* **Xưng hô với Rance**: Rick gọi Rance là `Bệ hạ` / `Ngài Rance`, tự xưng `thần` / `tôi`. Rance xưng `ta`, gọi `Rick` / `ngươi`.

#### 9. Barres Provence (バレス・プロバンス)
* **Thân phận**: Lão tướng quân râu tóc bạc phơ, Tổng tư lệnh quân đội Leazas, dạn dày trận mạc, vừa là một chiến tướng vừa là một nhà chiến thuật kiệt xuất.
* **Người kể chuyện / Lời dẫn**: `Lão tướng`, `ông`, `Barres`, `vị tướng già`, `lão tướng quân râu bạc`.
* **Mọi người xung quanh gọi Barres**: Triều đình & Binh sĩ gọi là `Đại tướng quân Barres`, `Tổng tư lệnh`; Haurein gọi là `Cha` / `Phụ thân`.
* **Xưng hô với Rance**: Barres xưng `lão thần` / `thần`, gọi Rance là `Bệ hạ`. Rance xưng `ta`, gọi `lão già Barres` / `lão già` / `ngươi`.

#### 10. Cordoba & Ex Van
* **Cordoba**: Tướng thiết giáp khổng lồ, "Bức tường sắt của Leazas". Người kể chuyện gọi là `Cordoba`, `vị tướng thiết giáp`. Mọi người gọi là `Tướng quân Cordoba`. Xưng `thần`, gọi Rance là `Bệ hạ`. Rance gọi `Cordoba` / `ngươi`.
* **Ex Van**: Quân sư thiên tài Leazas. Người kể chuyện gọi là `Ex Van`, `vị quân sư trẻ`. Mọi người gọi là `Quân sư Ex`. Xưng `thần`, gọi Rance là `Bệ hạ`. Rance gọi `Ex` / `ngươi`.

#### 11. Menad & Haurein
* **Menad**: Phó tướng Xích Quân dưới quyền Rick. Tomboy ngoài mặt nhưng e thẹn trước Rance. Lời dẫn gọi là `Menad`, `cô`, `nữ phó tướng`. Binh sĩ gọi là `Phó tướng Menad`. Menad xưng `em` / `tôi`, gọi `ngài Rance`. Rance gọi `Menad` / `cô bé` / `em`.
* **Haurein**: Con gái cưng của Barres, nữ kiếm sĩ muốn khẳng định mình trước cha. Lời dẫn gọi là `Haurein`, `cô`. Barres gọi là `Con gái`. Haurein xưng `tôi`, gọi `Bệ hạ` / `ngài Rance`. Rance gọi `Haurein` / `cô em`.

#### 12. Melfeis & Julia Lindom
* **Melfeis**: Nữ pháp sư nhân từ, cứu chữa thương binh. Lời dẫn gọi là `nàng`, `Melfeis`, `nữ pháp sư nhân từ`. Thương binh gọi là `Thiên sứ Melfeis`. Xưng `em`, gọi `ngài Rance`. Rance gọi `Melfeis` / `em`.
* **Julia**: Tân Đội trưởng Cận vệ tóc vàng kế thừa Leila. Lời dẫn gọi là `cô bé`, `Julia`. Cận vệ gọi là `Đội trưởng Julia`. Xưng `em`, gọi `Bệ hạ Rance`. Rance gọi `Julia` / `nhóc con` / `em`.

#### 13. Rafalia, Arlcoate & Anaseru (Học Viện Kỵ Sĩ)
* **Rafalia**: Hiếu chiến, tự tin thái quá. Lời dẫn gọi là `cô`, `Rafalia`. Xưng `tôi`, gọi `Bệ hạ`. Rance gọi `Rafalia` / `cô em`.
* **Arlcoate**: Cực kỳ nhút nhát, sợ giao tiếp. Lời dẫn gọi là `cô bé`, `Arlcoate`. Xưng `em`, gọi `ngài Rance`. Rance gọi `Arlcoate` / `nhóc nhút nhát`.
* **Anaseru**: Nữ giáo quan nghiêm nghị huấn luyện binh sĩ. Lời dẫn gọi là `nàng`, `Anaseru`. Học viên gọi là `Giáo quan Anaseru`. Xưng `tôi`, gọi `Bệ hạ`. Rance gọi `Anaseru` / `cô`.

#### 14. Wendy & Elisabeth
* **Wendy**: Hầu gái hoàng cung tươi tắn yêu nghề. Lời dẫn gọi là `cô hầu gái nhỏ`, `Wendy`. Xưng `em`, gọi `chủ nhân Rance`. Rance gọi `Wendy` / `em`.
* **Elisabeth**: Nữ quý tộc cựu hoàng tộc Leazas. Lời dẫn gọi là `nàng`, `Elisabeth`. Xưng `tôi`, gọi `ngài Rance`. Rance gọi `Elisabeth` / `nàng`.

---

### 5.3. Ninja & Lực Lượng Điệp Báo

#### 15. Kentou Kanami (見当かなみ)
* **Thân phận**: Nữ ninja thân cận của Lia và Leazas. Thường xuyên bị Rance trêu chọc, lột đồ, sàm sỡ và quấy rối, nhưng trong lòng dần nảy sinh tình cảm phức tạp khó nói.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `cô`, `Kanami`, `nữ ninja`, `cô nàng ninja điệp báo`.
* **Mọi người xung quanh gọi Kanami**: Lia gọi là `Kanami`; Maris gọi là `cô Kanami`; Suzume gọi trêu là `Kanami-chan`.
* **Xưng hô với Rance**: Kanami gọi Rance là `Tên Rance khốn khiếp!`, `Đồ biến thái!`, `Tên ác quỷ!`, tự xưng `tôi`. Rance xưng `ta` / `bố mày`, gọi `Kanami` / `con nhóc ninja` / `mày`.

#### 16. Suzume (鈴女 - すずめ)
* **Thân phận**: Nữ ninja tự do, tinh nghịch, lươn lẹo, dâm đãng và hám tiền. Thích làm tình, coi chuyện phòng the là trò tiêu khiển vui vẻ.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Suzume`, `cô nhóc ninja tinh quái`, `nữ ninja tự do`.
* **Mọi người xung quanh gọi Suzume**: Kanami gọi là `Con điên Suzume!`; Sill gọi là `Chị Suzume`.
* **Xưng hô với Rance**: Suzume gọi Rance là `Rance` / `Chàng Rance`, tự xưng `bé Suzume` / `em`. Rance xưng `ta`, gọi `Suzume` / `con nhóc ranh`.

---

### 5.4. Thành Phố Tự Do Custom & Toushin City

#### 17. Maria Custard (マリア・カスタード)
* **Thân phận**: Nhà phát minh thiên tài phái Tulip, chế tạo khẩu pháo Tulip 1. Bạn thân kiêm người tình từ thuở đầu của Rance. Tính cách tsundere, thực tế, luôn miệng cằn nhằn nhưng sát cánh trọn đời.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `cô`, `Maria`, `nữ phát minh`, `cô nàng tsundere`.
* **Mọi người xung quanh gọi Maria**: Binh sĩ Tulip gọi là `Đại nhân Maria`; Shizuka gọi là `Maria`.
* **Xưng hô với Rance**: Maria gọi Rance là `Rance`, tự xưng `tôi`. Rance gọi `Maria`, tự xưng `ta` / `anh`.

#### 18. Shizuka Masou (魔想志津香)
* **Thân phận**: Nữ pháp sư thiên tài số một lục địa. Căm ghét đàn ông, băng thanh ngọc khiết, khinh miệt thói dâm loạn của Rance. Dù ghét Rance cay đắng nhưng số phận luôn buộc cô phải chạm trán hắn.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Shizuka`, `nữ pháp sư kiêu kỳ`, `thiên tài ma pháp`, `tiểu thư Masou`.
* **Mọi người xung quanh gọi Shizuka**: Giới pháp sư gọi tôn kính là `Đại pháp sư Shizuka`; Maria gọi là `Shizuka`; Sill gọi là `Chị Shizuka`.
* **Xưng hô với Rance**: Shizuka gọi Rance là `Tên khốn Rance`, `Tên dâm tặc`, `Đồ cặn bã`, tự xưng `tôi`. Rance gọi `Shizuka`, `cô`, `ả kiêu kỳ`, tự xưng `ta`.

#### 19. Milli Walkers & Mill Walkers
* **Milli (Chị gái)**: Nữ thủ lĩnh bạo dâm, bắt binh sĩ nam nữ phục vụ tình dục. Lời dẫn gọi là `ả`, `Milli`, `nữ chúa bạo dâm`. Binh sĩ gọi là `Nữ vương Milli`. Xưng `chị đây` / `bà`, gọi Rance là `cậu em` / `Rance`. Rance gọi là `mụ điên Milli` / `ả đàn bà đồi bại`.
* **Mill (Em gái)**: Ngây thơ trong sáng, thuần dưỡng ảo thú. Lời dẫn gọi là `cô bé`, `Mill`. Milli gọi là `Mill, em gái bé nhỏ`. Xưng `em`, gọi `anh Rance`. Rance gọi `Mill` / `bé con`.

#### 20. Ran, Merim & Merci
* **Ran**: Thám hiểm Toushin xui xẻo. Lời dẫn gọi là `Ran`, `cô`. Xưng `em` / `tôi`, gọi `ngài Rance`. Rance gọi `Ran` / `nhóc xui xẻo`.
* **Merim**: Cô thủ quỹ ngân hàng Custom. Lời dẫn gọi là `Merim`, `cô`. Xưng `em`, gọi `ngài Rance`.
* **Merci**: Cô gái tiếp tân lanh lợi. Lời dẫn gọi là `Merci`, `cô`. Xưng `em`, gọi `ngài Rance`.

---

### 5.5. Đế Chế Quân Sự Helman

#### 21. Sheila Helman (シーラ・ヘルマン)
* **Thân phận**: Hoàng đế bù nhìn của Helman, ngây thơ, quý phái nhưng bất lực trước nội loạn. Sau khi đất nước thất thủ, nàng trở thành chiến lợi phẩm bị Rance biến thành đồ chơi tình dục riêng.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Sheila`, `nữ hoàng đế nhỏ`, `cô bé hoàng tộc`.
* **Mọi người xung quanh gọi Sheila**: Triều thần & Binh sĩ Helman (Hubert, Lelyukov) gọi là `Bệ hạ`, `Nữ hoàng đế Bệ hạ`; Patton gọi là `Sheila` / `Muội muội`.
* **Xưng hô với Rance**: Sheila xưng `tôi` / `ta`, gọi Rance là `Ngài Rance`. Rance xưng `ta`, gọi `Sheila` / `Hoàng đế bé nhỏ` / `nàng` / `em`.

#### 22. Patton Misurugi (パットン・ミスルギ)
* **Thân phận**: Cựu Thái tử Helman bị phế truất, từ bỏ quyền lực trở thành quyền vương võ sĩ. Hào sảng, trọng danh dự, chỉ tin vào nắm đấm.
* **Người kể chuyện / Lời dẫn**: `Chàng`, `anh`, `Patton`, `gã võ sĩ quyền cước`, `cựu thái tử`.
* **Mọi người xung quanh gọi Patton**: Hubert gọi tôn kính là `Điện hạ Patton`; Sheila gọi là `Huynh trưởng`; Binh sĩ gọi là `Đại sư Patton`.
* **Xưng hô với Rance**: Patton xưng `ta` / `tôi`, gọi Rance là `Rance`. Rance xưng `ta` / `tao`, gọi `Patton` / `tên cơ bắp`.

#### 23. Hubert Lipton & Lelyukov
* **Hubert**: Hiệp sĩ danh dự mẫu mực, trung thành với Helman và Patton. Lời dẫn gọi là `chàng`, `Hubert`, `người hiệp sĩ mẫu mực`. Xưng `tôi`, gọi Rance là `ngài Rance`. Rance gọi `Hubert` / `ngươi`.
* **Lelyukov**: Lão tướng quân kiên trung phương Bắc. Lời dẫn gọi là `lão tướng`, `ông`, `Lelyukov`. Binh sĩ gọi là `Tướng quân Lelyukov`. Xưng `lão phu` / `tôi`, gọi Rance là `ngài Rance`. Rance gọi `lão tướng` / `ngươi`.

#### 24. Aristoles & Cream
* **Aristoles**: Cựu sát thủ huyền thoại, mưu lược gia quân sự tính toán không sai một phân. Lời dẫn gọi là `chàng`, `Aristoles`, `kỳ tài mưu lược`. Xưng `tôi`, gọi Rance là `ngài Rance`. Rance gọi `Aristoles` / `ngươi`.
* **Cream**: Nữ quân sư tài ba sắc sảo, trên giường ân ái cực kỳ nồng cháy và thích đấu trí. Lời dẫn gọi là `nàng`, `Cream`, `nữ quân sư tài ba`. Xưng `tôi`, gọi Rance là `ngài Rance`. Rance gọi `Cream` / `cô ả sắc sảo`.

#### 25. Sayori Unga (サヨリ・ウンガ)
* **Thân phận**: Tiểu thư kiêu kỳ dòng họ quý tộc Unga. Ban đầu khinh Rance là tên cướp thô bỉ, nhưng cơ thể nàng dần bị cự vật của Rance uốn nắn khuất phục.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Sayori`, `tiểu thư kiêu kỳ`.
* **Mọi người xung quanh gọi Sayori**: Gia nhân gọi là `Tiểu thư Sayori`.
* **Xưng hô với Rance**: Sayori xưng `tôi`, gọi Rance là `Tên cướp vô lại!` / `ngài Rance`. Rance xưng `ta`, gọi `Sayori` / `tiểu thư`.

---

### 5.6. Vương Quốc Ma Pháp Zeth

#### 26. Gandhi The Zeth (ガンジー・ザ・ゼス)
* **Thân phận**: Quốc vương Zeth, ma chiến binh hộ pháp khổng lồ. Tính tình bộc trực như trẻ con, hào sảng, cực kỳ hiếu chiến.
* **Người kể chuyện / Lời dẫn**: `Ông`, `Gandhi`, `lão vương khổng lồ`, `Quốc vương Zeth`.
* **Mọi người xung quanh gọi Gandhi**: Triều thần Zeth gọi là `Bệ hạ`, `Quốc vương Bệ hạ`; Magic gọi là `Phụ vương` / `Cha`.
* **Xưng hô với Rance**: Gandhi xưng `ta`, gọi Rance là `Rance`. Rance xưng `ta`, gọi `lão già Gandhi` / `ngươi`.

#### 27. Magic The Gandhi (マジック・ザ・ガンジー)
* **Thân phận**: Công chúa Zeth, con gái Gandhi, một trong Tứ Đại Lãnh Chúa. Pháp sư thiên tài, mang phong thái quý phái kiêu kỳ nhưng cực kỳ lúng túng trước sự sàm sỡ thô bạo của Rance.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Magic`, `cô công chúa quý phái`, `nàng pháp sư tài ba`.
* **Mọi người xung quanh gọi Magic**: Thần dân Zeth gọi là `Công chúa Magic`, `Điện hạ`; Tứ đại lãnh chúa gọi là `Lãnh chúa Magic`; Gandhi gọi là `Con gái rượu`.
* **Lỗi máy dịch cấm tuyệt đối**: Từ `Magic` trong kịch bản thường bị máy dịch nhầm thành *"Phép thuật"*. Bắt buộc sửa thành tên riêng **Magic**!
* **Xưng hô với Rance**: Magic xưng `tôi`, gọi Rance là `Ngài Rance` / `Tên thô bỉ`. Rance xưng `ta`, gọi `Magic` / `cô công chúa`.

#### 28. Yamada Chizuko, Nagi Raghav & Uspira
* **Chizuko**: Tứ Đại Lãnh Chúa, mặc váy dạ hội xông pha trận mạc. Lời dẫn gọi là `nàng`, `Chizuko`, `cô ả lập dị`. Binh sĩ gọi là `Lãnh chúa Chizuko`. Xưng `tôi`, gọi `ngài Rance`. Rance gọi là `ả dị hợm Chizuko`.
* **Nagi**: Tứ Đại Lãnh Chúa, độc hành vô cảm, đắm chìm trong ma pháp. Lời dẫn gọi là `nàng`, `Nagi`, `pháp sư độc hành`. Xưng `tôi`, gọi `Rance`. Rance gọi là `ả lơ đễnh Nagi`.
* **Uspira**: Tứ Đại Lãnh Chúa Zeth kỳ cựu. Lời dẫn gọi là `bà`, `nàng`, `Uspira`. Xưng `tôi`, gọi `ngài Rance`. Rance gọi là `bà cô ma pháp Uspira`.

#### 29. Café Artful, Papaya Server & Anis
* **Café Artful**: Quý cô quý tộc Zeth mê thời trang và ma thuật cao cấp. (Cấm nhầm thành "quán cà phê"). Lời dẫn gọi là `quý cô Café`. Xưng `tôi`, gọi `ngài Rance`.
* **Papaya Server**: Trưởng lão ma pháp tính tình tếu táo. (Cấm nhầm thành quả "đu đủ"). Lời dẫn gọi là `lão pháp sư Papaya`. Xưng `lão phu` / `tôi`, gọi `cậu Rance`.
* **Anis**: Nữ pháp sư tham tiền hám bạc siêu cấp. Lời dẫn gọi là `con nhóc hám tiền Anis`. Xưng `em`, gọi `đại gia Rance` / `ngài Rance`.

---

### 5.7. Quần Đảo Phong Kiến JAPAN

#### 30. Oda Nobunaga (織田信長)
* **Thân phận**: Lãnh chúa gia tộc Oda ở JAPAN, nhưng linh hồn và thể xác đã bị Quỷ vương độc ác tha hóa chiếm đoạt. Trùm cuối của chiến dịch JAPAN.
* **Người kể chuyện / Lời dẫn**: `Hắn`, `Nobunaga`, `tên quỷ vương`, `lãnh chúa bị tha hóa`.
* **Mọi người xung quanh gọi Nobunaga**: Gia thần gọi là `Chúa công`, `Đại nhân Nobunaga`; Kouhime gọi là `Huynh trưởng Nobunaga` / `Anh hai`.
* **Xưng hô với Rance**: Nobunaga xưng `ta`, gọi Rance là `tên sâu bọ`. Rance xưng `tao` / `bố mày`, gọi Nobunaga là `tên quỷ` / `Nobunaga`.

#### 31. Oda Kouhime (香姫 - こうひめ)
* **Thân phận**: Tiểu công chúa em gái út Nobunaga, ngây thơ, dịu dàng, trong sáng. Coi Rance như bầu trời và đấng cứu thế của mình.
* **Người kể chuyện / Lời dẫn**: `Cô bé`, `Kouhime`, `tiểu công chúa`, `nàng công chúa nhỏ`.
* **Mọi người xung quanh gọi Kouhime**: Gia thần gọi là `Công chúa Kou`, `Tiểu thư Kouhime`; Isoroku gọi là `Kou-chan` / `Tiểu thư Kou`.
* **Xưng hô với Rance**: Kouhime xưng `Kou` / `em`, gọi Rance là `Chủ nhân Rance`. Rance xưng `ta`, gọi `Kou` / `Kouhime` / `em`.

#### 32. Yamamoto Isoroku (山本五十六)
* **Thân phận**: Đệ nhất nữ cung thủ samurai JAPAN. Đoan trang, trinh liệt, coi trọng danh dự võ sĩ đạo, dành trọn tình cảm sắt son cho Rance.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Isoroku`, `nữ dũng tướng samurai`, `nàng cung thủ đoan trang`.
* **Mọi người xung quanh gọi Isoroku**: Binh sĩ JAPAN gọi là `Tướng quân Yamamoto`, `Đại nhân Isoroku`; Kouhime gọi là `Chị Isoroku`.
* **Xưng hô với Rance**: Isoroku xưng `Isoroku` / `thiếp` / `tôi`, gọi Rance là `Tướng quân Rance` / `Chàng`. Rance xưng `ta` / `anh`, gọi `Isoroku` / `em`.

#### 33. Makoto & Torako
* **Makoto**: Thiếu nữ tiệm bánh dango tinh nghịch. Lời dẫn gọi là `cô bé dango Makoto`. Xưng `em`, gọi `ngài Rance`.
* **Torako**: Nữ kiếm sĩ dũng mãnh Mikawa. Lời dẫn gọi là `Torako`, `cô nàng cọp con`. Xưng `tôi`, gọi `ngài Rance`.

---

### 5.8. Ma Giới, Ma Nhân & Ma Vương

#### 34. Kurusu Miki (来栖美樹) - Little Princess
* **Thân phận**: Nữ sinh Nhật Bản mang định mệnh trở thành Ma Vương (Demon Lord). Lúc bình thường hiền lành, nhút nhát, thích ăn bánh ngọt; khi biến thân Ma Vương thì ma lực vô hạn tàn phá thế giới.
* **Người kể chuyện / Lời dẫn**: `Cô bé`, `Miki`, `tiểu Ma Vương`, `nữ sinh ngây thơ`.
* **Mọi người xung quanh gọi Miki**:
  - Kentarou (người yêu): Gọi là `Miki`.
  - Sill: Gọi thân mật là `Miki-chan` / `em Miki`.
  - Ma nhân phe Hornet: Gọi tôn kính là `Ma Vương Bệ hạ`, `Little Princess`.
  - Ma nhân phe Kayblis: Gọi khinh miệt là `Con nhóc Ma Vương`, `Ma Vương bù nhìn`.
* **Xưng hô với Rance**: Miki xưng `em` / `Miki`, gọi Rance là `Chú Rance` / `Anh Rance`. Rance xưng `ta`, gọi `Miki` / `nhóc Ma Vương`.

#### 35. Ogawa Kentarou (小川健太郎) & Thánh Đao Nikkou
* **Kentarou**: Bạn trai Miki, nắm giữ Thánh Đao Nikkou. Kình địch cay đắng nhất của Rance vì Rance luôn ve vãn Miki.
  - Người kể chuyện gọi là: `Chàng trai`, `cậu ta`, `Kentarou`, `người cầm thánh đao`.
  - Miki gọi là: `Kentarou-kun` / `Kentarou`. Nikkou gọi là: `Chủ nhân Kentarou`.
  - Xưng hô với Rance: Kentarou xưng `tao`, gọi Rance là `Mày` / `Tên Rance chết tiệt!`. Rance xưng `tao` / `bố mày`, gọi Kentarou là `thằng ranh` / `mày`.
* **Thánh Đao Nikkou (日光)**: Thánh kiếm biết nói, nghiêm trang, đối địch tư tưởng với Ma kiếm Chaos. Lời dẫn gọi là `thanh thánh đao`, `Nikkou`. Xưng `ta` / `bản đao`, gọi Rance là `kẻ dâm tặc`.

#### 36. Kayblis & Camilla
* **Kayblis**: Ma Nhân mạnh nhất phe chủ chiến xâm lược, nham hiểm tàn ác vô nhân tính. Lời dẫn gọi là `hắn`, `Kayblis`, `gã ma nhân xảo quyệt`, `Đệ Nhất Ma Nhân`. Thuộc hạ gọi là `Đại nhân Kayblis`. Xưng `bản tọa` / `ta`, gọi Rance là `tên người hạ đẳng`. Rance gọi là `tên khốn Kayblis`.
* **Camilla**: Nữ Ma nhân Long tộc kiêu hãnh của Kayblis. Lời dẫn gọi là `nàng`, `Camilla`, `nữ ma nhân rồng`. Xưng `ta`, gọi Rance là `tên người ngông cuồng`. Rance gọi là `Camilla` / `con rồng cái`.

#### 37. Hornet & Silky
* **Hornet**: Nữ Ma nhân thủ lĩnh phe ôn hòa, bảo hộ Ma Vương chân chính. Lời dẫn gọi là `nàng`, `Hornet`, `nữ chúa ma nhân`. Thuộc hạ gọi tôn kính là `Ngài Hornet`, `Hornet-sama`. Xưng `ta`, gọi `Rance` / `con người`.
* **Silky**: Nữ Ma nhân băng giá trầm mặc phò tá Hornet. Lời dẫn gọi là `nàng`, `Silky`, `ả ma nhân băng giá`. Xưng `ta`, gọi `Rance`.

#### 38. Satella (魔人サテラ)
* **Thân phận**: Nữ Ma nhân tạo Hộ vệ. Ban đầu khinh miệt loài người sâu bọ; sau khi thua cược bị Rance đè ra làm tình và dần mê mẩn khoái cảm nhục dục của hắn.
* **Người kể chuyện / Lời dẫn**: `Nàng`, `Satella`, `ả ma nhân kiêu hãnh`, `nữ ma nhân hộ vệ`.
* **Mọi người xung quanh gọi Satella**: Hornet gọi là `Satella`; Ma quân gọi là `Đại nhân Satella`; Sill gọi là `Cô Satella`.
* **Xưng hô với Rance**: Satella xưng `ta`, gọi Rance là `Tên con người hạ đẳng` (về sau gọi `Rance`). Rance xưng `ta`, gọi `Satella` / `ả ma nhân`.

#### 39. Các Ma Nhân Khác
* **Saizel & Hawzel**: Cặp chị em có cánh Ngụy Thiên Thần. Lời dẫn gọi là `hai ả`, `chị em thiên thần giả`.
* **Warg**: Ma nhân mộng giới hình hài bé gái ma quái. Lời dẫn gọi là `nó`, `Warg`.
* **Galtia**: Ma nhân háu ăn to lớn chỉ mê ẩm thực. Lời dẫn gọi là `gã`, `tên ma nhân háu ăn`.
* **Megalas**: Ma nhân tộc Horus bay lượn siêu thanh. Lời dẫn gọi là `hắn`, `Megalas`.
* **Medusa**: Ma nhân xà nữ ánh nhìn hóa đá. Lời dẫn gọi là `ả`, `Medusa`, `ả rắn độc`.
* **Kesselring**: Ma nhân ma cà rồng quý tộc cai quản bóng đêm. Lời dẫn gọi là `hắn`, `bá tước bóng đêm Kesselring`.
* **Babora**: Ma nhân khổng lồ như ngọn núi. Lời dẫn gọi là `tên cự thạch Babora`.
* **Redeye**: Ma nhân độc nhãn ẩn thân bóng tối. Lời dẫn gọi là `tên sát thủ chột mắt Redeye`.

---

### 5.9. Các Chủng Tộc Bí Ẩn: Tộc Nữ Tiên Kalar & Tộc Đất Nung Haniwa

#### 40. Tộc Nữ Tiên Kalar (カラー族)
* **Pastel Kalar (パステル・カラー)**: Nữ hoàng Kalar kiêu hãnh, căm thù đàn ông tột cùng. Sau bị Rance thị tẩm và sinh ra công chúa Reset Kalar. Lời dẫn gọi là `nàng`, `Pastel`, `Nữ hoàng Kalar`. Tộc nhân gọi là `Nữ hoàng Bệ hạ`. Xưng `ta`, gọi Rance là `tên người thô bỉ`.
* **Somita (ソミタ)**: Chiến binh canh giữ rừng thiêng. Lời dẫn gọi là `nàng`, `Somita`. Xưng `tôi`, gọi `ngài Rance`.

#### 41. Tộc Đất Nung Haniwa (ハニー)
* **Đại vương Mars (ハニー大王マーズ)**: Vua Haniwa thích tổ chức diễu hành Daimyo tốn kém tiền của. Lời dẫn gọi là `lão`, `ông`, `Đại vương Mars`. Thần dân kêu `Đại vương Mars (Haniwa~)`. Xưng `ta (Haniwa~)`, gọi `Rance`. Rance gọi là `lão tượng đất`.

---

### 5.10. Đấng Sáng Tạo, Thần Linh & Mascots

#### 42. Rudrasaum (ルドラサウム - Rudra)
* **Bản chất**: Đấng Sáng Tạo tối cao của vũ trụ Rance. Thực thể cá voi vũ trụ khổng lồ tạo ra thế giới và các chủng tộc chỉ để tiêu khiển. Lời dẫn gọi là `Đấng Sáng Tạo Rudrasaum`, `thực thể tối cao`. Xưng `Trẫm` / `Ta`, gọi con người là sinh vật nhỏ bé. Rance gọi là `Lão rùa già` / `Rudra`.

#### 43. Alice (アリス - Đấng Sáng Tạo AliceSoft)
* **Bản chất**: Mascot thỏ đại diện hãng game AliceSoft, thần bảo hộ và kiến tạo thế giới game. Ngụ tại Dinh thự Alice. Lời dẫn gọi là `nàng`, `Alice`, `nàng thỏ sáng tạo`. Xưng `bổn thần` / `Alice`, gọi Rance là `Rance-san`. Rance gọi là `ả tác giả` / `con thỏ Alice`.

---

### 5.11. Các Nữ Nhân & Nhân Vật Phụ Đặc Biệt Khác
* **Elena**: Nữ tu sĩ AL Giáo hoàn lương. Lời dẫn gọi là `nàng tu sĩ Elena`. Xưng `em`, gọi `ngài Rance`.
* **Saitou**: Búp bê sống Shangri-La. Lời dẫn gọi là `cô búp bê nhỏ Saitou`. Xưng `em`, gọi `chủ nhân Rance`.
* **Saulnia**: Thiếu nữ Kogal da nâu ngổ ngáo. Lời dẫn gọi là `cô nhóc da nâu Saulnia`. Xưng `em` / `tôi`, gọi `anh Rance`.
* **Martina**: Nữ quý tộc thương nhân sắc sảo. Lời dẫn gọi là `tiểu thư Martina`. Xưng `tôi`, gọi `ngài Rance`.
* **Katyusha**: Nữ học giả thông thái cổ vật. Lời dẫn gọi là `nữ học giả Katyusha`. Xưng `tôi`, gọi `ngài Rance`.
* **Aya**: Nữ y tá dịu hiền. Lời dẫn gọi là `cô y tá Aya`. Xưng `em`, gọi `ngài Rance`.
* **Mokomoko**: Thú nhân lông xù đáng yêu kêu "Moko~". Lời dẫn gọi là `bé con Mokomoko`. Xưng `em`, gọi `ngài Rance`.
* **Shariella**: Thiếu nữ quý tộc thanh tú nhu mì. Lời dẫn gọi là `tiểu thư Shariella`. Xưng `em`, gọi `ngài Rance`.

---

## 6. MA TRẬN QUAN HỆ & XƯNG HÔ CHÉO GIỮA CÁC NHÂN VẬT CHỦ CHỐT

Bảng ma trận dưới đây quy định chính xác xưng hô 2 chiều cho **toàn bộ các cặp nhân vật chủ chốt** khi giao tiếp trực tiếp với nhau:

| Cặp Nhân Vật | Tính Chất Mối Quan Hệ | Nhân Vật A Gọi B (Xưng gì) | Nhân Vật B Gọi A (Xưng gì) | Sắc Thái & Hoàn Cảnh Điển Hình |
| :--- | :--- | :--- | :--- | :--- |
| **Sill & Lia** | Tình địch / Chủ - Khách hoàng gia | **Sill** gọi Lia: `Nữ hoàng Lia` / `Bệ hạ` (xưng `em`) | **Lia** gọi Sill: `Sill` / `con bé nô lệ` (xưng `ta`) | Lia ghen tuông điên cuồng vì Rance cưng chiều Sill, nhưng miễn cưỡng chấp nhận. Sill luôn lễ phép, cam chịu. |
| **Sill & Maris** | Bằng hữu thân thiện chốn cung đình | **Sill** gọi Maris: `Cô Maris` / `Chị Maris` (xưng `em`) | **Maris** gọi Sill: `Cô Sill` / `Sill` (xưng `tôi`) | Maris quý mến đức tính nhẫn nhịn và sự chăm sóc chu đáo của Sill dành cho Rance. |
| **Sill & Kanami** | Bạn cùng khổ (đều bị Rance bắt nạt) | **Sill** gọi Kanami: `Cô Kanami` / `Kanami-chan` (xưng `em`) | **Kanami** gọi Sill: `Sill` (xưng `tôi`) | Cùng chia sẻ nỗi khổ bị Rance quấy rối; Kanami khuyên Sill bỏ trốn nhưng Sill từ chối. |
| **Sill & Shizuka** | Bạn tri kỷ thuở đầu / Bảo bọc | **Sill** gọi Shizuka: `Chị Shizuka` / `Cô Shizuka` (xưng `em`) | **Shizuka** gọi Sill: `Sill` / `em gái ngốc` (xưng `tôi` / `chị`) | Shizuka luôn thương cảm cho số phận nô lệ của Sill, tức giận vì Rance bóc lột Sill quá đáng. |
| **Sill & Maria** | Bạn thân kỳ cựu từ Custom | **Sill** gọi Maria: `Chị Maria` / `Cô Maria` (xưng `em`) | **Maria** gọi Sill: `Sill` (xưng `tôi`) | Maria động viên Sill, khuyên Sill không nên quá nhẫn nhục trước các trò biến thái của Rance. |
| **Sill & Miki** | Chị em đồng cảnh ngộ / Thân thiết | **Sill** gọi Miki: `Miki-chan` / `Em Miki` (xưng `chị` / `em`) | **Miki** gọi Sill: `Chị Sill` (xưng `em` / `Miki`) | Cả hai cùng thích làm bánh, tính cách ngây thơ hiền lành, an ủi lẫn nhau khi Rance giở trò. |
| **Lia & Maris** | Quân thần / Chị em tri kỷ từ nhỏ | **Lia** gọi Maris: `Maris` (xưng `ta` / `Lia`) | **Maris** gọi Lia: `Nữ hoàng Lia` / `Bệ hạ` (xưng `thần` / `tôi`; khi riêng tư: `Lia`) | Maris là người duy nhất dám và có thể can gián những cơn điên tình cuồng sát của Lia. |
| **Lia & Leila** | Quân vương & Cận vệ trung thành | **Lia** gọi Leila: `Đội trưởng Leila` / `Leila` (xưng `ta`) | **Leila** gọi Lia: `Bệ hạ` / `Nữ hoàng` (xưng `thần` / `tôi`) | Leila trung thành phụng sự ngai vàng Leazas, bảo vệ Lia trước mọi hiểm họa thích khách. |
| **Lia & Rick** | Quân vương & Đại tướng tiên phong | **Lia** gọi Rick: `Tướng quân Rick` / `Rick` (xưng `ta`) | **Rick** gọi Lia: `Bệ hạ` (xưng `thần`) | Lia tin tưởng giao phó Xích Quân cho Rick mở đường máu trên sa trường. |
| **Lia & Barres** | Quân vương & Lão thần rường cột | **Lia** gọi Barres: `Lão tướng quân Barres` / `Đại tướng` (xưng `ta`) | **Barres** gọi Lia: `Bệ hạ` (xưng `lão thần` / `thần`) | Barres nhìn Lia lớn lên từ bé, coi Lia vừa là nữ quân vương vừa như cháu gái hoàng gia. |
| **Lia & Kanami** | Chủ nhân tàn nhẫn & Ninja sai vặt | **Lia** gọi Kanami: `Kanami` / `con nhóc ăn hại` (xưng `ta`) | **Kanami** gọi Lia: `Bệ hạ` / `Nữ hoàng Lia` (xưng `tôi`) | Lia coi Kanami là công cụ tình báo và thường xuyên "gả bán" Kanami cho Rance giải tỏa dục vọng. |
| **Lia & Sheila** | Hai Nữ hoàng / Đối thủ chính trị | **Lia** gọi Sheila: `Nữ hoàng đế Sheila` / `Con bé bù nhìn` (xưng `ta`) | **Sheila** gọi Lia: `Nữ hoàng Lia` (xưng `tôi` / `ta`) | Lia coi thường sự yếu đuối của Sheila, đe dọa biến Helman thành chư hầu phục dịch Rance. |
| **Lia & Magic** | Ngoại giao hoàng tộc / Cạnh tranh | **Lia** gọi Magic: `Công chúa Magic` (xưng `ta`) | **Magic** gọi Lia: `Nữ hoàng Lia` (xưng `tôi`) | Giao hảo đồng minh chống Ma Nhân, nhưng Lia ngấm ngầm canh chừng không để Magic cướp Rance. |
| **Maris & Leila** | Bộ đôi trụ cột nội chính & quân sự | **Maris** gọi Leila: `Đội trưởng Leila` / `Leila` (xưng `tôi`) | **Leila** gọi Maris: `Thị nữ trưởng Maris` / `Maris` (xưng `tôi`) | Tương kính lẫn nhau, cùng phối hợp duy trì trật tự cung đình Leazas. |
| **Maris & Rick** | Tham mưu trưởng & Đại tướng quân | **Maris** gọi Rick: `Tướng quân Rick` (xưng `tôi`) | **Rick** gọi Maris: `Quan tổng quản Maris` (xưng `tôi`) | Trao đổi quân lương, khí tài chiến dịch và phối hợp tác chiến công thành. |
| **Maris & Barres** | Trí mưu nội triều & Trải nghiệm sa trường | **Maris** gọi Barres: `Lão tướng quân` (xưng `tôi` / `cháu`) | **Barres** gọi Maris: `Cô Maris` / `Thị nữ trưởng` (xưng `lão phu`) | Cực kỳ kính trọng tuổi tác và cống hiến trọn đời của nhau cho đất nước. |
| **Rick & Leila** | Kỳ phùng địch thủ / Bạn đồng liêu | **Rick** gọi Leila: `Đội trưởng Leila` / `Cô Leila` (xưng `tôi`) | **Leila** gọi Rick: `Tướng quân Rick` / `Rick` (xưng `tôi`) | Hai kiếm sĩ mạnh nhất Leazas, vừa là đồng đội vào sinh ra tử vừa cạnh tranh tài nghệ. |
| **Rick & Barres** | Hậu bối tài ba & Tiền bối đại thụ | **Rick** gọi Barres: `Đại tướng quân Barres` / `Tiền bối` (xưng `tôi` / `Rick`) | **Barres** gọi Rick: `Cậu Rick` / `Tướng quân Rick` (xưng `ta` / `lão phu`) | Barres truyền dạy kinh nghiệm trận mạc, Rick kính trọng Barres như người thầy quân sự. |
| **Rick & Menad** | Chủ tướng uy phong & Phó tướng si tình | **Rick** gọi Menad: `Menad` / `Phó tướng Menad` (xưng `ta` / `tôi`) | **Menad** gọi Rick: `Tướng quân Rick` / `Đại nhân Rick` (xưng `em` / `tôi`) | Rick nghiêm khắc rèn giũa Menad; Menad ngầm mến mộ Rick nhưng trước mặt lại tỏ ra vụng về. |
| **Rick & Cordoba** | Mũi kiếm công kích & Khiên sắt phòng ngự | **Rick** gọi Cordoba: `Tướng quân Cordoba` (xưng `tôi`) | **Cordoba** gọi Rick: `Tướng quân Rick` (xưng `tôi`) | Bộ đôi "Kiếm - Khiên" hoàn mỹ trên chiến trường Leazas. |
| **Barres & Haurein** | Cha ruột nghiêm khắc & Con gái cưng | **Barres** gọi Haurein: `Haurein` / `Con gái` (xưng `cha` / `ta`) | **Haurein** gọi Barres: `Thưa cha` / `Phụ thân` (xưng `con`) | Barres lo lắng cho tính hiếu thắng của con; Haurein nỗ lực lập công để cha tự hào. |
| **Barres & Ex Van** | Lão tướng dày dạn & Quân sư trẻ tuổi | **Barres** gọi Ex: `Cậu Ex` / `Quân sư Ex` (xưng `lão phu`) | **Ex** gọi Barres: `Lão tướng quân` (xưng `tôi` / `Ex`) | Ex vạch kế hoạch, Barres điều phối đại quân thực thi chuẩn xác. |
| **Kanami & Suzume** | Ninja chính quy & Ninja tự do quái dị | **Kanami** gọi Suzume: `Con điên Suzume!` / `Đồ biến thái!` (xưng `tôi`) | **Suzume** gọi Kanami: `Kanami-chan` / `Bé Kanami` (xưng `bé Suzume` / `chị`) | Suzume thích trêu chọc chuyện phòng the của Kanami với Rance khiến Kanami phát điên. |
| **Maria & Shizuka** | Đôi bạn thân chí cốt từ Custom | **Maria** gọi Shizuka: `Shizuka` (xưng `tôi` / `mình`) | **Shizuka** gọi Maria: `Maria` (xưng `tôi` / `mình`) | Đôi bạn tri kỷ cùng nhau trải qua hoạn nạn, luôn sát cánh kiềm chế các trò đồi trụy của Rance. |
| **Maria & Magic** | Nhà công nghệ Tulip & Pháp sư hoàng tộc | **Maria** gọi Magic: `Công chúa Magic` / `Magic` (xưng `tôi`) | **Magic** gọi Maria: `Cô Maria` (xưng `tôi`) | Trao đổi về kết hợp khoa học kỹ thuật và ma thuật Zeth chế tạo pháo ma pháp. |
| **Shizuka & Magic** | Hai thiên tài ma pháp đệ nhất lục địa | **Shizuka** gọi Magic: `Công chúa Magic` / `Magic` (xưng `tôi`) | **Magic** gọi Shizuka: `Cô Masou` / `Đại pháp sư Shizuka` (xưng `tôi`) | Vừa ngưỡng mộ vừa cạnh tranh ngầm về học thuật và lượng mana hủy diệt. |
| **Shizuka & Nagi** | Đồng môn ma pháp / Khắc khẩu | **Shizuka** gọi Nagi: `Nagi` / `Cô ả lơ đễnh` (xưng `tôi`) | **Nagi** gọi Shizuka: `Shizuka` (xưng `tôi`) | Nagi chỉ quan tâm thí nghiệm ma thuật khiến Shizuka nhiều lần cạn lời. |
| **Patton & Sheila** | Anh em ruột cựu hoàng tộc Helman | **Patton** gọi Sheila: `Sheila` / `Muội muội` (xưng `ta` / `anh`) | **Sheila** gọi Patton: `Huynh trưởng Patton` / `Anh hai` (xưng `muội` / `em`) | Patton đau lòng vì không bảo vệ được Sheila khỏi bàn tay Rance; Sheila tha thứ cho anh. |
| **Patton & Hubert** | Chủ tướng cũ & Cận thần trung kiên | **Patton** gọi Hubert: `Hubert` (xưng `ta` / `tôi`) | **Hubert** gọi Patton: `Điện hạ Patton` (xưng `thần` / `tôi`) | Hubert quyết tâm đi theo Patton dù Patton đã từ bỏ ngôi vị để trở thành võ sĩ. |
| **Patton & Gandhi** | Hai dũng tướng cơ bắp hào sảng | **Patton** gọi Gandhi: `Lão vương Gandhi` / `Gandhi` (xưng `ta`) | **Gandhi** gọi Patton: `Nhóc Patton` / `Võ sĩ Patton` (xưng `ta`) | Đam mê tỉ thí sức mạnh cơ bắp và đấm đá tay đôi, nói chuyện sòng phẳng. |
| **Gandhi & Magic** | Cha bộc trực & Con gái quý phái | **Gandhi** gọi Magic: `Magic` / `Con gái rượu` (xưng `cha` / `ta`) | **Magic** gọi Gandhi: `Phụ vương` / `Cha` (xưng `con`) | Magic thường xuyên xấu hổ và đau đầu trước những trò quậy phá bộc trực của cha. |
| **Magic & Chizuko** | Công chúa lãnh đạo & Lãnh chúa lập dị | **Magic** gọi Chizuko: `Chizuko` / `Lãnh chúa Chizuko` (xưng `tôi`) | **Chizuko** gọi Magic: `Công chúa Magic` / `Điện hạ` (xưng `tôi`) | Chizuko phục tùng hoàng tộc Zeth nhưng vẫn giữ phong cách mặc váy dạ hội ra trận. |
| **Kouhime & Nobunaga**| Em gái nhỏ & Anh trai (trước tha hóa) | **Kouhime** gọi Nobunaga: `Huynh trưởng Nobunaga` / `Anh hai` (xưng `Kou` / `em`) | **Nobunaga** gọi Kouhime: `Kou` / `Kouhime` (xưng `ta` / `huynh`) | Tình anh em ruột thịt sâu nặng trước khi Nobunaga bị ác ma đoạt xác. |
| **Kouhime & Isoroku** | Tiểu công chúa & Nữ hộ vệ trung trinh | **Kouhime** gọi Isoroku: `Chị Isoroku` (xưng `Kou` / `em`) | **Isoroku** gọi Kouhime: `Công chúa Kou` / `Tiểu thư Kou` (xưng `Isoroku` / `thần`) | Isoroku thề bảo vệ Kouhime đến giọt máu cuối cùng trước hiểm họa diệt vong JAPAN. |
| **Miki & Kentarou** | Cặp tình nhân học sinh Nhật Bản | **Miki** gọi Kentarou: `Kentarou-kun` / `Kentarou` (xưng `em` / `Miki` / `tớ`) | **Kentarou** gọi Miki: `Miki` (xưng `anh` / `tớ`) | Tình yêu thuần khiết, sâu sắc. Kentarou sẵn sàng đối đầu cả Ma giới và Rance để bảo vệ Miki. |
| **Kentarou & Nikkou** | Chủ nhân sử dụng & Linh hồn Thánh Đao | **Kentarou** gọi Nikkou: `Đao Nikkou` / `Bác Nikkou` (xưng `cháu` / `tôi`) | **Nikkou** gọi Kentarou: `Kentarou` / `Chủ nhân` (xưng `ta` / `bản đao`) | Nikkou hướng dẫn Kentarou kiếm thuật và giữ vững đạo đức diệt quỷ. |
| **Chaos & Nikkou** | Hai thanh kiếm cổ đại đối địch tư tưởng | **Chaos** gọi Nikkou: `Thanh sắt cổ hủ` / `Nikkou` (xưng `bản kiếm`) | **Nikkou** gọi Chaos: `Thanh kiếm đồi trụy` / `Chaos` (xưng `ta`) | Chửi bới nhau không ngớt về chuyện tình dục và chính nghĩa mỗi khi chạm mặt. |
| **Kayblis & Camilla** | Thống soái tàn bạo & Nữ tướng thân cận | **Kayblis** gọi Camilla: `Camilla` (xưng `bản tọa`) | **Camilla** gọi Kayblis: `Ngài Kayblis` (xưng `tôi` / `ta`) | Camilla phò tá Kayblis vì lý tưởng Ma nhân thống trị, nhưng ghét thói bẩn thỉu của hắn. |
| **Kayblis & Hornet** | Kẻ phản đồ xâm lược & Lãnh tụ ôn hòa | **Kayblis** gọi Hornet: `Ả đàn bà yếu đuối` / `Hornet` (xưng `bản tọa`) | **Hornet** gọi Kayblis: `Tên phản đồ Kayblis` / `Ngươi` (xưng `ta`) | Thù hận sâu sắc không đội trời chung, phân chia Ma giới thành hai chiến tuyến rực lửa. |
| **Hornet & Silky** | Nữ chúa tôn kính & Hộ vệ băng tuyết | **Hornet** gọi Silky: `Silky` (xưng `ta`) | **Silky** gọi Hornet: `Hornet-sama` / `Ngài Hornet` (xưng `tôi`) | Silky sẵn sàng hy sinh tính mạng và linh hồn để bảo vệ lý tưởng của Hornet. |
| **Hornet & Satella** | Lãnh tụ bảo hộ & Ma nhân hộ vệ | **Hornet** gọi Satella: `Satella` (xưng `ta`) | **Satella** gọi Hornet: `Hornet-sama` / `Ngài Hornet` (xưng `tôi` / `ta`) | Cùng thuộc phe bảo vệ Ma Vương chân chính; Satella kính phục tấm lòng của Hornet. |
| **Pastel & Somita** | Nữ hoàng Kalar & Nữ chiến binh hộ vệ | **Pastel** gọi Somita: `Somita` (xưng `ta`) | **Somita** gọi Pastel: `Nữ hoàng Bệ hạ` / `Đại nhân Pastel` (xưng `thần` / `tôi`) | Tuyệt đối trung thành, canh giữ sự thuần khiết của Rừng Kalar trước loài người. |

---

## 7. QUY CHUẨN PHÂN CẢNH HẬU CUNG & NGÔN NGỮ PHÒNG THE (H-SCENES)

Phân cảnh ân ái 18+ là linh hồn của dòng game Rance. Các lỗi máy dịch tự động thường phá hỏng hoàn toàn bầu không khí gợi cảm. Khi dịch hoặc hiệu đính các phân cảnh này, **bắt buộc tuân thủ nghiêm ngặt các quy tắc sau**:

### 7.1. Danh Sách Lỗi Máy Dịch Cấm Tuyệt Đối

1. **Từ "came" / "I came"**:
   - ❌ **CẤM**: *"Tôi đến"*, *"Tôi đã đến"*, *"Tôi tới rồi"*.
   - ✅ **BẮT BUỘC DỊCH**: **`Thiếp... ra rồi...`** / **`Em... lên đỉnh rồi...`** / **`Ra... sướng quá ra mất rồi...`** / **`A... em bắn rồi!`**
2. **Từ "Darling" khi nữ nhân gọi Rance**:
   - ❌ **CẤM**: *"Em yêu"* (Lỗi đảo lộn giới tính của máy dịch khi nữ gọi nam).
   - ✅ **BẮT BUỘC DỊCH**: **`Chàng`** / **`Chàng yêu`** / **`Anh yêu`** / **`Chàng Rance ơi`**.
3. **Từ "I love you" khi nữ nhân thổ lộ trong lúc ân ái**:
   - ❌ **CẤM**: *"Anh yêu em"*, *"Tôi yêu bạn"*.
   - ✅ **BẮT BUỘC DỊCH**: **`Thiếp yêu chàng...`** / **`Em yêu anh...`** / **`Lia yêu chàng nhất trên đời!`**
4. **Từ "Take that!" của Rance khi dập hông / thúc mạnh**:
   - ❌ **CẤM**: *"Lấy cái đó đi!"*.
   - ✅ **BẮT BUỘC DỊCH**: **`Nếm mùi này!`** / **`Đỡ lấy này!`** / **`Xem đại pháo của ta đây!`**
5. **Đại từ xưng hô của Rance trên giường**:
   - ❌ **CẤM**: *"Tôi - bạn"*, *"anh - em"* sến súa kiểu phim tình cảm.
   - ✅ **BẮT BUỘC DỊCH**: Tự xưng **`Ta`** (khi cuồng nhiệt: **`Bố mày`** / **`Ông đây`**); gọi đối phương là **`Em`** / **`Nàng`** / **`Con nhóc`** / **`Ả dâm đãng`**.

---

### 7.2. Từ Vựng Nhục Cảm & Cơ Thể Học Phòng The

| Thuật Ngữ Gốc (EN / JP) | Bản Dịch Tiếng Việt Chuẩn | Bối Cảnh & Ngữ Cảnh Sử Dụng |
| :--- | :--- | :--- |
| **Hyper weapon (ハイパー兵器)** | Siêu vũ khí / Đại pháo | Cách Rance tự hào gọi cự vật cương cứng khổng lồ của mình. |
| **Cock / Dick (ペニス / 男根)** | Cự vật / Dương vật / Đại pháo | Tránh dùng từ quá chợ búa trong văn miêu tả trữ tình; chỉ dùng lời thô khi Rance quát dọa. |
| **Pussy / Crotch (秘部 / 蜜壺 / 膣)**| Nơi mật ngọt / Âm hộ / Hoa huyệt / Khe kín / Cô bé | Miêu tả nơi thầm kín của nữ giới đang ướt đẫm khát khao. |
| **Climax / Orgasm (絶頂 / 快楽)** | Cực khoái / Lên đỉnh / Xuất tinh | Trạng thái đạt đỉnh cao của khoái lạc thể xác. |
| **Thrust / Rocking hips (突く / 腰を振る)**| Thúc mạnh / Dập hông liên hồi / Đâm sâu | Chuyển động giao hoan mãnh liệt, cuồng bạo của Rance. |
| **Sopping / Wet (びしょ濡れ / 蜜)** | Ướt đẫm / Nhơm nhớp / Mật ngọt tuôn trào | Dịch nhờn hưng phấn tràn ngập nơi hạ bộ của nữ nhân. |
| **White fluid / Semen (白濁液 / 精液)**| Tinh hoa trắng đục / Dòng bạch dịch / Tinh dịch | Dịch sinh mệnh bắn ra ngập tràn khi Rance xuất tinh. |
| **Flesh on flesh (肉のぶつかる音)**| Tiếng da thịt va chạm dữ dội | Tiếng bạch bạch liên hoàn khi thân thể va đập lúc ân ái. |

---

### 7.3. Sắc Thái Lời Thoại Theo Tính Cách Nữ Nhân Khi Ân Ái
* **Lia (Cuồng yêu Yandere)**: Rên rỉ trong đê mê cuồng nhiệt, sẵn sàng trao cả thế giới cho Rance:
  - *"Chàng yêu... mạnh nữa lên... thiếp là của chàng... nếu chàng muốn thế giới... chúng ta sẽ cùng nhau chinh phục nó...!"*
* **Sill (Nô lệ phục tùng)**: Ngoan ngoãn, vừa đau đớn vừa ngập tràn hạnh phúc:
  - *"Chủ nhân Rance... ư... sướng quá... em... em ra mất rồi..."*
* **Shizuka / Kanami (Tsundere chống cự bị khuất phục)**: Ban đầu cắn răng chửi bới, sau bị khoái cảm đánh gục:
  - *"Dừng lại... tên dâm tặc... đừng chạm vào đó... á... không được... tha cho tôi... aahn!"*
* **Sheila (Hoàng đế thất trận nhút nhát)**: Khóc nấc vì xấu hổ nhưng cơ thể không cưỡng lại được:
  - *"Ngài Rance... xin ngài... nhẹ một chút... tôi... tôi không chịu nổi nữa rồi..."*
* **Isoroku (Samurai đoan trang trinh liệt)**: Xấu hổ giữ kẽ lúc đầu, lúc cao trào thì run rẩy đón nhận:
  - *"Tướng quân... thiếp... không thể kìm nén được nữa... xin chàng hãy ban phát cho Isoroku..."*

---

## 8. HỆ THỐNG THUẬT NGỮ CHUẨN (TERMINOLOGY GLOSSARY)

### 8.1. Địa Danh, Bản Đồ Chiến Lược & Mê Cung

#### Các Vùng Đất & Lãnh Thổ Bản Đồ (Map Regions)
- **Leazas Castle (リーザス城)**: Thành Leazas (Hoàng thành Leazas)
- **Parapara Fortress (パラパラ砦)**: Pháo đài Parapara
- **North (北部)**: Miền Bắc
- **South (南部)**: Miền Nam
- **West (西部)**: Miền Tây
- **Oku (奥)**: Vùng Nội Địa Oku
- **Ys (イース)**: Vùng Ys
- **Oaks (オークス)**: Vùng Oaks
- **Baranchi (バランチ)**: Vùng Baranchi
- **Ponara (ポナラ)**: Vùng Ponara
- **Prettiria (プリティリア)**: Vùng Prettiria
- **Alan (アラン)**: Vùng Alan
- **Scale (スケール)**: Vùng Scale
- **Maunes (モウネス)**: Vùng Maunes
- **Poor (貧民街)**: Khu Bần Hàn / Xóm Nghèo
- **Rich (貴族街)**: Khu Phú Hào / Khu Quý Tộc
- **Rockearth (ロックアース)**: Vùng Rockearth
- **Ice (氷雪地帯)**: Vùng Băng Giá
- **Diphtheria (ジフテリア)**: Vùng Diphtheria
- **Lazeal (ラジール)**: Vùng Lazeal
- **Custom (カスタム)**: Thành phố Tự do Custom
- **Toushin City (闘神都市)**: Thành phố Đấu Thần Toushin
- **Mars (マーズ領)**: Vùng Đất Mars
- **Red (赤の地)**: Vùng Đỏ (Xích Địa)
- **Zeo (ゼオ)**: Vùng Zeo
- **M-Land (Ｍランド)**: Công viên M-Land
- **Shangri-La (シャングリラ)**: Miền Đất Hứa Shangri-La
- **Kalar Forest (カラーの森)**: Rừng Kalar
- **Monster Realm (魔界)**: Lãnh địa Ma Giới

#### Danh Mục Mê Cung & Hầm Ngục Cổ Đại (Dungeons & Labyrinths)
- **Thieves’ Hideout (盗賊の隠れ家)**: Sào huyệt Sơn tặc
- **Monsters’ Cave (怪物の洞窟)**: Hang Quái vật
- **Thieves’ Cave (盗賊の洞窟)**: Hang Đạo tặc
- **Snow Dungeon (雪の迷宮)**: Mê cung Tuyết
- **Ho Raga’s Tower (ホ・ラガの塔)**: Tháp Ho Raga
- **Natural Foe’s Dungeon (天敵のダンジョン)**: Mê cung Thiên Địch
- **Green Village (緑の村)**: Làng Xanh
- **Summit’s Mouth (山頂の火口)**: Miệng Núi Đỉnh
- **Piar’s Ship (パイアールの船)**: Chiến hạm của Piar
- **Uncurse Dungeon (呪い解きの迷宮)**: Mê cung Giải Nguyền
- **Rising Dragon Mountain (昇竜山)**: Núi Thăng Long
- **Peach Blossom Spring (桃源郷)**: Đào Hoa Nguyên
- **Orochi’s Pit (オロチの穴)**: Vực Quái Xà Orochi (Bát Kỳ Đại Xà)
- **Isolated Shrine Island (孤島の社)**: Đảo Miếu Cô Lập
- **Giant Battleship (巨艦)**: Siêu Thiết Giáp Hạm
- **Mt. Salen (サレン山)**: Núi Salen
- **Stone-Cutter Dungeon (石切りの迷宮)**: Mê cung Thợ Cắt Đá
- **Dungeon of Lies (嘘つきの迷宮)**: Mê cung Dối Trá
- **Mos’s Dungeon (モスの迷宮)**: Mê cung của Mos
- **Maid Graveyard (メイドの墓場)**: Nghĩa địa Hầu gái
- **Rex’s Dungeon (レックスの迷宮)**: Mê cung của Rex
- **Holy Gal’s Dungeon (聖ギャルの迷宮)**: Mê cung Thánh Nữ Gyaru
- **Dangerous Hole (危険な穴)**: Hố Sâu Tử Thần

---

### 8.2. Quân Chủng & Binh Chủng Tác Chiến
- **Band of Thieves (盗賊団)**: Băng trộm / Băng sơn tặc Rance
- **Royal Guard (近衛隊 / 親衛隊)**: Cận vệ Hoàng gia Leazas
- **Leazas Knights (リーザス騎士)**: Kỵ sĩ Leazas
- **Leazas Soldiers (リーザス兵)**: Binh sĩ Leazas
- **Leazas Mages (リーザス魔術師)**: Pháp sư Leazas
- **Red Army (赤軍)**: Xích Quân (Đạo quân xung kích của Rick)
- **Helman Knights (ヘルマン騎士)**: Kỵ sĩ Helman
- **Magic Warrior (魔法戦士)**: Ma chiến binh (vừa cận chiến vừa dùng ma pháp)
- **Martial Artist / Fist Fighter (武道家)**: Võ sĩ quyền cước (Patton)
- **Phantom Beast (幻獣)**: Ảo thú (Mill Walkers)
- **JAPAN Archers (JAPAN弓兵)**: Cung thủ JAPAN (Isoroku)
- **Holy Knights (聖騎士)**: Thánh kỵ sĩ AL Giáo
- **False Angel Knights (偽天使騎士)**: Ngụy thiên thần (chị em Seizel & Hawzel)
- **Horus (ホルス)**: Tộc người chim Horus (Megalas)
- **Haniwa (ハニー)**: Đội quân tượng đất Haniwa
- **Mercenary (傭兵)**: Lính đánh thuê (Louis, Cecil)
- **Robot Freak (カラクリ)**: Người máy chiến đấu Freak & Hanty

---

### 8.3. Chiêu Thức, Tuyệt Kỹ & Ma Pháp
- **Rance Attack (ランスアタック)**: Rance Đột Kích (Tuyệt kỹ công phá trứ danh của Rance)
- **By the Way (ついでに)**: Nhân Tiện (Đòn chém tiện tay đoạt mạng của Rick)
- **White Destruction Beam (白破壊光線)**: Tia Bạch Hủy Diệt (Shizuka, Magic)
- **Black Destruction Beam (黒破壊光線)**: Tia Hắc Hủy Diệt (Chizuko, Nagi)
- **Cheater Beam (インチキ光線)**: Tia Gian Lận (Rance)
- **Chaotic Dance (乱舞)**: Khiêu vũ Hỗn loạn (Patton)
- **Whirlwind Shot (疾風打ち)**: Bắn Lốc Xoáy (Yamamoto Isoroku)
- **Evil-Purifying Overlord's Light**: Ánh sáng Bá vương Thanh tẩy Tà ác (Gandhi)
- **Soaring Dove (飛翔鳩)**: Nhạn Phi Song Đao (Rolex)
- **High Speed (ハイスピード)**: Tốc độ cao (Megalas)
- **Daimyo Procession (大名行列)**: Rước Daimyo (Đại vương Mars)
- **Vanish Bomb (バニッシュボム)**: Bom biến mất (Ninja)
- **Ice Arrow (氷の矢)**: Mũi tên băng (Melfeis)

---

### 8.4. Bảo Bối, Cổ Vật & Trang Bị (50 Items Trong SET_ITEM)
1. **Chaos (魔剣カオス)**: Ma Kiếm Chaos
2. **Nikkou (聖刀日光)**: Thánh Đao Nikkou
3. **Pop. Staff (ポロンの杖)**: Quyền trượng Poron
4. **N. Writings (北の書)**: Cổ thư Phương Bắc
5. **S. Writings (南の書)**: Cổ thư Phương Nam
6. **L. Holy Sword (リーザス聖剣)**: Thánh kiếm Leazas
7. **By Lord (バイロード)**: Kiếm By Lord
8. **Sub. Ninja (忍びの巻物)**: Nhẫn thuật Toàn thư
9. **DO Pot (ドゥの壷)**: Bình hồ lô DO
10. **Safety Bonsai (無事の盆栽)**: Bonsai Bình An
11. **Snow Charm (雪のお守り)**: Bùa Tuyết Hộ Mệnh
12. **Barrier Blade (結界の刃)**: Lưỡi đao Kết Giới
13. **Love Potion (惚れ薬)**: Thuốc Kích Dục / Tình Dược
14. **Foreclosure (差し押さえ)**: Lệnh Tịch Biên
15. **Gourd Statue (ひょうたん像)**: Tượng Hồ Lô
16. **Monkey Statue (猿の像)**: Tượng Linh Hầu
17. **Flower Statue (花の像)**: Tượng Trăm Hoa
18. **Bonsai Statue (盆栽の像)**: Tượng Cây Kiểng
19. **Clothes (Sill) (シィルの服)**: Trang phục của Sill
20. **Crystal Sword (水晶の剣)**: Pha Lê Kiếm
21. **Crystal Ring (水晶の指輪)**: Nhẫn Pha Lê
22. **Orgasmic Men (悶絶ダンディ)**: Thuốc Cường Dương Cực Phẩm
23. **Wisdom Ring (英知の指輪)**: Nhẫn Trí Tuệ
24. **Ultimate Sweet (極上の菓子)**: Điểm tâm Tuyệt hảo
25. **Supreme Sweet (至高の菓子)**: Bánh ngọt Chí tôn
26. **C. Kaiju A (怪獣の卵A)**: Trứng Quái Thú A
27. **C. Kaiju B (怪獣の卵B)**: Trứng Quái Thú B
28. **Fog Card (霧のカード)**: Thẻ bài Mù Sương
29. **Happiness Ring (幸福の指輪)**: Nhẫn Hạnh Phúc
30. **Space Shell (宇宙の貝)**: Vỏ ốc Không Gian
31. **SA Shell (SAの貝)**: Vỏ ốc SA
32. **Arkanoid Shell (ブロック崩しの貝)**: Vỏ ốc Phá Khối
33. **Evil Statue (邪神像)**: Tượng Tà Thần
34. **Tange Dog (丹下犬)**: Chú chó Tange
35. **Magic Barrier (魔法結界)**: Kết giới Ma thuật
36. **Bird Corpse (鳥の死骸)**: Xác chim Thần bí
37. **Shiranui (不知火)**: Danh đao Shiranui
38. **Vevetar Mutant (ベベター変異体)**: Dị biến thể Vevetar
39. **Jugon (ジュゴン)**: Ngư nhân Jugon
40. **Marimo (マリモ)**: Tảo cầu Marimo
41. **Hawaiian Sword (ハワイアンソード)**: Gươm Hawaii
42. **Aztec Armor (アステカの鎧)**: Giáp trụ Aztec
43. **Hirami Lemon (ヒラミレモン)**: Chanh rừng Hirami
44. **Ninja Birdlime (忍びの鳥もち)**: Nhựa dính Ninja
45. **Giant B. Key (巨大戦艦の鍵)**: Chìa khóa Siêu Thiết Giáp Hạm
46. **Aluminum Axe (アルミの斧)**: Rìu Nhôm
47. **Golden Axe (金の斧)**: Rìu Vàng Ròng
48. **Doping Drug (ドーピング薬)**: Thần dược Kích lực
49. **Charge Horn (突撃ラッパ)**: Tù và Xung Trận
50. **E. Nurse (救急ナース)**: Y tá Cấp cứu

---

### 8.5. Cơ Chế Ma Thuật, Thần Thánh & Thế Giới
- **Demon Lord / Maou (魔王)**: Ma Vương (Chúa tể tối cao, bất tử, ma lực vô hạn - Miki).
- **Majin (魔人)**: Ma Nhân (Thuộc hạ cấp cao của Ma Vương, nắm giữ quyền năng siêu phàm).
- **Majin Invulnerability (魔人の無敵結界)**: Kết giới Bất tử của Ma Nhân (Miễn nhiễm 100% mọi sát thương thường; chỉ Ma kiếm Chaos hoặc Thánh đao Nikkou mới chém xuyên được).
- **Kalar Crystal (カラーのクリスタル)**: Tinh thể Kalar (Viên ngọc trên trán nữ tiên Kalar biểu trưng cho trinh tiết).
- **Level / Level Cap (レベル / レベル限界)**: Cấp độ / Giới hạn Cấp độ (Hệ thống định lượng sức mạnh sinh mệnh đại lục).
- **LP Year (LP年 / ルドラ年)**: Năm LP (Kỷ nguyên lịch pháp đại lục, game bắt đầu năm LP 0005).
- **AL Church (AL教)**: Giáo hội AL (Tôn giáo độc thần tôn thờ Chúa AL thống trị đại lục).
- **OK Association (OK協会)**: Hiệp hội OK (Mạng lưới buôn bán nô lệ ngầm xuyên quốc gia).

---

### 8.6. Giao Diện & Chỉ Số Vận Hành Game
- **Command / Turn (コマンド / ターン)**: Lệnh điều hành / Lượt chơi
- **Total Funds / Budget (総国庫 / 予算)**: Tổng ngân quỹ / Ngân sách quốc gia
- **Military Budget (軍事予算)**: Ngân sách quân sự
- **Incidental Expenses (雑費)**: Chi phí lặt vặt
- **Total Casualties (総損害)**: Tổng thương vong
- **Morale (士気)**: Sĩ khí binh đoàn
- **Superiority (優勢度)**: Độ ưu thế chiến trường
- **Troop Count (兵数)**: Binh lực / Quân số
- **Harem Mode (ハーレムモード)**: Chế độ Hậu cung
- **Subordinates (部下)**: Danh sách Bộ hạ / Tướng lĩnh
- **Labyrinth Exploration (迷宮探索)**: Thám hiểm Mê cung
- **Decisive Battle (決戦 / 一騎討ち)**: Trận thư hùng / Quyết đấu tay đôi
- **Siege Warfare (攻城戦 / 籠城戦)**: Công thành chiến / Thủ thành chiến

---

## 9. MẪU PROMPT CHỈ THỊ CHO AI DỊCH THUẬT & REGEX HẬU XỬ LÝ

### 9.1. System Prompt Cho Công Cụ AI (Gemini / Claude / GPT)

```text
Bạn là chuyên gia biên tập và dịch thuật kịch bản Visual Novel kỳ cựu, phụ trách dịch tựa game huyền thoại "Kichikuou Rance" (Rance Bạo Chúa) sang tiếng Việt.

HÃY TUÂN THỦ NGHIÊM NGẶT CÁC NGUYÊN TẮC BẮT BUỘC SAU:

1. QUY CHUẨN NGƯỜI KỂ CHUYỆN (THIRD-PERSON NARRATION / LỜI DẪN):
- Khi miêu tả Rance: Dùng "hắn", "Rance", "gã", "tên bạo chúa", "anh" (khi ân ái). TUYỆT ĐỐI KHÔNG dùng "nó" hay "anh ta".
- Khi miêu tả Nữ nhân/Hậu cung: Dùng "nàng", "cô", "cô bé", "Nữ hoàng", "tiểu thư", [Tên]. TUYỆT ĐỐI KHÔNG dùng "nó" hay "ả" (trừ phi miêu tả kẻ thù).
- Khi miêu tả Tướng lĩnh/Lão thần: Dùng "lão tướng", "ông", "chàng", "vị hiệp sĩ", [Tên].
- Khi miêu tả Kẻ thù/Ma nhân: Dùng "hắn", "tên ma nhân", "ác quỷ", "gã", "quái vật".

2. BẢN CHẤT VÀ XƯNG HÔ ĐỐI THOẠI CỦA RANCE:
- Rance là kẻ kiêu ngạo, bạo chúa, dâm loạn tột cùng, tự xưng là "Ta" (hoặc "Tao/Bố mày" khi chửi bới, khinh bỉ kẻ thù).
- TUYỆT ĐỐI KHÔNG BAO GIỜ dùng "tôi - bạn" cho Rance.
- Với phụ nữ yêu quý/hậu cung: Rance gọi "Em" (với nữ hoàng/công chúa gọi "Nàng/Em"), xưng "Ta".
- Với phụ nữ chống đối/ngang bướng: Rance gọi "Cô/Ả/Con ranh/Mày", xưng "Ta" (hoặc "Bố mày").
- Với thuộc hạ nam: Rance gọi "Ngươi/Chú mày", xưng "Ta".
- Với kẻ thù kình địch nam (Kentarou, quái vật): Rance gọi "Mày", xưng "Tao/Bố mày".
- Tiếng cười thương hiệu của Rance: "Gahahahaha!" hoặc "Ga ha ha ha!".

3. XƯNG HÔ CHÉO CỦA CÁC NHÂN VẬT CHỦ CHỐT:
- Sill Plain: Xưng "em", gọi Rance là "Chủ nhân Rance" hoặc "ngài". Gọi Lia là "Nữ hoàng Lia".
- Nữ hoàng Lia: Xưng "thiếp/em", gọi Rance là "Chàng Rance/Chàng/Chàng yêu". Gọi Maris là "Maris". Gọi Sill là "Sill/con bé nô lệ".
- Maris Amaryllis: Xưng "tôi/thần", gọi Rance là "Bệ hạ Rance/Bệ hạ". Gọi Lia là "Nữ hoàng Lia/Bệ hạ".
- Shizuka Masou: Xưng "tôi", gọi Rance là "Tên khốn Rance/Tên dâm tặc". Gọi Maria là "Maria". Gọi Magic là "Công chúa Magic".
- Kentou Kanami: Xưng "tôi", gọi Rance là "Tên Rance khốn khiếp!". Gọi Lia là "Bệ hạ". Gọi Suzume là "Con điên Suzume".
- Maria Custard: Xưng "tôi", gọi Rance là "Rance". Gọi Shizuka là "Shizuka".
- Yamamoto Isoroku: Xưng "thiếp/tôi", gọi Rance là "Tướng quân Rance/Chàng". Gọi Kouhime là "Công chúa Kou".
- Sheila Helman: Xưng "tôi", gọi Rance là "Ngài Rance". Gọi Patton là "Huynh trưởng Patton".
- Patton Misurugi: Xưng "ta/tôi", gọi Rance là "Rance". Gọi Hubert là "Hubert". Gọi Sheila là "Sheila/Muội muội".
- Ogawa Kentarou: Xưng "tao", gọi Rance là "Mày/Tên Rance chết tiệt". Gọi Miki là "Miki".
- Kurusu Miki: Xưng "em/Miki", gọi Rance là "Chú Rance/Anh Rance". Gọi Kentarou là "Kentarou-kun".
- Tướng sĩ Leazas (Rick, Barres, Cordoba, Ex): Xưng "thần/tôi", gọi Rance là "Bệ hạ/Ngài Rance".

4. QUY TẮC CẢNH NÓNG HẬU CUNG (H-SCENES):
- CẤM dịch "came" thành "tôi đến" -> Dịch là "Thiếp... ra rồi..." / "Em... lên đỉnh rồi..." / "Ra mất rồi...".
- CẤM dịch "Darling" thành "Em yêu" khi nhân vật nữ gọi Rance -> Dịch là "Chàng" / "Chàng yêu".
- CẤM dịch "I love you" thành "anh yêu em" khi nữ nhân nói -> Dịch là "Thiếp yêu chàng..." / "Em yêu anh...".
- CẤM dịch "Take that!" thành "Lấy cái đó đi!" -> Dịch là "Nếm mùi này!" / "Đỡ lấy này!".
- "cock / dick / hyper weapon" -> "cự vật" / "siêu vũ khí" / "đại pháo".
- "pussy" -> "âm hộ" / "nơi mật ngọt" / "hoa huyệt" / "cô bé".

5. TÊN RIÊNG KHÔNG ĐƯỢC DỊCH NGHĨA ĐEN:
- Sill -> Giữ nguyên "Sill" (KHÔNG dịch thành "ngưỡng cửa" hay "bệ cửa").
- Magic The Gandhi -> Công chúa "Magic" (KHÔNG dịch thành "Phép thuật").
- Cream -> Nữ quân sư "Cream" (KHÔNG dịch thành "Kem").
- Cell / Seru -> "Cell" (KHÔNG dịch thành "Tế bào" hay "Di động").
- Papaya Server -> Pháp sư "Papaya" (KHÔNG dịch thành quả "Đu đủ").
- Chaos -> Ma kiếm "Chaos" (KHÔNG dịch thành "Hỗn loạn").
- Café Artful -> Quý cô "Café" (KHÔNG dịch thành "Quán cà phê").
```

---

### 9.2. Danh Mục Các Mẫu Regex Thay Thế Tự Động (Auto-Postprocessing Rules)

```python
import re

CORRECTION_RULES = [
    # 1. Sửa lỗi Sill bị dịch thành ngưỡng cửa / bệ cửa
    (r'(?:Bệ cửa|Ngưỡng cửa)', 'Sill'),
    
    # 2. Sửa lỗi tên riêng bị dịch thô
    (r'Phép thuật「', 'Magic「'),
    (r'Kem「', 'Cream「'),
    (r'Tế bào「', 'Cell「'),
    (r'Đu đủ「', 'Papaya「'),
    (r'Hỗn loạn「', 'Chaos「'),
    (r'Quán cà phê「', 'Café「'),
    
    # 3. Sửa lỗi H-scene trong lời thoại của Lia
    (r'(Lia\s*「[^」]*?)(?:Em yêu)([^」]*?」)', r'Chàng yêu'),
    (r'(Lia\s*「[^」]*?)(?:tôi\.\.\. đến|tôi đến)([^」]*?」)', r'thiếp... ra rồi'),
    (r'(Lia\s*「[^」]*?)(?:anh yêu em)([^」]*?」)', r'thiếp yêu chàng'),
    (r'(Lia\s*「[^」]*?)bạn([^」]*?」)', r'chàng'),
    (r'(Lia\s*「[^」]*?)tôi([^」]*?」)', r'thiếp'),
    
    # 4. Sửa lỗi Rance dùng tôi - bạn
    (r'(Rance\s*「[^」]*?)tôi([^」]*?」)', r'ta'),
    (r'(Rance\s*「[^」]*?)bạn([^」]*?」)', r'ngươi'),
    (r'(Rance\s*「[^」]*?)Lấy cái đó đi!([^」]*?」)', r'Nếm mùi này!'),
    
    # 5. Sửa lỗi tiếng cười Rance
    (r'Haha+', 'Gahahahaha!'),
    (r'Hahaha+', 'Gahahahaha!'),
]
```
