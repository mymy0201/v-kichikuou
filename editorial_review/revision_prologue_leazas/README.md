# Vietnamese Editorial Revision 1 — Prologue & Leazas Scripts (2026-10-14)

## Overview & Scope

- **Target Scope**: Priority 1 — Prologue and entire Leazas storyline & character event scripts.
- **Word Count**: **122,288 dialogue words** (Under the 200,000 words cap).
- **Files Processed**: 37 files inspected; **31 files revised** with **3,754 edited dialogue blocks**.
- **Rule Set**: Fully aligned with [QUY_TAC_XUNG_HO_VA_THUAT_NGU.md](file:///d:/Kichikuou%20Rance/QUY_TAC_XUNG_HO_VA_THUAT_NGU.md).

## Major Editorial Improvements

1. **Rance Personality & Pronouns**:
   - Replaced all machine-translated first-person `tôi` in Rance's speech and inner thoughts (`Iｶﾝｶﾞｴ.ADV`) with `ta` (or `tao`/`bố mày`).
   - Standardized laughter to `Gahahahaha!`.
   - Rance addresses beloved heroines (Sill, Wendy, Melfeis, Arlcoate, Julia, Menad, Soul) as `em`; royalty (Lia) as `nàng`; proud knights (Leila, Haurein) as `cô`; ninja (Kanami) as `mày`/`cô`; and generals (Rick, Barres, Cordoba, Ex) as `ngươi`.

2. **Character-Specific Relationships & Honorifics**:
   - **Sill Plain (`Gｼｨﾙ.ADV`)**: Completely purged "Ngưỡng cửa" (35 machine-translation artifacts). Corrected address to `Chủ nhân Rance` / `ngài`, self `em` (removed all "cậu chủ", "thầy Rance", "bạn").
   - **Lia Parapara Leazas (`Gﾘｱ.ADV`)**: Corrected address to `Chàng Rance` / `Chàng yêu`, self `thiếp` (removed "em yêu", "anh yêu", "bạn").
   - **Soul Less (`Gｿｳﾙ.ADV`)**: Purged 102 occurrences of "Linh hồn" used for Soul. Corrected address to `Đại ca Rance` / `đại ca`, self `em`.
   - **Barres Provence (`Gﾊﾞﾚｽ.ADV`, `Gﾊｳﾚｰﾝ.ADV`)**: Corrected court address to `Bệ hạ`, self `lão thần`. Restored family address with Haurein (`con` - `cha`).
   - **Rick Addison & Generals (`Gﾘｯｸ.ADV`, `Gﾚｲﾗ.ADV`, `Iｼﾚｲﾌﾞ.ADV`)**: Addressed Rance as `Bệ hạ`, self `thần`. Respected peer address between Rick and Leila (`anh` - `cô`).
   - **Leila, Haurein, Menad, Melfeis, Kanami, Suzume, Wendy, Julia, Rafalia, Arlcoate, Mokomoko, Anasel, Rebecca**.

3. **Standardized Terminology**:
   - Location: `Phòng khán giả` -> `Phòng yết kiến`.
   - Factions & Armies: `Xích Quân`, `Hắc Quân`, `Bạch Quân`, `Thanh Quân`, `Cận vệ Hoàng gia`.
   - Nations: `Đế chế Helman`, `Vương quốc Ma pháp Zeth`, `Vương quốc Leazas`.
   - Core concepts: `Ma Nhân`, `Ma Vương`, `Tứ Đại Lãnh Chúa`, `Siêu vũ khí`, `Rance Đột Kích`, `Nhân Tiện`, `Tia Bạch Hủy Diệt`, `Tia Hắc Hủy Diệt`, `Tia Gian Lận`, `Sĩ khí`, `Độ ưu thế`.

4. **Syntax & Script Integrity**:
   - 100% of executable commands, labels, variables, and line flow verified identical to originals.
   - Reflowed paragraphs to max 32 characters per line with `R` separators.

## Build & Installation

- **Compiler**: `xsys35c_tools/xsys35c.exe --project=src/xsys35c.cfg --outdir=editorial_review/revision_prologue_leazas/build` (Return code: 0).
- **Game Binaries Installed**:
  - `KICHIKUSA.ALD` (2,433,552 bytes)
  - `System39.ain` (3,534,974 bytes)
- **Verification**: Decompiled with `xsys35dc.exe` into `verified_build/` confirming all revised dialogue.
- **Backups**:
  - `backup/src/`: Original source files before this revision pass.
  - `backup/game/`: Game binaries immediately prior to installing this build.
- **Detailed Change Log**: Stored in `changes.json` (3,754 itemized revisions).
