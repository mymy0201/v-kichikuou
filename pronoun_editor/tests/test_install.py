from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import Project
from core import digest,render_adv
from install import install_build,protected_hashes

class InstallTests(unittest.TestCase):
    def test_installs_and_rebases_multiple_saved_scripts_together(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);args=self.setup_case(root);p,dest,first,report,baseline,protected=args
            (root/'scripts/b.ADV').write_text("'Second line.'\n",encoding='utf-8')
            second=p.load('b.ADV');second['rows'][0].update(text='Latest second line.',spans=[])
            second=p.save({**second,'row':second['rows'][0]})
            baseline['b.ADV']=digest((root/'scripts/b.ADV').read_bytes())
            (dest/'src/b.ADV').write_bytes(render_adv((root/'scripts/b.ADV').read_bytes(),second['rows']))
            install_build(p,dest,[first,second],report,baseline,protected)
            self.assertIn('Latest second line',(root/'scripts/b.ADV').read_text(encoding='utf-8'))
            self.assertEqual(p.load('b.ADV')['rows'][0]['original'],'Latest second line.')
            self.assertFalse(p.load('b.ADV')['conflict'])
            self.assertEqual(protected_hashes(root),protected)

    def setup_case(self,root):
        (root/'scripts').mkdir();(root/'scripts/a.ADV').write_text("'Tôi nghe cô.'\n",encoding='utf-8')
        (root/'GAME.ALD').write_bytes(b'old archive');(root/'System39.ain').write_bytes(b'old symbols')
        (root/'KICHIKUSA.asd').write_bytes(b'user save');(root/'.xsys35rc').write_bytes(b'user config')
        p=Project(root);p.config['install_files']={'GAME.ALD':'GAME.ALD','System39.ain':'System39.ain'}
        doc=p.load('a.ADV');doc['rows'][0]['text']='Ta nghe cô.'
        dest=root/'.pronoun-editor/builds/test';(dest/'src').mkdir(parents=True);(dest/'game').mkdir()
        (dest/'src/a.ADV').write_bytes(render_adv((root/'scripts/a.ADV').read_bytes(),doc['rows']))
        (dest/'game/GAME.ALD').write_bytes(b'new archive');(dest/'game/System39.ain').write_bytes(b'new symbols')
        baseline={'a.ADV':digest((root/'scripts/a.ADV').read_bytes())}
        report={'status':'passed','compiler':True,'roundtrip':True,'review':[{'id':doc['rows'][0]['id'],'before':'Tôi nghe cô.','after':'Ta nghe cô.'}],
                'guide':None,'archives_before':{n:digest((root/n).read_bytes()) for n in p.config['install_files'].values()}}
        return p,dest,doc,report,baseline,protected_hashes(root)

    def test_installs_source_archives_and_rebases_without_touching_save(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);args=self.setup_case(root);p,dest,doc,report,base,protected=args
            install_build(*args)
            self.assertEqual((root/'GAME.ALD').read_bytes(),b'new archive')
            self.assertIn('Ta nghe',(root/'scripts/a.ADV').read_text(encoding='utf-8'))
            self.assertEqual((Path(report['backup'])/'GAME.ALD').read_bytes(),b'old archive')
            self.assertEqual(protected_hashes(root),protected)
            self.assertFalse(p.load('a.ADV')['conflict'])
            self.assertEqual(p.load('a.ADV')['rows'][0]['original'],'Ta nghe cô.')

    def test_unverified_or_stale_build_cannot_install(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);args=self.setup_case(root);args[3]['roundtrip']=False
            with self.assertRaises(ValueError):install_build(*args)
            args[3]['roundtrip']=True;(root/'GAME.ALD').write_bytes(b'other build')
            with self.assertRaisesRegex(ValueError,'changed while building'):install_build(*args)
            self.assertEqual((root/'GAME.ALD').read_bytes(),b'other build')

    def test_failure_restores_source_and_archives(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);args=self.setup_case(root)
            import install
            original=install.os.replace;counter=[0]
            def fail_once(src,dst):
                counter[0]+=1
                if counter[0]==2:raise PermissionError('Game is locking an archive')
                return original(src,dst)
            with patch('install.os.replace',side_effect=fail_once):
                with self.assertRaisesRegex(ValueError,'original files restored'):install_build(*args)
            self.assertEqual((root/'GAME.ALD').read_bytes(),b'old archive')
            self.assertEqual((root/'scripts/a.ADV').read_text(encoding='utf-8'),"'Tôi nghe cô.'\n")
            self.assertFalse(args[3]['installed'])

    def test_metadata_then_indexes_preserves_partial_queue_status(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);args=self.setup_case(root)
            er=root/'editorial_review';(er/'scripts_by_size_20261022').mkdir(parents=True)
            queue=er/'scripts_by_size_20261022/order.json';queue.write_text(json.dumps([{'file':'a.ADV','status':'pending'}]))
            (er/'README-current.txt').write_text('Active review: editorial_review/old\n')
            (root/'tools').mkdir()
            (root/'tools/update_review_indexes.py').write_text('''from pathlib import Path
import json,sys
r=Path(__file__).resolve().parents[1]
b=r/'editorial_review/pronoun_studio_test'
assert all((b/n).exists() for n in ['inventory.json','coverage.json','review.json','validation.json','order.json'])
assert json.loads((r/'editorial_review/scripts_by_size_20261022/order.json').read_text())[0]['status']=='pending'
if '--check' not in sys.argv:
 (r/'scripts_by_size.md').write_text('updated')
 (r/'excluded_h_scene_lines.md').write_text('updated')
 (r/'editorial_review/review_indexes.generated.json').write_text('{"unresolved": []}')
else:
 assert (r/'scripts_by_size.md').read_text()=='updated'
''',encoding='utf-8')
            install_build(*args)
            self.assertEqual(json.loads(queue.read_text())[0]['status'],'pending')
            self.assertTrue(args[3]['review_indexes']['checked'])

if __name__=='__main__':unittest.main()
