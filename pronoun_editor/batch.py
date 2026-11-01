"""Collect every pending text draft, independently of the editor dropdown."""
from pathlib import Path
from core import digest,render_adv,render_json,LITERAL,parse_adv
import json

def collect_documents(project,body):
    selected=project.load(body['file'])
    if selected['conflict'] or selected['source_sha256']!=body['source_sha256'] or selected['draft_revision']!=body['draft_revision']:
        raise ValueError('Source or draft changed. Reload before compiling.')
    documents=[selected]
    for path in sorted((project.state/'drafts').glob('*.json')):
        frozen=json.loads(path.read_text(encoding='utf-8'))
        name=frozen.get('file')
        # Archived reset drafts are history, not active compiler inputs.
        if not isinstance(name,str) or path!=project.draft_path(name) or name==selected['file']:continue
        if not any(r['text']!=r['original'] for r in frozen.get('rows',[])):continue
        try:document=project.load(name)
        except (OSError,ValueError) as error:raise ValueError(f'{name}: cannot load pending draft: {error}') from error
        if document['conflict']:raise ValueError(f'{name}: pending draft conflicts with the source. Restore this file and reconcile it before compiling.')
        documents.append(document)
    return documents

def check_snapshots(project,documents):
    for doc in documents:
        current=project.load(doc['file'])
        if current['conflict'] or current['source_sha256']!=doc['source_sha256'] or current['draft_revision']!=doc['draft_revision']:
            raise ValueError(f"{doc['file']}: draft or source changed while building. Compile again.")

def stage_document(project,doc,source,require_pixels=False):
    name=doc['file'];raw=project.file(name).read_bytes()
    try:
        if name.lower().endswith('.adv'):rendered=render_adv(raw,doc['rows'],project.config['encoding'],font_path=project.root/'unifont_jp.otf')
        else:rendered=render_json(raw,doc['rows'],project.config['encoding'])
    except ValueError as error:raise ValueError(f'{name}: {error}') from error
    font_path=project.root/'unifont_jp.otf';measured=False
    changed_rows=[r for r in doc['rows'] if r['text']!=r['original']]
    changed_indices=[i for i,r in enumerate(doc['rows']) if r['text']!=r['original']]
    staged_rows=parse_adv(rendered,project.config['encoding']) if name.lower().endswith('.adv') else []
    if staged_rows and len(staged_rows)!=len(doc['rows']):raise ValueError(name+': dialogue structure changed during reflow.')
    if font_path.exists() and name.lower().endswith('.adv') and changed_rows:
        try:from PIL import ImageFont
        except ImportError:
            if require_pixels:raise ValueError('Pixel validation needs Pillow. Use the updated portable runtime.')
        else:
            lines=rendered.decode(project.config['encoding']).splitlines();fonts={}
            for ordinal in changed_indices:
                row=staged_rows[ordinal]
                size=row['font']
                if size not in fonts:fonts[size]=ImageFont.truetype(str(font_path),size)
                limit=600 if row['width']==50 else 336
                for index in row['indices']:
                    if fonts[size].getlength(LITERAL.fullmatch(lines[index])[2])>limit:
                        raise ValueError(f"{name} {row['id']}: edited line exceeds {limit}px. Shorten it before installing.")
            measured=True
    (source/name).write_bytes(rendered)
    review=[dict(file=name,id=r['id'],lines=r['lines'],before=r['original'],after=r['text']) for r in changed_rows]
    pending=[]
    for row in doc['rows']:
        for role in ('self','call'):
            value=row.get(role,'').strip();unknown=[s for s in row['spans'] if s['role']=='unknown']
            if value and unknown and not any(s['role']==role for s in row['spans']) and all(s['text'].casefold()!=value.casefold() for s in unknown):
                pending.append({'file':name,'id':row['id'],'role':role,'value':value})
    return {'sha256':digest(rendered),'changed':raw!=rendered,'review':review,'pending':pending,'pixels':measured}
