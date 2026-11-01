from pathlib import Path
import tempfile,unittest,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from source_alignment import align

class SourceAlignmentTests(unittest.TestCase):
    def test_selected_source_version_is_used_and_content_changes_invalidate_cache(self):
        from app import Project
        from japanese import references
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);(root/'scripts').mkdir();(root/'version1').mkdir();(root/'version2').mkdir()
            template="!VAR1 : 1!\n!VAR2 : 2!\n!VAR3 : 3!\n'{}'\n!VAR4 : 4!\n!VAR5 : 5!\n"
            (root/'scripts/a.ADV').write_text(template.format('Translated dialogue.'),encoding='utf-8')
            for folder,text in [('version1','Version one.'),('version2','Version two.')]:
                (root/folder/'a.ADV').write_text(template.format(text),encoding='utf-8')
            p=Project(root);p.config['english_source_dir']='version1'
            self.assertEqual(next(iter(references(p,'a.ADV','english')['rows'].values()))['text'],'Version one.')
            p.config['english_source_dir']='version2'
            self.assertEqual(next(iter(references(p,'a.ADV','english')['rows'].values()))['text'],'Version two.')
            (root/'version2/a.ADV').write_text(template.format('Updated version two.'),encoding='utf-8')
            self.assertEqual(next(iter(references(p,'a.ADV','english')['rows'].values()))['text'],'Updated version two.')
            (root/'version2/a.ADV').unlink()
            batch=root/'editorial_review/test';batch.mkdir(parents=True)
            import json
            (batch/'aligned_scene_evidence.json').write_text(json.dumps([dict(file='a.ADV',scene='entry',after='Translated dialogue.',english='Wrong old version.')]),encoding='utf-8')
            self.assertEqual(references(p,'a.ADV','english')['rows'],{})

    def test_changed_prose_reflow_variable_alias_and_regenerated_labels(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);vi=root/'vi';jp=root/'jp';vi.mkdir();jp.mkdir()
            (vi/'variables.txt').write_text('VAR0000\nVAR0001\n',encoding='utf-8')
            (jp/'variables.txt').write_text('RND\nVALUE\n',encoding='utf-8')
            (vi/'a.ADV').write_text("!VAR0001 : 8!\nY 4, 2:\n*L_0a:\n'Totally edited'\nR\n'Vietnamese text.'\n\\L_0b:\n!VAR0000 : 3!\nY 4, 3:\n",encoding='utf-8')
            (jp/'a.ADV').write_text("!VALUE : 8!\nY 4, 2:\n*L_9a:\n'原文の台詞。'\n\\L_9b:\n!RND : 3!\nY 4, 3:\n",encoding='utf-8')
            result=align(vi/'a.ADV',jp/'a.ADV')
            self.assertEqual(next(iter(result['rows'].values()))['text'],'原文の台詞。')
            self.assertEqual(result['stats']['mapped_rows'],1)

    def test_unmatched_commands_do_not_force_ordinal_mapping(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp)
            (root/'a.ADV').write_text("!VAR1 : 1!\n!VAR2 : 2!\n!VAR3 : 3!\n!VAR4 : 4!\n'First line.'\n!VAR5 : 5!\n'Unrelated added branch.'\n!VAR6 : 999!\n",encoding='utf-8')
            (root/'b.ADV').write_text("!VAR1 : 1!\n!VAR2 : 2!\n!VAR3 : 3!\n!VAR4 : 4!\n'Original first.'\n!VAR5 : 5!\n'Original second.'\n!VAR6 : 6!\n",encoding='utf-8')
            result=align(root/'a.ADV',root/'b.ADV')
            self.assertEqual(result['stats']['mapped_rows'],1)
            self.assertEqual(next(iter(result['rows'].values()))['text'],'Original first.')
