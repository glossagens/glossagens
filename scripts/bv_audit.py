#!/usr/bin/env python3
"""BV Audit Script — STILLGELEGT am 27.08.2026.

Dieses Einweg-Skript rief `check_claim_support` in einer Schleife auf. Das ist
serverseitig ein Claude-Aufruf, der opencaselaw $0.05–$0.50 je Aufruf kostet;
das Kontingent liegt bei 200 Aufrufen pro Tag und IP. Genau solche Schleifen
haben am 23.08.2026 zur Sperrung des Glossagens-Clients geführt.

Ersetzt durch `agent/skills/glossagens-audit/audit.py`: dieselben Prüfstufen,
aber ohne LLM-Aufruf bei opencaselaw — das Grounding-Urteil fällt ein
Judge-Subagent des jeweiligen Agenten.

    python3 agent/skills/glossagens-audit/audit.py content/kommentar/bv --all

Der Code bleibt als Beleg dessen stehen, was nicht mehr getan wird; ausführbar
ist er nicht mehr.
"""
import re, os, json, time, sys, urllib.request

sys.exit(
    "bv_audit.py ist stillgelegt (LLM-Aufrufe zulasten von opencaselaw).\n"
    "Ersatz: python3 agent/skills/glossagens-audit/audit.py content/kommentar/bv --all"
)

BASE = '/opt/glossagens/content/kommentar/bv'
REPORT = '/opt/glossagens/scripts/bv_audit_report.json'
MCP_URL = 'https://mcp.opencaselaw.ch/mcp'
OCL_BASE = 'https://mcp.opencaselaw.ch/entscheid'

# Skip already rebuilt articles
SKIP = {'art-050', 'art-089'}

def extract_citations():
    """Extract all OCL citation IDs from BV articles, grouped by article."""
    articles = {}
    all_unique = set()
    for art_dir in sorted(os.listdir(BASE)):
        if art_dir in SKIP or art_dir.startswith('_'):
            continue
        art_path = os.path.join(BASE, art_dir)
        if not os.path.isdir(art_path):
            continue
        cits = set()
        for fname in ['_index.md', 'rechtsprechung.md']:
            fpath = os.path.join(art_path, fname)
            if os.path.exists(fpath):
                content = open(fpath).read()
                for m in re.finditer(r'(bge_BGE_\d+_[IV]+_\d+|bger_\d+[A-Z]_\d+_\d+)', content):
                    cits.add(m.group(1))
                    all_unique.add(m.group(1))
        if cits:
            articles[art_dir] = sorted(cits)
    return articles, sorted(all_unique)


def check_http(cit_id):
    """Check if citation exists on OCL (HTTP status)."""
    url = f'{OCL_BASE}/{cit_id}'
    try:
        req = urllib.request.Request(url, method='HEAD')
        resp = urllib.request.urlopen(req, timeout=10)
        return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return 0


def check_claim(cit_id, claim_text):
    """Run check_claim_support via OCL MCP."""
    payload = json.dumps({
        "jsonrpc": "2.0", "id": 1,
        "method": "tools/call",
        "params": {
            "name": "check_claim_support",
            "arguments": {"claim": claim_text, "decision_id": cit_id}
        }
    }).encode()
    req = urllib.request.Request(MCP_URL, data=payload,
        headers={'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'})
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        raw = resp.read().decode()
        for line in raw.split('\n'):
            if line.startswith('data: '):
                payload_data = json.loads(line[6:])
                text = payload_data['result']['content'][0]['text']
                m_supports = re.search(r'"supports"\s*:\s*"([^"]+)"', text)
                m_conf = re.search(r'"confidence"\s*:\s*([0-9.]+)', text)
                return {
                    'supports': m_supports.group(1) if m_supports else 'unknown',
                    'confidence': float(m_conf.group(1)) if m_conf else None
                }
        return {'supports': 'parse_error', 'confidence': None}
    except Exception as e:
        return {'supports': f'error: {e}', 'confidence': None}


def get_article_title(art_dir):
    """Extract title from _index.md."""
    fpath = os.path.join(BASE, art_dir, '_index.md')
    if os.path.exists(fpath):
        content = open(fpath).read()
        m = re.search(r'title:\s*"([^"]+)"', content)
        if m:
            return m.group(1)
    return art_dir


def build_claim(cit_id, art_dir, art_title):
    """Build a claim text for check_claim_support."""
    if cit_id.startswith('bge_BGE_'):
        parts = cit_id.replace('bge_BGE_', '').split('_')
        bge_ref = f'BGE {parts[0]} {parts[1]} {parts[2]}'
    else:
        parts = cit_id.replace('bger_', '').split('_')
        bge_ref = f'BGer {parts[0]}_{parts[1]}/{parts[2]}'

    topic = art_title.split('—')[-1].strip() if '—' in art_title else art_title
    return f'{bge_ref} befasst sich mit {topic}'


# --- MAIN ---
print("=== BV AUDIT — Phase 1+2 ===\n")

# Load previous results if resuming
prev_results = {}
if os.path.exists(REPORT):
    prev_results = json.load(open(REPORT))
    print(f"Resuming: {len(prev_results.get('http', {}))} HTTP checks, {len(prev_results.get('claims', {}))} claim checks already done")

articles, all_citations = extract_citations()
print(f"BV-Artikel: {len(articles)} (ohne {', '.join(SKIP)})")
print(f"Unique Zitate: {len(all_citations)}\n")

# Phase 1: HTTP check
print("--- Phase 1: HTTP-Status ---")
http_results = prev_results.get('http', {})
if http_results:
    # Convert string keys back
    http_results = {k: v for k, v in http_results.items()}

unchecked_http = [c for c in all_citations if c not in http_results]

if unchecked_http:
    print(f"Prüfe HTTP-Status für {len(unchecked_http)} Zitate...")
    for i, cit in enumerate(unchecked_http):
        status = check_http(cit)
        http_results[cit] = status
        sys.stdout.write(f'\r  [{i+1}/{len(unchecked_http)}] {cit}: HTTP {status}      ')
        sys.stdout.flush()
        time.sleep(0.3)
    print()

http_200 = [c for c, s in http_results.items() if s == 200]
http_404 = [c for c, s in http_results.items() if s == 404]
print(f"HTTP 200: {len(http_200)}, HTTP 404: {len(http_404)}, Other: {len(http_results) - len(http_200) - len(http_404)}")

# Phase 2: check_claim_support for HTTP 200 citations
print("\n--- Phase 2: check_claim_support ---")
claim_results = prev_results.get('claims', {})
if claim_results:
    claim_results = {k: v for k, v in claim_results.items()}

unchecked_claims = [c for c in http_200 if c not in claim_results]

if unchecked_claims:
    print(f"Prüfe claim support für {len(unchecked_claims)} Zitate...")
    for i, cit in enumerate(unchecked_claims):
        # Find which article(s) this citation belongs to
        for art_dir, cits in articles.items():
            if cit in cits:
                art_title = get_article_title(art_dir)
                claim_text = build_claim(cit, art_dir, art_title)
                break
        else:
            claim_text = f'{cit} befasst sich mit Bundesverfassungsrecht'

        result = check_claim(cit, claim_text)
        claim_results[cit] = result
        sys.stdout.write(f'\r  [{i+1}/{len(unchecked_claims)}] {cit}: {result["supports"]} (conf={result["confidence"]})      ')
        sys.stdout.flush()
        time.sleep(0.5)
    print()

# Summary by article
print("\n=== ERGEBNIS PRO ARTIKEL ===\n")
for art_dir in sorted(articles.keys()):
    cits = articles[art_dir]
    art_title = get_article_title(art_dir)
    supported = sum(1 for c in cits if claim_results.get(c, {}).get('supports') == 'yes')
    partial = sum(1 for c in cits if claim_results.get(c, {}).get('supports') == 'partial')
    no = sum(1 for c in cits if claim_results.get(c, {}).get('supports') == 'no')
    contradicts = sum(1 for c in cits if claim_results.get(c, {}).get('supports') == 'contradicts')
    http404 = sum(1 for c in cits if http_results.get(c) == 404)
    other = len(cits) - supported - partial - no - contradicts - http404

    ratio_str = f'{supported}/{len(cits)}' if cits else 'N/A'
    if cits:
        ratio = supported / len(cits)
        cat = 'A' if ratio >= 0.8 else 'B' if ratio >= 0.5 else 'C'
    else:
        cat = '-'

    print(f'{art_dir} ({art_title}):')
    print(f'  Total={len(cits)} Supported={supported} Partial={partial} No={no} Contradicts={contradicts} 404={http404} Other={other} → Kategorie {cat}')

# Save full results
report = {
    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
    'articles': {k: v for k, v in articles.items()},
    'http': {str(k): v for k, v in http_results.items()},
    'claims': {str(k): v for k, v in claim_results.items()}
}
with open(REPORT, 'w') as f:
    json.dump(report, f, indent=2)
print(f'\nReport saved: {REPORT}')