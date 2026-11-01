'use strict';
let timer;
self.onmessage=event=>{
 const {id,key}=event.data;clearInterval(timer);
 const ping=()=>fetch('/api/session',{method:'POST',headers:{'Content-Type':'application/json','X-Editor-Key':key},body:JSON.stringify({client_id:id,event:'alive'}),cache:'no-store'}).catch(()=>{});
 ping();timer=setInterval(ping,5000);
};
