"""Run: python app.py --project /path/to/game. Uses Python 3.10+ only."""
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import argparse
import datetime
import json
import os
import secrets
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
sys.path.insert(0, str(Path(__file__).resolve().parent))
from core import digest, parse_adv, parse_json, render_adv, render_json, tokens, guide_rules, roundtrip_literals, LITERAL, PORTRAIT_NAMES
from install import install_build, protected_hashes
from build_store import BuildSlot
from batch import collect_documents,stage_document,check_snapshots
import ollama_client as ollama
from japanese import references as japanese_references
from lifecycle import BrowserSessions,clean_server_registration

if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w', encoding='utf-8')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w', encoding='utf-8')

BASE = Path(getattr(sys, '_MEIPASS', Path(__file__).parent))
LOCK = threading.RLock()
KEY = secrets.token_urlsafe(32)
JOB = {'running': False}
AI_JOBS = {}

def detect_project_root(explicit=None):
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if p.name == 'pronoun_editor' and (p.parent / 'translation').is_dir():
            return str(p.parent)
        if p.name == 'dist' and (p.parent.parent / 'translation').is_dir():
            return str(p.parent.parent)
        return str(p)
    base = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent
    candidates = [base, base.parent, base.parent.parent, Path.cwd()]
    for c in candidates:
        if c.is_dir() and ((c / 'translation').is_dir() or (c / 'src').is_dir() or (c / 'AI_TRANSLATION_GUIDE.md').is_file() or (c / 'QUY_TAC_XUNG_HO_VA_THUAT_NGU.md').is_file() or (c / 'xsys35c.exe').is_file() or (c / '.pronoun-editor').is_dir()):
            return str(c.resolve())
    if base.name in ('pronoun_editor', 'dist', 'bin') and base.parent.is_dir():
        return str(base.parent.resolve())
    return str(base.resolve())


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)

class Project:
    def __init__(self, root):
        self.root = Path(root).expanduser().resolve()
        if not self.root.is_dir(): raise ValueError('Project folder does not exist.')
        if self.root.name == 'pronoun_editor' and ((self.root.parent / 'translation').is_dir() or (self.root.parent / 'src').is_dir()):
            self.root = self.root.parent
        elif self.root.name == 'dist' and ((self.root.parent.parent / 'translation').is_dir() or (self.root.parent.parent / 'src').is_dir()):
            self.root = self.root.parent.parent
        self.state = self.root / '.pronoun-editor'
        self.config_file = self.state / 'project.json'
        default_config = self.detect_defaults()
        if self.config_file.exists():
            self.config = {**default_config, **read_json(self.config_file)}
        else:
            self.config = default_config
            write_json(self.config_file, self.config)
        self.config['ollama']=ollama.settings(self.config.get('ollama'))
        self.source = (self.root / self.config['source_dir']).resolve()
        if not self.source.is_relative_to(self.root) or self.source == self.root:
            raise ValueError('source_dir must be a subfolder of the project (for example src or scripts).')

    def detect_defaults(self):
        source_dir = None
        guide = 'QUY_TAC_XUNG_HO_VA_THUAT_NGU.md' if (self.root / 'QUY_TAC_XUNG_HO_VA_THUAT_NGU.md').is_file() else 'AI_TRANSLATION_GUIDE.md'

        readme_current = self.root / 'translation' / 'README-current.txt'
        if readme_current.is_file():
            try:
                for line in readme_current.read_text(encoding='utf-8').splitlines():
                    if line.startswith('Latest sources:'):
                        for part in line.split():
                            if 'full-vi' in part:
                                p = Path(part)
                                if p.is_dir():
                                    try: source_dir = str(p.relative_to(self.root)).replace('\\', '/')
                                    except ValueError: source_dir = str(p)
                                break
                    elif line.startswith('Guide:'):
                        g_part = line.split('Guide:', 1)[1].strip()
                        gp = Path(g_part)
                        if gp.is_file():
                            try: guide = str(gp.relative_to(self.root)).replace('\\', '/')
                            except ValueError: guide = str(gp)
            except Exception:
                pass

        if not source_dir:
            for candidate in [
                'translation/vesta-skill-names-edit/full-vi',
                'translation/character-map-reaudit/full-vi',
                'translation/coverage-through15-edit/full-vi',
                'translation/full-vi',
                'translation/vi',
                'src',
                'scripts'
            ]:
                if (self.root / candidate).is_dir():
                    source_dir = candidate
                    break
        if not source_dir:
            source_dir = 'src' if (self.root / 'src').is_dir() else 'scripts'

        config = {
            'source_dir': source_dir,
            'guide': guide,
            'encoding': 'utf-8',
            'compiler': [],
            'decompiler': [],
            'extra_pronouns': [
                'công tử', 'tiểu thư', 'huynh trưởng', 'đại ca', 'sơ', 'đầu lĩnh',
                'lão đại', 'thảo dân', 'thuộc hạ', 'thiện tín', 'công chúa', 'tướng quân',
                'đại nhân', 'thống lĩnh', 'tiểu đệ', 'bần đạo', 'gã này', 'bản tọa',
                'quân sư', 'chúa công'
            ],
            'install_files': {},'ollama':dict(ollama.DEFAULTS)
        }

        rebuild_ps1 = self.root / 'translation' / 'vesta-skill-names-edit' / 'rebuild.ps1'
        if rebuild_ps1.is_file():
            config['compiler'] = [
                'powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', str(rebuild_ps1).replace('\\', '/'),
                '-SourceDir', '{source}', '-OutputFile', '{output}/data.vi-vesta-skill-names.dts'
            ]
            config['install_files'] = {'data.vi-vesta-skill-names.dts': 'Vietnamese/data.dts'}
        elif (self.root / 'xsys35c.exe').exists():
            config['compiler'] = [str(self.root / 'xsys35c.exe'), '--project={source}/xsys35c.cfg', '--outdir={output}']
            config['decompiler'] = [str(self.root / 'xsys35dc.exe'), '{output}', '--outdir={verified}']
            config['install_files'] = {'KICHIKUSA.ALD': 'KICHIKUSA.ALD', 'System39.ain': 'System39.ain'}

        return config

    def file(self, name):
        path = (self.source / name).resolve()
        if not path.is_relative_to(self.source) or path.suffix.lower() not in ('.adv', '.json') or not path.is_file():
            raise ValueError('Choose an ADV or JSON file inside the source folder.')
        return path

    def draft_path(self, name):
        return self.state / 'drafts' / (digest(name.encode()) + '.json')

    def completed_scripts(self):
        path=self.state/'completed-scripts.json'
        return read_json(path).get('files',{}) if path.exists() else {}

    def set_completed(self,body):
        path=self.file(body['file'])
        if type(body.get('complete')) is not bool:raise ValueError('Complete must be true or false.')
        name=str(path.relative_to(self.source)).replace('\\','/')
        records=self.completed_scripts()
        if body['complete']:
            records[name]={'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           'source_sha256':digest(path.read_bytes()),'status':'User completed editor worklist; no editorial coverage claim.'}
        else:records.pop(name,None)
        write_json(self.state/'completed-scripts.json',{'schema_version':1,'files':records})
        return self.info()

    def load(self, name):
        path = self.file(name); raw = path.read_bytes(); sha = digest(raw)
        if path.suffix.lower() == '.adv':
            rows = parse_adv(raw, self.config['encoding'])
        else:
            rows = parse_json(raw, self.config['encoding'], self.config.get('extra_pronouns', []))
        draft_path = self.draft_path(name)
        draft = read_json(draft_path) if draft_path.exists() else None
        conflict = bool(draft and draft['source_sha256'] != sha)
        if draft:
            # A changed source must not silently inherit offsets from an old file.
            if not conflict: rows = draft['rows']
        for row in rows:
            if not draft or conflict:
                row['spans'] = tokens(row['text'], self.config.get('extra_pronouns', []))
            if row.get('speaker_hint') is not None and not row.get('speaker_name'):
                row['speaker_name'] = PORTRAIT_NAMES.get(row['speaker_hint'], '')
            row.setdefault('self', ''); row.setdefault('call', '')
        return dict(file=name, source_sha256=sha, rows=rows, conflict=conflict,
                    draft_revision=draft.get('draft_revision', 0) if draft else 0,
                    draft_available=bool(draft), encoding=self.config['encoding'])

    def save(self, body):
        doc = self.load(body['file'])
        if doc['conflict'] or doc['source_sha256'] != body['source_sha256']:
            raise ValueError('Source changed on disk. Export the old draft for comparison, then reset and reload.')
        if body['draft_revision'] != doc['draft_revision']:
            raise ValueError('Another window saved this draft. Reload before editing.')
        row = next((r for r in doc['rows'] if r['id'] == body['row']['id']), None)
        if row is None: raise ValueError('Dialogue no longer exists.')
        before = dict(row)
        for key in ('text', 'speaker', 'addressee', 'self', 'call'):
            if not isinstance(body['row'].get(key, ''), str): raise ValueError('Fields must be text.')
            row[key] = body['row'].get(key, '')
        from core import replace_roles
        spans = body['row'].get('spans', tokens(row['text']))
        replace_roles(row['text'], spans, {})  # validate every saved selection
        row['spans'] = spans
        if body.get('ollama_metadata'):
            row['ollama_review']=body['ollama_metadata']
        doc['draft_revision'] += 1
        write_json(self.draft_path(body['file']), doc)
        audit = self.state/'history.jsonl'
        with audit.open('a', encoding='utf-8') as f:
            f.write(json.dumps(dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                file=body['file'], source_sha256=doc['source_sha256'], before=before, after=row,
                rule=body.get('rule')), ensure_ascii=False) + '\n')
        return doc

    def guide(self):
        path = (self.root/self.config['guide']).resolve()
        if not path.is_file(): return dict(text='', rules=[], warnings=['Guide file not found: '+str(path)], path=str(path))
        raw = path.read_bytes(); text = raw.decode('utf-8-sig'); rules, warnings = guide_rules(text)
        return dict(path=str(path), text=text, rules=rules, warnings=warnings, sha256=digest(raw))

    def save_guide(self,body):
        path=(self.root/self.config['guide']).resolve()
        if not path.is_relative_to(self.root) or path.suffix.lower() not in ('.md','.markdown'):
            raise ValueError('Choose a Markdown guide inside this project in Settings before editing it.')
        text=body.get('text')
        if not isinstance(text,str):raise ValueError('Guide content must be text.')
        raw=path.read_bytes() if path.exists() else None
        sha=digest(raw) if raw is not None else None
        if body.get('sha256')!=sha:
            raise ValueError('The guide changed on disk. Your editor text is retained; reload the saved guide before overwriting it.')
        rules,warnings=guide_rules(text)
        if warnings:raise ValueError('Fix the guide before saving: '+'; '.join(warnings))
        stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-')+secrets.token_hex(3)
        if raw is not None:
            backup=self.state/'backups/guides'/(stamp+'.md')
            backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(raw)
        newline='\r\n' if raw is not None and b'\r\n' in raw else '\n'
        content=text.replace('\r\n','\n').replace('\r','\n').replace('\n',newline).encode('utf-8')
        if raw is not None and raw.startswith(b'\xef\xbb\xbf'):content=b'\xef\xbb\xbf'+content
        path.parent.mkdir(parents=True,exist_ok=True)
        temporary=path.with_name(path.name+'.pronoun-guide.tmp')
        try:
            temporary.write_bytes(content)
            # Recheck after backup/validation to catch edits from another app.
            if (digest(path.read_bytes()) if path.exists() else None)!=sha:
                raise ValueError('The guide changed while saving. Reload it and try again.')
            os.replace(temporary,path)
        finally:
            if temporary.exists():temporary.unlink()
        return self.guide()

    def info(self):
        candidate_files = []
        if self.source.exists():
            for p in self.source.rglob('*'):
                if p.is_file() and p.suffix.lower() in ('.adv', '.json'):
                    candidate_files.append(p)

        def has_dialogues(p):
            if p.suffix.lower() == '.adv': return True
            try:
                with p.open('r', encoding='utf-8', errors='ignore') as f:
                    chunk = f.read(16384)
                    return '"type": "message"' in chunk or '"type":"message"' in chunk or '"dialogues"' in chunk or '"text"' in chunk
            except Exception:
                return False

        dialogue_files = []
        other_files = []
        for p in candidate_files:
            rel = str(p.relative_to(self.source)).replace('\\', '/')
            if has_dialogues(p):
                dialogue_files.append(rel)
            else:
                other_files.append(rel)

        files = sorted(dialogue_files) + sorted(other_files)
        completed=self.completed_scripts()
        return dict(root=str(self.root), files=[name for name in files if name not in completed],
                    all_files=files,completed_files=[name for name in files if name in completed],
                    config=self.config, guide=self.guide(),
                    ollama_key_configured=ollama.KeyVault(self.state).configured(self.config['ollama']['base_url']))

    def build(self, body, compile_game, install_game=False):
        with BuildSlot(self.state) as slot:
            result=self._build(body,compile_game,install_game,slot.working)
            context=result.pop('_install_context',None)
            report=result['report']
            if report['status']=='passed':
                check_snapshots(self,context[0])
                slot.publish()
                try:
                    if install_game:
                        documents,baseline,protected=context
                        install_build(self,slot.current,documents,report,baseline,protected)
                    write_json(slot.current/'validation.json',report)
                    slot.commit()
                    result['path']=str(slot.current)
                    return result
                except Exception as error:
                    report.update(status='failed',error=str(error))
            # Failed attempts keep the previous successful build and one diagnostic log.
            (self.state/'last-build.log').write_text(result['log'],encoding='utf-8')
            write_json(self.state/'last-build-error.json',report)
            result['path']=str(self.state/'last-build-error.json')
            return result

    def _build(self, body, compile_game, install_game, dest):
        documents=collect_documents(self,body)
        doc=documents[0]
        stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-') + secrets.token_hex(3)
        source, output, verified = dest/'src', dest/'game', dest/'verified'
        baseline={str(p.relative_to(self.source)):digest(p.read_bytes()) for p in self.source.rglob('*') if p.is_file()}
        protected=protected_hashes(self.root)
        archives_before={dst:digest((self.root/dst).read_bytes()) if (self.root/dst).is_file() else None for dst in self.config['install_files'].values()}
        # Always apply active saved text drafts, including hidden/completed files.
        shutil.copytree(self.source,source)
        staged={d['file']:stage_document(self,d,source,require_pixels=install_game) for d in documents}
        pixel_checked=any(item['pixels'] for item in staged.values())
        pending=[item for value in staged.values() for item in value['pending']]
        output.mkdir();verified.mkdir()
        write_json(dest/'translated.json',dict(doc,documents={d['file']:d for d in documents}))
        changed=[row for value in staged.values() for row in value['review']]
        report = dict(file=body['file'], source_sha256=doc['source_sha256'],
                      build_id=stamp,build_path=str(self.state/'build'),
                      staged_sha256=staged[doc['file']]['sha256'], guide=self.guide().get('sha256'),
                      review=changed, included_drafts=[d['file'] for d in documents],
                      changed_scripts=[name for name,item in staged.items() if item['changed']],
                      included_text_edits=len(changed),unapplied_pronoun_fields=pending,
                      staged_script_hashes={name:item['sha256'] for name,item in staged.items()},
                      coverage='Saved user draft corrections only; no full-scene review inferred.',
                      exclusions='No H labels inferred. Existing project exclusions remain authoritative.',
                      installed=False, roundtrip=False, compiler=False,
                      archives_before=archives_before,
                      pixel_widths_checked=pixel_checked,
                      layout=('Existing ADV slots and command stream preserved; character limits checked. Pixel/live visual validation pending.'
                              if Path(body['file']).suffix.lower() == '.adv' else
                              'JSON fields preserved. Layout validation belongs to the configured game adapter/compiler.'),
                      source_hashes={str(p.relative_to(source)):digest(p.read_bytes()) for p in source.rglob('*') if p.is_file()})
        write_json(dest/'review.json', report)
        if pixel_checked:
            report['layout']='Existing line slots and commands preserved; edited lines measured with unifont_jp.otf. Live scene visual check not performed.'
        variables = {'source':str(source), 'output':str(output), 'verified':str(verified),
                     'project':str(self.root), 'json':str(dest/'translated.json')}
        log = []
        try:
            if compile_game:
                if not self.config['compiler']: raise ValueError('No compiler configured. Edit Project settings; the staged script is already exported.')
                for label in ('compiler', 'decompiler'):
                    argv = self.config.get(label, [])
                    if not argv: continue
                    command = [s.format(**variables) for s in argv]
                    result = subprocess.run(command, cwd=dest, capture_output=True, timeout=180,
                                            creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
                    log.append(result.stdout.decode('utf-8', errors='replace') + result.stderr.decode('utf-8', errors='replace'))
                    if result.returncode: raise ValueError(f'{label} failed ({result.returncode}). See build.log.')
                    report[label] = True
                if self.config.get('decompiler'):
                    for p in source.rglob('*.ADV'):
                        other = verified/p.relative_to(source)
                        if not other.exists(): raise ValueError('Missing round-trip script: '+p.name)
                        # Compare text plus inline MS strings; labels may be renamed by decompilation.
                        if roundtrip_literals(p.read_text(encoding=self.config['encoding'])) != roundtrip_literals(other.read_text(encoding=self.config['encoding'])):
                            raise ValueError('Round-trip text differs: '+p.name)
                    report['roundtrip'] = True
                    report['roundtrip_scripts'] = len(list(source.rglob('*.ADV')))
                else:
                    report['roundtrip'] = True
            report['status'] = 'passed'
        except Exception as e:
            report['status'] = 'failed'; report['error'] = str(e)
        (dest/'build.log').write_text('\n'.join(log), encoding='utf-8')
        write_json(dest/'validation.json', report)
        return dict(path=str(dest), report=report, log='\n'.join(log)[-6000:],
                    _install_context=(documents,baseline,protected))

PROJECT = None

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args): pass

    def send(self, data, status=200, content_type='application/json; charset=utf-8'):
        raw = json.dumps(data, ensure_ascii=False).encode('utf-8') if isinstance(data, (dict, list)) else data
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(raw)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'")
        self.end_headers(); self.wfile.write(raw)

    def allowed(self):
        return (self.headers.get('Host') == f'127.0.0.1:{self.server.server_port}'
                and self.headers.get('Sec-Fetch-Site', 'none') in ('none', 'same-origin'))

    def do_GET(self):
        if not self.allowed(): return self.send({'error':'Invalid host'}, 403)
        url = urlparse(self.path); query = parse_qs(url.query)
        if url.path=='/api/session/stream':
            if query.get('token',[''])[0]!=KEY:return self.send({'error':'Invalid local session'},403)
            client_id=query.get('client_id',[''])[0]
            try:self.server.browser_sessions.touch(client_id,'alive')
            except ValueError as error:return self.send({'error':str(error)},400)
            try:
                self.connection.settimeout(10)
                self.send_response(200);self.send_header('Content-Type','text/event-stream')
                self.send_header('Cache-Control','no-store');self.send_header('X-Accel-Buffering','no');self.end_headers()
                self.wfile.write(b'retry: 1000\n\n');self.wfile.flush()
                while True:
                    self.wfile.write(b': editor heartbeat\n\n');self.wfile.flush()
                    self.server.browser_sessions.touch(client_id,'alive')
                    time.sleep(1)
            except (OSError,ValueError):pass
            finally:self.server.browser_sessions.touch(client_id,'disconnect')
            return
        try:
            with LOCK:
                if url.path == '/api/project': return self.send(PROJECT.info())
                if url.path == '/api/document': return self.send(PROJECT.load(query['file'][0]))
                if url.path == '/api/japanese': return self.send(japanese_references(PROJECT,query['file'][0]))
                if url.path == '/api/english': return self.send(japanese_references(PROJECT,query['file'][0],'english'))
                if url.path == '/api/job': return self.send(JOB)
                if url.path == '/api/ollama/job':
                    job=AI_JOBS.get(query.get('id',[''])[0])
                    if job is None:return self.send({'error':'Ollama request expired.'},404)
                    return self.send(job)
                if url.path == '/api/draft':
                    return self.send(read_json(PROJECT.draft_path(query['file'][0])))
                if url.path == '/api/version':
                    name = query['file'][0]; p = PROJECT.file(name); d = PROJECT.draft_path(name)
                    return self.send({'version':f'{digest(p.read_bytes())}:{d.stat().st_mtime_ns if d.exists() else 0}'})
                if url.path == '/bootstrap.js':
                    return self.send(('window.EDITOR_KEY='+json.dumps(KEY)+';').encode(), content_type='text/javascript')
                assets = {'/':'index.html', '/app.js':'app.js', '/pronouns.js':'pronouns.js', '/heartbeat.js':'heartbeat.js', '/style.css':'style.css'}
                if url.path not in assets: return self.send({'error':'Not found'}, 404)
                ext = Path(assets[url.path]).suffix
                return self.send((BASE/'web'/assets[url.path]).read_bytes(), content_type={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8'}[ext])
        except (ValueError, KeyError, OSError) as e: self.send({'error':str(e)}, 400)

    def do_POST(self):
        global PROJECT, JOB
        if not self.allowed():
            return self.send({'error':'Invalid local session'}, 403)
        try:
            length = int(self.headers.get('Content-Length', 0))
            if length > 8_000_000: raise ValueError('Request too large.')
            body = json.loads(self.rfile.read(length))
            authorized=self.headers.get('X-Editor-Key')==KEY
            if not authorized and not (self.path=='/api/session' and body.get('token')==KEY):
                return self.send({'error':'Invalid local session'},403)
            if self.path=='/api/session':
                self.server.browser_sessions.touch(body.get('client_id'),body.get('event'))
                return self.send({'status':'ok'})
            if self.path=='/api/shutdown':
                self.server.browser_sessions.request_exit()
                return self.send({'status':'shutting_down','waiting_for_build':bool(JOB.get('running'))})
            if self.path == '/api/ollama/models':
                with LOCK:
                    project=PROJECT
                    config=ollama.settings(body.get('ollama',project.config['ollama']))
                    supplied=body.get('api_key','')
                    if not isinstance(supplied,str):raise ValueError('API key must be text.')
                    key=supplied.strip() or ollama.KeyVault(project.state).read(config['base_url'])
                models=ollama.list_models(config,key)
                return self.send({'models':models,'message':f'Connected. {len(models)} models available.'})
            with LOCK:
                if JOB.get('running'): raise ValueError('A build is running. Wait for it to finish.')
                if self.path == '/api/save': return self.send(PROJECT.save(body))
                if self.path == '/api/completion':return self.send(PROJECT.set_completed(body))
                if self.path == '/api/guide':return self.send(PROJECT.save_guide(body))
                if self.path == '/api/guide/preview':
                    if not isinstance(body.get('text'),str):raise ValueError('Guide content must be text.')
                    rules,warnings=guide_rules(body['text'])
                    return self.send({'rules':rules,'warnings':warnings})
                if self.path == '/api/project':
                    PROJECT = Project(body['root']); return self.send(PROJECT.info())
                if self.path == '/api/settings':
                    config = body['config']
                    for language in ('japanese','english'):
                        folder=config.get(language+'_source_dir','')
                        if not isinstance(folder,str):raise ValueError(language+' source folder must be text.')
                        if folder.strip():
                            reference=(PROJECT.root/folder.strip()).resolve()
                            if not reference.is_dir() or not any(reference.glob('*.ADV')):
                                raise ValueError(language.capitalize()+' source folder must contain extracted ADV scripts.')
                        config[language+'_source_dir']=folder.strip()
                    for key in ('source_dir','guide','encoding'):
                        if not isinstance(config.get(key), str): raise ValueError(key+' must be text.')
                    for key in ('compiler','decompiler','extra_pronouns'):
                        if not isinstance(config.get(key, []), list) or any(not isinstance(s, str) for s in config.get(key, [])):
                            raise ValueError(key+' must be a list of strings.')
                    mapping=config.get('install_files',{})
                    if not isinstance(mapping,dict) or any(not isinstance(k,str) or not isinstance(v,str) for k,v in mapping.items()):
                        raise ValueError('install_files must map compiled archive names to project-relative destinations.')
                    candidate = (PROJECT.root/config['source_dir']).resolve()
                    if candidate == PROJECT.root or not candidate.is_relative_to(PROJECT.root): raise ValueError('source_dir must be a project subfolder.')
                    config['ollama']=ollama.settings(config.get('ollama'))
                    if 'api_key' in config.get('ollama',{}):raise ValueError('Use the API key field instead of project JSON.')
                    supplied=body.get('ollama_api_key','')
                    if not isinstance(supplied,str):raise ValueError('API key must be text.')
                    vault=ollama.KeyVault(PROJECT.state)
                    if body.get('clear_ollama_key'):vault.clear()
                    if supplied.strip():vault.save(supplied,config['ollama']['base_url'])
                    write_json(PROJECT.config_file, config); PROJECT = Project(PROJECT.root)
                    return self.send(PROJECT.info())
                if self.path == '/api/ollama/revise':
                    project=PROJECT
                    job_id=secrets.token_urlsafe(16)
                    for old in list(AI_JOBS):
                        if len(AI_JOBS)<20:break
                        if not AI_JOBS[old].get('running'):del AI_JOBS[old]
                    if len(AI_JOBS)>=20:raise ValueError('Too many active Ollama requests.')
                    AI_JOBS[job_id]={'running':True,'message':'Ollama is identifying participants and revising pronouns…'}
                    def revise_line():
                        try:
                            revision=ollama.revise(project,body)
                            with LOCK:
                                if PROJECT.root!=project.root:raise ValueError('Project changed; the Ollama response was not applied.')
                                if JOB.get('running'):raise ValueError('A build started; the Ollama response was not applied. Try again after the build.')
                                if project.guide().get('sha256')!=revision['guide_sha256']:
                                    raise ValueError('The guide changed during the Ollama request. Please retry.')
                                metadata={k:revision[k] for k in ('model','reason','confidence','guide_sha256','request_sha256')}
                                saved=project.save({'file':body['file'],'row':revision['row'],
                                    'source_sha256':revision['source_sha256'],'draft_revision':revision['draft_revision'],
                                    'rule':{'provider':'Ollama',**metadata},'ollama_metadata':metadata})
                                AI_JOBS[job_id]={'running':False,'document':saved,**metadata}
                        except Exception as error:
                            with LOCK:AI_JOBS[job_id]={'running':False,'error':str(error)}
                    threading.Thread(target=revise_line,daemon=True).start()
                    return self.send({'job_id':job_id})
                if self.path == '/api/reset':
                    p = PROJECT.draft_path(body['file'])
                    if p.exists(): p.rename(p.with_suffix('.'+str(time.time_ns())+'.backup.json'))
                    return self.send(PROJECT.load(body['file']))
                if self.path in ('/api/build', '/api/export', '/api/install'):
                    project, compile_game, install_game = PROJECT, self.path != '/api/export', self.path == '/api/install'
                    JOB = dict(running=True, message='Preparing staged output…')
                    def work():
                        global JOB
                        try: result = project.build(body, compile_game, install_game)
                        except Exception as e: result = {'error':str(e)}
                        with LOCK: JOB = dict(running=False, **result)
                    threading.Thread(target=work, daemon=True).start()
                    return self.send(JOB)
                return self.send({'error':'Not found'}, 404)
        except (ValueError, KeyError, OSError, TypeError) as e: self.send({'error':str(e)}, 400)

def main():
    global PROJECT
    parser = argparse.ArgumentParser(description='Offline pronoun editor for ADV and dialogue JSON.')
    parser.add_argument('--project', default=detect_project_root())
    parser.add_argument('--port', type=int, default=0)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    project_root = detect_project_root(args.project)
    PROJECT = Project(project_root)

    server_file = PROJECT.state / 'server.json'
    if server_file.is_file():
        try:
            info = read_json(server_file)
            alive_url = info.get('url')
            if alive_url:
                import urllib.request
                req = urllib.request.Request(alive_url + 'bootstrap.js', headers={'User-Agent': 'PronounStudio-Ping'})
                with urllib.request.urlopen(req, timeout=0.8) as resp:
                    if resp.status == 200:
                        if not args.no_browser: webbrowser.open(alive_url)
                        return
        except Exception:
            pass

    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    server.browser_sessions=BrowserSessions()
    def watch_browser():
        while True:
            time.sleep(.5)
            # Let an active compile/install finish before releasing its host.
            with LOCK:
                stop=server.browser_sessions.should_shutdown(busy=bool(JOB.get('running')))
            if stop:
                server.shutdown()
                return
    threading.Thread(target=watch_browser,daemon=True).start()
    url = f'http://127.0.0.1:{server.server_port}/'
    try:
        write_json(server_file, {'port': server.server_port, 'pid': os.getpid(), 'url': url})
    except Exception:
        pass
    print('Pronoun Editor: '+url, flush=True)
    if not args.no_browser: webbrowser.open(url)
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally:
        clean_server_registration(server_file,os.getpid())
        server.server_close()

if __name__ == '__main__': main()
