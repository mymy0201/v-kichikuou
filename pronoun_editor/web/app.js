const PORTRAITS = {"0": "None", "1": "Rance", "2": "Sill", "3": "Bound", "4": "Soul", "5": "Lia", "6": "Maris", "7": "Leila", "8": "Menad", "9": "Kanami", "10": "Haurein", "11": "Melfeis", "12": "Unga", "13": "Rebecca", "14": "Cell", "15": "Anacelle", "16": "Mercy", "17": "Ruberan", "18": "Sheela", "19": "Stessel", "20": "Stessel", "21": "Shariella", "22": "Shariella", "23": "Shariella", "24": "Isoroku Yamamoto", "25": "Kouhime", "26": "Cream", "27": "Aoi", "28": "Katyusha", "29": "Saulnia", "30": "Saulnia", "31": "Camilla", "32": "Mokomoko", "33": "Makoto", "34": "Horaga", "35": "Kayblis", "36": "Wendy", "37": "Suzume", "38": "Elizabeth", "39": "Amiran", "40": "Amiran", "41": "Amiran", "42": "Gandhi", "43": "Chizuko", "44": "Papaya", "45": "Nagi", "46": "Somita", "47": "Somita", "48": "Somita", "49": "Shizuka", "50": "Maria", "51": "Sill", "52": "Annis", "53": "Annis", "54": "Miki", "55": "Kentarou", "56": "Red Eye", "57": "Red Eye", "58": "Magic", "59": "Sieg", "60": "Sieg", "61": "Chizuko", "62": "Kapara", "63": "Merim", "64": "Sanakia", "65": "Reili", "66": "Ran / Eleanor", "67": "Milli", "68": "Mill", "69": "Mill", "70": "Mill", "71": "Suke-san", "72": "Kaoru", "73": "Silky", "74": "Warg", "75": "Satella", "76": "Aviator", "77": "Arlcoate", "78": "Rafalia", "79": "Aya", "80": "Cafe", "81": "Julia", "82": "Pie-R", "83": "Martina", "84": "PG-7", "85": "PG-9", "86": "Martina", "87": "Martina", "88": "Kỵ sĩ Carfe", "89": "Cecil", "90": "Louis", "91": "Martina", "92": "Martina", "93": "Martina", "94": "Saitou", "95": "Saitou", "96": "Color", "97": "Cordoba", "98": "Tougen", "99": "Elena", "100": "Fuuka", "246": "Kayb-one", "247": "Kayb-nyan", "248": "Chaos", "249": "Hồn ma", "250": "Bóng đen", "252": "Bóng đen", "253": "Athena 2", "254": "Lính canh Zeth", "255": "Hoàng tử quái vật", "256": "Tường thành", "257": "Xacalite", "258": "Melfeis", "259": "Melfeis", "260": "Menad", "261": "Kinkaid", "262": "Barres", "263": "Sanakia", "352": "Alice", "356": "Alice", "357": "Alice", "365": "Saitou", "366": "Alice", "368": "Alice", "380": "Lập trình viên WAO", "381": "WAO", "382": "Suzu", "383": "WAO", "384": "Hầu gái AliceSoft", "385": "AliceSoft Staff", "386": "AliceSoft Staff", "387": "AliceSoft Staff", "388": "AliceSoft Staff", "390": "Orion", "395": "AliceSoft Staff", "397": "AliceSoft Staff", "401": "Ruberan", "402": "Barres", "403": "Rick", "404": "Cordoba", "405": "Ex", "406": "Kinkaid", "407": "Pegasus", "408": "Shangri-La", "409": "Shangri-La", "410": "Nữ quan Leazas", "411": "Thị trưởng Ice / Reili", "412": "Hào kiệt Diphtheria", "413": "Gengorou", "414": "Đại vương Mars", "415": "Kayblis", "416": "Kesselring", "417": "Nobunaga Oda", "418": "Noberu Maeda", "419": "Washi Tada", "420": "Katsuie", "421": "Ninja JAPAN", "422": "Sát thủ JAPAN", "423": "Patton", "424": "Hanty", "425": "Hubert", "426": "Freak", "427": "Mineva", "428": "Saizel", "429": "Saizel", "430": "Asuka", "431": "Dodge", "432": "Aristoles", "433": "Convert", "434": "Lelyukov", "435": "Tami", "436": "Maha", "437": "Nero", "438": "Pamela", "439": "Alexei", "440": "Ortega", "441": "Freak / Omega", "442": "Camilla", "443": "Graco (Rockearth)", "444": "Satella", "445": "Lei", "446": "Lei", "447": "Meglass", "448": "Cordoba", "449": "Freia / Ninja", "450": "Medusa", "451": "Kaito", "452": "Galtia", "453": "Red Eye", "454": "Babora", "455": "Medusa / Sứ đồ Alefgard", "456": "Saias", "457": "Uspira", "458": "Kabachahn", "459": "Magic", "460": "Rebecca", "461": "La Vaswald", "462": "Olhound", "463": "Thánh kỵ sĩ", "464": "Giáo hoàng AL", "465": "Giáo sĩ AL", "466": "Camilla", "467": "Carol", "468": "Nagi / Ragarl", "469": "Hầu gái Kesselring", "470": "Thương nhân", "471": "Nữ quan / Hầu cận", "472": "Soul", "473": "Binh sĩ", "474": "Sakanaku", "475": "Jibul", "476": "Horaga", "477": "Takeege", "478": "Rue / Thuộc hạ Chizuko", "479": "Binh sĩ Leazas", "480": "Ninja Suzume", "481": "Britti", "482": "Kayb-nyan", "483": "Strength / Silky", "484": "Côn đồ / Bound", "485": "Ngụy thiên thần", "486": "Giáo sĩ AL", "487": "Seconaot", "488": "Contaot", "489": "Salbenaot", "490": "King Dragon (KD)", "491": "Đại diện Giáo hoàng", "492": "Alefgard", "493": "Pastel Kalar", "494": "Somita", "495": "Vua Hanny", "496": "Giám mục AL", "497": "Giám định viên", "498": "Rolex", "499": "Hoàng tử quái vật"};
'use strict';
const $ = id => document.getElementById(id);
let project, doc, page=0, version='', saving=false, editing=null, editSpans=[], buildTimer=null, loadSequence=0, pendingRole=null, guideBaseText="", guideSha=null, aiBusy=false;
const size=40;
let japaneseRows={},japaneseStatus='Japanese reference not loaded.';
try{$('showJapanese').checked=localStorage.getItem('showJapaneseHover')==='true';}catch{}
async function loadJapanese(){
 const current=doc;if(!current||!$('showJapanese').checked)return;
 const root=project.root,name=current.file,sha=current.source_sha256,referenceVersion=project.config.japanese_source_dir||'';
 japaneseRows={};japaneseStatus='Loading original Japanese…';render();
 try{const data=await api('japanese?file='+encodeURIComponent(name));
 if(!doc||project.root!==root||doc.file!==name||doc.source_sha256!==sha||(project.config.japanese_source_dir||'')!==referenceVersion)return;
 japaneseRows=data.rows||{};japaneseStatus='No matching Japanese passage found in this source version.';render();
 }catch(error){if(doc?.file===name&&project.root===root){japaneseStatus='Japanese reference unavailable: '+error.message;render();}}
}
$('showJapanese').onchange=()=>{try{localStorage.setItem('showJapaneseHover',$('showJapanese').checked);}catch{}if($('showJapanese').checked)loadJapanese();else render();};

let englishRows={},englishStatus='English reference not loaded.';
try{$('showEnglish').checked=localStorage.getItem('showEnglishHover')==='true';}catch{}
async function loadEnglish(){
 const current=doc;if(!current||!$('showEnglish').checked)return;
 const root=project.root,name=current.file,sha=current.source_sha256,referenceVersion=project.config.english_source_dir||'';
 englishRows={};englishStatus='Loading original English…';render();
 try{const data=await api('english?file='+encodeURIComponent(name));
 if(!doc||project.root!==root||doc.file!==name||doc.source_sha256!==sha||(project.config.english_source_dir||'')!==referenceVersion)return;
 englishRows=data.rows||{};englishStatus='No matching English passage found in this source version.';render();
 }catch(error){if(doc?.file===name&&project.root===root){englishStatus='English reference unavailable: '+error.message;render();}}
}
$('showEnglish').onchange=()=>{try{localStorage.setItem('showEnglishHover',$('showEnglish').checked);}catch{}if($('showEnglish').checked)loadEnglish();else render();};

const terms=['Sự Thánh Thiện của cậu','Đức Thánh Cha','các bạn','các anh','chúng tôi','chúng ta','bọn ta','bọn tôi','các ngươi','anh ta','cô ta','ông ta','anh ấy','cô ấy','bệ hạ','ngài','ta','tôi','tao','tớ','mình','ngươi','mày','bạn','anh','chị','em','cô','ông','bà','hắn','nàng','chàng','nó','con','cha','mẹ','chú','bác','cậu',
 'công tử', 'tiểu thư', 'huynh trưởng', 'đại ca', 'sơ', 'đầu lĩnh', 'lão đại', 'thảo dân', 'thuộc hạ', 'thiện tín', 'công chúa', 'tướng quân', 'đại nhân', 'thống lĩnh', 'tiểu đệ', 'bần đạo', 'gã này', 'bản tọa', 'quân sư', 'chúa công'];
const selfTerms=new Set(['tôi','ta','tao','tớ','chúng tôi','chúng ta','bọn ta','bọn tôi','thảo dân','thuộc hạ','tiểu đệ','bần đạo','gã này','bản tọa']);
const callTerms=new Set(['ngươi','mày','các ngươi','các bạn','bệ hạ','đức thánh cha','công tử','tiểu thư','huynh trưởng','đại ca','sơ','đầu lĩnh','lão đại','đại nhân','tướng quân','công chúa','thống lĩnh','chúa công']);
function el(tag,attrs={},text){const n=document.createElement(tag);for(const [k,v] of Object.entries(attrs)){if(k==='class')n.className=v;else n.setAttribute(k,v);}if(text!==undefined)n.textContent=text;return n;}
function notice(text,error=false){$('notice').textContent=text;$('notice').classList.toggle('error',error);document.querySelectorAll('.dialogerror').forEach(n=>n.remove());if(error){const open=document.querySelector('dialog[open]');if(open)open.append(el('p',{class:'dialogerror',role:'alert'},text));}}
async function api(path,body){const r=await fetch('/api/'+path,body?{method:'POST',headers:{'Content-Type':'application/json','X-Editor-Key':window.EDITOR_KEY},body:JSON.stringify(body)}:{});const data=await r.json();if(!r.ok)throw new Error(data.error||'Request failed');return data;}
function guard(fn){return async(...args)=>{try{await fn(...args);}catch(e){notice(e.message,true);}};}
function tokenize(text){const all=[...new Set([...terms,...(project?.config.extra_pronouns||[])])].filter(Boolean).sort((a,b)=>b.length-a.length);const re=new RegExp('(?<![\\p{L}\\p{N}_])(?:'+all.map(s=>s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|')+')(?![\\p{L}\\p{N}_])','giu');return [...text.matchAll(re)].map(m=>({start:Array.from(text.slice(0,m.index)).length,end:Array.from(text.slice(0,m.index+m[0].length)).length,text:m[0],role:selfTerms.has(m[0].toLowerCase())?'self':callTerms.has(m[0].toLowerCase())?'call':'unknown'}));}
function highlighted(text,spans){const f=document.createDocumentFragment(),chars=Array.from(text);let p=0;for(const s of [...spans].sort((a,b)=>a.start-b.start)){f.append(document.createTextNode(chars.slice(p,s.start).join('')));f.append(el('mark',{class:s.role,title:s.role},chars.slice(s.start,s.end).join('')));p=s.end;}f.append(document.createTextNode(chars.slice(p).join('')));return f;}
const replace=(row,values)=>PronounEdit.replace(row,values);
function match(row){return project.guide.rules.filter(r=>r.speaker.toLowerCase()===row.speaker.trim().toLowerCase()&&r.addressee.toLowerCase()===row.addressee.trim().toLowerCase());}
function download(name,data){const url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'}));const a=el('a',{href:url,download:name});a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
async function loadProject(info,preferred){
 const selected=preferred||doc?.file||$('files').value;project=info||await api('project');
 $('projectPath').textContent=project.root;$('rootPath').value=project.root;
 $('files').replaceChildren(...project.files.map(f=>el('option',{value:f},f)));
 if(project.files.includes(selected))$('files').value=selected;
 $('files').disabled=!project.files.length;
 if(!project.files.length)$('files').append(el('option',{value:''},project.all_files?.length?'All scripts complete':'No scripts found'));
 $('completedScripts').textContent=`Completed (${(project.completed_files||[]).length})`;
 $('names').replaceChildren(...[...new Set(project.guide.rules.flatMap(r=>[r.speaker,r.addressee]))].sort().map(s=>el('option',{value:s})));
 $('pronouns').replaceChildren(...terms.map(s=>el('option',{value:s})));
 $('compile').textContent=Object.keys(project.config.install_files||{}).length?'Compile & install ↗':'Compile to game ↗';
 if(project.files.length)await loadFile();else{
  doc=null;render();
  notice(project.all_files?.length?'All scripts are marked complete. You can still compile, or restore a script from Completed.':'No scripts found. Set source_dir in Settings or add ADV / JSON files to the scripts folder.');
 }
}
async function loadFile(){
 if(saving)return;
 if(!project.files.length){doc=null;render();return;}
 const ticket=++loadSequence, name=$('files').value;
 doc=null;japaneseRows={};japaneseStatus='Japanese reference not loaded.';englishRows={};englishStatus='English reference not loaded.'; render(); notice('Loading '+name+'…');
 const [info,loaded,current]=await Promise.all([api('project'),api('document?file='+encodeURIComponent(name)),api('version?file='+encodeURIComponent(name))]);
 if(ticket!==loadSequence)return;
 project.guide=info.guide;doc=loaded;version=current.version;page=0;render();if($('showJapanese').checked)loadJapanese();if($('showEnglish').checked)loadEnglish();
 notice(doc.conflict?'Source changed; resolve the saved draft before editing.':`${doc.rows.length} dialogue blocks loaded. Changes save automatically to JSON.`);
}
async function save(row,rule){if(saving)throw new Error('A save is in progress. Please try again.');if(doc.conflict)throw new Error('Resolve the source conflict first.');saving=true;try{doc=await api('save',{file:doc.file,source_sha256:doc.source_sha256,draft_revision:doc.draft_revision,row,rule});version=(await api('version?file='+encodeURIComponent(doc.file))).version;render();notice('Saved to translation JSON. Dialogue preview updated.');}finally{saving=false;}}
function field(value,placeholder,onchange,list,oninput){
 const input=el('input',{value,placeholder,'aria-label':placeholder,...(list?{list}:{})});input.disabled=doc.conflict;
 let committed=value;
 const commit=guard(async()=>{if(input.value===committed)return;const next=input.value;committed=next;try{await onchange(next);}catch(e){committed=value;throw e;}});
 input.commitEdit=commit;
 input.addEventListener('change',commit);input.addEventListener('blur',commit);
 if(oninput)input.addEventListener('input',()=>oninput(input.value));
 input.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();commit();input.blur();}});return input;
}
async function setPronoun(row,role,value){
 value=value.trim();if(!value)throw new Error('Enter the replacement pronoun.');
 const prepared=PronounEdit.prepare(row,role);
 if(prepared.needsChoice){openEditor(row);pendingRole={role,value};notice(prepared.reason+' Assign '+role+' below, then Save dialogue to apply “'+value+'”.',true);return;}
 await save({...replace(prepared.row,{[role]:value}),[role]:value});
}
function previewPronoun(row,role,value,cell){
 if(!value.trim())return;
 const prepared=PronounEdit.prepare(row,role);if(prepared.needsChoice)return;
 const changed=replace(prepared.row,{[role]:value.trim()}),tr=cell.closest('tr');if(!tr)return;
 for(const node of tr.querySelectorAll('.preview,.full'))node.replaceChildren(highlighted(changed.text,changed.spans));
}
function roleCell(row,role){
 const cell=el('td'),pair=el('div',{class:'rolefields'}),name=role==='self'?'speaker':'addressee';
 pair.append(field(row[name],role==='self'?'Speaker name':'Addressee name',v=>save({...row,[name]:v}),'names'));
 pair.append(el('span',{},'→'));
 const input=field(row[role],role==='self'?'Self':'Call',v=>setPronoun(row,role,v),'pronouns',v=>previewPronoun(row,role,v,cell));
 pair.append(input);cell.append(pair);
 const bottom=el('div',{class:'rolebottom'}),detected=[...new Set(row.spans.filter(s=>s.role===role).map(s=>s.text))];
 const prepared=PronounEdit.prepare(row,role),candidates=[...new Set(prepared.row.spans.filter(s=>s.role===role).map(s=>s.text))];
 bottom.append(el('div',{class:'rolehint'},detected.length?'In dialogue: '+detected.join(' · '):!prepared.needsChoice?'Will replace: '+candidates.join(' · '):'Select a target with Edit'));
 const apply=el('button',{class:'applypronoun','aria-label':'Apply '+(role==='self'?'Self':'Call'),title:'Apply this field to the dialogue'},'Apply');
 apply.disabled=doc.conflict;apply.onpointerdown=e=>e.preventDefault();apply.onclick=guard(()=>setPronoun(row,role,input.value));bottom.append(apply);cell.append(bottom);return cell;
}
function render(){const body=$('rows');body.replaceChildren();$('markComplete').disabled=!doc;$('compile').disabled=!(project?.all_files||project?.files||[]).length;$('export').disabled=$('compile').disabled;if(!doc){$('counts').textContent='No script selected';$('empty').hidden=false;$('empty').textContent=project?.all_files?.length?'All scripts complete. Use Completed to restore a file.':'No scripts available.';$('conflict').hidden=true;return;}$('empty').textContent='No matching dialogue.';$('conflict').hidden=!doc.conflict;const q=$('search').value.toLowerCase(),filter=$('filter').value;const rows=doc.rows.filter(r=>[r.text,r.speaker,r.addressee,r.scene].join(' ').toLowerCase().includes(q)&&(filter==='all'||filter==='changed'&&r.text!==r.original||filter==='unknown'&&r.spans.some(s=>s.role==='unknown')||filter==='named'&&r.speaker));const pages=Math.max(1,Math.ceil(rows.length/size));page=Math.max(0,Math.min(page,pages-1));$('counts').textContent=`${rows.length} dialogue blocks · ${doc.rows.filter(r=>r.text!==r.original).length} edited · ${project.guide.rules.length} guide rules`;const sel=$('pageSelect');if(sel.options.length!==pages){sel.replaceChildren(...Array.from({length:pages},(_,i)=>el('option',{value:i},i+1)));}sel.value=page;$('pageTotal').textContent=`of ${pages}`;$('prev').disabled=page===0;$('next').disabled=page===pages-1;$('empty').hidden=rows.length>0;
 for(const row of rows.slice(page*size,(page+1)*size)){const tr=el('tr',{class:row.text!==row.original?'changed':''}),td=el('td'),meta=el('div',{class:'rowmeta'});meta.append(el('span',{},row.lines.length?'L'+row.lines[0]+'–'+row.lines.at(-1):'#'+row.id),el('span',{},row.scene));if(row.text!==row.original)meta.append(el('span',{class:'badge'},'EDITED'));if(row.ollama_review)meta.append(el('span',{class:'badge',title:row.ollama_review.reason||''},'OLLAMA · '+row.ollama_review.confidence));if(row.speaker_hint!==undefined&&row.speaker_hint!==null){
      const charName = row.speaker_name || PORTRAITS[row.speaker_hint] || '';
      const badgeText = 'Portrait ' + row.speaker_hint + (charName ? ' ----> ' + charName : '') + ' · confirm speaker';
      const badge = el('span', {class: 'badge portrait-badge', title: charName ? 'Portrait ' + row.speaker_hint + ': ' + charName + ' (Click to set as speaker)' : 'Portrait ' + row.speaker_hint}, badgeText);
      if(charName){
        badge.style.cursor = 'pointer';
        badge.addEventListener('click', guard(async()=>{
          row.speaker = charName;
          await save({...row, speaker: charName});
          render();
        }));
      }
      meta.append(badge);
    }td.append(meta);const dialogue=el('div',{class:'dialogue',tabindex:'0'}),preview=el('div',{class:'preview'}),full=el('div',{class:'full'});preview.append(highlighted(row.text,row.spans));full.append(highlighted(row.text,row.spans));if($('showJapanese').checked){const jp=japaneseRows[row.id],section=el('div',{class:'jp-reference',lang:'ja'});section.append(el('strong',{},jp?'Original Japanese · '+jp.scope:'Original Japanese'),el('div',{},jp?jp.text:japaneseStatus));if(jp)section.append(el('small',{},jp.source+(jp.reference_lines?.length?' · source lines '+jp.reference_lines[0]+'–'+jp.reference_lines.at(-1):'')));full.append(section);}if($('showEnglish').checked){const jp=englishRows[row.id],section=el('div',{class:'jp-reference',lang:'en'});section.append(el('strong',{},jp?'English reference · '+jp.scope:'English reference'),el('div',{},jp?jp.text:englishStatus));if(jp)section.append(el('small',{},jp.source+(jp.reference_lines?.length?' · source lines '+jp.reference_lines[0]+'–'+jp.reference_lines.at(-1):'')));full.append(section);}dialogue.append(preview,full);td.append(dialogue);tr.append(td,roleCell(row,'self'),roleCell(row,'call'));const util=el('td'),buttons=el('div',{class:'utilities'});for(const [label,cls,fn] of [['Edit','',()=>openEditor(row)],['Apply MD','auto',()=>applyRule(row)],['Revise with Ollama','ai',()=>reviseOllama(row)],[Object.keys(project.config.install_files||{}).length?'Compile & install':'Compile','',()=>build(true)]]){const b=el('button',{class:cls,title:label.startsWith('Compile')?'Compile this script and install it when configured':label},label);b.disabled=doc.conflict;if(label.startsWith('Compile'))b.onpointerdown=e=>e.preventDefault();b.addEventListener('click',guard(fn));buttons.append(b);}util.append(buttons);const rules=match(row);util.append(el('div',{class:'ruleevidence'},rules.length===1?'Guide line '+rules[0].line:rules.length>1?'Multiple rules · choose in guide':'Identify both names to match a rule'));tr.append(util);body.append(tr);}}
async function applyRule(row,chosen){if(!row.speaker||!row.addressee)throw new Error('Enter the speaker and addressee names first. Portrait hints do not establish who is being addressed.');const matches=match(row),rule=chosen||(matches.length===1?matches[0]:null);if(!rule){showGuide(row);notice(matches.length?'Multiple matching rules: choose one in the guide.':'No exact pair rule found. Read the guide or add an explicit pronouns block.');return;}const count=row.spans.filter(s=>s.role==='self'||s.role==='call').length;if(!count)throw new Error('Use Edit to assign Self / Call occurrences first.');const result=replace(row,{self:rule.self,call:rule.call});await save({...result,self:rule.self,call:rule.call},rule);notice(`Applied guide line ${rule.line} to ${count} assigned occurrences. ${row.spans.filter(s=>s.role==='unknown').length} ambiguous occurrences left for review.`);}
function openEditor(row){pendingRole=null;editing=structuredClone(row);editSpans=structuredClone(row.spans);$('editTitle').textContent=row.id;$('editText').value=row.text;const i=doc.rows.findIndex(r=>r.id===row.id);$('context').textContent=doc.rows.slice(Math.max(0,i-1),i+2).map(r=>`${r.id}${r.id===row.id?' [CURRENT]':''}\n${r.original}`).join('\n\n');renderTokens();$('editor').showModal();}
function renderTokens(){const box=$('tokens');box.replaceChildren();for(const [i,s] of editSpans.entries()){const wrap=el('label',{class:'token '+s.role});wrap.append(el('span',{},s.text));const select=el('select',{'aria-label':'Role of '+s.text+' at '+s.start});for(const [value,text] of [['unknown','Unassigned'],['self','Self'],['call','Call'],['other','Third / ignore']])select.append(el('option',{value},text));select.value=s.role;select.onchange=()=>{editSpans[i].role=select.value;renderTokens();};wrap.append(select);box.append(wrap);}if(!editSpans.length)box.append(el('p',{class:'hint'},'No known pronouns. Select text above to assign a custom phrase.'));}
function markSelection(role){const input=$('editText'),a=Array.from(input.value.slice(0,input.selectionStart)).length,b=Array.from(input.value.slice(0,input.selectionEnd)).length;if(a===b){notice('Select a phrase in the dialogue first.',true);return;}editSpans=editSpans.filter(s=>s.end<=a||s.start>=b);editSpans.push({start:a,end:b,text:Array.from(input.value).slice(a,b).join(''),role});editSpans.sort((x,y)=>x.start-y.start);renderTokens();}
function showGuide(row){$('guidePath').textContent=project.guide.path;$('guideSource').textContent=project.guide.text;$('guideStats').textContent=`${project.guide.rules.length} explicit pair rules imported. `+project.guide.warnings.join(' ');$('guideSearch').value=row?row.speaker:'';function draw(){const q=$('guideSearch').value.toLowerCase(),list=$('ruleList');list.replaceChildren();for(const r of project.guide.rules.filter(r=>JSON.stringify(r).toLowerCase().includes(q))){const card=el('div',{class:'rulecard'});card.append(el('strong',{},`${r.speaker} → ${r.addressee}`),el('div',{},`Self: ${r.self}   ·   Call: ${r.call}`),el('small',{},`Line ${r.line} · ${r.context||''}`));const detail=el('details');detail.append(el('summary',{},'Source evidence'),el('pre',{},r.source));card.append(detail);if(row&&r.speaker.toLowerCase()===row.speaker.toLowerCase()&&r.addressee.toLowerCase()===row.addressee.toLowerCase()){const b=el('button',{class:'primary'},'Apply this rule');b.onclick=guard(async()=>{await applyRule(row,r);$('guideDialog').close();});card.append(b);}list.append(card);}}$('guideSearch').oninput=draw;draw();$('guideText').value=project.guide.text;guideBaseText=$('guideText').value;guideSha=project.guide.sha256??null;$('guideSaveStatus').textContent='Edit the guide and save to reload its rules.';guideMode(false);$('guideDialog').showModal();}
async function build(compile){
 await document.activeElement.commitEdit?.();while(saving)await new Promise(r=>setTimeout(r,40));
 const buildDoc=doc||(project.completed_files?.length?await api('document?file='+encodeURIComponent(project.completed_files[0])):null);
 if(!buildDoc)throw new Error('Choose a script first.');
 const install=compile&&Object.keys(project.config.install_files||{}).length>0;
 $('buildTitle').textContent=install?'Compiling & installing…':compile?'Compiling game…':'Exporting script…';
 $('buildStatus').textContent=install?'Validating the build, backing up current files, and updating the game.':'Preparing this script’s saved edits.';
 $('buildLog').textContent='';$('buildDialog').showModal();
 try{await api(install?'install':compile?'build':'export',{file:buildDoc.file,source_sha256:buildDoc.source_sha256,draft_revision:buildDoc.draft_revision});}
 catch(e){$('buildTitle').textContent='Build could not start';$('buildStatus').textContent=e.message;throw e;}
 clearInterval(buildTimer);
 buildTimer=setInterval(guard(async()=>{
  const job=await api('job');if(job.running)return;clearInterval(buildTimer);
  const failure=job.error||job.report?.error,installed=job.report?.installed;
  $('buildTitle').textContent=failure?'Build needs attention':installed?'Installed in game':compile?'Compilation complete':'Script exported';
  $('buildStatus').textContent=(failure?failure+'\n':'')+(job.path||'');
  $('buildLog').textContent=(job.log||'')+'\n\n'+(job.report?(installed?`Source and game archives updated. Restart the game to load the changes.\nBackup: ${job.report.backup}\n`:'Output is staged; game files were not updated.\n')+`Saved text edits: ${job.report.included_text_edits||0}\nChanged scripts: ${(job.report.changed_scripts||[]).join(", ")}\nPronoun fields awaiting assignment: ${(job.report.unapplied_pronoun_fields||[]).length}\nRound-trip verified: ${job.report.roundtrip}\n${job.report.layout}`:'');
  if(installed){if(project.files.length)await loadFile();else await loadProject(await api('project'));}
  notice(failure||(installed?'Installed successfully. Restart the game.':'Output ready: '+job.path),!!failure);
 }),600);
}
$('files').onchange=guard(loadFile);$('reload').onclick=guard(loadFile);$('search').oninput=()=>{page=0;render();};$('filter').onchange=()=>{page=0;render();};$('prev').onclick=()=>{if(page>0){page--;render();}};$('next').onclick=()=>{page++;render();};$('pageSelect').onchange=(e)=>{page=parseInt(e.target.value,10)||0;render();};$('guide').onclick=()=>showGuide();$('closeGuide').onclick=closeGuide;$('editText').oninput=()=>{editSpans=tokenize($('editText').value);renderTokens();};$('markSelf').onclick=()=>markSelection('self');$('markCall').onclick=()=>markSelection('call');$('saveEdit').onclick=guard(async()=>{let row={...editing,text:$('editText').value,spans:editSpans};if(pendingRole){if(!editSpans.some(s=>s.role===pendingRole.role))throw new Error('Assign at least one occurrence to '+pendingRole.role+' first.');row={...replace(row,{[pendingRole.role]:pendingRole.value}),[pendingRole.role]:pendingRole.value};}await save(row);pendingRole=null;$('editor').close();});$('compile').onclick=guard(()=>build(true));$('export').onclick=guard(()=>build(false));$('closeBuild').onclick=()=>$('buildDialog').close();$('settings').onclick=openSettings;$('saveSettings').onclick=guard(saveSettings);$('project').onclick=()=>$('projectDialog').showModal();$('openProject').onclick=guard(async()=>{await loadProject(await api('project',{root:$('rootPath').value}));$('projectDialog').close();});$('downloadDraft').onclick=guard(async()=>download('previous-translation-draft.json',await api('draft?file='+encodeURIComponent(doc.file))));$('reset').onclick=guard(async()=>{doc=await api('reset',{file:doc.file});await loadFile();});$('shutdown').onclick=guard(async()=>{if(!confirm('Shut down Pronoun Studio? This stops the local background server.'))return;try{await api('shutdown',{});}catch(e){}document.body.innerHTML='<div style="display:flex;align-items:center;justify-content:center;height:100vh;flex-direction:column;font-family:system-ui,-apple-system,sans-serif;color:#18302e;background:#f4f6f2;text-align:center;padding:20px;"><div style="background:#c5e6aa;color:#173e35;border-radius:10px;padding:6px 14px;font-size:28px;font-weight:750;margin-bottom:16px;">P.</div><h1 style="font-size:24px;margin:0 0 10px;">Pronoun Studio has shut down</h1><p style="color:#697974;font-size:14px;max-width:440px;margin:0;">The local server has stopped cleanly. You can now close this browser tab.</p></div>';});
setInterval(async()=>{if(!doc||saving||document.querySelector('dialog[open]')||['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName))return;try{const next=(await api('version?file='+encodeURIComponent(doc.file))).version;if(version&&next!==version){const savedPage=page;await loadFile();page=savedPage;render();notice(doc.conflict?'Source changed. Your saved draft needs reconciliation.':'Reloaded the latest file changes.',doc.conflict);}}catch(e){notice(e.message,true);}},2000);
guard(loadProject)();

for(const id of ['compile','export'])$(id).onpointerdown=e=>e.preventDefault();

function guideMode(edit){
 $('guideRulesPane').hidden=edit;$('guideEditPane').hidden=!edit;
 $('guideRulesTab').setAttribute('aria-selected',String(!edit));$('guideEditTab').setAttribute('aria-selected',String(edit));
 if(edit)$('guideText').focus();
}
function closeGuide(){
 if($('guideText').value!==guideBaseText&&!confirm('Discard the unsaved guide changes?'))return;
 $('guideDialog').close();
}
$('guideDialog').addEventListener('cancel',e=>{e.preventDefault();closeGuide();});
$('guideRulesTab').onclick=()=>guideMode(false);$('guideEditTab').onclick=()=>guideMode(true);
$('guideText').oninput=()=>{$('guideSaveStatus').textContent=$('guideText').value===guideBaseText?'No unsaved changes.':'Unsaved changes · Ctrl+S to save';};
$('previewGuide').onclick=guard(async()=>{
 const result=await api('guide/preview',{text:$('guideText').value});
 $('guideSaveStatus').textContent=result.warnings.length?'Fix before saving: '+result.warnings.join('; '):`${result.rules.length} pair rules found. The guide has not been saved yet.`;
});
$('saveGuide').onclick=guard(async()=>{
 $('saveGuide').disabled=true;
 try{
  const guide=await api('guide',{text:$('guideText').value,sha256:guideSha});
  project.guide=guide;guideSha=guide.sha256;$('guideText').value=guide.text;guideBaseText=$('guideText').value;
  $('guideSource').textContent=guide.text;$('guidePath').textContent=guide.path;$('guideStats').textContent=`${guide.rules.length} explicit pair rules imported. `+guide.warnings.join(' ');
  $('names').replaceChildren(...[...new Set(guide.rules.flatMap(r=>[r.speaker,r.addressee]))].sort().map(s=>el('option',{value:s})));
  $('guideSearch').oninput();render();
  $('guideSaveStatus').textContent=`Saved. ${guide.rules.length} rules reloaded and ready for Apply MD.`;
  notice('Translation guide saved; rule suggestions refreshed.');
 }finally{$('saveGuide').disabled=false;}
});
$('guideText').addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='s'){e.preventDefault();$('saveGuide').click();}});
$('reloadGuide').onclick=guard(async()=>{
 if($('guideText').value!==guideBaseText&&!confirm('Replace your unsaved guide text with the version on disk?'))return;
 project.guide=(await api('project')).guide;const guide=project.guide;
 $('guideText').value=guide.text;guideBaseText=$('guideText').value;guideSha=guide.sha256??null;
 $('guideSource').textContent=guide.text;$('guideSearch').oninput();render();
 $('guideSaveStatus').textContent='Reloaded the guide from disk.';
});

function openSettings(){
 const advanced=structuredClone(project.config);delete advanced.ollama;
 $('settingsText').value=JSON.stringify(advanced,null,2);
 $('japaneseSource').value=project.config.japanese_source_dir||'';$('englishSource').value=project.config.english_source_dir||'';
 const c=project.config.ollama||{};
 $('ollamaEnabled').checked=!!c.enabled;$('ollamaUrl').value=c.base_url||'http://127.0.0.1:11434';$('ollamaModel').value=c.model||'';
 $('ollamaTimeout').value=c.timeout||120;$('ollamaContext').value=c.context_lines??2;
 $('ollamaKey').value='';$('ollamaClearKey').checked=false;
 $('ollamaKeyStatus').textContent=project.ollama_key_configured?'An API key is saved for this endpoint. Leave this field blank to keep it.':'No API key saved for this endpoint. Local Ollama usually needs no key.';
 $('ollamaTestStatus').textContent='';$('settingsDialog').showModal();
}
function ollamaSettings(){
 return {...(project.config.ollama||{}),enabled:$('ollamaEnabled').checked,base_url:$('ollamaUrl').value.trim(),model:$('ollamaModel').value.trim(),timeout:Number($('ollamaTimeout').value),context_lines:Number($('ollamaContext').value)};
}
async function saveSettings(){
 const config=JSON.parse($('settingsText').value);config.ollama=ollamaSettings();config.japanese_source_dir=$('japaneseSource').value.trim();config.english_source_dir=$('englishSource').value.trim();
 $('saveSettings').disabled=true;
 try{await loadProject(await api('settings',{config,ollama_api_key:$('ollamaKey').value,clear_ollama_key:$('ollamaClearKey').checked}));$('ollamaKey').value='';$('settingsDialog').close();notice('Settings saved. Ollama is '+(project.config.ollama.enabled?'enabled.':'disabled.'));}
 finally{$('saveSettings').disabled=false;}
}
$('defaultReferences').onclick=()=>{$('japaneseSource').value='';$('englishSource').value='';};
$('ollamaLocal').onclick=()=>{$('ollamaUrl').value='http://127.0.0.1:11434';};
$('ollamaCloud').onclick=()=>{$('ollamaUrl').value='https://ollama.com';};
$('testOllama').onclick=guard(async()=>{
 $('testOllama').disabled=true;$('ollamaTestStatus').textContent='Connecting…';
 try{const data=await api('ollama/models',{ollama:ollamaSettings(),api_key:$('ollamaKey').value});$('ollamaModels').replaceChildren(...data.models.map(name=>el('option',{value:name})));$('ollamaTestStatus').textContent=data.message;if(!$('ollamaModel').value&&data.models.length)$('ollamaModel').value=data.models[0];}
 catch(e){$('ollamaTestStatus').textContent=e.message;throw e;}finally{$('testOllama').disabled=false;}
});
$('closeOllama').onclick=()=>$('ollamaDialog').close();
async function reviseOllama(row){
 if(aiBusy)throw new Error('An Ollama revision is already running.');
 if(!project.config.ollama?.enabled||!project.config.ollama?.model){openSettings();notice('Enable Ollama and choose a model, then save Settings.',true);return;}
 await document.activeElement.commitEdit?.();while(saving)await new Promise(r=>setTimeout(r,40));
 row=doc.rows.find(r=>r.id===row.id);const file=doc.file;
 aiBusy=true;$('ollamaTitle').textContent='Revising with '+project.config.ollama.model;
 $('ollamaStatus').textContent='Identifying speaker and addressee, then revising pronouns…';$('ollamaReason').textContent='';$('ollamaBefore').textContent=row.text;$('ollamaAfter').textContent='Waiting for Ollama…';$('ollamaDialog').showModal();
 try{
  const task=await api('ollama/revise',{file,row_id:row.id,source_sha256:doc.source_sha256,draft_revision:doc.draft_revision});
  let result;
  for(;;){await new Promise(r=>setTimeout(r,800));result=await api('ollama/job?id='+encodeURIComponent(task.job_id));if(!result.running)break;}
  if(result.error)throw new Error(result.error);
  const changed=result.document.rows.find(r=>r.id===row.id);
  if(doc?.file===file){doc=result.document;version=(await api('version?file='+encodeURIComponent(file))).version;render();}
  $('ollamaTitle').textContent='Ollama revision saved';$('ollamaAfter').textContent=changed.text;
  $('ollamaStatus').textContent=`Speaker: ${changed.speaker||'Uncertain'} · Addressee: ${changed.addressee||'Uncertain'} · Confidence: ${result.confidence}`;
  $('ollamaReason').textContent=result.reason;
  notice('Ollama filled the names and revised pronouns in '+file+'. Review the result before compiling.');
 }catch(e){$('ollamaTitle').textContent='Ollama needs attention';$('ollamaStatus').textContent=e.message;$('ollamaAfter').textContent='The dialogue was not changed.';throw e;}
 finally{aiBusy=false;}
}

$('markComplete').onpointerdown=e=>e.preventDefault();
$('markComplete').onclick=guard(async()=>{
 if(!doc)return;if(aiBusy)throw new Error('Wait for the Ollama revision to finish before marking this script complete.');
 await document.activeElement.commitEdit?.();while(saving)await new Promise(r=>setTimeout(r,40));
 if($('editor').open)return;
 const name=doc.file,index=project.files.indexOf(name);
 const info=await api('completion',{file:name,complete:true});
 const next=info.files[Math.min(index,info.files.length-1)];
 await loadProject(info,next);notice(name+' marked complete and hidden from the editor. It remains included in source compilation.');
});
function renderCompleted(){
 const list=$('completedList');list.replaceChildren();
 for(const file of project.completed_files||[]){
  const row=el('div',{class:'completed-item'}),button=el('button',{'aria-label':'Restore '+file},'Restore');
  row.append(el('span',{},file),button);
  button.onclick=guard(async()=>{const current=doc?.file;const info=await api('completion',{file,complete:false});await loadProject(info,current||file);renderCompleted();notice(file+' restored to the script list.');});
  list.append(row);
 }
 if(!list.children.length)list.append(el('p',{class:'hint'},'No scripts marked complete.'));
}
$('completedScripts').onclick=()=>{renderCompleted();$('completedDialog').showModal();};
$('closeCompleted').onclick=()=>$('completedDialog').close();
// A document ID belongs to one loaded page. It changes on reload/BFCache restore,
// so a close beacon cannot be undone by an old in-flight heartbeat.
let editorSessionId,editorHeartbeat;
function startEditorSession(){
 editorSessionId=crypto.randomUUID();if(editorHeartbeat)editorHeartbeat.close();
 editorHeartbeat=new EventSource('/api/session/stream?client_id='+encodeURIComponent(editorSessionId)+'&token='+encodeURIComponent(window.EDITOR_KEY));
}
function closeEditorSession(){
 if(editorHeartbeat)editorHeartbeat.close();
 if(!editorSessionId)return;
 const payload=JSON.stringify({client_id:editorSessionId,event:'close',token:window.EDITOR_KEY});
 if(!navigator.sendBeacon('/api/session',new Blob([payload],{type:'application/json'})))
  fetch('/api/session',{method:'POST',headers:{'Content-Type':'application/json','X-Editor-Key':window.EDITOR_KEY},body:payload,keepalive:true}).catch(()=>{});
}
window.addEventListener('pagehide',closeEditorSession);
window.addEventListener('pageshow',event=>{if(event.persisted)startEditorSession();});
startEditorSession();

// Page shortcuts must not interfere with cursor movement, native form controls,
// browser navigation chords, IME input, or modal editors.
document.addEventListener('keydown',event=>{
 if(!['ArrowLeft','ArrowRight'].includes(event.key)||event.defaultPrevented||event.isComposing||event.altKey||event.ctrlKey||event.metaKey||event.shiftKey)return;
 if(!doc||saving||document.querySelector('dialog[open]'))return;
 const target=event.target;
 if(target.isContentEditable||target.closest('input,textarea,select,[role="textbox"],[role="combobox"],[role="slider"]'))return;
 const button=$(event.key==='ArrowLeft'?'prev':'next');
 event.preventDefault();if(!button.disabled)button.click();
});
