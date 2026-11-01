"""Local test double for the UI contract; no real credentials or cloud requests."""
from http.server import BaseHTTPRequestHandler,HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass
    def send_json(self,data,status=200):
        raw=json.dumps(data,ensure_ascii=False).encode('utf-8');self.send_response(status)
        self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)
    def do_GET(self):
        if self.path!='/api/tags':return self.send_json({},404)
        self.send_json({'models':[{'name':'test-pronoun-model'}]})
    def do_POST(self):
        if self.path!='/api/chat':return self.send_json({},404)
        if self.headers.get('Authorization')!='Bearer test-only-key':return self.send_json({},401)
        data=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        context=json.loads(data['messages'][1]['content'])
        assert context['selected']['text']=='Aster「Tôi gọi cô.」'
        result={'speaker':'Aster','addressee':'Mira','self':'ta','call':'cô','assignments':[{'index':0,'role':'self'},{'index':1,'role':'call'}],'confidence':'high','reason':'The supplied context and guide identify Aster speaking to Mira.'}
        self.send_json({'message':{'content':json.dumps(result,ensure_ascii=False)}})

if __name__=='__main__':HTTPServer(('127.0.0.1',11535),Handler).serve_forever()
