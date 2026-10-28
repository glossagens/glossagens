// Zugang zu GitHub als GitHub App «Glossagens Chat-Einreichung».
//
// Die App darf nur Inhalte und Pull Requests von glossagens/glossagens
// schreiben; das Ruleset «main schützen» verlangt für main einen PR mit einer
// Freigabe, die sich die App nicht selbst geben kann. Den privaten Schlüssel
// hält der Worker als Secret GITHUB_APP_KEY (PKCS#8, `openssl pkcs8 -topk8`);
// daraus entsteht je Isolate ein Installations-Token, das eine Stunde gilt.

const API = "https://api.github.com";

let token = null; // { wert, bis }

function b64url(daten) {
  const bytes = typeof daten === "string" ? new TextEncoder().encode(daten) : new Uint8Array(daten);
  let s = "";
  for (const b of bytes) s += String.fromCharCode(b);
  return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

export function base64(text) {
  const bytes = new TextEncoder().encode(text);
  let s = "";
  for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(s);
}

function pemZuDer(pem) {
  if (/BEGIN RSA PRIVATE KEY/.test(pem)) {
    throw new Error("GITHUB_APP_KEY ist im PKCS#1-Format; vorher `openssl pkcs8 -topk8 -nocrypt` anwenden.");
  }
  const b64 = pem.replace(/-----[^-]+-----/g, "").replace(/\s+/g, "");
  return Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
}

async function appJwt(env) {
  const jetzt = Math.floor(Date.now() / 1000);
  const kopf = b64url(JSON.stringify({ alg: "RS256", typ: "JWT" }));
  // iat 60 s zurück: GitHub verlangt das bei abweichenden Uhren.
  const last = b64url(JSON.stringify({ iat: jetzt - 60, exp: jetzt + 540, iss: String(env.GITHUB_APP_ID) }));
  const schluessel = await crypto.subtle.importKey("pkcs8", pemZuDer(env.GITHUB_APP_KEY), { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["sign"]);
  const signatur = await crypto.subtle.sign("RSASSA-PKCS1-v1_5", schluessel, new TextEncoder().encode(`${kopf}.${last}`));
  return `${kopf}.${last}.${b64url(signatur)}`;
}

async function installationsToken(env) {
  if (token && token.bis - Date.now() > 5 * 60 * 1000) return token.wert;
  const r = await fetch(`${API}/app/installations/${env.GITHUB_INSTALLATION_ID}/access_tokens`, {
    method: "POST",
    headers: kopfzeilen(`Bearer ${await appJwt(env)}`),
    body: JSON.stringify({ permissions: { contents: "write", pull_requests: "write" } }),
  });
  if (!r.ok) throw new Error(`GitHub-Anmeldung fehlgeschlagen (HTTP ${r.status}).`);
  const d = await r.json();
  token = { wert: d.token, bis: Date.parse(d.expires_at) };
  return token.wert;
}

function kopfzeilen(auth) {
  return {
    Authorization: auth,
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "glossagens-mcp",
    "Content-Type": "application/json",
  };
}

// Ein Aufruf der REST-API; `erlaubt` sind Status, die kein Fehler sind (404 beim Nachschauen).
export async function github(env, methode, pfad, body, erlaubt = []) {
  const r = await fetch(`${API}${pfad}`, {
    method: methode,
    headers: kopfzeilen(`Bearer ${await installationsToken(env)}`),
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  if (!r.ok && !erlaubt.includes(r.status)) {
    const text = await r.text();
    throw new Error(`GitHub ${methode} ${pfad.split("?")[0]}: HTTP ${r.status} ${text.slice(0, 200)}`);
  }
  return { status: r.status, daten: r.status === 204 ? null : await r.json().catch(() => null) };
}

// Für Tests.
export function _tokenVergessen() {
  token = null;
}
