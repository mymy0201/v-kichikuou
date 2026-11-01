from pathlib import Path
import json
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import Project
from build_store import BuildSlot

class BuildAndGuideTests(unittest.TestCase):
    def test_build_includes_other_saved_drafts_even_when_hidden_as_complete(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            p=self.project(Path(tmp))
            (p.root/'scripts/b.json').write_text('[{"text":"Unchanged"}]',encoding='utf-8')
            doc=p.load('a.json');row=doc['rows'][0];row.update(text='Ta nghe cô.',spans=[])
            p.save({**doc,'row':row})
            (p.state/'completed-scripts.json').write_text(json.dumps({'a.json':{'complete':True}}),encoding='utf-8')
            result=p.build(p.load('b.json'),False)
            self.assertIn('Ta nghe',(Path(result['path'])/'src/a.json').read_text(encoding='utf-8'))
            self.assertEqual(result['report']['included_text_edits'],1)
            self.assertIn('a.json',result['report']['changed_scripts'])

    def project(self,root):
        (root/'scripts').mkdir()
        (root/'scripts/a.json').write_text('[{"text":"Tôi nghe cô.","speaker":"A","addressee":"B"}]',encoding='utf-8')
        p=Project(root);p.config['guide']='guide.md'
        return p

    def test_single_build_replaces_previous_contents_and_failure_retains_success(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            p=self.project(Path(tmp));doc=p.load('a.json')
            first=p.build(doc,False);dest=Path(first['path'])
            self.assertEqual(dest,p.state/'build')
            (dest/'stale.txt').write_text('must disappear')
            row=doc['rows'][0];row.update(text='Ta nghe cô.',spans=[])
            saved=p.save({**doc,'row':row})
            second=p.build(saved,False)
            self.assertEqual(second['path'],first['path'])
            self.assertFalse((dest/'stale.txt').exists())
            self.assertIn('Ta nghe',(dest/'src/a.json').read_text(encoding='utf-8'))
            prior=(dest/'translated.json').read_bytes()
            p.config['compiler']=[sys.executable,'-c','raise SystemExit(7)']
            failed=p.build(saved,True)
            self.assertEqual(failed['report']['status'],'failed')
            self.assertEqual((dest/'translated.json').read_bytes(),prior)
            self.assertFalse((p.state/'.build-next').exists())
            self.assertFalse((p.state/'.build-previous').exists())
            self.assertFalse((p.state/'builds').exists())

    def test_promotion_rolls_back_and_other_process_build_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            state=Path(tmp)/'.pronoun-editor';(state/'build').mkdir(parents=True)
            (state/'build/old.txt').write_text('previous')
            with self.assertRaisesRegex(ValueError,'test failure'):
                with BuildSlot(state) as slot:
                    with self.assertRaisesRegex(ValueError,'Another editor'):
                        with BuildSlot(state):pass
                    slot.working.mkdir();(slot.working/'new.txt').write_text('new')
                    slot.publish();raise ValueError('test failure')
            self.assertEqual((state/'build/old.txt').read_text(),'previous')

    def test_guide_save_preserves_format_backups_and_reloads_rules(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);p=self.project(root)
            original=b'\xef\xbb\xbf# Guide\r\n';(root/'guide.md').write_bytes(original)
            guide=p.guide()
            text='# Guide\n```pronouns\n[{"speaker":"A","addressee":"B","self":"ta","call":"cô"}]\n```\n'
            saved=p.save_guide({'text':text,'sha256':guide['sha256']})
            self.assertEqual(saved['rules'][0]['self'],'ta')
            self.assertTrue((root/'guide.md').read_bytes().startswith(b'\xef\xbb\xbf'))
            self.assertIn(b'\r\n',(root/'guide.md').read_bytes())
            backups=list((p.state/'backups/guides').glob('*.md'))
            self.assertEqual(len(backups),1);self.assertEqual(backups[0].read_bytes(),original)
            with self.assertRaisesRegex(ValueError,'changed on disk'):
                p.save_guide({'text':'outdated','sha256':guide['sha256']})
            current=(root/'guide.md').read_bytes()
            with self.assertRaisesRegex(ValueError,'Fix the guide'):
                p.save_guide({'text':'```pronouns\n{bad json}\n```','sha256':saved['sha256']})
            self.assertEqual((root/'guide.md').read_bytes(),current)

    def test_missing_guide_can_be_created(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            p=self.project(Path(tmp))
            self.assertEqual(p.save_guide({'text':'# New guide','sha256':None})['text'],'# New guide')

if __name__=='__main__':unittest.main()
