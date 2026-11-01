from pathlib import Path
import json
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import Project
from lifecycle import BrowserSessions,clean_server_registration

class CompletionTests(unittest.TestCase):
    def test_completion_hides_only_the_dropdown_and_can_be_restored(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root=Path(tmp);(root/'scripts').mkdir()
            for name in ('a.ADV','b.ADV'):(root/'scripts'/name).write_text("'Tôi nghe đây.'\n",encoding='utf-8')
            project=Project(root);info=project.set_completed({'file':'a.ADV','complete':True})
            self.assertEqual(info['files'],['b.ADV'])
            self.assertEqual(info['all_files'],['a.ADV','b.ADV'])
            self.assertEqual(info['completed_files'],['a.ADV'])
            self.assertEqual(Project(root).info()['completed_files'],['a.ADV'])
            build=project.build(project.load('b.ADV'),False)
            self.assertTrue((Path(build['path'])/'src/a.ADV').is_file())
            project.set_completed({'file':'b.ADV','complete':True})
            self.assertEqual(project.info()['files'],[])
            # A hidden file can still be the entry document for an all-complete build.
            build=project.build(project.load('a.ADV'),False)
            self.assertTrue((Path(build['path'])/'src/b.ADV').is_file())
            self.assertEqual(project.set_completed({'file':'a.ADV','complete':False})['files'],['a.ADV'])
            self.assertEqual((root/'scripts/a.ADV').read_text(encoding='utf-8'),"'Tôi nghe đây.'\n")

class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.now=0
        self.sessions=BrowserSessions(clock=lambda:self.now,startup_grace=10,heartbeat_timeout=20,close_grace=3)

    def test_last_closed_tab_exits_after_grace(self):
        self.sessions.touch('document-1','alive');self.sessions.touch('document-1','close')
        self.now=2;self.assertFalse(self.sessions.should_shutdown())
        self.now=3;self.assertTrue(self.sessions.should_shutdown())

    def test_reload_and_another_open_tab_keep_host_alive(self):
        self.sessions.touch('document-1','alive');self.sessions.touch('document-2','alive')
        self.sessions.touch('document-1','close');self.now=5
        self.assertFalse(self.sessions.should_shutdown())
        self.sessions.touch('document-2','close');self.now=6
        self.sessions.touch('reload-doc','alive');self.now=9
        self.assertFalse(self.sessions.should_shutdown())

    def test_late_heartbeat_cannot_revive_a_closed_tab(self):
        self.sessions.touch('document-1','alive');self.sessions.touch('document-1','close')
        self.now=1;self.sessions.touch('document-1','alive');self.now=3
        self.assertTrue(self.sessions.should_shutdown())

    def test_stream_disconnect_exits_but_reconnect_within_grace_survives(self):
        self.sessions.touch('document-1','alive');self.sessions.touch('document-1','disconnect')
        self.now=2;self.sessions.touch('document-1','alive');self.now=4
        self.assertFalse(self.sessions.should_shutdown())
        self.sessions.touch('document-1','disconnect');self.now=7
        self.assertTrue(self.sessions.should_shutdown())

    def test_crashed_browser_and_never_opened_browser_timeout(self):
        self.now=10;self.assertTrue(self.sessions.should_shutdown())
        self.now=0;self.sessions.touch('document-1','alive');self.now=21
        self.assertFalse(self.sessions.should_shutdown());self.now=24
        self.assertTrue(self.sessions.should_shutdown())

    def test_active_build_finishes_before_explicit_or_automatic_exit(self):
        self.sessions.touch('document-1','alive');self.sessions.touch('document-1','close');self.now=4
        self.assertFalse(self.sessions.should_shutdown(busy=True))
        self.assertTrue(self.sessions.should_shutdown())
        self.sessions.touch('document-2','alive');self.sessions.request_exit()
        self.assertFalse(self.sessions.should_shutdown(busy=True))
        self.assertTrue(self.sessions.should_shutdown())

    def test_registration_cleanup_only_removes_its_own_pid(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            path=Path(tmp)/'server.json';path.write_text(json.dumps({'pid':456}))
            clean_server_registration(path,123);self.assertTrue(path.exists())
            clean_server_registration(path,456);self.assertFalse(path.exists())

if __name__=='__main__':unittest.main()
