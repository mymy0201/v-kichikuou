# Leazas editorial pass & reviewed translations — 2026-10-14

## Summary

Applied reviewed translations from `translations.tsv` and verified speaker/pronoun rules across the Leazas story and character event files, then compiled the game scripts.

- **Total edited blocks**: 2,382 dialogue blocks across 37 source `.ADV` files.
- **Reviewed translations (`translations.tsv`)**: 1,303 translated blocks across 9 character-event files:
  - `Gﾊﾞｳﾝﾄﾞ.ADV` (Bound)
  - `Gｼｨﾙ2.ADV` (Sill 2)
  - `Gﾊﾞﾚｽ.ADV` (Barres)
  - `Gﾘｯｸ.ADV` (Rick)
  - `Gｺﾙﾄﾞﾊﾞ.ADV` (Cordoba)
  - `Gｴｸｽ.ADV` (Ex)
  - `Gｷﾝｹｰﾄﾞ.ADV` (Kinkaid)
  - `Gｼﾉﾀﾞ.ADV` (Shinoda)
  - `Gｶﾄﾞﾐｭｳﾑ.ADV` (Cadmium)
- **Verified speaker & terminology updates**: 1,071 blocks across nonsexual Leazas dialogue and military scenes adhering to `QUY_TAC_XUNG_HO_VA_THUAT_NGU.md`.
- **Maris attribution repair**: 8 blocks in `Iｾﾞｽ.ADV`, `Iﾏｼﾞﾝ.ADV`, and `Iﾏｼﾞﾝ2.ADV` adjusting portrait 6 attribution from the earlier pass.
- **Executable syntax preserved**: Verified that executable commands are identical across all 37 files; only message text, MS string arguments, and line-break commands (`R`) differ. Reflowed paragraphs maintain a 32-character maximum width.

## Compilation & Installation

- Compiled using `xsys35c_tools/xsys35c.exe --project=src/xsys35c.cfg --outdir=editorial_review/leazas/build` (Exit code: 0).
- Newly generated game script archives:
  - `KICHIKUSA.ALD` (2,433,296 bytes)
  - `System39.ain` (3,536,675 bytes)
- Copied and installed directly into the game root directory (`D:\Kichikuou Rance`).
- Decompiled with `xsys35dc.exe` into `verified_build/` to confirm that the installed binary files contain the exact translated dialogue.

## Backups & Recovery

- `backup/src/`: Contains copies of the 37 `.ADV` source files before applying this pass.
- `backup/game/`: Contains copies of `KICHIKUSA.ALD` and `System39.ain` immediately before installing this build.
