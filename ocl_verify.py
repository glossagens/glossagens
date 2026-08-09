#!/usr/bin/env python3
"""OCL API verification script for Glossagens articles."""
import json
import urllib.request
import urllib.error
import sys
import time

API_BASE = "https://mcp.opencaselaw.ch/api"

def ocl_cite(reference):
    """Verify a BGE reference via OCL cite endpoint."""
    url = f"{API_BASE}/cite?reference={reference.replace(' ', '+')}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "GlossagensVerify/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            return {"status": "ok", "data": data}
    except urllib.error.HTTPError as e:
        return {"status": "error", "code": e.code, "msg": str(e)}
    except Exception as e:
        return {"status": "error", "msg": str(e)}

def ocl_search(query, size=20):
    """Search OCL API for decisions."""
    url = f"{API_BASE}/search?query={query.replace(' ', '+')}&size={size}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "GlossagensVerify/1.0"})
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode())
            return {"status": "ok", "data": data}
    except urllib.error.HTTPError as e:
        return {"status": "error", "code": e.code, "msg": str(e)}
    except Exception as e:
        return {"status": "error", "msg": str(e)}

if __name__ == "__main__":
    action = sys.argv[1]
    
    if action == "cite":
        # Verify individual citations
        refs = sys.argv[2:]
        for ref in refs:
            result = ocl_cite(ref)
            if result["status"] == "ok":
                d = result["data"]
                print(f"✓ {ref} — {d.get('bge_reference', 'N/A')} — {d.get('date', 'N/A')}")
            else:
                print(f"✗ {ref} — {result.get('code', '')} {result.get('msg', '')}")
            time.sleep(0.3)
    
    elif action == "search":
        query = sys.argv[2]
        size = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        result = ocl_search(query, size)
        if result["status"] == "ok":
            data = result["data"]
            cases = data.get("results", data.get("cases", []))
            for c in cases:
                ref = c.get("bge_reference", c.get("reference", ""))
                title = c.get("title", "")[:100]
                date = c.get("date", "N/A")
                print(f"{ref} | {date} | {title}")
        else:
            print(f"Error: {result}")