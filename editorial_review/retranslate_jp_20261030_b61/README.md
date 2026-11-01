# Batch61 — Rick and Hanny complete stories plus three small diagnostic/map scripts

Batch61: FULL completion of Gﾘｯｸ.ADV (136 VI/144 JP), PCMPLAY.ADV (1 VI/1 JP), WAO_MAP.ADV (2 VI/2 JP), M.ADV (1 VI/1 JP), Gﾊﾆｰ.ADV (125 VI/133 JP). 113 boxes corrected {'Gﾘｯｸ.ADV': 72, 'WAO_MAP.ADV': 1, 'M.ADV': 1, 'Gﾊﾆｰ.ADV': 39}. Compile/201 text round trips passed; commands/waits/box counts, other sources, fonts/config/drafts/saves and skipped Miki preserved. No live playthrough.

Gﾘｯｸ.ADV: All six events: Leila relationship audience, bereavement audience, helmet and monster fear, sparring request, Maris confession and rejection, Wendy corridor teasing. Every utterance and event branch read; adult non-graphic relationship references only, no explicit sexual scene. Faithful recent manual edits retained.

PCMPLAY.ADV: Entire PCM dispatch and fallback diagnostic read against original Japanese; translated error prefix, punctuation and both H3 numeric slots retained unchanged.

WAO_MAP.ADV: Entire map helper read, including all dispatch cases, coordinate test and fallthrough diagnostic. X/Y labels and both H0 outputs retained; fallthrough error distinguished from an ordinary command error.

M.ADV: Entire map movement helper read, all dispatch cases and WAO_SUB forwarding retained. Fallthrough diagnostic corrected to a control-flow error.

Gﾊﾆｰ.ADV: Every event and menu branch: idle summons, arrival with 5000 Haniwa, Julia as nonsexual pet, first/repeat shrine visits, both recruitment outcomes, population-count joke, Julia talent and upgrade, tale and song, power-up/remodel offers and results. Medical nudity remains non-graphic and faithful existing text retained; no erotic scene. All numerical effects and dynamic names preserved.

Japanese primary; English reference only. Merged speaker boxes tagged inline; no waits, boxes or portrait commands added. No live visual playthrough.

265 Vietnamese and 281 normalized Japanese groups read across five files. Rick:72 corrected boxes; Hanny:39; WAO_MAP/M:one each. PCMPLAY retained unchanged after full comparison. Hanny dynamic pages tested with all50 catalog names (150 composed variants), original population/stat numbers preserved, both recruitment choices and all6 shrine-menu labels/conditions reviewed. See dynamic_layout_validation.json.

Baseline reconciliation: current installed archives differed from batch60 metadata, but decompiled text matched all201 current sources. Four intervening source changes exactly matched batch54 pre-restoration backups and were preserved unchanged. Baseline archives and hashes saved under baseline/; no claim to new review of those four files. See baseline_reconciliation.json.

Batch61 INSTALLED: hashes match validated staging; previous archives backed up; saves and skipped Miki unchanged.
