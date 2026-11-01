# Pronoun Studio

An offline, portable dialogue editor. No account, API key, Node.js, database or
Internet connection is needed. The Windows portable distribution includes Python.

## Start

- In this project, double-click **PronounStudio.exe** in the `pronoun_editor` folder. It starts silently without opening a cmd terminal window and opens your default browser automatically.
- Closing the last Pronoun Studio browser tab/window shuts down its local host after
  a short grace period (about 3 seconds). Reloading or keeping another editor tab open
  keeps the host alive. A heartbeat also handles browser crashes (up to about 3 minutes).
  An active compile/install is allowed to finish before shutdown. The app stops its
  own host only, not unrelated browser or system processes.
- You can also use **Exit** to stop the host, including when other editor tabs are open.
- If you launch `PronounStudio.exe` while it is already running, it brings up your existing browser session instead of spawning duplicate processes.
- On another Windows PC, extract `dist/PronounStudio-Windows.zip`, then double-click `PronounStudio/PronounStudio.exe`. Choose **Open project** and enter the project folder.
- With Python 3.10+ installed, you can also run `python app.py --project "/path/to/project"`.
  macOS/Linux users can run `sh launch.sh --project "/path/to/project"`.
- To rebuild the single executable after editing code or web assets, run `python build_exe.py`.

## Edit

1. Choose a script and optionally search/filter its dialogue blocks. Use the left
   and right arrow keys to move between the filtered pages. Shortcuts are inactive
   inside text fields, dropdowns, and dialogs, so normal editing still works.
2. The **Original Dialogue** column displays the latest edited text, with highlighted
   pronouns. Hover or focus it for the full paragraph. **Edit** also shows original
   text and neighboring blocks.
3. **Self** contains the speaker's editable name on the left and pronoun on the right.
   **Call** contains the addressee and pronoun. Enter names to match guide rules.
   Explicit speaker prefixes such as `Rance「` are imported. Portrait IDs are hints
   only; the program does not infer listeners from portraits.
4. In **Edit**, assign each highlighted occurrence to Self, Call, Third/ignore, or
   Unassigned. Select any custom phrase in the text and choose Mark selection.
   Ambiguous words such as `anh`, `cô`, `con` start Unassigned. Detected roles such as
   `tôi` are suggestions; inspect quoted speech before applying a rule.
5. Editing a Self/Call pronoun updates the preview while you type and saves on Enter
   or blur. If there are no assigned occurrences and exactly one distinct unassigned
   pronoun, it becomes the replacement target automatically. Otherwise a target picker
   opens. Explicit Third/ignore occurrences are never automatically selected. The small
   **Apply** button also applies an already-entered value (including old saved drafts). **Apply MD** applies an exact pair rule. Multiple matches open a chooser;
   missing names/rules are reported. The rule source and line number remain visible.
6. Changes save on blur or Enter to `.pronoun-editor/drafts/*.json`. Whole-dialogue
   edits save using **Save dialogue**. History records before/after text and rules.
   Search, pagination and the two-second disk refresh keep large scripts usable.
7. An external source change creates a conflict instead of overwriting your work.
   Download the old draft, then **Archive draft & reload source** and reconcile it.
   The archived JSON is retained alongside the active drafts.

## Completed scripts

Click **Mark complete** beside the script dropdown to hide the current file from
that editor worklist. Completion is stored per project and survives restart.
**Completed (N)** lists hidden files with a **Restore** button for each.

The compiler still receives the complete source tree, including completed scripts;
completion does not remove files from the compiler's project/header list. Compile
and install draft changes before marking a script complete if you want those edits
in the game. Uninstalled drafts remain saved and can be restored for editing.
When every script is complete, the compile/export buttons remain available.

This is an editor worklist status chosen by the user; it does not change Japanese
review coverage, exclusion metadata, or mark a partial editorial review complete.

## Ollama pronoun revision

Open **Settings → Ollama API**. Enable the feature, choose a local server or
Ollama Cloud, enter the endpoint and model, and save. **Test connection & list
models** checks the endpoint and loads model names into the model field.

- Local: `http://127.0.0.1:11434` (usually no key).
- Cloud: `https://ollama.com` (API key required; use a model returned by the list).
- Keep the API key field blank to retain the saved key. Use **Remove saved API key**
  to clear it. Windows stores it with DPAPI encryption, bound to your user and the
  endpoint origin. On other systems the key file has owner-only permissions.
  Keys never appear in project JSON, API responses, model context, or audit history.
  Re-enter the key when moving to another PC.

Click **Revise with Ollama** on one dialogue. The request contains the selected
line, its original text, known pronoun occurrence indices, nearby lines, portrait
hints, parsed guide rules and a bounded relevant Markdown excerpt. Settings control
the timeout and number of nearby lines. The server returns JSON assignments and
participant names. The app automatically fills Speaker Name/Addressee Name and
replaces only the assigned first/second-person pronoun occurrences. It retains
third-person occurrences explicitly marked Third/ignore and all other wording.

A result dialog shows before/after, confidence and explanation. Uncertain names
remain empty. Review the result before compiling. Each revision is saved as a draft
and logged with the model, guide hash and before/after text. It is not a Japanese
scene review. Requests are per-line only; there is no automatic bulk pass.
External edits or guide changes during a request prevent stale responses from
replacing newer work. API errors leave the dialogue unchanged.

The client uses Ollama's [native chat API](https://docs.ollama.com/api/chat),
[model list](https://docs.ollama.com/api/tags), and
[cloud authentication](https://docs.ollama.com/api/authentication).
Local endpoints receive a response schema; cloud requests use a JSON-only prompt
and the same strict response validation because cloud structured output support
is limited.

## Markdown guides

The app imports explicit, single-choice Vietnamese relationship-table cells:

```text
| **Magic** xưng `tôi`, gọi Chizuko `cô` |
| **Lia** gọi Magic: `Công chúa Magic` (xưng `ta`) |
```

For other formats, add a `pronouns` fenced JSON array (see the demo guide).
Fields: `speaker`, `addressee`, `self`, `call`, optional `context`.
The full original Markdown is available in **Translation guide**. Ambiguous prose,
alternatives and contextual exceptions are not silently converted into defaults.
Use the current row's inline field to override a rule for an angry or unusual line.
To edit it inside the app, open **Translation guide → Edit Markdown**. Use **Check rules**
to validate the rule blocks, then **Save guide** (or Ctrl+S). Saving writes the configured
Markdown file and reloads rules and character suggestions immediately. The previous
file is backed up under `.pronoun-editor/backups/guides/`. External changes are detected
before saving; unsaved editor text is retained if a conflict is reported.

## Export and compile

**Export script** reads saved translation JSON and generates a staged source tree.
**Compile & install** runs the compiler and decompiler, validates the result, backs up
current files, and updates both the selected source script and installed game archives.
Restart the game to load the updated archives. Per-row buttons compile the selected
*script*, including all its saved edits. Other scripts' drafts are not included.
If install destinations are not configured, the button says **Compile to game** and
only creates staged output. A pending pronoun field that has not changed the dialogue
blocks compilation with an actionable message instead of silently building old text.

There is one current output under `.pronoun-editor/build/`. Each successful export or
compile replaces that folder, including stale files from the previous output. A failed
compile keeps the last successful build; its diagnostic report/log is saved as
`.pronoun-editor/last-build-error.json` and `last-build.log`. Temporary build folders
are removed after completion. Installation backups are kept separately.

The current build contains:

- `translated.json`: the saved dialogue, roles, names and original source hash;
- `src/`: snapshot of all current source files, with this script's edits applied;
- `game/`: compiler output; `verified/`: optional decompiler output;
- `review.json`, `validation.json`, `build.log`: provenance, actual changed blocks,
  preserved-source hashes, validation and compiler output.

The Kichikuou Rance configuration detects `xsys35c.exe` and `xsys35dc.exe` in the
project folder and installs `KICHIKUSA.ALD` and `System39.ain` to that same folder. It preserves commands, waits, newline style and the existing number
of literal line slots. Overlong edits stop compilation with a row-specific error.
Ordinary lines use 28 characters; wide lines use 50, with a tighter limit for larger
fonts. When `unifont_jp.otf` is present, edited lines are also measured with Pillow
before installation. The Windows package includes Pillow. Live scene visual QA
remains a manual check.
The round-trip check compares all ADV literal and MS strings after decompilation.

Installation keeps a backup under `.pronoun-editor/backups/<build-id>/`, verifies hashes,
checks that saves/font assets are unchanged, and restores originals if installation
fails. The selected draft is rebased to the installed source, so the next edit does
not conflict with the app's own installation. Close a running game if it locks archives.

For this repository, installation records inventory, partial coverage, before/after
edits, source provenance and validation; appends a manual batch to queue metadata
without marking the script fully reviewed; then runs `tools/update_review_indexes.py`
and `--check`. Existing exclusion indices remain untouched. Unresolved index records
are copied into the batch for inspection, never guessed. This mechanical installation
does not establish Japanese scene alignment or claim a full editorial review.

## Other projects and extension

A project contains a `src/` or `scripts/` subfolder. Open **Settings** to change:

```json
{
  "source_dir": "scripts",
  "guide": "guide.md",
  "encoding": "utf-8",
  "compiler": ["C:/Tools/compiler.exe", "{source}", "{output}"],
  "decompiler": [],
  "extra_pronouns": ["Your Majesty"],
  "install_files": {"GAME.ALD": "GAME.ALD", "System39.ain": "System39.ain"}
}
```

Commands are argument arrays, executed without a shell. Placeholders are
`{project}`, `{source}`, `{output}`, `{verified}` and `{json}`. Configure only your
own trusted compiler; its executable and dependencies must be available on that PC.
Settings are stored per project in `.pronoun-editor/project.json`.

Native adapters:

- AliceSoft `.ADV`, UTF-8 by default: consecutive literal lines form editable blocks;
  blocks are deliberately split at control/formatting commands. Embedded `MS` strings
  and menu labels are not exposed as dialogue.
- `.json`: array of objects, or `{ "dialogues": [...] }`. Each object needs `text`;
  optional `speaker`, `addressee`, `scene`. Unknown fields are retained on export.
  JSON projects can point their compiler at `{source}` or the editor's `{json}` file.

Add another adapter by implementing parse/render functions in `core.py` and adding
its file extension/dispatch in `app.py`. All offsets use Unicode code points, so emoji
do not shift pronoun selections. The frontend uses vanilla HTML/CSS/JavaScript.

## Development

`python -m unittest discover -s tests -v`

`node tests/test_pronouns.js`

On Windows, `python build_portable.py` bundles the current Python standard library,
DLLs and Python license into a relocatable ZIP. It includes only the Pillow dependency needed for font measurements, with its license;
other installed third-party packages are excluded. Use `--reuse-runtime` to update the
ZIP while an already-bundled runtime is running. The portable runtime is Windows-specific; the source app is cross-platform.

## Saved drafts and compilation

Compilation includes all saved text drafts, including scripts hidden as complete. Installation updates all included sources and rebases their drafts together, preventing later builds from reverting them. Unassigned pronoun fields remain metadata until their occurrences are assigned. Layout errors block installation and identify the script and dialogue; the previous working build remains intact.

## Original Japanese hover

Tick **Show original JP on hover** above the table. Hover or focus a dialogue to see the live translation and its Japanese reference. The choice is remembered in this browser. Recorded review evidence is matched by current source text and scene anchors; multi-box evidence is labelled **aligned scene passage**. Missing or conflicting mappings show an unavailable message instead of assuming that Japanese and Vietnamese line numbers match.

Other projects can supply `japanese-lines.json` in the project root, with an explicit mapping tied to the source SHA-256:

```json
{
  "sample.ADV": {
    "source_sha256": "SHA256_OF_CURRENT_SOURCE_BYTES",
    "rows": { "scene_label:123": "Original Japanese text" }
  }
}
```

The row ID is the editor's scene label and current one-based source line, separated by a colon. A changed source hash invalidates explicit mappings until they are updated. JP references are read-only and do not change drafts or compiled scripts.

## English hover

Tick **Show English on hover** independently of the JP checkbox. Both references can appear together. Each choice is remembered in this browser. English uses recorded scene evidence and labels multi-box passages; unavailable or conflicting alignments are never guessed. Other projects can supply `english-lines.json` with the same source-hash/row-ID format as `japanese-lines.json`. Hover references are read-only.

## Choose original source versions

In **Settings → Original source versions for hover**, set separate Japanese and English folders. Use a project-relative path or an absolute path to an extracted version containing `.ADV` files and its `variables.txt`. Leave blank to use the bundled originals. **Use bundled source versions** resets both fields.

Hover now also aligns directly against these original scripts using matching gameplay command runs, branch instructions and message boundaries. Variable aliases, regenerated labels, font changes and wordwrapping are normalized. Entire command-bounded passages are labelled accordingly; they may span more than one translated box. Changed branches without reliable boundaries remain unavailable. References are cached by source/reference content and selected path, so changing either version refreshes the mappings. A custom version uses that selected source rather than historical notes from another version.
