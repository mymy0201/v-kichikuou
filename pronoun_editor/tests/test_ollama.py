from pathlib import Path
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import Project
import ollama_client as oc
from core import tokens

class OllamaTests(unittest.TestCase):
    def project(self,root):
        (root/'scripts').mkdir()
        (root/'scripts/a.json').write_text(json.dumps([{'text':'🙂 Tôi gọi cô.','speaker':'','addressee':''}],ensure_ascii=False),encoding='utf-8')
        p=Project(root);p.config['ollama']=oc.settings({'enabled':True,'base_url':'https://ollama.com','model':'test-model'})
        return p

    def response(self):
        return {'speaker':'Aster','addressee':'Mira','self':'ta','call':'cô','assignments':[{'index':0,'role':'self'},{'index':1,'role':'call'}],'confidence':'medium','reason':'Test context identifies both people.'}

    def test_native_cloud_request_and_only_pronouns_change(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            p=self.project(Path(tmp));doc=p.load('a.json')
            def fake(config,path,key,payload):
                self.assertEqual(path,'chat');self.assertFalse(payload['stream']);self.assertNotIn('format',payload)
                data=json.loads(payload['messages'][1]['content'])
                self.assertEqual(data['selected']['text'],'🙂 Tôi gọi cô.')
                self.assertEqual(data['occurrences'][0]['index'],0)
                self.assertNotIn('api_key',data)
                return {'message':{'content':json.dumps(self.response())}}
            result=oc.revise(p,{**doc,'row_id':'0'},transport=fake)
            self.assertEqual(result['row']['text'],'🙂 Ta gọi cô.')
            self.assertEqual(result['row']['speaker'],'Aster')
            self.assertEqual(result['row']['addressee'],'Mira')
            self.assertEqual(p.load('a.json')['rows'][0]['text'],'🙂 Tôi gọi cô.')

    def test_local_request_uses_schema(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            p=self.project(Path(tmp));p.config['ollama']['base_url']='http://127.0.0.1:11434'
            doc=p.load('a.json')
            def fake(config,path,key,payload):
                self.assertEqual(payload['format'],oc.SCHEMA)
                return {'message':{'content':json.dumps(self.response())}}
            self.assertEqual(oc.revise(p,{**doc,'row_id':'0'},transport=fake)['confidence'],'medium')

    def test_stale_request_and_invalid_model_output_rejected(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            p=self.project(Path(tmp));doc=p.load('a.json')
            with self.assertRaisesRegex(ValueError,'changed'):
                oc.revise(p,{**doc,'source_sha256':'wrong','row_id':'0'})
            def fake(*args,**kwargs):return {'message':{'content':'not JSON'}}
            with self.assertRaisesRegex(ValueError,'valid pronoun JSON'):oc.revise(p,{**doc,'row_id':'0'},transport=fake)

    def test_invalid_and_protected_occurrence_roles(self):
        row={'text':'Tôi gọi cô.','spans':tokens('Tôi gọi cô.')}
        invalid=self.response();invalid['assignments']=[{'index':99,'role':'call'}]
        with self.assertRaises(ValueError):oc.validate_result(row,invalid)
        invalid['assignments']=[{'index':0,'role':'self'},{'index':0,'role':'call'}]
        with self.assertRaises(ValueError):oc.validate_result(row,invalid)
        row['spans'][1]['role']='other'
        with self.assertRaisesRegex(ValueError,'protected third-person'):oc.validate_result(row,self.response())

    def test_secret_is_origin_bound_and_not_in_project_info(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            p=self.project(Path(tmp));vault=oc.KeyVault(p.state)
            vault.save('test-secret-123','https://ollama.com')
            self.assertEqual(vault.read('https://ollama.com'),'test-secret-123')
            self.assertEqual(vault.read('https://another.example'),'')
            self.assertNotIn('test-secret-123',json.dumps(p.info()))
            if sys.platform=='win32':self.assertNotIn('test-secret-123',vault.path.read_text())
            vault.clear();self.assertFalse(vault.configured('https://ollama.com'))

    def test_endpoint_validation_and_normalization(self):
        self.assertEqual(oc.settings({'base_url':'https://ollama.com/api/chat'})['base_url'],'https://ollama.com')
        for url in ('file:///tmp/data','https://user:key@example.com','https://example.com?key=secret'):
            with self.assertRaises(ValueError):oc.settings({'base_url':url})

if __name__=='__main__':unittest.main()
