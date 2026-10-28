// Prüfungen für Beiträge aus dem Chat (Tool `beitrag_pruefen`).
//
// Reine Funktionen ohne Netz: Was abzurufen ist — die aktuelle Datei, die
// Wortlaut-Daten, die Links —, holt index.js und gibt es herein. So bleibt die
// Prüfung testbar und das spätere Einreichen ruft genau dieselbe auf.
//
// Massstab sind die Regeln in CLAUDE.md. Was der Hugo-Build ohnehin abfängt
// (unbekannte Sachgebiete, falsche `normen`), prüft `pr-build.yml`; hier steht,
// was ein Chat vor dem Einreichen selbst korrigieren kann — und vor allem, was
// nie auf die Seite darf: hugo.toml rendert rohes HTML (`unsafe = true`).

export const PFLICHTFELDER = ["title", "weight", "date", "lastmod", "description", "tags", "revisions"];
export const THEMA_PFLICHTFELDER = ["title", "date", "lastmod", "description", "tags", "revisions", "typ", "kurz", "sachgebiete"];
// data/themen/typen.yaml
export const THEMA_TYPEN = ["grundlage", "institution", "verfahren", "rechtsfolgen", "kantonsvergleich"];
// Seit 28.10.2026 abgeschafft (CLAUDE.md, „Revisions-Vermerk").
const ABGESCHAFFT = ["agent_verified", "mcp_verified"];

export const MAX_DATEI = 300000;

// Im Bestand vorkommend und harmlos. Alles andere an HTML wird abgewiesen.
const ERLAUBTES_HTML = new Set(["br", "sup", "sub"]);
const CALLOUT_TYPEN = ["default", "info", "warning", "error", "important"];

// Nur diese Hosts ruft die Link-Prüfung ab — kein beliebiger Abruf fremder URLs.
// Fedlex fehlt bewusst: Die Seite ist eine Single-Page-App und antwortet auf
// jeden Pfad mit 200.
export const GEPRUEFTE_HOSTS = ["entscheidsuche.ch", "www.bger.ch", "bger.ch", "mcp.opencaselaw.ch"];

// --- Frontmatter --------------------------------------------------------------

export function frontmatterTrennen(md) {
  const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  return m ? { fm: m[1], text: md.slice(m[0].length), kopf: m[0] } : { fm: null, text: md, kopf: "" };
}

export function frontmatterZusammen(fm, text) {
  return `---\n${fm}\n---\n${text}`;
}

function felder(fm) {
  return new Set([...fm.matchAll(/^([A-Za-z_][\w-]*):/gm)].map((m) => m[1]));
}

function feldWert(fm, name) {
  const m = fm.match(new RegExp(`^${name}:[ \\t]*(.*)$`, "m"));
  return m ? m[1].trim().replace(/^(["'])(.*)\1$/, "$2") : null;
}

// Leser für den revisions-Block — genügt für die Pflichtfelder. `roh` ist der
// Eintrag ohne Einrückung, für den Vergleich alt/neu.
export function revisionenLesen(fm) {
  const zeilen = fm.split("\n");
  const start = zeilen.findIndex((z) => /^revisions:/.test(z));
  if (start === -1) return [];
  const eintraege = [];
  for (let i = start + 1; i < zeilen.length; i++) {
    const zeile = zeilen[i];
    if (/^\S/.test(zeile)) break; // nächstes Feld auf oberster Ebene
    if (!zeile.trim()) continue;
    const neu = zeile.match(/^\s*-\s+(.*)$/);
    if (neu) eintraege.push({ felder: {}, roh: [] });
    if (!eintraege.length) continue;
    const e = eintraege[eintraege.length - 1];
    const inhalt = neu ? neu[1] : zeile.trim();
    e.roh.push(inhalt.trim());
    const kv = inhalt.match(/^(\w+):\s*(.*)$/);
    if (kv) e.felder[kv[1]] = kv[2].trim().replace(/^(["'])(.*)\1$/, "$2");
  }
  return eintraege.map((e) => ({ ...e.felder, roh: e.roh.join("\n") }));
}

// Neuer Eintrag zuoberst, `lastmod` auf heute. Werte als JSON-String: das ist
// gültiges YAML in doppelten Anführungszeichen.
export function revisionEinfuegen(fm, { by, model, note }, heute) {
  const eintrag = (ein) =>
    [`${ein}- date: ${heute}`, `${ein}  by: ${JSON.stringify(by)}`, `${ein}  model: ${JSON.stringify(model)}`, `${ein}  note: ${JSON.stringify(note)}`].join("\n");
  if (/^revisions:\s*$/m.test(fm)) {
    const ein = fm.match(/^revisions:\s*\n(\s*)-/m)?.[1] ?? "  ";
    fm = fm.replace(/^revisions:\s*$/m, `revisions:\n${eintrag(ein)}`);
  } else if (/^revisions:/m.test(fm)) {
    fm = fm.replace(/^revisions:.*$/m, `revisions:\n${eintrag("  ")}`); // revisions: []
  } else {
    fm = `${fm}\nrevisions:\n${eintrag("  ")}`;
  }
  return /^lastmod:/m.test(fm) ? fm.replace(/^lastmod:.*$/m, `lastmod: ${heute}`) : `${fm}\nlastmod: ${heute}`;
}

const DATUM = /^\d{4}-\d{2}-\d{2}$/;

export function frontmatterPruefen(fm, { art, heute }) {
  const fehler = [];
  const warnungen = [];
  if (fm == null) return { fehler: ["Kein Frontmatter: Die Datei muss mit `---`, den Feldern und `---` beginnen."], warnungen };
  if (/\t/.test(fm)) fehler.push("Frontmatter enthält Tabulatoren; YAML verlangt Leerzeichen.");

  const vorhanden = felder(fm);
  const pflicht = art === "thema" ? THEMA_PFLICHTFELDER : PFLICHTFELDER;
  const fehlend = pflicht.filter((f) => !vorhanden.has(f));
  if (fehlend.length) fehler.push(`Pflichtfelder fehlen im Frontmatter: ${fehlend.join(", ")}.`);
  for (const f of ABGESCHAFFT) {
    if (new RegExp(`^\\s*-?\\s*${f}:`, "m").test(fm)) fehler.push(`Feld \`${f}\` ist abgeschafft und darf nicht mehr gesetzt werden; wie die Belege geprüft wurden, gehört als Klartext in die \`note\` der Revision.`);
  }
  for (const f of ["title", "description"]) {
    if (vorhanden.has(f) && !feldWert(fm, f)) fehler.push(`Feld \`${f}\` ist leer.`);
  }
  for (const f of ["date", "lastmod"]) {
    const w = feldWert(fm, f);
    if (w != null && !DATUM.test(w)) fehler.push(`Feld \`${f}\`: Datum im Format JJJJ-MM-TT erwartet, nicht "${w}".`);
  }
  if (art !== "thema") {
    const w = feldWert(fm, "weight");
    if (w != null && !/^\d+$/.test(w)) fehler.push(`Feld \`weight\`: ganze Zahl erwartet, nicht "${w}".`);
  } else {
    const typ = feldWert(fm, "typ");
    if (typ && !THEMA_TYPEN.includes(typ)) fehler.push(`Feld \`typ\`: "${typ}" ist unbekannt. Möglich: ${THEMA_TYPEN.join(", ")}.`);
    if (vorhanden.has("kurz") && !feldWert(fm, "kurz") && !/^kurz:\s*[>|]/m.test(fm)) fehler.push("Feld `kurz` ist leer.");
    if (/^sachgebiete:\s*\[\s*\]\s*$/m.test(fm)) fehler.push("Feld `sachgebiete` ist leer; mindestens ein Schlüssel aus /sachgebiete/ (Untergebiet vor Sachgebiet).");
  }

  const rev = revisionenLesen(fm);
  if (vorhanden.has("revisions") && !rev.length) fehler.push("`revisions` enthält keinen Eintrag.");
  if (rev[0]) {
    const fehlt = ["date", "by", "model", "note"].filter((f) => !rev[0][f]);
    if (fehlt.length) fehler.push(`Jüngster Revisionseintrag ohne ${fehlt.join(", ")}. \`note\` beschreibt die Änderung und wie die Belege geprüft wurden.`);
    if (rev[0].date && !DATUM.test(rev[0].date)) fehler.push(`Revision: Datum im Format JJJJ-MM-TT erwartet, nicht "${rev[0].date}".`);
    else if (rev[0].date && rev[0].date > heute) fehler.push(`Revision: Datum ${rev[0].date} liegt in der Zukunft.`);
  }
  return { fehler, warnungen };
}

// Bestehende Einträge bleiben unverändert erhalten, ein neuer kommt zuoberst.
export function revisionenVergleichen(fmAlt, fmNeu) {
  const alt = revisionenLesen(fmAlt).map((e) => e.roh);
  const neu = revisionenLesen(fmNeu).map((e) => e.roh);
  if (neu.length === alt.length && neu.every((r, i) => r === alt[i])) {
    return ["Kein neuer Revisionseintrag. Jede Änderung braucht einen Eintrag zuoberst in `revisions` (oder den Parameter `revision`)."];
  }
  if (neu.length !== alt.length + 1 || !alt.every((r, i) => r === neu[i + 1])) {
    return ["Die bisherigen Revisionseinträge wurden verändert oder entfernt. Sie bleiben unverändert stehen; nur ein neuer Eintrag kommt zuoberst dazu."];
  }
  return [];
}

// --- Text ---------------------------------------------------------------------

function zeileVon(text, index) {
  return text.slice(0, index).split("\n").length;
}

// Code-Blöcke und Inline-Code durch Leerraum gleicher Länge ersetzen: Darin
// ist HTML harmlos (Hugo maskiert es), und die Zeilennummern stimmen weiter.
function ohneCode(text) {
  const leer = (s) => s.replace(/[^\n]/g, " ");
  return text.replace(/^(```|~~~)[\s\S]*?^\1\s*$/gm, leer).replace(/`[^`\n]*`/g, leer);
}

export function shortcodesFinden(text) {
  return [...text.matchAll(/\{\{([<%])\s*(\/?)\s*([\w/.-]+)([^}]*?)\s*[>%]\}\}/g)].map((m) => ({
    roh: m[0], art: m[1], schliessend: m[2] === "/", name: m[3], attribute: m[4].trim(), index: m.index,
  }));
}

function attributeLesen(s) {
  const paare = [...s.matchAll(/(\w+)="([^"]*)"/g)].map((m) => [m[1], m[2]]);
  const rest = s.replace(/(\w+)="([^"]*)"/g, "").trim();
  return { paare: Object.fromEntries(paare), rest };
}

export function linksFinden(text) {
  const t = ohneCode(text);
  const links = [];
  for (const m of t.matchAll(/(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(\s*<?([^)\s>]*)>?(?:\s+"[^"]*")?\s*\)/g)) {
    links.push({ bild: m[1] === "!", text: m[2], url: m[3], zeile: zeileVon(t, m.index) });
  }
  for (const m of t.matchAll(/^\s{0,3}\[([^\]]+)\]:\s*<?(\S+?)>?(?:\s+"[^"]*")?\s*$/gm)) {
    links.push({ bild: false, text: m[1], url: m[2], zeile: zeileVon(t, m.index) });
  }
  return links;
}

function schemaZulaessig(url) {
  if (/^(https?:\/\/|\/|#|mailto:)/i.test(url)) return true;
  return !/^[a-z][a-z0-9+.-]*:/i.test(url); // relativ: ohne Schema
}

export function inhaltPruefen(text, { art, teil }) {
  const fehler = [];
  const warnungen = [];
  const ohne = ohneCode(text);

  // Rohes HTML: Die Seite rendert es ungefiltert.
  const html = new Map();
  for (const m of ohne.matchAll(/<\/?([a-zA-Z][\w-]*)\b([^>]*)>/g)) {
    const name = m[1].toLowerCase();
    if (ERLAUBTES_HTML.has(name) && !/[^\s/]/.test(m[2])) continue;
    if (!html.has(m[0])) html.set(m[0], zeileVon(ohne, m.index));
  }
  if (/<!--/.test(ohne)) fehler.push("HTML-Kommentare (`<!-- -->`) sind nicht zulässig.");
  for (const [tag, zeile] of html) {
    if (/^<(https?:|mailto:)/i.test(tag)) continue;
    fehler.push(`Rohes HTML ist nicht zulässig: \`${kurz(tag, 60)}\` (Zeile ${zeile}). Erlaubt sind nur <br>, <sup>, <sub> ohne Attribute; alles andere in Markdown.`);
  }

  // Attribut-Blöcke von Goldmark: nur Anker und Klassen, keine Attribute mit Wert.
  for (const m of ohne.matchAll(/\{:?\s*(?:[#.][\w-]|[A-Za-z_][\w-]*\s*=)[^}\n]*\}/g)) {
    if (/[=“"'<>]/.test(m[0])) fehler.push(`Attribut-Block \`${kurz(m[0], 60)}\` (Zeile ${zeileVon(ohne, m.index)}): nur \`{#anker}\` und \`{: .klasse}\` sind zulässig.`);
    else if (/gesetzeszitat/.test(m[0])) warnungen.push(`\`{: .gesetzeszitat}\` (Zeile ${zeileVon(ohne, m.index)}) ist überholt: Den Normtext setzt \`{{< wortlaut >}}\`.`);
  }

  // Shortcodes: Hugo wertet sie auch in Code-Blöcken aus, deshalb im ganzen Text.
  const shortcodes = shortcodesFinden(text);
  const geoeffnet = (text.match(/\{\{[<%]/g) || []).length;
  if (geoeffnet !== shortcodes.length) fehler.push("Unvollständiger Shortcode: Jedes `{{<` braucht ein schliessendes `>}}` auf derselben Zeile.");
  let callouts = 0;
  for (const s of shortcodes) {
    const zeile = zeileVon(text, s.index);
    if (s.art === "%") {
      fehler.push(`Shortcode \`${kurz(s.roh, 60)}\` (Zeile ${zeile}): nur die Form \`{{< … >}}\` ist zulässig.`);
      continue;
    }
    const { paare, rest } = attributeLesen(s.attribute);
    if (s.name === "wortlaut" && !s.schliessend) {
      const unbekannt = Object.keys(paare).filter((k) => !["gesetz", "art"].includes(k));
      if (rest || unbekannt.length) fehler.push(`\`${s.roh}\` (Zeile ${zeile}): nur die Attribute gesetz="…" und art="art-NNN" sind zulässig.`);
      else if ((paare.gesetz && !/^[a-z0-9-]+$/.test(paare.gesetz)) || (paare.art && !/^art-\d{3,4}[a-z]*$/.test(paare.art))) {
        fehler.push(`\`${s.roh}\` (Zeile ${zeile}): gesetz als Verzeichnisname ("stgb"), art dreistellig ("art-015").`);
      } else if (art === "thema" && !(paare.gesetz && paare.art)) {
        fehler.push(`\`${s.roh}\` (Zeile ${zeile}): In Themen braucht der Shortcode gesetz="…" und art="…".`);
      }
    } else if (s.name === "callout") {
      if (s.schliessend) callouts--;
      else {
        callouts++;
        if (rest || Object.keys(paare).some((k) => k !== "type") || (paare.type && !CALLOUT_TYPEN.includes(paare.type))) {
          fehler.push(`\`${s.roh}\` (Zeile ${zeile}): callout nur mit type="${CALLOUT_TYPEN.join('|')}".`);
        }
      }
    } else {
      fehler.push(`Shortcode \`${kurz(s.roh, 60)}\` (Zeile ${zeile}) ist nicht zulässig. Erlaubt sind \`wortlaut\` und \`callout\`.`);
    }
  }
  if (callouts !== 0) fehler.push("`{{< callout >}}` und `{{< /callout >}}` stehen nicht paarweise.");

  // Links
  for (const l of linksFinden(text)) {
    if (l.bild) fehler.push(`Bilder sind nicht zulässig (Zeile ${l.zeile}): \`${kurz(l.url, 60)}\`.`);
    else if (!schemaZulaessig(l.url)) fehler.push(`Link mit unzulässigem Schema (Zeile ${l.zeile}): \`${kurz(l.url, 60)}\`. Nur https://, http:// und Pfade wie /kommentar/….`);
  }

  // Tabellen gehören in den Textfluss, nicht in Code-Blöcke (CLAUDE.md).
  if (/^(```|~~~)\s*(markdown|md)\s*$/im.test(text)) fehler.push("Kein Text und keine Tabelle in ```markdown-Codeblöcke fassen — Hugo zeigt sie sonst als Quelltext.");
  for (const m of text.matchAll(/^(```|~~~)[^\n]*\n([\s\S]*?)^\1\s*$/gm)) {
    if (/^\s*\|.*\|\s*$/m.test(m[2]) && /^\s*\|?\s*:?-{3,}/m.test(m[2])) {
      fehler.push(`Tabelle in einem Code-Block (Zeile ${zeileVon(text, m.index)}): Tabellen direkt als Markdown in den Text setzen.`);
    }
  }

  if (text.includes("ß")) warnungen.push("Der Text enthält «ß»; Glossagens schreibt Schweizer Rechtschreibung (ss). Ausnahme: wörtliche Zitate aus deutschen Quellen.");

  if (art === "kommentar" && teil === "kommentar") {
    const abschnitt = text.match(/^##\s+Gesetzeswortlaut[^\n]*\n([\s\S]*?)(?=^##\s|(?![\s\S]))/m);
    if (!abschnitt) warnungen.push("Kein Abschnitt `## Gesetzeswortlaut`; er enthält nur `{{< wortlaut >}}`.");
    else {
      if (!/\{\{<\s*wortlaut\b/.test(abschnitt[1])) fehler.push("Im Abschnitt `## Gesetzeswortlaut` fehlt `{{< wortlaut >}}`. Den Normtext nie selbst abschreiben.");
      if (/^>/m.test(abschnitt[1])) fehler.push("Im Abschnitt `## Gesetzeswortlaut` steht ein Zitatblock. Der Normtext kommt nur aus `{{< wortlaut >}}`.");
    }
  }
  if (art === "thema") {
    const ohneAnker = ohne.split("\n").filter((z) => /^#{2,3}\s/.test(z) && !/\{#[\w-]+\}\s*$/.test(z));
    if (ohneAnker.length) warnungen.push(`Überschriften ohne festen Anker (\`## Titel {#anker}\`): ${ohneAnker.slice(0, 5).map((z) => `«${z.replace(/^#+\s*/, "")}»`).join(", ")}${ohneAnker.length > 5 ? " …" : ""}.`);
  }
  return { fehler, warnungen };
}

// --- Entscheid-Links -----------------------------------------------------------

const MONATE = ["januar", "februar", "märz", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "dezember"];

function datumImText(text) {
  const m = text.match(/\b(\d{1,2})\.\s*(\d{1,2}\.|[A-Za-zäÄ]+)\s*(\d{4})\b/);
  if (!m) return null;
  const monat = m[2].endsWith(".") ? parseInt(m[2], 10) : MONATE.indexOf(m[2].toLowerCase()) + 1;
  if (!monat || monat > 12) return null;
  return `${m[3]}-${String(monat).padStart(2, "0")}-${m[1].padStart(2, "0")}`;
}

// Linktext und Ziel eines entscheidsuche-Links gegeneinander: Nennt der Text
// eine BGE- bzw. BGer-Nummer oder ein Datum, muss es zum Dokument passen. So
// fielen erfundene Zitate auf, die auf ein echtes, aber anderes Urteil zeigten.
export function linkAbgleich(text, url) {
  const m = url.match(/entscheidsuche\.ch\/docs\/(CH_BGE|CH_BGer)\/[A-Za-z]+_[A-Za-z]+_\d+_([^_]+)_(\d{4}(?:-\d{2}-\d{2})?)\.(?:html|pdf)/);
  if (!m) return null;
  const [, sammlung, nummer, datum] = m;
  if (sammlung === "CH_BGE") {
    // URL: BGE-098-IV-293, Text: BGE 98 IV 293
    const norm = (band, teil, seite) => `${parseInt(band, 10)} ${teil.toUpperCase()} ${parseInt(seite, 10)}`;
    const ziel = nummer.match(/^BGE-(\d+)-([IVab]+)-(\d+)$/i);
    if (!ziel) return null;
    const genannt = [...text.matchAll(/\bBGE\s+(\d{2,3})\s+([IV]+[ab]?)\s+(\d+)/gi)].map((x) => norm(x[1], x[2], x[3]));
    const z = norm(ziel[1], ziel[2], ziel[3]);
    if (genannt.length && !genannt.includes(z)) return `Linktext nennt BGE ${genannt.join(", BGE ")}, der Link führt zu BGE ${z}.`;
    return null;
  }
  // URL: 6B-770-2025 (ältere Sammlungen auch C-169-2006 oder 462-2025) —
  // verglichen werden Nummer und Jahr.
  const ziel = nummer.match(/(\d+)-(\d{4})$/);
  const genannt = [...text.matchAll(/\b(\d{1,2}[A-Z]{1,2})_(\d+)\/(\d{4})\b/g)];
  if (ziel && genannt.length && !genannt.some((x) => parseInt(x[2], 10) === parseInt(ziel[1], 10) && x[3] === ziel[2])) {
    return `Linktext nennt ${genannt.map((x) => x[0]).join(", ")}, der Link führt zu ${nummer.replace(/-(\d+)-(\d{4})$/, "_$1/$2")}.`;
  }
  const d = datumImText(text);
  if (d && datum.length === 10 && d !== datum) return `Linktext nennt das Datum ${d}, das verlinkte Urteil stammt vom ${datum}.`;
  return null;
}

// --- Prüfauftrag und Belegprotokoll ---------------------------------------------
//
// Der Server prüft Belege nicht selbst — das wäre bei Dutzenden Volltexten je
// Beitrag zu teuer. Er zieht die Belegstellen mechanisch aus dem Text, und der
// Chat der einreichenden Person liest jeden Entscheid und legt je Stelle den
// tragenden Satz vor (Format angelehnt an das Verdikt-Ledger des Audits). Der
// Server prüft nur, ob das Protokoll vollständig und in sich stimmig ist; die
// Redaktion kontrolliert die Trägersätze im Pull Request.

const ENTSCHEID_URL = /entscheidsuche\.ch\/docs\/|bger\.ch\/|opencaselaw\.ch\/entscheid/;
const ENTSCHEID_TEXT = /\bBGE\s+\d{2,3}\s+[IV]+[ab]?\s+\d+|\b\d{1,2}[A-Z]{1,2}_\d+\/\d{4}\b/g;
export const URTEILE = ["traegt", "traegt_teilweise"];

// Einheiten, an denen Belege hängen: Absätze; Listenpunkte und Tabellenzeilen
// je für sich. Überschriften und Code-Blöcke tragen keine Belege.
function einheiten(text) {
  const zeilen = text.split("\n");
  const liste = [];
  let aktuell = null;
  let imCode = false;
  const abschliessen = () => {
    if (aktuell) liste.push(aktuell);
    aktuell = null;
  };
  zeilen.forEach((z, i) => {
    if (/^(```|~~~)/.test(z)) {
      imCode = !imCode;
      abschliessen();
      return;
    }
    if (imCode || !z.trim() || /^#{1,6}\s/.test(z)) {
      abschliessen();
      return;
    }
    const eigen = /^\s*([-*+]|\d+\.)\s|^\s*\|/.test(z);
    if (eigen || !aktuell) {
      abschliessen();
      aktuell = { zeile: i + 1, text: z };
      if (eigen) abschliessen();
    } else {
      aktuell.text += `\n${z}`;
    }
  });
  abschliessen();
  return liste;
}

function ohneLinks(s) {
  return s.replace(/!?\[((?:[^\[\]]|\[[^\]]*\])*)\]\([^)]*\)/g, "$1");
}

function zitateIn(s) {
  return [...s.matchAll(/«([^«»]+)»/g)].map((m) => m[1].trim()).filter((z) => z.split(/\s+/).length >= 3);
}

// Vereinheitlicht Leerraum, Striche, Anführungszeichen und weiche Trennstriche,
// damit ein wörtliches Zitat auch bei typografischen Unterschieden passt.
export function normalisieren(s) {
  return String(s)
    .replace(/­/g, "")
    .replace(/[‐-―−]/g, "-")
    .replace(/[„“”"«»‹›‚‘’']/g, "'")
    .replace(/\s+/g, " ")
    .trim();
}

// Ein Zitat passt, wenn alle Stücke zwischen Auslassungen ([…], (…), ...) und
// eigenen Einfügungen ([der Täter]) in dieser Reihenfolge im Trägersatz stehen.
export function zitatEnthalten(zitat, traeger) {
  const t = normalisieren(traeger);
  const stuecke = zitat
    .split(/\[[^\]]*\]|\(\s*(?:…|\.\.\.)\s*\)|…|\.\.\./)
    .map((x) => normalisieren(x).replace(/^[\s.,;:]+|[\s.,;:]+$/g, ""))
    .filter((x) => x.length > 3);
  let ab = 0;
  for (const s of stuecke) {
    const i = t.indexOf(s, ab);
    if (i < 0) return false;
    ab = i + s.length;
  }
  return stuecke.length > 0;
}

// Belegstellen im (neuen) Text; bei Änderungen nur in Einheiten, die es im
// bisherigen Text nicht gab. Nummern B1, B2 … in Textreihenfolge — beim
// Einreichen entstehen aus demselben Text dieselben Nummern.
export function belegstellenFinden(text, altText = null) {
  const alt = new Set(altText == null ? [] : einheiten(altText).map((e) => normalisieren(e.text)));
  const stellen = [];
  const ohneLink = [];
  let einheitNr = 0;
  for (const e of einheiten(text)) {
    if (alt.has(normalisieren(e.text))) continue;
    einheitNr++;
    const links = linksFinden(e.text).filter((l) => !l.bild && ENTSCHEID_URL.test(l.url));
    const rest = e.text.replace(/!?\[((?:[^\[\]]|\[[^\]]*\])*)\]\([^)]*\)/g, "");
    for (const m of rest.matchAll(ENTSCHEID_TEXT)) ohneLink.push({ zeile: e.zeile, entscheid: m[0] });
    const gesehen = new Set();
    for (const l of links) {
      if (gesehen.has(l.url)) continue;
      gesehen.add(l.url);
      const anker = l.url.match(/#consideration_([\d.]+)/)?.[1];
      stellen.push({
        id: `B${stellen.length + 1}`,
        einheit: einheitNr,
        zeile: e.zeile + l.zeile - 1,
        entscheid: ohneLinks(l.text).replace(/\s+/g, " ").trim(),
        url: l.url,
        pinpoint: anker ? `E. ${anker.replace(/\.$/, "")}` : null,
        aussage: ohneLinks(e.text).replace(/^\s*([-*+]|\d+\.)\s+|^\s*\|\s*/, "").replace(/\s+/g, " ").trim(),
        zitate: zitateIn(ohneLinks(e.text)),
      });
    }
  }
  return { stellen, ohneLink };
}

// Mechanische Prüfung des Protokolls: vollständig, Trägersatz vorhanden, jedes
// Zitat steht im Trägersatz, nichts Unbelegtes stehen gelassen.
export function belegeAbgleichen(stellen, belege) {
  const fehler = [];
  const warnungen = [];
  if (!Array.isArray(belege)) return { fehler: ["`belege` muss eine Liste sein: ein Eintrag je Punkt des Prüfauftrags."], warnungen, eintraege: new Map() };
  const eintraege = new Map();
  for (const b of belege) {
    const id = String(b?.id ?? "").trim().toUpperCase();
    if (!id) continue;
    if (eintraege.has(id)) warnungen.push(`Belegprotokoll: ${id} doppelt; der erste Eintrag gilt.`);
    else eintraege.set(id, b);
  }
  const bekannt = new Set(stellen.map((s) => s.id));
  const fremd = [...eintraege.keys()].filter((id) => !bekannt.has(id));
  if (fremd.length) warnungen.push(`Belegprotokoll: ${fremd.join(", ")} gibt es im Prüfauftrag nicht (Text seit der Prüfung geändert?) — ignoriert.`);
  const fehlend = stellen.filter((s) => !eintraege.has(s.id)).map((s) => s.id);
  if (fehlend.length) fehler.push(`Belegprotokoll unvollständig: Es fehlen ${fehlend.join(", ")}.`);

  const traegerJeEinheit = new Map();
  for (const s of stellen) {
    const b = eintraege.get(s.id);
    if (!b) continue;
    const traeger = typeof b.traegersatz === "string" ? b.traegersatz.trim() : "";
    if (traeger.length < 30) fehler.push(`${s.id}: \`traegersatz\` fehlt oder ist zu kurz — den tragenden Satz wörtlich aus dem Entscheid kopieren.`);
    else if (traeger.length > 3000) fehler.push(`${s.id}: \`traegersatz\` ist zu lang (höchstens 3000 Zeichen); nur die tragenden Sätze.`);
    else if (normalisieren(traeger) === normalisieren(s.aussage)) fehler.push(`${s.id}: Der Trägersatz ist der eigene Text. Er muss aus dem Entscheid stammen.`);
    if (!String(b.fundstelle ?? "").trim()) fehler.push(`${s.id}: \`fundstelle\` fehlt (z. B. "E. 2.3", "Regeste").`);
    if (!URTEILE.includes(b.urteil)) {
      fehler.push(`${s.id}: \`urteil\` "${b.urteil ?? ""}" ist nicht zulässig. Trägt der Entscheid die Aussage nicht, die Aussage korrigieren oder den Beleg streichen und neu prüfen.`);
    } else if (b.urteil === "traegt_teilweise" && !String(b.anmerkung ?? "").trim()) {
      fehler.push(`${s.id}: Bei "traegt_teilweise" in \`anmerkung\` festhalten, was der Entscheid nicht trägt und wie die Aussage eingeschränkt ist.`);
    }
    if (traeger) traegerJeEinheit.set(s.einheit, [...(traegerJeEinheit.get(s.einheit) ?? []), traeger]);
  }
  // Ein Zitat gehört zu einem der Entscheide seines Absatzes.
  const geprueft = new Set();
  for (const s of stellen) {
    for (const z of s.zitate) {
      const schluessel = `${s.einheit}\u0000${z}`;
      if (geprueft.has(schluessel)) continue;
      geprueft.add(schluessel);
      const traeger = traegerJeEinheit.get(s.einheit) ?? [];
      if (traeger.length && !traeger.some((t) => zitatEnthalten(z, t))) {
        fehler.push(`Zeile ${s.zeile}: Das Zitat «${kurz(z, 80)}» steht in keinem Trägersatz dieses Absatzes. Wörtliche Zitate genau so aus dem Entscheid übernehmen und den Satz als Trägersatz angeben — oder das Zitat in eigene Worte fassen.`);
      }
    }
  }
  return { fehler, warnungen, eintraege };
}

// --- Abschnitte -----------------------------------------------------------------

function ueberschriftOhneAnker(z) {
  return z.replace(/\s*\{#[^}]*\}\s*$/, "").trim();
}

function ueberschriftenIndizes(zeilen) {
  const idx = [];
  let imCode = false;
  zeilen.forEach((z, i) => {
    if (/^(```|~~~)/.test(z)) imCode = !imCode;
    else if (!imCode && /^#{1,6}\s/.test(z)) idx.push(i);
  });
  return idx;
}

// Ersetzt den Abschnitt, dessen Überschrift `abschnitt` enthält, bis zur
// nächsten Überschrift gleicher oder höherer Ebene — denselben Bereich, den
// das Lesen mit `abschnitt` liefert. Ohne Überschrift im neuen Text bleibt die
// alte stehen. `entfernt` nennt Unterabschnitte, die im neuen Text fehlen: Ein
// Modell, das nur einen Absatz schickt, soll nicht stillschweigend die
// Unterabschnitte löschen.
export function abschnittErsetzen(text, abschnitt, neu) {
  const zeilen = text.split("\n");
  const idx = ueberschriftenIndizes(zeilen);
  const suche = String(abschnitt).toLowerCase().trim();
  const treffer = idx.filter((i) => zeilen[i].toLowerCase().includes(suche));
  if (!suche || !treffer.length) {
    throw new Error(`Kein Abschnitt mit "${abschnitt}" in der Überschrift. Vorhanden:\n${idx.map((i) => ueberschriftOhneAnker(zeilen[i])).join("\n")}`);
  }
  if (treffer.length > 1) {
    throw new Error(`"${abschnitt}" passt auf mehrere Überschriften; bitte eindeutig angeben:\n${treffer.map((i) => ueberschriftOhneAnker(zeilen[i])).join("\n")}`);
  }
  const start = treffer[0];
  const ebene = zeilen[start].match(/^#+/)[0].length;
  const ende = idx.find((i) => i > start && zeilen[i].match(/^#+/)[0].length <= ebene) ?? zeilen.length;
  let ersatz = String(neu).replace(/\r\n/g, "\n").trim().split("\n");
  if (!/^#{1,6}\s/.test(ersatz[0])) ersatz = [zeilen[start], "", ...ersatz];
  const vorEnde = ende < zeilen.length ? [""] : [];
  const neuTitel = new Set(ueberschriftenIndizes(ersatz).map((i) => ueberschriftOhneAnker(ersatz[i])));
  const entfernt = idx.filter((i) => i > start && i < ende).map((i) => ueberschriftOhneAnker(zeilen[i])).filter((t) => !neuTitel.has(t));
  return {
    text: [...zeilen.slice(0, start), ...ersatz, ...vorEnde, ...zeilen.slice(ende)].join("\n").replace(/\n*$/, "\n"),
    entfernt,
  };
}

// Text ohne Frontmatter, aber mit Leerzeilen an dessen Stelle: So beziehen
// sich die Zeilennummern der Befunde auf die ganze Datei.
export function koerperMitVersatz(md) {
  const { kopf, text } = frontmatterTrennen(md);
  return "\n".repeat((kopf.match(/\n/g) || []).length) + text;
}

function abschnitte(text) {
  const zeilen = text.split("\n");
  const idx = ueberschriftenIndizes(zeilen);
  const teile = [];
  const grenzen = [0, ...idx, zeilen.length];
  for (let k = 0; k < grenzen.length - 1; k++) {
    const von = grenzen[k];
    const bis = grenzen[k + 1];
    if (von === bis) continue;
    const titel = k === 0 && !idx.includes(0) ? "(Anfang)" : ueberschriftOhneAnker(zeilen[von]);
    teile.push({ titel, zeilen: zeilen.slice(von, bis).map((z) => z.trimEnd()).filter((z, i, a) => z || (i > 0 && a[i - 1])) });
  }
  return teile;
}

// Zusammenfassung je Abschnitt: was ist neu, weg oder geändert.
export function abschnitteVergleichen(alt, neu) {
  const a = abschnitte(alt);
  const n = abschnitte(neu);
  const schluessel = (liste) => {
    const zaehler = {};
    return liste.map((s) => {
      zaehler[s.titel] = (zaehler[s.titel] || 0) + 1;
      return { ...s, key: `${s.titel}#${zaehler[s.titel]}` };
    });
  };
  const ak = new Map(schluessel(a).map((s) => [s.key, s]));
  const nk = schluessel(n);
  const zeilen = [];
  for (const s of nk) {
    const vorher = ak.get(s.key);
    if (!vorher) zeilen.push(`neu: ${s.titel} (${s.zeilen.length} Zeilen)`);
    else {
      const x = new Set(vorher.zeilen);
      const y = new Set(s.zeilen);
      const plus = s.zeilen.filter((z) => !x.has(z)).length;
      const minus = vorher.zeilen.filter((z) => !y.has(z)).length;
      if (plus || minus) zeilen.push(`geändert: ${s.titel} (+${plus}/−${minus} Zeilen)`);
      ak.delete(s.key);
    }
  }
  for (const s of ak.values()) zeilen.push(`entfernt: ${s.titel}`);
  return zeilen;
}

// Welche Felder der obersten Ebene sich geändert haben (revisions ausgenommen).
export function frontmatterVergleichen(alt, neu) {
  const bloecke = (fm) => {
    const map = new Map();
    let name = null;
    for (const z of fm.split("\n")) {
      const m = z.match(/^([A-Za-z_][\w-]*):/);
      if (m) name = m[1];
      if (name) map.set(name, `${map.get(name) ?? ""}${z}\n`);
    }
    return map;
  };
  const a = bloecke(alt);
  const n = bloecke(neu);
  return [...new Set([...a.keys(), ...n.keys()])].filter((k) => k !== "revisions" && a.get(k) !== n.get(k));
}

// --- Sonstiges ------------------------------------------------------------------

// Git-Blob-SHA, wie ihn auch die GitHub-API als `sha` einer Datei führt. Damit
// lässt sich beim Einreichen prüfen, ob die Datei seit dem Lesen geändert wurde.
export async function gitSha(text) {
  const inhalt = new TextEncoder().encode(text);
  const kopf = new TextEncoder().encode(`blob ${inhalt.length}\0`);
  const alles = new Uint8Array(kopf.length + inhalt.length);
  alles.set(kopf);
  alles.set(inhalt, kopf.length);
  const hash = await crypto.subtle.digest("SHA-1", alles);
  return [...new Uint8Array(hash)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

export function heute() {
  return new Intl.DateTimeFormat("sv-SE", { timeZone: "Europe/Zurich" }).format(new Date());
}

function kurz(s, n) {
  s = String(s).replace(/\s+/g, " ");
  return s.length > n ? `${s.slice(0, n - 1)}…` : s;
}
