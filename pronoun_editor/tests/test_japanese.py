from pathlib import Path
import sys,tempfile,json,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import Project
from japanese import references
from core import digest

class JapaneseTests(unittest.TestCase):
    def test_english_reference_is_independent_of_japanese(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);p=self.setup_project(root);batch=root/'editorial_review/test';batch.mkdir(parents=True)
            entry=dict(file='a.ADV',scene='scene',after='This is the translated line.',japanese='原文です。',english='Verified English line.')
            path=batch/'aligned_scene_evidence.json';path.write_text(json.dumps([entry]),encoding='utf-8')
            self.assertEqual(references(p,'a.ADV','english')['rows']['scene:2']['text'],'Verified English line.')
            self.assertEqual(references(p,'a.ADV')['rows']['scene:2']['text'],'原文です。')
            path.write_text(json.dumps([entry,dict(entry,english='Different English.')]),encoding='utf-8')
            self.assertEqual(references(p,'a.ADV','english')['rows'],{})
            self.assertTrue(references(p,'a.ADV')['rows'])

    def setup_project(self,root):
        (root/'scripts').mkdir();(root/'scripts/a.ADV').write_text("*scene:\n'This is the translated line.'\n",encoding='utf-8')
        return Project(root)
    def test_scene_evidence_and_ambiguity(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);p=self.setup_project(root);batch=root/'editorial_review/test';batch.mkdir(parents=True)
            entry=dict(file='a.ADV',scene='scene',after='This is the translated line.',japanese='原文です。')
            path=batch/'aligned_scene_evidence.json';path.write_text(json.dumps([entry]),encoding='utf-8')
            self.assertEqual(references(p,'a.ADV')['rows']['scene:2']['text'],'原文です。')
            path.write_text(json.dumps([entry,dict(entry,japanese='別の原文。')]),encoding='utf-8')
            self.assertEqual(references(p,'a.ADV')['rows'],{})
            path.write_text(json.dumps([dict(entry,scene='other')]),encoding='utf-8')
            self.assertEqual(references(p,'a.ADV')['rows'],{})
    def test_explicit_line_mapping_requires_current_source_hash(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);p=self.setup_project(root);source=root/'scripts/a.ADV'
            mapping={'a.ADV':dict(source_sha256=digest(source.read_bytes()),rows={'scene:2':'原文'})}
            (root/'japanese-lines.json').write_text(json.dumps(mapping),encoding='utf-8')
            self.assertEqual(references(p,'a.ADV')['rows']['scene:2']['scope'],'line')
            source.write_text(source.read_text(encoding='utf-8')+'R\n',encoding='utf-8')
            self.assertEqual(references(p,'a.ADV')['rows'],{})
