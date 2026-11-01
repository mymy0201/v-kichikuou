# Translation editing

Read `TRANSLATION_EDITING_WORKFLOW.md`,
`QUY_TAC_XUNG_HO_VA_THUAT_NGU.md`, and
`editorial_review/README-current.txt` before translation work.

Use the verified original Japanese as the semantic base and English only as a
reference. Edit Vietnamese directly after reading each scene and its branches.
Preserve the latest manual changes, gameplay commands, combat UI, Unicode fonts,
layout fixes and saves. Do not rerun old machine-translation or bulk-pronoun
pipelines on reviewed text. Record source provenance, aligned scene evidence,
before/after edits, actual coverage, exclusions and validation results.

After every editing batch, manual text correction or layout reflow, update the
root files `scripts_by_size.md` and `excluded_h_scene_lines.md`. Finish writing
the batch inventory/coverage/review/validation and queue metadata first, then run
`tools/update_review_indexes.py` and `tools/update_review_indexes.py --check`
with the installed Python interpreter. Do not mark a partial review complete or
infer H labels for unread text. Preserve the original exclusion indices and
source provenance so current one-based line ranges can be regenerated after
line shifts. Inspect unresolved records in the generated index; never guess
current line numbers from historical line numbers or JP/VI ordinal equality.
