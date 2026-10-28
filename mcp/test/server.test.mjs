// Prüft den MCP-Server ohne Netz und ohne wrangler: `node mcp/test/server.test.mjs`.
// fetch wird durch kleine Fixtures ersetzt; Site und Repo sind erfunden, aber
// im Format von /kommentar/index.json, /themen/index.json und data/wortlaut/.

import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import worker, { _speicherLeeren, artikelSlug, beitragPruefen, gesetzFinden, letzteRevision, normErkennen, wortlautText } from "../src/index.js";
import { gitSha, heute, inhaltPruefen, linkAbgleich } from "../src/pruefen.js";

const SITE = "https://site.test";
const RAW = "https://raw.test";
const ENV = { SITE_URL: SITE, RAW_URL: RAW };

const KATALOG = {
  erzeugt: "2026-10-28T12:00:00Z",
  gesetze: {
    stgb: {
      kuerzel: "StGB", name: "Schweizerisches Strafgesetzbuch", ebene: "bund", sr: "311.0", srl: "", kanton: "", url: `${SITE}/kommentar/stgb/`,
      artikel: {
        "art-070": { titel: "Art. 70 StGB — Einziehung", beschreibung: "Einziehung deliktischer Vermögenswerte", tags: ["Einziehung", "Bruttoprinzip"], url: `${SITE}/kommentar/stgb/art-070/`, lastmod: "2026-10-15", sachgebiete: ["strafrecht"], teile: ["kommentar", "rechtsprechung"] },
        "art-305bis": { titel: "Art. 305bis StGB — Geldwäscherei", beschreibung: "Geldwäscherei", tags: ["Geldwäscherei"], url: `${SITE}/kommentar/stgb/art-305bis/`, lastmod: "2026-09-01", sachgebiete: ["strafrecht"], teile: ["kommentar"] },
      },
    },
    or: {
      kuerzel: "OR", name: "Obligationenrecht", ebene: "bund", sr: "220", srl: "", kanton: "", url: `${SITE}/kommentar/or/`,
      artikel: {
        "art-336c": { titel: "Art. 336c OR — Kündigung zur Unzeit", beschreibung: "Sperrfristen bei Krankheit", tags: ["Kündigung", "Sperrfrist"], url: `${SITE}/kommentar/or/art-336c/`, lastmod: "2026-10-01", sachgebiete: ["schuldrecht.arbeit"], teile: ["kommentar"] },
      },
    },
    "vrg-lu": {
      kuerzel: "VRG", name: "Gesetz über die Verwaltungsrechtspflege", ebene: "kantonal", sr: "", srl: "40", kanton: "LU", url: `${SITE}/kommentar/vrg-lu/`,
      artikel: {
        "art-015": { titel: "§ 15 VRG LU — Fristen", beschreibung: "", tags: [], url: `${SITE}/kommentar/vrg-lu/art-015/`, lastmod: "2026-08-01", sachgebiete: [], teile: ["kommentar"] },
      },
    },
  },
};

const THEMEN = {
  themen: {
    "folgen-ungerechtfertigte-kuendigung": { titel: "Folgen einer ungerechtfertigten Kündigung", url: `${SITE}/themen/folgen-ungerechtfertigte-kuendigung/`, kurz: "Was gilt, wenn die Kündigung missbräuchlich oder zur Unzeit erfolgt.", typ: "rechtsfolgen", normen: ["or/art-336c"], stichworte: [] },
  },
};

const ART_070 = `---
title: "Art. 70 StGB — Einziehung"
weight: 70
date: 2026-08-01
lastmod: 2026-10-15
description: "Einziehung von Vermögenswerten"
tags: ["Einziehung"]
revisions:
  - date: 2026-10-15
    by: "Claude Code"
    model: "claude-opus-4-8"
  - date: 2026-08-01
    by: "Hermes Agent"
    model: "hermes3"
---

## Gesetzeswortlaut

{{< wortlaut >}}

## Kommentierung

### Bruttoprinzip

Text zum Bruttoprinzip.

### Kasuistik

Fälle an der Straße.
`;

const WORTLAUT_070 = {
  sr: "311.0", art: "70", stand: "2025-01-01", eli: "https://www.fedlex.admin.ch/eli/cc/54/757_781_799", anker: "art_70",
  nummer: "Art. 70", titel: "Einziehung von Vermögenswerten",
  html: '<p><sup>1</sup> Das Gericht verfügt die Einziehung.<sup><a href="#wl-fn-1" id="wl-fnbck-1">7</a></sup></p><dl><dt>a. </dt><dd>erstens;</dd><dt>b. </dt><dd>zweitens &amp; drittens.</dd></dl><p><sup>2</sup> Art. 260<sup>ter</sup> bleibt vorbehalten.</p><div class="wortlaut-fussnoten"><p id="wl-fn-1">Fassung gemäss AS 2000 1</p></div>',
};

const DATEIEN = {
  [`${SITE}/kommentar/index.json`]: KATALOG,
  [`${SITE}/themen/index.json`]: THEMEN,
  [`${RAW}/content/kommentar/stgb/art-070/_index.md`]: ART_070,
  [`${RAW}/content/kommentar/stgb/art-070/rechtsprechung.md`]: "---\ntitle: \"Rechtsprechung zu Art. 70 StGB\"\n---\n\n## Leitentscheide\n\nBGE …\n",
  [`${RAW}/data/wortlaut/stgb/art-070.json`]: WORTLAUT_070,
  [`${RAW}/content/themen/folgen-ungerechtfertigte-kuendigung/_index.md`]: "---\ntitle: x\n---\n\n## Übersicht {#uebersicht}\n\nInhalt.\n",
};

let abrufe = [];
globalThis.fetch = async (url) => {
  abrufe.push(String(url));
  const d = DATEIEN[String(url)];
  if (d === undefined) return new Response("nicht gefunden", { status: 404 });
  return new Response(typeof d === "string" ? d : JSON.stringify(d), { status: 200 });
};

async function rpc(nachricht, { methode = "POST", pfad = "/mcp" } = {}) {
  const req = new Request(`https://mcp.test${pfad}`, {
    method: methode,
    headers: { "Content-Type": "application/json", Accept: "application/json, text/event-stream" },
    body: methode === "POST" ? (typeof nachricht === "string" ? nachricht : JSON.stringify(nachricht)) : undefined,
  });
  return worker.fetch(req, ENV);
}

async function tool(name, args) {
  const r = await rpc({ jsonrpc: "2.0", id: 1, method: "tools/call", params: { name, arguments: args } });
  assert.equal(r.status, 200);
  const d = await r.json();
  return { text: d.result.content[0].text, fehler: Boolean(d.result.isError) };
}

let bestanden = 0;
async function pruefe(name, fn) {
  _speicherLeeren();
  abrufe = [];
  try {
    await fn();
    bestanden++;
  } catch (e) {
    console.error(`✗ ${name}`);
    throw e;
  }
}

// --- Hilfsfunktionen ---------------------------------------------------------

await pruefe("artikelSlug", () => {
  assert.equal(artikelSlug("70"), "art-070");
  assert.equal(artikelSlug("Art. 70"), "art-070");
  assert.equal(artikelSlug("art-070"), "art-070");
  assert.equal(artikelSlug("305bis"), "art-305bis");
  assert.equal(artikelSlug("Art. 24a"), "art-024a");
  assert.equal(artikelSlug("1234"), "art-1234");
  assert.equal(artikelSlug("abc"), null);
});

await pruefe("gesetzFinden", () => {
  const g = KATALOG.gesetze;
  assert.equal(gesetzFinden(g, "StGB"), "stgb");
  assert.equal(gesetzFinden(g, "stgb"), "stgb");
  assert.equal(gesetzFinden(g, "SR 311.0"), "stgb");
  assert.equal(gesetzFinden(g, "220"), "or");
  assert.equal(gesetzFinden(g, "VRG LU"), "vrg-lu");
  assert.equal(gesetzFinden(g, "vrg-lu"), "vrg-lu");
  assert.equal(gesetzFinden(g, "ZGB"), null);
});

await pruefe("normErkennen", () => {
  const g = KATALOG.gesetze;
  assert.deepEqual(normErkennen(g, "StGB 70"), { dir: "stgb", slug: "art-070", vorhanden: true });
  assert.deepEqual(normErkennen(g, "Art. 70 StGB"), { dir: "stgb", slug: "art-070", vorhanden: true });
  assert.deepEqual(normErkennen(g, "or336c"), { dir: "or", slug: "art-336c", vorhanden: true });
  assert.deepEqual(normErkennen(g, "305bis StGB"), { dir: "stgb", slug: "art-305bis", vorhanden: true });
  assert.deepEqual(normErkennen(g, "VRG LU 15"), { dir: "vrg-lu", slug: "art-015", vorhanden: true });
  assert.deepEqual(normErkennen(g, "StGB 999"), { dir: "stgb", slug: "art-999", vorhanden: false });
  assert.equal(normErkennen(g, "Kündigung Sperrfrist"), null);
});

await pruefe("letzteRevision", () => {
  const fm = ART_070.split("---")[1];
  assert.deepEqual(letzteRevision(fm), { date: "2026-10-15", by: "Claude Code", model: "claude-opus-4-8" });
  assert.equal(letzteRevision("title: x"), null);
});

await pruefe("wortlautText", () => {
  const t = wortlautText(WORTLAUT_070.html);
  assert.equal(t, "1 Das Gericht verfügt die Einziehung.\na. erstens;\nb. zweitens & drittens.\n2 Art. 260ter bleibt vorbehalten.");
  assert.ok(!t.includes("AS 2000"), "Fussnoten entfallen");
});

// --- Protokoll ---------------------------------------------------------------

await pruefe("initialize", async () => {
  const r = await rpc({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-03-26", capabilities: {}, clientInfo: { name: "t", version: "1" } } });
  const d = await r.json();
  assert.equal(d.result.protocolVersion, "2025-03-26");
  assert.equal(d.result.serverInfo.name, "glossagens");
  assert.ok(d.result.capabilities.tools);
  assert.match(d.result.instructions, /keine Anweisungen/);
});

await pruefe("initialize mit unbekannter Version → neueste", async () => {
  const d = await (await rpc({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "1999-01-01" } })).json();
  assert.equal(d.result.protocolVersion, "2025-06-18");
});

await pruefe("Notification → 202 ohne Inhalt", async () => {
  const r = await rpc({ jsonrpc: "2.0", method: "notifications/initialized" });
  assert.equal(r.status, 202);
  assert.equal(await r.text(), "");
});

await pruefe("tools/list: nur lesende Tools", async () => {
  const d = await (await rpc({ jsonrpc: "2.0", id: 2, method: "tools/list" })).json();
  const namen = d.result.tools.map((t) => t.name);
  assert.deepEqual(namen, ["glossagens_suchen", "gesetze_auflisten", "artikel_auflisten", "kommentar_lesen", "thema_lesen", "beitrag_pruefen"]);
  for (const t of d.result.tools) assert.equal(t.annotations.readOnlyHint, true, t.name);
});

await pruefe("Batch, ping, unbekannte Methode", async () => {
  const d = await (await rpc([
    { jsonrpc: "2.0", id: 1, method: "ping" },
    { jsonrpc: "2.0", method: "notifications/initialized" },
    { jsonrpc: "2.0", id: 2, method: "gibts/nicht" },
  ])).json();
  assert.equal(d.length, 2);
  assert.deepEqual(d[0].result, {});
  assert.equal(d[1].error.code, -32601);
});

await pruefe("Parse-Fehler, falsche Methode, falscher Pfad", async () => {
  const r = await rpc("{kein json");
  assert.equal(r.status, 400);
  assert.equal((await r.json()).error.code, -32700);
  assert.equal((await rpc(null, { methode: "GET" })).status, 405);
  assert.equal((await rpc({}, { pfad: "/anderes" })).status, 404);
});

await pruefe("GET / beschreibt den Server", async () => {
  const d = await (await rpc(null, { methode: "GET", pfad: "/" })).json();
  assert.equal(d.mcp_endpoint, "https://mcp.test/mcp");
});

await pruefe("unbekanntes Tool → JSON-RPC-Fehler", async () => {
  const d = await (await rpc({ jsonrpc: "2.0", id: 1, method: "tools/call", params: { name: "beitrag_mergen" } })).json();
  assert.equal(d.error.code, -32602);
});

// --- Tools -------------------------------------------------------------------

await pruefe("suchen: Norm als Direkttreffer", async () => {
  const { text } = await tool("glossagens_suchen", { anfrage: "StGB 70" });
  assert.match(text, /^Direkttreffer: Art\. 70 StGB/);
  assert.match(text, /gesetz="stgb" artikel="art-070" · https:\/\/site\.test\/kommentar\/stgb\/art-070\//);
});

await pruefe("suchen: fehlender Artikel verweist auf Einreichung", async () => {
  const { text } = await tool("glossagens_suchen", { anfrage: "StGB 999" });
  assert.match(text, /Art\. 999 StGB gibt es noch keinen Kommentar/);
});

await pruefe("suchen: Stichworte treffen Kommentar und Thema", async () => {
  const { text } = await tool("glossagens_suchen", { anfrage: "Kündigung" });
  assert.match(text, /Thema: Folgen einer ungerechtfertigten Kündigung/);
  assert.match(text, /Art\. 336c OR/);
});

await pruefe("suchen: alle Wörter müssen vorkommen", async () => {
  const { text } = await tool("glossagens_suchen", { anfrage: "Einziehung Sperrfrist" });
  assert.match(text, /^Keine Treffer/);
});

await pruefe("gesetze_auflisten: Bund vor Kanton, SR numerisch", async () => {
  const { text } = await tool("gesetze_auflisten", {});
  const reihe = [...text.matchAll(/^- (\S+)/gm)].map((m) => m[1]);
  assert.deepEqual(reihe, ["OR", "StGB", "VRG"]);
  assert.match(text, /LU SRL 40/);
});

await pruefe("artikel_auflisten", async () => {
  const { text } = await tool("artikel_auflisten", { gesetz: "StGB" });
  assert.match(text, /- art-070: Art\. 70 StGB — Einziehung · auch: rechtsprechung/);
  assert.match(text, /- art-305bis: Art\. 305bis StGB — Geldwäscherei$/m);
});

await pruefe("artikel_auflisten: unbekanntes Gesetz", async () => {
  const { text, fehler } = await tool("artikel_auflisten", { gesetz: "ZGB" });
  assert.ok(fehler);
  assert.match(text, /nicht kommentiert\. Vorhanden: OR, StGB, VRG/);
});

await pruefe("kommentar_lesen: Wortlaut eingesetzt, Frontmatter weg", async () => {
  const { text, fehler } = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "70" });
  assert.ok(!fehler, text);
  assert.match(text, /^# Art\. 70 StGB — Einziehung\nQuelle: https:\/\/site\.test\/kommentar\/stgb\/art-070\//);
  assert.match(text, /Letzte Änderung: 2026-10-15 durch Claude Code \(claude-opus-4-8\)\nHinweis: KI-erstellter Text/);
  assert.match(text, /> \*\*Art\. 70 StGB — Einziehung von Vermögenswerten\*\* \(Stand 2025-01-01, https:\/\/www\.fedlex\.admin\.ch\/eli\/cc\/54\/757_781_799#art_70\)/);
  assert.match(text, /> 1 Das Gericht verfügt die Einziehung\./);
  assert.ok(!text.includes("{{<"), "kein Shortcode mehr");
  assert.ok(!text.includes("revisions:"), "kein Frontmatter");
});

await pruefe("kommentar_lesen: Abschnitt", async () => {
  const { text } = await tool("kommentar_lesen", { gesetz: "stgb", artikel: "art-070", abschnitt: "brutto" });
  assert.match(text, /### Bruttoprinzip\n\nText zum Bruttoprinzip\.$/);
  assert.ok(!text.includes("Kasuistik"));
});

await pruefe("kommentar_lesen: unbekannter Abschnitt nennt Gliederung", async () => {
  const { text, fehler } = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "70", abschnitt: "Gibtsnicht" });
  assert.ok(fehler);
  assert.match(text, /### Kasuistik/);
});

await pruefe("kommentar_lesen: Rechtsprechung", async () => {
  const { text } = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "70", teil: "rechtsprechung" });
  assert.match(text, /^# Rechtsprechung zu Art\. 70 StGB\nQuelle: .*art-070\/rechtsprechung\//);
});

await pruefe("kommentar_lesen: fehlender Teil, fehlender Artikel", async () => {
  let r = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "70", teil: "strafzumessung" });
  assert.ok(r.fehler);
  assert.match(r.text, /Vorhanden: kommentar, rechtsprechung/);
  r = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "71" });
  assert.ok(r.fehler);
  assert.match(r.text, /Zu Art\. 71 StGB gibt es bei Glossagens keinen Kommentar/);
});

await pruefe("kommentar_lesen: Hinweis auch ohne Revisionen", async () => {
  DATEIEN[`${RAW}/content/kommentar/stgb/art-305bis/_index.md`] = "---\ntitle: x\n---\n\nText.";
  const { text } = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "305bis" });
  assert.ok(!text.includes("Letzte Änderung"));
  assert.match(text, /Hinweis: KI-erstellter Text/);
});

await pruefe("kommentar_lesen: fehlende Wortlaut-Daten brechen nicht ab", async () => {
  DATEIEN[`${RAW}/content/kommentar/or/art-336c/_index.md`] = "---\ntitle: x\n---\n\n## Gesetzeswortlaut\n\n{{< wortlaut >}}\n";
  const { text, fehler } = await tool("kommentar_lesen", { gesetz: "OR", artikel: "336c" });
  assert.ok(!fehler);
  assert.match(text, /\[Gesetzeswortlaut art-336c or hier nicht abrufbar/);
});

await pruefe("thema_lesen", async () => {
  const { text } = await tool("thema_lesen", { slug: "/themen/folgen-ungerechtfertigte-kuendigung/" });
  assert.match(text, /^# Folgen einer ungerechtfertigten Kündigung/);
  assert.match(text, /Betroffene Bestimmungen: or\/art-336c/);
  assert.match(text, /## Übersicht/);
});

await pruefe("thema_lesen: ungültiger Slug greift nicht auf fremde Pfade", async () => {
  const { fehler } = await tool("thema_lesen", { slug: "../../hugo.toml" });
  assert.ok(fehler);
  assert.ok(!abrufe.some((u) => u.includes("hugo.toml")));
});

// --- Quelltext und beitrag_pruefen --------------------------------------------

const BGE_URL = "https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-144-III-519_2018.html";
DATEIEN[BGE_URL] = "<html></html>";
const CTX = { site: SITE, raw: RAW };
const REVISION = { by: "Claude (claude.ai)", model: "claude-opus-5-5", note: "Bruttoprinzip ergänzt; BGE via entscheidsuche geprüft" };
const sha = (s) => createHash("sha1").update(`blob ${Buffer.byteLength(s)}\0${s}`).digest("hex");

await pruefe("gitSha wie git hash-object", async () => {
  assert.equal(await gitSha(ART_070), sha(ART_070));
  assert.equal(await gitSha(""), "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391");
});

await pruefe("kommentar_lesen quelltext: unverändert, mit version", async () => {
  const { text } = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "70", format: "quelltext" });
  assert.match(text, /^# Quelltext content\/kommentar\/stgb\/art-070\/_index\.md\nversion: [0-9a-f]{40}\n/);
  assert.ok(text.includes(`version: ${sha(ART_070)}`));
  assert.ok(text.includes(ART_070.trimEnd()), "Datei unverändert samt Frontmatter und Shortcode");
});

await pruefe("kommentar_lesen quelltext mit abschnitt", async () => {
  const { text } = await tool("kommentar_lesen", { gesetz: "StGB", artikel: "70", format: "quelltext", abschnitt: "Gesetzeswortlaut" });
  assert.match(text, /===== Anfang =====\n## Gesetzeswortlaut\n\n\{\{< wortlaut >\}\}\n===== Ende =====/);
});

await pruefe("beitrag_pruefen: Abschnitt ersetzen", async () => {
  const e = await beitragPruefen({ gesetz: "StGB", artikel: "70", version: sha(ART_070), abschnitt: "Bruttoprinzip", text: `Neu nach [BGE 144 III 519](${BGE_URL}).`, revision: REVISION }, CTX);
  assert.deepEqual(e.fehler, []);
  assert.deepEqual(e.warnungen, [], "ß in der Kasuistik ist Altlast, nicht Teil der Änderung");
  assert.equal(e.bestehend, 1);
  assert.ok(e.datei.includes("### Bruttoprinzip\n\nNeu nach [BGE 144 III 519]"));
  assert.ok(e.datei.includes("\n\n### Kasuistik\n\nFälle an der Straße.\n"), "übrige Abschnitte unverändert");
  assert.ok(e.datei.includes(`revisions:\n  - date: ${heute()}\n    by: "Claude (claude.ai)"\n    model: "claude-opus-5-5"\n    note: "Bruttoprinzip ergänzt; BGE via entscheidsuche geprüft"\n  - date: 2026-10-15`));
  assert.ok(e.datei.includes(`lastmod: ${heute()}`));
  assert.deepEqual(e.aenderungen, ["Frontmatter: lastmod", "geändert: ### Bruttoprinzip (+1/−1 Zeilen)"]);
  assert.equal(e.links.abgerufen, 1);
  assert.ok(abrufe.includes(BGE_URL));
});

await pruefe("beitrag_pruefen: version fehlt, veraltet; revision fehlt", async () => {
  let e = await beitragPruefen({ gesetz: "StGB", artikel: "70", abschnitt: "Bruttoprinzip", text: "x", revision: REVISION }, CTX);
  assert.match(e.fehler.join(), /`version` fehlt/);
  e = await beitragPruefen({ gesetz: "StGB", artikel: "70", version: "abc", abschnitt: "Bruttoprinzip", text: "x", revision: REVISION }, CTX);
  assert.match(e.fehler.join(), /seit dem Lesen geändert/);
  e = await beitragPruefen({ gesetz: "StGB", artikel: "70", version: sha(ART_070), abschnitt: "Bruttoprinzip", text: "x" }, CTX);
  assert.match(e.fehler.join(), /`revision` fehlt/);
});

await pruefe("beitrag_pruefen: Abschnitt unbekannt oder mehrdeutig → Tool-Fehler", async () => {
  let r = await tool("beitrag_pruefen", { gesetz: "StGB", artikel: "70", version: sha(ART_070), abschnitt: "Gibtsnicht", text: "x", revision: REVISION });
  assert.ok(r.fehler);
  assert.match(r.text, /Vorhanden:\n## Gesetzeswortlaut/);
  r = await tool("beitrag_pruefen", { gesetz: "StGB", artikel: "70", version: sha(ART_070), abschnitt: "##", text: "x", revision: REVISION });
  assert.match(r.text, /passt auf mehrere Überschriften/);
});

await pruefe("beitrag_pruefen: Unterabschnitte gehen nicht stillschweigend verloren", async () => {
  let e = await beitragPruefen({ gesetz: "StGB", artikel: "70", version: sha(ART_070), abschnitt: "Kommentierung", text: "Nur ein Absatz.", revision: REVISION }, CTX);
  assert.match(e.fehler.join(), /lässt Unterabschnitte weg: «Bruttoprinzip», «Kasuistik»/);
  e = await beitragPruefen({ gesetz: "StGB", artikel: "70", version: sha(ART_070), abschnitt: "Kommentierung", text: "Einleitung.\n\n### Bruttoprinzip\n\nNeu.\n\n### Kasuistik\n\nFälle.", revision: REVISION }, CTX);
  assert.deepEqual(e.fehler, []);
});

await pruefe("beitrag_pruefen: Zeilennummern beziehen sich auf die ganze Datei", async () => {
  const datei = ART_070.replace("Text zum Bruttoprinzip.", "Text <div>x</div>");
  const zeile = datei.split("\n").findIndex((z) => z.includes("<div>")) + 1;
  const e = await beitragPruefen({ gesetz: "StGB", artikel: "70", version: sha(ART_070), datei, revision: REVISION }, CTX);
  assert.ok(e.fehler.some((f) => f.includes(`(Zeile ${zeile + 4})`)), `${e.fehler.join()} — erwartet Zeile ${zeile} + 4 Zeilen Revision`);
});

await pruefe("beitrag_pruefen: bisherige Revisionen verändert", async () => {
  const datei = ART_070.replace('by: "Hermes Agent"', 'by: "Jemand"').replace("revisions:", `revisions:\n  - date: ${heute()}\n    by: "x"\n    model: "y"\n    note: "z"`);
  const e = await beitragPruefen({ gesetz: "StGB", artikel: "70", version: sha(ART_070), datei }, CTX);
  assert.match(e.fehler.join(), /bisherigen Revisionseinträge wurden verändert/);
});

const NEU_071 = `---
title: "Art. 71 StGB — Ersatzforderungen"
weight: 71
date: ${heute()}
lastmod: ${heute()}
description: "Ersatzforderung des Staates"
tags: ["Einziehung"]
---

## Gesetzeswortlaut

{{< wortlaut >}}

## Kommentierung

Text.
`;

await pruefe("beitrag_pruefen: neuer Artikel, revision als Parameter", async () => {
  const e = await beitragPruefen({ gesetz: "StGB", artikel: "71", datei: NEU_071, revision: REVISION }, CTX);
  assert.equal(e.neu, true);
  assert.equal(e.ziel.pfad, "content/kommentar/stgb/art-071/_index.md");
  assert.deepEqual(e.fehler, []);
  assert.match(e.warnungen.join(), /Wortlaut-Daten fehlen noch für stgb\/art-071/);
  assert.match(e.datei, /\nrevisions:\n  - date: \d{4}-\d{2}-\d{2}\n    by: "Claude \(claude\.ai\)"/);
});

await pruefe("beitrag_pruefen: unzulässige Inhalte", async () => {
  const boese = NEU_071.replace("tags:", "agent_verified: true\ntags:").replace("Text.", [
    '<script>alert(1)</script> und <div class="x">x</div>, aber <br> und 260<sup>ter</sup> sind erlaubt.',
    "[Klick](javascript:alert(1)) ![Bild](https://example.com/x.png)",
    '{{< ref "x.md" >}} {{% callout %}}x{{% /callout %}}',
    "Absatz {: onclick=\"x\"}",
    "```markdown\n| a | b |\n|---|---|\n```",
  ].join("\n\n")).replace("{{< wortlaut >}}", "{{< wortlaut >}}\n\n> Art. 71 abgeschrieben");
  const e = await beitragPruefen({ gesetz: "StGB", artikel: "71", datei: boese, revision: REVISION }, CTX);
  const f = e.fehler.join("\n");
  for (const muster of [/`agent_verified` ist abgeschafft/, /<script>/, /<div class="x">/, /unzulässigem Schema.*javascript/, /Bilder sind nicht zulässig/, /\{\{< ref "x\.md" >\}\}.*nicht zulässig/, /nur die Form `\{\{< … >\}\}`/, /Attribut-Block/, /```markdown/, /Zitatblock/]) {
    assert.match(f, muster);
  }
  assert.doesNotMatch(f, /`<br>`|`<sup>`/);
});

await pruefe("beitrag_pruefen: toter Link und falsches Linkziel", async () => {
  const datei = NEU_071.replace("Text.", `[BGE 999 IV 1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-999-IV-1_2030.html) und [BGE 140 IV 57](${BGE_URL}).`);
  const e = await beitragPruefen({ gesetz: "StGB", artikel: "71", datei, revision: REVISION }, CTX);
  assert.match(e.fehler.join(), /Link führt ins Leere \(HTTP 404\)/);
  assert.match(e.warnungen.join(), /Linktext nennt BGE 140 IV 57, der Link führt zu BGE 144 III 519/);
});

await pruefe("beitrag_pruefen: neues Thema", async () => {
  const datei = `---\ntitle: "Testthema"\ndate: ${heute()}\nlastmod: ${heute()}\ndescription: "x"\ntags: []\ntyp: erfunden\nkurz: "Kurz."\nsachgebiete: []\n---\n\n## Ohne Anker\n\n{{< wortlaut >}}\n`;
  const e = await beitragPruefen({ thema: "testthema", datei, revision: REVISION }, CTX);
  const f = e.fehler.join("\n");
  assert.match(f, /`typ`: "erfunden" ist unbekannt/);
  assert.match(f, /`sachgebiete` ist leer/);
  assert.match(f, /In Themen braucht der Shortcode gesetz/);
  assert.match(e.warnungen.join(), /Überschriften ohne festen Anker/);
});

await pruefe("beitrag_pruefen über JSON-RPC: Bericht", async () => {
  const { text, fehler } = await tool("beitrag_pruefen", { gesetz: "StGB", artikel: "70", version: sha(ART_070), abschnitt: "Kasuistik", text: "Fälle an der Strasse.", revision: REVISION });
  assert.ok(!fehler, text);
  assert.match(text, /^# Prüfung: content\/kommentar\/stgb\/art-070\/_index\.md \(Änderung\)\nErgebnis: keine Fehler\./);
  assert.match(text, /- geändert: ### Kasuistik/);
  assert.match(text, /nicht ob der Inhalt juristisch stimmt/);
});

await pruefe("linkAbgleich", () => {
  assert.equal(linkAbgleich("BGE 98 IV 293 E. 4a", "https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-098-IV-293_1972.html"), null);
  assert.match(linkAbgleich("BGer 7B_1312/2025 E. 3.3", "https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1312-2026_2026-05-01.html"), /7B_1312\/2026/);
  assert.match(linkAbgleich("BGer 6B_1/2020 vom 3. März 2020", "https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_006_6B-1-2020_2020-03-04.html"), /Datum 2020-03-03/);
  assert.equal(linkAbgleich("E. 3.1", BGE_URL), null);
});

await pruefe("inhaltPruefen: Code-Blöcke und Autolinks", () => {
  const { fehler } = inhaltPruefen("`<div>` im Code\n\n```\n<div>\n```\n\n<https://glossagens.ch>", { art: "kommentar", teil: "rechtsprechung" });
  assert.deepEqual(fehler, []);
});

await pruefe("Zwischenspeicher: Katalog nur einmal geholt", async () => {
  await tool("artikel_auflisten", { gesetz: "StGB" });
  await tool("artikel_auflisten", { gesetz: "OR" });
  assert.equal(abrufe.filter((u) => u.endsWith("/kommentar/index.json")).length, 1);
});

await pruefe("Quelle nicht erreichbar → Tool-Fehler statt Absturz", async () => {
  const echt = globalThis.fetch;
  globalThis.fetch = async () => new Response("", { status: 503 });
  try {
    const { text, fehler } = await tool("gesetze_auflisten", {});
    assert.ok(fehler);
    assert.match(text, /nicht erreichbar \(HTTP 503/);
  } finally {
    globalThis.fetch = echt;
  }
});

console.log(`✓ ${bestanden} Prüfungen bestanden`);
