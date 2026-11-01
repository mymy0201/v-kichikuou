from pathlib import Path
import json
import tempfile
import unittest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from core import tokens, replace_roles, parse_adv, render_adv, parse_json, render_json, guide_rules, command_skeleton, roundtrip_literals
from app import Project

FIXTURE = "*L_01:\r\n\t'🙂 Tôi gọi cô.'\r\n\tR\r\n\t'Cô có nghe tôi không?'\r\n\t\\L_99:\r\n\t!VAR0001 : 5!\r\n"

class EditorTests(unittest.TestCase):
    def test_decompiler_quote_normalization(self):
        original = "'He said " + chr(34) + 'hello' + chr(34) + ".'"
        escaped = original.replace(chr(34), chr(92) * 2 + chr(34))
        self.assertEqual(roundtrip_literals(original), roundtrip_literals(escaped))

    def test_unicode_boundaries_longest_match(self):
        text='🙂 Ta thấy anh ta. Các bạn nghe ta không? tàu tai'
        found=tokens(text)
        self.assertEqual([s['text'] for s in found],['Ta','anh ta','Các bạn','ta'])
        self.assertEqual(replace_roles(text,found,{'self':'tôi','call':'các anh'}),
                         '🙂 Tôi thấy anh ta. Các anh nghe tôi không? tàu tai')

    def test_invalid_offsets_rejected(self):
        with self.assertRaises(ValueError): replace_roles('ta',[{'start':0,'end':2,'text':'tôi','role':'self'}],{'self':'tôi'})

    def test_adv_noop_byte_identity_and_command_preservation(self):
        raw=FIXTURE.encode(); rows=parse_adv(raw)
        self.assertEqual(len(rows),1)
        self.assertEqual(render_adv(raw,rows),raw)
        rows[0]['text']='🙂 Ta gọi cô. Cô có nghe ta không?'
        output=render_adv(raw,rows)
        self.assertEqual(command_skeleton(FIXTURE),command_skeleton(output.decode()))
        self.assertIn(b'!VAR0001 : 5!',output)
        self.assertIn(b'\r\n',output)

    def test_adv_overflow_and_injection(self):
        raw=FIXTURE.encode(); rows=parse_adv(raw)
        for text in ['a '*200,"x' !VAR1 : 9!",'a\\b','a\nb']:
            rows[0]['text']=text
            with self.assertRaises(ValueError): render_adv(raw,rows)

    def test_json_keeps_unknown_fields(self):
        raw=json.dumps({'meta':42,'dialogues':[{'text':'Tôi đây','speaker':'A','custom':9}]}).encode()
        rows=parse_json(raw);rows[0]['text']='Ta đây'
        output=json.loads(render_json(raw,rows))
        self.assertEqual(output['meta'],42)
        self.assertEqual(output['dialogues'][0]['custom'],9)
        self.assertEqual(output['dialogues'][0]['text'],'Ta đây')

    def test_guide_import_does_not_guess_alternatives(self):
        guide='| **Magic** xưng `tôi`, gọi Chizuko `cô` |\n| **Lia** gọi Magic: `Công chúa` (xưng `ta`) |\n| **A** gọi B: `anh` / `ngươi` (xưng `tôi`) |'
        rules,warnings=guide_rules(guide)
        self.assertEqual(len(rules),2)
        self.assertEqual(rules[0]['addressee'],'Chizuko')
        self.assertEqual(rules[1]['self'],'ta')
        self.assertEqual(warnings,[])

    def test_drafts_conflicts_and_staging(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);(root/'scripts').mkdir();source=root/'scripts/a.ADV';source.write_bytes(FIXTURE.encode())
            p=Project(root); doc=p.load('a.ADV');row=doc['rows'][0]
            row['text']='🙂 Ta gọi cô. Cô có nghe ta không?';row['spans']=tokens(row['text'])
            body={**doc,'row':row}; saved=p.save(body)
            self.assertEqual(p.load('a.ADV')['draft_revision'],1)
            with self.assertRaises(ValueError): p.save(body)
            result=p.build(saved,False)
            self.assertEqual(result['report']['status'],'passed')
            self.assertEqual(source.read_bytes(),FIXTURE.encode())
            self.assertIn('Ta gọi', (Path(result['path'])/'src/a.ADV').read_text(encoding='utf-8'))
            source.write_bytes((FIXTURE+';external\r\n').encode())
            self.assertTrue(p.load('a.ADV')['conflict'])
            with self.assertRaises(ValueError): p.build(saved,False)
            with self.assertRaises(ValueError): p.file('../outside.ADV')

    def test_srpg_json_parsing_and_rendering(self):
        srpg_fixture = {
            "name": "Map 1",
            "mapName": "Venecia",
            "openingEvents": [
                {
                    "name": "Intro",
                    "pages": [
                        {
                            "commands": [
                                {
                                    "id": 1,
                                    "type": "message",
                                    "speaker": "ゼイド",
                                    "data": ["Chào công tử Zechs, tôi đã đến."]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        raw = json.dumps(srpg_fixture, ensure_ascii=False).encode('utf-8')
        rows = parse_json(raw)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['speaker'], 'Zade')
        self.assertEqual(rows[0]['scene'], 'Intro')
        self.assertEqual(rows[0]['text'], 'Chào công tử Zechs, tôi đã đến.')
        rows[0]['text'] = 'Chào huynh trưởng Zechs, đệ đã đến.'
        rendered = render_json(raw, rows)
        reloaded = json.loads(rendered.decode('utf-8'))
        self.assertEqual(reloaded['openingEvents'][0]['pages'][0]['commands'][0]['data'][0],
                         'Chào huynh trưởng Zechs, đệ đã đến.')

    def test_vestaria_guide_markdown_tables(self):
        guide = (
            "| Người nói (A) | Người nghe (B) | A xưng | A gọi B | Sắc thái |\n"
            "| :--- | :--- | :--- | :--- | :--- |\n"
            "| **Zade** | **Athol** | `Tôi` / `Ta` | `Tiểu thư Athol` / `Nàng` | Tôn kính |\n"
            "| **Dune** ⬌ **Jean** | Bạn thân | `Cậu` - `Tớ` | Dân dã |\n"
        )
        rules, warnings = guide_rules(guide)
        self.assertEqual(len(rules), 3)
        self.assertEqual(rules[0]['speaker'], 'Zade')
        self.assertEqual(rules[0]['addressee'], 'Athol')
        self.assertEqual(rules[0]['self'], 'Tôi / Ta')
        self.assertEqual(rules[0]['call'], 'Tiểu thư Athol / Nàng')
        self.assertEqual(rules[1]['speaker'], 'Dune')
        self.assertEqual(rules[1]['addressee'], 'Jean')
        self.assertEqual(rules[2]['speaker'], 'Jean')
        self.assertEqual(rules[2]['addressee'], 'Dune')

    def test_portrait_speaker_hint_and_name(self):
        script = (
            "*L_00001:\n"
            "!VAR0521 : 111!\n"
            "*L_00002:\n"
            "!VAR0521 : 311!\n"
            "*L_scene:\n"
            "!VAR0516 : 43!\n"
            "\\L_00002:\n"
            "\\L_00001:\n"
            "'Chào ngài Rance.'\n"
        )
        rows = parse_adv(script.encode('utf-8'))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['speaker_hint'], 43)
        self.assertEqual(rows[0]['speaker_name'], 'Chizuko')

if __name__=='__main__':unittest.main()

