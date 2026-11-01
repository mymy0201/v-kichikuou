# Japanese-based contextual review — 2026-10-22

Imported the workflow from `D:\Vestaria\TRANSLATION_EDITING_WORKFLOW.md` and
adapted it in the project-root `TRANSLATION_EDITING_WORKFLOW.md`. Root
`AGENTS.md` and `editorial_review/README-current.txt` make it the workflow for
future editing. Vestaria's names, translation choices and engine-specific layout
rules were not imported.

## Sources

- **Primary:** original Japanese scenario extracted from the freeware disc
  archive distributed at <https://alicefree.fastlast.org/> and linked by the
  engine maintainer's supported-games page. The extracted scenario is decompiled
  under `reference/japanese/` (201 scripts).
- **Reference:** the English freeware package from
  <https://haniwa.website/games/>, decompiled under `reference/english/`.
- **Editable baseline:** the current `src/` as it existed at the start of this
  pass, retaining the later manual revisions, fonts, combat UI and layout fixes.
- **Terminology:** the current `QUY_TAC_XUNG_HO_VA_THUAT_NGU.md`, including the
  October 18 addenda. It was not modified.

`provenance.json` records URLs and hashes. The downloaded reference packages were
used only as data; their executables were not run.

## Installed changes

**205 reviewed corrections in seven scripts:**

- `Iﾌﾟﾛﾛｰｸﾞ.ADV`: the opening; including division of raid loot, Soul's family
  background, and Bound's self-correcting joke.
- `Iﾄｳｿﾞｸ.ADV`: raid tutorial, military warnings, pursuit and transition to
  Leazas; including the inverted troop-strength warning and the Log B name.
- `Iﾊﾝﾗﾝ.ADV`: Kanami's discovery, Rance recovering, the wedding and coronation;
  including incorrect subjects, snores changed to laughs, and omitted Japanese
  ceremony wording.
- `Iｶﾝｶﾞｴ.ADV`: selected nonsexual reminders, including Menad embezzling supplies
  rather than money and Rance's resolve to recover Sill.
- `Gﾊﾞﾚｽ.ADV`: Barres's family and court events, honorific jokes and commands.
- `Gﾘｯｸ.ADV`: Rick's court and Maris conversations, helmet weakness and military
  dialogue. Maris and Rick do not address each other as though the other is king.
- `Gｴｸｽ.ADV`: Ex's rebellion, return and punishment branches; restored proper
  names and corrected meanings that were already wrong in the English reference.

Every entry in `review.json` contains Japanese, English, the previous Vietnamese,
the edit and its reason. Some entries target a single existing text-box fragment
inside a larger scene. These are corrections, not a count of whole scenes.

## Coverage and remaining work

**The complete Prologue/Leazas character scope is not finished.** `scope.json`
lists 51 candidate files, the source-unit ranges actually read, exclusions and
remaining files. The seven scripts above have contextual review records; other
Leazas character routes, shared territory dialogue and optional branches remain
pending a Japanese-based pass. Historical edits in those files are retained, but
are not relabeled as newly reviewed.

Sexual material involving minors is excluded. Related intimate passages were not
rewritten in this pass. A source-unit marked read is not a claim that every line
was changed or that the translation cannot be improved further.

Japanese/English/Vietnamese group ordinals can differ: headers and narration were
sometimes combined in the old Vietnamese scripts. Candidate command matching was
used to locate scenes, then the actual dialogue was read. Equal indices alone
were never treated as proof of alignment. The full source inventory is retained
so the next pass can continue without rebuilding from an older translation.

## Verification and installation

- Full compilation succeeded.
- Decompiled output was checked against **all 201 current source scripts**.
- Every executable command and existing wait in the edited scripts is identical
  to the pre-edit Vietnamese source. Only text and `R` line breaks changed.
- Changed lines were measured with the installed `unifont_jp.otf` at the actual
  font size: up to 336 px in ordinary boxes and 600 px in wide boxes, within the
  current 28/50-character limits. Existing box counts were preserved.
- All other source files, including combat UI and layout code, are unchanged.
- Player save hashes before/after match. Fonts and font configuration are kept.
- Installed `KICHIKUSA.ALD` and `System39.ain` match the verified staging build.
- Live visual playthrough of these scenes was **not performed**.

Restart the game to load the installed build.

## Files

- `review.json`, `edits.json`: contextual edits and evidence.
- `scope.json`, `scope-summary.txt`: actual coverage and candidate scope.
- `inventory.json`: frozen three-language scene evidence.
- `validation.json`, `layout.json`: structural, layout, build and save checks.
- `complete_changes.diff`: complete applied source diff.
- `backup/src/`, `backup/game/`: exact pre-pass source and installed binaries.
- `build/`, `verified_build/`: staged build and verification decompilation.
- `VESTARIA_WORKFLOW.original.md`: unchanged copy of the source workflow.
