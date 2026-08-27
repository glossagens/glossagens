#!/usr/bin/env python3
"""OpenCaseLaw MCP/REST helper for autonomous Glossagens workflow.
Usage as a module: from ocl_helper import OCL
   ocl=OCL(); data=ocl.get_law('StGB','8'); ...
CLI: python3 ocl_helper.py <action> <args...>
   get_law <abbrev> <article>
   leading_cases <law_code> <article> [limit]
   regeste <decision_id>
   cite <reference> [pinpoint]
   case_brief <decision_id>
   doctrine <query>
   search <query> [limit]
   decisions_search <query> [limit]
"""
import json, urllib.request, urllib.error, urllib.parse, sys, time

MCP='https://mcp.opencaselaw.ch/mcp'
REST='https://mcp.opencaselaw.ch/api'
# Ehrliche Kennung statt Browser-Tarnung: der Betreiber soll erkennen können,
# wer da anfragt — und uns notfalls gezielt bremsen statt die IP zu sperren.
UA='glossagens/1.0 (+https://glossagens.ch)'
# Tools, die serverseitig ein LLM anwerfen und opencaselaw $0.05–$0.50 je Aufruf
# kosten (Kontingent 200/Tag/IP). Werden hier nicht mehr aufgerufen; die
# Grounding-Prüfung läuft über agent/skills/glossagens-audit/audit.py.
BILLED={'check_claim_support','attest_response','reflect'}

def _mcp(tool, arguments):
    if tool in BILLED:
        return {'error': f'{tool} ist gesperrt (LLM-Aufruf zulasten von '
                         'opencaselaw). Grounding läuft über '
                         'agent/skills/glossagens-audit/audit.py.'}
    payload={'jsonrpc':'2.0','id':1,'method':'tools/call',
             'params':{'name':tool,'arguments':arguments}}
    data=json.dumps(payload).encode()
    req=urllib.request.Request(MCP, data=data, headers={
        'Content-Type':'application/json',
        'Accept':'application/json, text/event-stream',
        'User-Agent':UA})
    for attempt in range(3):
        try:
            resp=urllib.request.urlopen(req, timeout=60)
            raw=resp.read().decode()
            for line in raw.split('\n'):
                if line.startswith('data: '):
                    p=json.loads(line[6:])
                    content=p['result']['content'][0]['text']
                    try: return json.loads(content)
                    except json.JSONDecodeError: return content
            return raw
        except urllib.error.HTTPError as e:
            # 403/429 nicht wiederholen: genau die Wiederholschleife ohne
            # Backoff hat am 23.08.2026 zur Sperre dieses Clients geführt.
            if e.code in (403,429):
                return {'error':f'HTTP {e.code} — Anfrage abgewiesen, kein Retry. '
                                 'Kontakt: team@jonashertner.com'}
            if attempt==2: return {'error':str(e)}
            time.sleep(2**attempt)
        except Exception as e:
            if attempt==2: return {'error':str(e)}
            time.sleep(2**attempt)
    return {'error':'timeout'}

def _rest(path, **params):
    url=REST+path
    if params:
        url+='?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url, headers={'User-Agent':UA})
    for attempt in range(3):
        try:
            resp=urllib.request.urlopen(req, timeout=60)
            return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (403,429):
                return {'error':f'HTTP {e.code} — Anfrage abgewiesen, kein Retry. '
                                 'Kontakt: team@jonashertner.com'}
            if attempt==2: return {'error':str(e)}
            time.sleep(2**attempt)
        except Exception as e:
            if attempt==2: return {'error':str(e)}
            time.sleep(2**attempt)
    return {'error':'timeout'}

class OCL:
    def get_law(self, abbrev, article, lang='de'):
        return _rest(f'/laws/{urllib.parse.quote(abbrev)}')
    def article_text(self, abbrev, article, lang='de'):
        d=self.get_law(abbrev)
        if 'articles' not in d: return None
        for a in d['articles']:
            num=str(a.get('article_number',''))
            if num==article or num.replace('-','')==article:
                return a
        return None
    def leading_cases(self, law, article, limit=15):
        return _rest('/leading-cases', law=law, article=article, limit=limit)
    def regeste(self, decision_id):
        return _rest(f'/regeste/{urllib.parse.quote(decision_id)}')
    def case_brief(self, decision_id):
        return _rest(f'/case-brief/{urllib.parse.quote(decision_id)}')
    def cite(self, reference, pinpoint=None):
        p={'reference':reference}
        if pinpoint: p['pinpoint']=pinpoint
        return _rest('/cite', **p)
    def doctrine(self, query):
        return _mcp('get_doctrine', {'query':query})
    def find_leading_cases(self, law_code, article, query=None, limit=15):
        a={'law_code':law_code,'article':article,'limit':limit}
        if query: a['query']=query
        return _mcp('find_leading_cases', a)
    def search_decisions(self, query, limit=30, court=None):
        a={'query':query,'limit':limit}
        if court: a['court']=court
        return _mcp('search_decisions', a)
    def decisions_search(self, query, limit=30, court=None):
        p={'q':query,'limit':limit}
        if court: p['court']=court
        return _rest('/decisions', **p)
    def erwaegung(self, decision_id, e_number):
        """Wortlaut einer Erwägung — der Text, gegen den ein Beleg zu prüfen ist."""
        return _mcp('get_erwaegung', {'decision_id':decision_id,'e_number':e_number})
    def decision_structure(self, decision_id):
        """Vorhandene Erwägungsnummern — statt einen Pinpoint zu schätzen."""
        return _mcp('get_decision_structure', {'decision_id':decision_id})
    # attest() entfernt: `attest_response` ist ein LLM-Aufruf zulasten von
    # opencaselaw. Die Schlussprüfung macht agent/skills/glossagens-audit/audit.py.

if __name__=='__main__':
    o=OCL(); action=sys.argv[1]
    if action=='get_law':
        d=o.get_law(sys.argv[2])
        art=o.article_text(sys.argv[2], sys.argv[3])
        print(json.dumps({'law_title':d.get('title'),'sr':d.get('sr_number'),
              'article':art}, ensure_ascii=False, indent=2))
    elif action=='leading_cases':
        print(json.dumps(o.leading_cases(sys.argv[2],sys.argv[3],
              int(sys.argv[4]) if len(sys.argv)>4 else 15),
              ensure_ascii=False, indent=2))
    elif action=='regeste':
        print(json.dumps(o.regeste(sys.argv[2]), ensure_ascii=False, indent=2))
    elif action=='case_brief':
        print(json.dumps(o.case_brief(sys.argv[2]), ensure_ascii=False, indent=2))
    elif action=='cite':
        print(json.dumps(o.cite(sys.argv[2],
              sys.argv[3] if len(sys.argv)>3 else None), ensure_ascii=False, indent=2))
    elif action=='doctrine':
        r=o.doctrine(sys.argv[2]); print(r if isinstance(r,str) else json.dumps(r,ensure_ascii=False,indent=2)[:6000])
    elif action=='find_leading_cases':
        print(json.dumps(o.find_leading_cases(sys.argv[2],sys.argv[3],
              sys.argv[4] if len(sys.argv)>4 else None,
              int(sys.argv[5]) if len(sys.argv)>5 else 15), ensure_ascii=False, indent=2)[:8000])
    elif action=='decisions_search':
        print(json.dumps(o.decisions_search(sys.argv[2],
              int(sys.argv[3]) if len(sys.argv)>3 else 30), ensure_ascii=False, indent=2)[:6000])