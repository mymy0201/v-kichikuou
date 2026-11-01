"""Original Japanese from explicit mappings and recorded scene evidence.

Never align independent language versions by line number or ordinal position.
"""
from pathlib import Path
import json
from core import parse_adv,digest
from source_alignment import project_references

def norm(text):return ' '.join(text.split()) if isinstance(text,str) else ''

def references(project,name,language='japanese'):
    if language not in ('japanese','english'):raise ValueError('Unsupported reference language.')
    source=project.file(name);raw=source.read_bytes()
    if source.suffix.lower()!='.adv':return {'rows':{},'note':language.capitalize()+' reference unavailable for this adapter.'}
    if project.config.get(language+'_source_dir'):
        return project_references(project,name,language)
    rows=parse_adv(raw,project.config['encoding']);result={}
    explicit=project.root/(language+'-lines.json')
    if explicit.exists():
        data=json.loads(explicit.read_text(encoding='utf-8')).get(name,{})
        if data.get('source_sha256')==digest(raw):
            for row in rows:
                text=data.get('rows',{}).get(row['id'])
                if isinstance(text,str) and text.strip():result[row['id']]={'text':text,'scope':'line','source':language+'-lines.json'}
    aligned=project_references(project,name,language)
    for key,value in aligned['rows'].items():result.setdefault(key,value)
    # Exact current Vietnamese text + recorded scene anchors are required. An
    # aligned scene passage may cover multiple boxes; label its scope explicitly.
    candidates={r['id']:{} for r in rows if r['id'] not in result}
    for path in sorted((project.root/'editorial_review').glob('*/aligned_scene_evidence.json')):
        entries=json.loads(path.read_text(encoding='utf-8'))
        if not isinstance(entries,list):continue
        inventory=None
        for entry in entries:
            if entry.get('file')!=name:continue
            jp=entry.get(language+'_override') or entry.get(language)
            after=norm(entry.get('after'));scene=entry.get('scene')
            if not isinstance(jp,str) or not jp.strip() or not after:continue
            if not scene:
                if inventory is None:
                    inv=path.parent/'inventory.json'
                    inventory=json.loads(inv.read_text(encoding='utf-8')) if inv.exists() else {}
                group=entry.get('group');groups=inventory.get(name,{}).get('vi',[])
                if isinstance(group,int) and 0<=group<len(groups):scene=groups[group].get('scene')
            if not scene:continue
            matches=[r for r in rows if r['scene']==scene and len(norm(r['text']))>=12 and (' '+norm(r['text'])+' ') in (' '+after+' ')]
            for row in matches:
                if row['id'] in candidates:candidates[row['id']][norm(jp)]={'text':jp,'scope':'aligned scene passage','source':path.relative_to(project.root).as_posix()}
    for key,options in candidates.items():
        if len(options)==1:result[key]=next(iter(options.values()))
    return {'rows':result,'stats':aligned.get('stats',{}),'note':'Explicit mappings, recorded scene evidence and source command alignment; unavailable lines are never guessed.'}
