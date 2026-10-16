# Prologue, Leazas and combat translation corrections

Applied 630 text corrections across the current translation. In total, 46 source
files changed, including the native combat-label rendering changes. The compiled
`KICHIKUSA.ALD` and `System39.ain` have been installed in the game directory.
Restart the game to load the new archive.

The rule file used is `QUY_TAC_XUNG_HO_VA_THUAT_NGU.md`, SHA-256
`60fd1dfa6829c942c117b45d84533d755f4086618185f473538b2b279c8daf6f`.

Changes include:

- Prologue: restored Rance's name where it had been translated as “Chạy đua,”
  corrected nonsexual narration and applied the new Ice location terminology.
- Leazas: corrected the coronation address to the crowd, Lia's address to her
  maid, Kanami and Menad's conversation, wedding dialogue, Maris and Rick's
  conversation, Ex's title, and the Thành Leazas terminology.
- Combat: translated remaining English labels, generic commanders and map
  regions; corrected skill names and mistranslated combat statistics and orders.
- Replaced the on-screen English TROOPS / HP / ANNIHILATED / UNABLE TO FIGHT
  graphics with native Vietnamese text. Original graphics archives and digit
  sprites are preserved. Expanded battle-menu widths for Vietnamese labels.

## Verification

- Full source compilation succeeded.
- Decompilation of the build reproduced every changed file's text literals.
- Executable-command comparison found no gameplay logic changes. The only
  permitted differences are native label drawing and combat-menu widths.
- An isolated engine test executed all four Vietnamese combat labels without
  engine warnings or errors. It used a separate save directory.
- Hidden-window screen capture was blank, so visual layout in a live battle has
  not been confirmed. The captured image is not evidence of rendering quality.
- Installed archive hashes match the verified build (`validation.json`).

## Scope limitations

Sexual scenes were excluded from this editing pass, including passages involving
minors. English fragments and older wording remain in those excluded passages.
Proper character names, monster names, and intentional foreign-language phrases
are retained. This report does not claim a complete line-by-line literary review
of the whole game.

## Review and recovery

- `complete_changes.diff`: complete source diff for this pass.
- `changes.json`, `additional_changes.json`: before/after text corrections.
- `manual.tsv`: manually reviewed corrections keyed to `inventory.json`.
- `validation.json`: checks and installed-file hashes.
- `backup/src/`: source files as they existed immediately before this pass.
- `backup/game/`: previous installed scenario archive and string table.
- `build/`, `verified_build/`: compiled output and verification decompilation.

Native text rendering was checked against the engine's official command
implementations at https://github.com/kichikuou/xsystem35-sdl2/tree/master/src.
The locally downloaded C files are reference material only and are not part of
the game build.
