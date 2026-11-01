"""Bundle this app with the current Windows Python runtime, no pip dependency."""
from pathlib import Path
import shutil
import sys
import zipfile
import argparse
import filecmp

APP=Path(__file__).resolve().parent
RUNTIME=Path(sys.base_prefix)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--reuse-runtime', action='store_true', help='Package an already bundled runtime (safe while the app is running).')
    args=parser.parse_args()
    target=APP/'runtime'
    target.mkdir(exist_ok=True)
    if args.reuse_runtime:
        if not (target/'python.exe').exists():raise SystemExit('Bundle the runtime first without --reuse-runtime.')
        bundle_pillow(target)
        package()
        return
    for pattern in ('python.exe','pythonw.exe','python*.dll','vcruntime*.dll','LICENSE.txt'):
        for p in RUNTIME.glob(pattern):shutil.copy2(p,target/p.name)
    shutil.copytree(RUNTIME/'DLLs',target/'DLLs',dirs_exist_ok=True)
    version=f'python{sys.version_info.major}{sys.version_info.minor}'
    with zipfile.ZipFile(target/(version+'.zip'),'w',zipfile.ZIP_DEFLATED) as z:
        for p in (RUNTIME/'Lib').rglob('*'):
            rel=p.relative_to(RUNTIME/'Lib')
            if p.is_file() and p.suffix in ('.py','.txt','.pem') and not any(x in rel.parts for x in ('site-packages','__pycache__','test','tests','idlelib','tkinter','turtledemo','ensurepip')):
                z.write(p,rel.as_posix())
    (target/(version+'._pth')).write_text(f'{version}.zip\nDLLs\n.\n..\n',encoding='utf-8')
    bundle_pillow(target)
    package()

def bundle_pillow(target):
    import PIL
    source=Path(PIL.__file__).parent
    def copy_changed(src,dst):
        if Path(dst).exists() and filecmp.cmp(src,dst,shallow=False):return dst
        return shutil.copy2(src,dst)
    shutil.copytree(source,target/'Lib/PIL',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'),copy_function=copy_changed)
    libs=source.parent/'pillow.libs'
    if libs.exists():shutil.copytree(libs,target/'Lib/pillow.libs',dirs_exist_ok=True,copy_function=copy_changed)
    license_dir=next(source.parent.glob('pillow-*.dist-info/licenses'),None)
    if license_dir:shutil.copytree(license_dir,target/'licenses/Pillow',dirs_exist_ok=True)
    for path in target.glob('python*._pth'):
        contents=path.read_text(encoding='utf-8')
        if 'Lib\n' not in contents:path.write_text(contents+'Lib\n',encoding='utf-8')
        # This bundled Python has a certificate-trust patch that loads its PEM
        # beside ssl.py. OpenSSL cannot read certificate files inside a ZIP.
        pem=RUNTIME/'Lib/codex-rejected-cas.pem'
        if pem.exists():
            shutil.copy2(RUNTIME/'Lib/ssl.py',target/'Lib/ssl.py')
            shutil.copy2(pem,target/'Lib'/pem.name)
            entries=path.read_text(encoding='utf-8').splitlines()
            entries=['Lib']+[s for s in entries if s!='Lib']
            path.write_text('\n'.join(entries)+'\n',encoding='utf-8')

def package():
    dest=APP/'dist';dest.mkdir(exist_ok=True)
    with zipfile.ZipFile(dest/'PronounStudio-Windows.zip','w',zipfile.ZIP_DEFLATED) as z:
        for name in ('app.py','core.py','japanese.py','source_alignment.py','batch.py','install.py','build_store.py','ollama_client.py','lifecycle.py','Launch.cmd','launch.sh','README.md','web','runtime','examples'):
            p=APP/name
            files=p.rglob('*') if p.is_dir() else [p]
            for f in files:
                if f.is_file() and not any(part in f.parts for part in ('__pycache__','.pronoun-editor')):
                    z.write(f,Path('PronounStudio')/f.relative_to(APP))
    print(dest/'PronounStudio-Windows.zip')

if __name__=='__main__':main()
