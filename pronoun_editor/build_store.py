"""One published build per project, with a temporary replacement and process lock."""
from pathlib import Path
import os
import shutil

class BuildSlot:
    def __init__(self,state):
        self.state=Path(state).resolve()
        self.current=self.state/'build'
        self.working=self.state/'.build-next'
        self.previous=self.state/'.build-previous'
        self.published=False
        self.committed=False
        self.lock=None

    def remove(self,path):
        path=Path(path)
        if path.parent.resolve()!=self.state or path.name not in ('.build-next','.build-previous') or path.is_symlink():
            raise ValueError('Refusing to remove a path outside the managed build workspace.')
        if path.exists():shutil.rmtree(path)

    def __enter__(self):
        self.state.mkdir(parents=True,exist_ok=True)
        self.lock=(self.state/'build.lock').open('a+b')
        if not (self.state/'build.lock').stat().st_size:
            self.lock.write(b'0');self.lock.flush()
        self.lock.seek(0)
        try:
            if os.name=='nt':
                import msvcrt
                msvcrt.locking(self.lock.fileno(),msvcrt.LK_NBLCK,1)
            else:
                import fcntl
                fcntl.flock(self.lock.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
        except OSError:
            self.lock.close()
            raise ValueError('Another editor is building this project. Wait for it to finish.')
        try:
            if any(p.is_symlink() for p in (self.current,self.previous,self.working)):
                raise ValueError('Build folders cannot be symbolic links.')
            if self.previous.exists() and not self.current.exists():self.previous.rename(self.current)
            self.remove(self.previous)
            self.remove(self.working)
            return self
        except Exception:
            self.lock.close();raise

    def publish(self):
        if self.current.exists():self.current.rename(self.previous)
        try:self.working.rename(self.current)
        except Exception:
            if self.previous.exists():self.previous.rename(self.current)
            raise
        self.published=True

    def commit(self):
        self.committed=True

    def __exit__(self,*error):
        try:
            if self.published and not self.committed:
                self.current.rename(self.working)
                if self.previous.exists():self.previous.rename(self.current)
            self.remove(self.working)
            if self.committed:self.remove(self.previous)
        finally:
            if self.lock:self.lock.close()
