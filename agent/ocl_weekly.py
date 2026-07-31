#!/usr/bin/env python3
"""Weekly autonomous Glossagens helper — OpenCaseLaw.

Strategy:
  - MCP get_law(abbrev, article) -> markdown string with verbatim article text (complete)
  - REST /leading-cases          -> ranked leading cases (complete JSON)
  - REST /regeste/{id}           -> regeste + citation strings (complete JSON)
  - REST /decisions?query        -> decision search (complete JSON)
  - REST /laws/{abbrev}          -> article list (for numbering)
  - MCP get_doctrine             -> doctrinal overview (fallback)
"""
import urllib.request, urllib.parse, json, sys, time, re

REST = 'https://mcp.opencaselaw.ch/api'
MCP = 'https://mcp.opencaselaw.ch/mcp'

def _rest(path, params=None, timeout=120):
    url = REST + path
    if params:
        url += '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(3):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode())
        except Exception as e:
            if attempt == 2:
                return {'error': str(e)}
            time.sleep(2)
    return {'error': 'timeout'}

def _mcp(tool, arguments, timeout=180):
    payload = {'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
               'params': {'name': tool, 'arguments': arguments}}
    req = urllib.request.Request(MCP, data=json.dumps(payload).encode(),
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json, text/event-stream'})
    for attempt in range(3):
        try:
            raw = urllib.request.urlopen(req, timeout=timeout).read().decode()
            for line in raw.split('\n'):
                if line.startswith('data: '):
                    p = json.loads(line[6:])
                    txt = p['result']['content'][0]['text']
                    try:
                        parsed = json.loads(txt)
                    except json.JSONDecodeError:
                        return txt
                    if isinstance(parsed, str):
                        try:
                            return json.loads(parsed)
                        except json.JSONDecodeError:
                            return parsed
                    return parsed
            return raw
        except Exception as e:
            if attempt == 2:
                return {'error': str(e)}
            time.sleep(2)
    return {'error': 'timeout'}

def get_law_markdown(abbrev, article):
    """Return markdown string for one article (verbatim text)."""
    return _mcp('get_law', {'abbreviation': abbrev, 'article': str(article)})

def find_leading_cases(law_code, article, limit=15):
    """MCP tool — article-specific ranked leading cases with inline regesten.
    Returns markdown string: 'Leading Cases on Art. {art} {LAW} ...'."""
    return _mcp('find_leading_cases', {'law_code': law_code, 'article': str(article), 'limit': limit})

def find_leading_cases_rest(law_code, article, limit=15):
    """REST fallback (NOT article-specific — generic). Avoid."""
    return _rest('/leading-cases', {'law': law_code, 'article': str(article), 'limit': limit})

def get_regeste(decision_id):
    """Return dict: decision_id, decision_date, regeste, citation_string_de, markdown_link, canonical_url."""
    return _rest('/regeste/' + urllib.parse.quote(decision_id))

def search_decisions(query, limit=30):
    """Return dict with 'results' list of decisions matching query."""
    return _rest('/decisions', {'query': query, 'limit': limit})

def get_doctrine(query):
    return _mcp('get_doctrine', {'query': query})

def cite(reference, pinpoint=None):
    p = {'reference': reference}
    if pinpoint:
        p['pinpoint'] = pinpoint
    return _rest('/cite', p)

def extract_article_markdown(md, article):
    """From a get_law_markdown response, extract the section for a specific article."""
    # Pattern: ### Art. {num}
    pat = re.compile(r'### Art\.?\s*' + re.escape(str(article)) + r'\b(.*?)(?=### Art\.|$)', re.S)
    m = pat.search(md)
    return m.group(1).strip() if m else None

if __name__ == '__main__':
    action = sys.argv[1]
    if action == 'law':
        r = get_law_markdown(sys.argv[2], sys.argv[3])
    elif action == 'leading':
        lim = int(sys.argv[4]) if len(sys.argv) > 4 else 15
        r = find_leading_cases(sys.argv[2], sys.argv[3], lim)
    elif action == 'regeste':
        r = get_regeste(sys.argv[2])
    elif action == 'search':
        lim = int(sys.argv[3]) if len(sys.argv) > 3 else 30
        r = search_decisions(sys.argv[2], lim)
    elif action == 'doctrine':
        r = get_doctrine(sys.argv[2])
    elif action == 'cite':
        r = cite(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        r = {'error': 'unknown action'}
    print(json.dumps(r, ensure_ascii=False, indent=2) if not isinstance(r, str) else r)