"""Track editor browser tabs, not unrelated browser or system processes."""
import threading
import time

class BrowserSessions:
    def __init__(self,clock=time.monotonic,startup_grace=120,heartbeat_timeout=180,close_grace=3):
        self.clock=clock;self.started=clock();self.startup_grace=startup_grace
        self.heartbeat_timeout=heartbeat_timeout;self.close_grace=close_grace
        self.sessions={};self.lock=threading.Lock();self.empty_since=None;self.explicit_exit=False

    def touch(self,client_id,event):
        if not isinstance(client_id,str) or not 8<=len(client_id)<=128 or event not in ('alive','close','disconnect'):
            raise ValueError('Invalid editor session.')
        with self.lock:
            now=self.clock();old=self.sessions.get(client_id)
            if event=='close':self.sessions[client_id]={'seen':now,'closed':True}
            elif event=='disconnect':
                if not old or not old['closed']:self.sessions[client_id]={'seen':now,'closed':False,'disconnected':True}
            elif not old or not old['closed']:
                self.sessions[client_id]={'seen':now,'closed':False};self.empty_since=None
            # A late in-flight heartbeat cannot revive a closed document. Reloads
            # and restored pages use a fresh document ID.
            if not any(not s['closed'] and not s.get('disconnected') and now-s['seen']<self.heartbeat_timeout for s in self.sessions.values()):
                if self.empty_since is None:self.empty_since=now
            for key in list(self.sessions):
                if key!=client_id and now-self.sessions[key]['seen']>self.heartbeat_timeout*2:del self.sessions[key]

    def request_exit(self):
        with self.lock:self.explicit_exit=True

    def should_shutdown(self,busy=False):
        with self.lock:
            if busy:return False
            if self.explicit_exit:return True
            now=self.clock()
            if not self.sessions:return now-self.started>=self.startup_grace
            if any(not s['closed'] and not s.get('disconnected') and now-s['seen']<self.heartbeat_timeout for s in self.sessions.values()):return False
            if self.empty_since is None:self.empty_since=now
            return now-self.empty_since>=self.close_grace

def clean_server_registration(path,pid):
    import json
    try:
        if path.exists() and json.loads(path.read_text(encoding='utf-8')).get('pid')==pid:path.unlink()
    except (OSError,ValueError):pass
