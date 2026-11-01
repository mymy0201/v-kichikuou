/* Pure occurrence-level editing, shared by the UI and regression tests. */
(function(root){
 'use strict';
 function prepare(row,role){
  const copy=structuredClone(row);
  if(copy.spans.some(s=>s.role===role))return {row:copy};
  const unknown=copy.spans.filter(s=>s.role==='unknown');
  const words=new Set(unknown.map(s=>s.text.toLocaleLowerCase()));
  if(words.size===1){unknown.forEach(s=>s.role=role);return {row:copy};}
  return {row:copy,needsChoice:true,reason:unknown.length?'Choose which highlighted words to replace.':'Select a phrase in Edit and assign it to '+role+'.'};
 }
 function replace(row,values){
  const chars=Array.from(row.text);let result='',p=0,spans=[];
  for(const s of [...row.spans].sort((a,b)=>a.start-b.start)){
   result+=chars.slice(p,s.start).join('');let word=values[s.role]||s.text;
   if(s.text[0]!==s.text[0].toLowerCase())word=word[0].toUpperCase()+word.slice(1);
   const start=Array.from(result).length;result+=word;
   spans.push({...s,start,end:Array.from(result).length,text:word});p=s.end;
  }
  result+=chars.slice(p).join('');return {...row,text:result,spans};
 }
 const api={prepare,replace};
 if(typeof module!=='undefined')module.exports=api;else root.PronounEdit=api;
})(typeof window!=='undefined'?window:globalThis);
