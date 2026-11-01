"""Transactional installation of a verified build, with rollback and review records."""
from pathlib import Path
import datetime
import json
import os
import shutil
import subprocess
import sys
from core import digest, parse_adv, parse_json,command_skeleton

def run_indexer(indexer,suffix,root):
    if getattr(sys,'frozen',False):
        # A frozen GUI executable is not a Python CLI; execute the trusted project
        # indexer inside this interpreter instead of launching the GUI with -c.
        import contextlib,io,runpy
        from types import SimpleNamespace
        class Capture(io.StringIO):
            def reconfigure(self,**kwargs):pass
        stream=Capture();old_args=sys.argv[:];old_path=sys.path[:];code=0
        try:
            sys.argv=[str(indexer),*suffix];sys.path.insert(0,str(indexer.parent))
            with contextlib.redirect_stdout(stream),contextlib.redirect_stderr(stream):
                try:runpy.run_path(str(indexer),run_name='__main__')
                except SystemExit as error:
                    code=error.code if isinstance(error.code,int) else 1 if error.code else 0
                    if error.code:print(error.code)
        finally:sys.argv=old_args;sys.path[:]=old_path
        return SimpleNamespace(returncode=code,stdout=stream.getvalue().encode('utf-8'),stderr=b'')
    runner="import sys,runpy;from pathlib import Path;script=sys.argv[1];sys.path.insert(0,str(Path(script).parent));sys.argv=sys.argv[1:];runpy.run_path(script,run_name='__main__')"
    return subprocess.run([sys.executable,'-c',runner,str(indexer),*suffix],cwd=root,capture_output=True,timeout=180,
                          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))

def json_write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def confined(root, relative):
    p=(root/relative).resolve()
    if not p.is_relative_to(root.resolve()) or p==root.resolve():
        raise ValueError('Installation path must stay inside its project: '+str(relative))
    return p

def protected_hashes(root):
    paths=list(root.glob('*.asd')) + list((root/'save').rglob('*')) + list((root/'Vietnamese'/'Save').rglob('*'))
    paths += [root/n for n in ('unifont_jp.otf','.xsys35rc')]
    return {str(p.relative_to(root)):digest(p.read_bytes()) for p in paths if p.is_file()}

def install_build(project, dest, doc, report, baseline, protected):
    if report.get('status')!='passed' or not report.get('compiler') or not report.get('roundtrip'):
        raise ValueError('Installation requires successful compilation and decompiler verification.')
    root=project.root; output=dest/'game'; stage=dest/'src'
    mapping=project.config.get('install_files',{})
    if not mapping: raise ValueError('No install_files configured. Build output remains available in the staging folder.')
    current={str(p.relative_to(project.source)):digest(p.read_bytes()) for p in project.source.rglob('*') if p.is_file()}
    if current!=baseline: raise ValueError('Source changed while building. Compile again before installing.')
    documents=doc if isinstance(doc,list) else [doc]
    from batch import check_snapshots
    check_snapshots(project,documents)
    doc=documents[0]
    for name,sha in report.get('archives_before',{}).items():
        live=confined(root,name)
        if (digest(live.read_bytes()) if live.is_file() else None)!=sha:
            raise ValueError('Installed game changed while building. Compile again.')
    if protected_hashes(root)!=protected: raise ValueError('Saves or protected assets changed while building. Retry after closing the game.')
    targets={project.file(d['file']):(stage/d['file']).read_bytes() for d in documents}
    for src,dst in mapping.items():
        staged=confined(output,src); live=confined(root,dst)
        if live.suffix.lower() not in ('.ald','.ain','.dts'):
            raise ValueError('This installer accepts game archives (.ald/.ain/.dts) only; saves and assets are protected.')
        if not staged.is_file() or not staged.stat().st_size: raise ValueError('Missing compiled archive: '+src)
        if live in targets: raise ValueError('Duplicate installation destination.')
        targets[live]=staged.read_bytes()
    build_id=report.get('build_id',dest.name)
    batch='pronoun_studio_'+build_id
    er=root/'editorial_review'; batch_dir=er/batch
    queue=er/'scripts_by_size_20261022/order.json'
    indexer=root/'tools/update_review_indexes.py'
    has_workflow=indexer.is_file() and queue.is_file()
    ancillary=[project.draft_path(d['file']) for d in documents]
    completion_file=project.state/'completed-scripts.json'
    if completion_file.exists():ancillary.append(completion_file)
    if has_workflow:
        ancillary += [queue, er/'README-current.txt', root/'scripts_by_size.md', root/'excluded_h_scene_lines.md', er/'review_indexes.generated.json']
    # Snapshot all files touched by install/metadata hooks before the first mutation.
    backup=project.state/'backups'/build_id; originals={}
    for path in [*targets,*ancillary]:
        originals[path]=path.read_bytes() if path.exists() else None
        if originals[path] is not None:
            p=backup/path.relative_to(root);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(originals[path])
    def replace_file(path, data):
        path.parent.mkdir(parents=True,exist_ok=True)
        temporary=path.with_name(path.name+'.pronoun-install.tmp')
        temporary.write_bytes(data)
        try: os.replace(temporary,path)
        finally:
            if temporary.exists():temporary.unlink()
    try:
        for path,data in targets.items():replace_file(path,data)
        report['installed_hashes']={str(p.relative_to(root)):digest(p.read_bytes()) for p in targets}
        for path,data in targets.items():
            if digest(path.read_bytes())!=digest(data):raise ValueError('Installed file verification failed: '+path.name)
        if protected_hashes(root)!=protected:raise ValueError('Protected files changed during installation.')
        report['installed']=True
        report['backup']=str(backup)
        report['protected_files_unchanged']=len(protected)
        if has_workflow:
            inventory={};coverage={};references={}
            review=[dict(r,file=r.get('file',doc['file'])) for r in report['review']]
            for document in documents:
                name=document['file'];oldraw=originals[project.file(name)]
                oldrows=(parse_adv if name.lower().endswith('.adv') else parse_json)(oldraw,project.config['encoding'])
                inventory[name]={'vi':[dict(r,start=r['lines'][0] if r['lines'] else None,end=r['lines'][-1] if r['lines'] else None) for r in oldrows]}
                edits=[r for r in review if r['file']==name]
                coverage[name]={'full_file_scope_complete':False,'correction_entries':len(edits),
                    'edited_dialogue_ids':[r['id'] for r in edits],
                    'semantic_review':'User saved corrections; JP scene alignment not established by this tool.',
                    'excluded_chunks':[],'exclusions_note':'Historical exclusion indices and provenance retained without reclassification.'}
                source_backup=batch_dir/'backup/src'/name;source_backup.parent.mkdir(parents=True,exist_ok=True);source_backup.write_bytes(oldraw)
                references[name]={}
                for lang in ('japanese','english'):
                    ref=er/'japanese_base_20261022/reference'/lang/name
                    if ref.exists():references[name][lang]={'path':str(ref.relative_to(root)),'sha256':digest(ref.read_bytes()),'aligned':False}
            json_write(batch_dir/'inventory.json',inventory)
            json_write(batch_dir/'coverage.json',coverage)
            json_write(batch_dir/'review.json',review)
            json_write(batch_dir/'provenance.json',{'source_hashes':{d['file']:d['source_sha256'] for d in documents},'guide_sha256':report['guide'],
                       'reference_files':references,'semantic_base':'No new translation or automatic JP alignment claimed.', 'original_exclusion_metadata':'Unmodified'})
            json_write(batch_dir/'validation.json',report)
            (batch_dir/'README.md').write_text('# Manual corrections from Pronoun Studio\n\nSaved draft dialogue edits only; not a complete scene/file review.\nBackup and validated build: '+str(dest)+'\n',encoding='utf-8')
            q=json.loads(queue.read_text(encoding='utf-8'))
            for row in q:
                if row['file'] in {d['file'] for d in documents}:row.setdefault('manual_edit_batches',[]).append(batch)
            json_write(queue,q)
            json_write(batch_dir/'order.json',q)
            with (er/'README-current.txt').open('a',encoding='utf-8') as f:
                f.write('\nLatest installed manual correction: editorial_review/'+batch+' (partial; queue review status unchanged)\n')
            # Write complete batch metadata first, then regenerate and verify indexes.
            logs=[]
            for suffix in ([],['--check']):
                result=run_indexer(indexer,suffix,root)
                logs.append(result.stdout.decode('utf-8',errors='replace')+result.stderr.decode('utf-8',errors='replace'))
                if result.returncode:raise ValueError('Review index update failed: '+logs[-1][-1800:])
            (batch_dir/'index-update.log').write_text('\n'.join(logs),encoding='utf-8')
            generated=json.loads((er/'review_indexes.generated.json').read_text(encoding='utf-8'))
            unresolved=generated.get('unresolved',[])
            json_write(batch_dir/'unresolved-index-records.json',unresolved)
            report['review_indexes']={'checked':True,'unresolved_records':len(unresolved),
                                      'unresolved_note':'Historical unresolved records retained; no guessed line mappings.'}
        # Rebase every installed draft together so later compiles cannot revert it.
        for document in documents:
            name=document['file']
            installed_raw=project.file(name).read_bytes()
            rows=(parse_adv if name.lower().endswith('.adv') else parse_json)(installed_raw,project.config['encoding'])
            oldraw=originals[project.file(name)]
            if len(rows)!=len(document['rows']):raise ValueError(name+': dialogue count changed unexpectedly during installation.')
            if name.lower().endswith('.adv') and command_skeleton(oldraw.decode(project.config['encoding']))!=command_skeleton(installed_raw.decode(project.config['encoding'])):
                raise ValueError(name+': gameplay commands changed during installation.')
            for row,previous in zip(rows,document['rows']):
                for key in ('speaker','addressee','self','call','ollama_review'):
                    if key in previous:row[key]=previous[key]
                if row['text']==previous.get('text'):row['spans']=previous['spans']
            json_write(project.draft_path(name),dict(document,source_sha256=digest(installed_raw),rows=rows,draft_revision=document['draft_revision']+1,conflict=False))
        if completion_file.exists():
            completed=json.loads(completion_file.read_text(encoding='utf-8'))
            for document in documents:
                name=document['file']
                if name in completed.get('files',{}):completed['files'][name]['source_sha256']=digest(project.file(name).read_bytes())
            json_write(completion_file,completed)
        report['installed_script_hashes']={d['file']:digest(project.file(d['file']).read_bytes()) for d in documents}
        if has_workflow:json_write(batch_dir/'validation.json',report)
        return report
    except Exception as error:
        rollback_errors=[]
        for path,data in originals.items():
            try:
                if data is None:
                    if path.exists():path.unlink()
                else:replace_file(path,data)
            except Exception as rollback_error:rollback_errors.append(str(rollback_error))
        report.update(installed=False,status='failed',rollback_errors=rollback_errors)
        if batch_dir.exists():json_write(batch_dir/'validation.json',dict(report,error=str(error),rolled_back=not rollback_errors))
        if rollback_errors:raise ValueError('Installation failed; rollback needs attention: '+'; '.join(rollback_errors)) from error
        raise ValueError('Installation cancelled; original files restored. '+str(error)) from error
