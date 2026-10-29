/*
 * Entwurfsansicht (/entwurf/?pr=123), siehe layouts/entwurf/list.html.
 *
 * Ablauf: Daten laden (entwurfLaden) → je Datei Frontmatter abtrennen, Text in
 * Blöcke (Leerzeile) teilen → Blöcke vergleichen; geänderte Blöcke Wort für
 * Wort vergleichen und <ins>/<del> in den Markdown-Quelltext setzen → mit
 * markdown-it rendern, mit DOMPurify bereinigen.
 */
(function () {
  'use strict';

  var wurzel = document.getElementById('gl-entwurf');
  if (!wurzel) return;
  var repo = wurzel.getAttribute('data-repo');
  var API = 'https://api.github.com/repos/' + repo;

  // Platzhalter ohne Leerzeichen: überstehen Tokenisierung und Markdown als ein Wort.
  var PH_WORTLAUT = 'GLENTWURFWORTLAUT';
  var PH_SHORTCODE = 'GLENTWURFSHORTCODE';

  // ---------- Datenquelle ----------
  // Einzige Stelle, die GitHub kennt. Für Variante C durch einen Abruf beim
  // Worker ersetzen, der dasselbe Objekt liefert.
  function json(url) {
    return fetch(url, { headers: { Accept: 'application/vnd.github+json' } }).then(function (r) {
      if (r.ok) return r.json();
      var e = new Error('HTTP ' + r.status);
      e.status = r.status;
      e.limit = r.headers.get('x-ratelimit-remaining') === '0';
      throw e;
    });
  }
  function roh(quelle, sha, pfad) {
    var url = 'https://raw.githubusercontent.com/' + quelle + '/' + sha + '/' +
      pfad.split('/').map(encodeURIComponent).join('/');
    return fetch(url).then(function (r) {
      if (!r.ok) throw new Error('Datei nicht lesbar: ' + pfad + ' (' + r.status + ')');
      return r.text();
    });
  }
  function entwurfLaden(nr) {
    return json(API + '/pulls/' + nr).then(function (pr) {
      return json(API + '/compare/' + pr.base.sha + '...' + pr.head.sha).then(function (cmp) {
        var basis = cmp.merge_base_commit.sha;
        var kopf = (pr.head.repo && pr.head.repo.full_name) || repo;
        var dateien = cmp.files.filter(function (f) {
          return /^content\/.*\.md$/.test(f.filename);
        });
        return Promise.all(dateien.map(function (f) {
          return Promise.all([
            f.status === 'added' ? '' : roh(repo, basis, f.previous_filename || f.filename),
            f.status === 'removed' ? '' : roh(kopf, pr.head.sha, f.filename)
          ]).then(function (t) {
            return { pfad: f.filename, status: f.status, alt: t[0], neu: t[1] };
          });
        })).then(function (geladen) {
          return {
            nummer: pr.number,
            titel: pr.title,
            url: pr.html_url,
            zustand: pr.merged_at ? 'gemergt' : (pr.state === 'open' ? (pr.draft ? 'Entwurf' : 'offen') : 'geschlossen'),
            weitere: cmp.files.length - dateien.length,
            dateien: geladen
          };
        });
      });
    });
  }

  // ---------- Zerlegen ----------
  function teile(text) {
    var m = /^---\r?\n([\s\S]*?)\r?\n---[ \t]*(?:\r?\n|$)/.exec(text);
    return m ? { fm: m[1], body: text.slice(m[0].length) } : { fm: '', body: text };
  }
  function vorbereiten(md) {
    return md
      .replace(/\{\{[<%]\s*wortlaut\b[\s\S]*?[>%]\}\}/g, PH_WORTLAUT)
      .replace(/\{\{[<%][\s\S]*?[>%]\}\}/g, PH_SHORTCODE)
      .replace(/^(#{1,6}[ \t].*?)[ \t]*\{#[^}]*\}[ \t]*$/gm, '$1');
  }
  function bloecke(body) {
    return vorbereiten(body.replace(/\r\n/g, '\n')).split(/\n[ \t]*\n/)
      .map(function (b) { return b.replace(/^\n+|\s+$/g, ''); })
      .filter(Boolean);
  }
  // Markdown-Links bleiben ein Token, sonst landen Tags mitten in [Text](URL);
  // Tabellenstriche sind eigene Tokens, damit Zellen einzeln vergleichbar bleiben.
  function tokens(s) {
    return s.match(/\[[^\]\n]*\]\([^)\s]*\)|\s+|\||[^\s|]+/g) || [];
  }

  function woerter(toks) {
    return toks.filter(function (t) { return /[^\s|]/.test(t); }).length;
  }

  // ---------- Markieren ----------
  function umschliesse(stueck, tag) {
    var m = /^(\s*)([\s\S]*?)(\s*)$/.exec(stueck);
    return m[2] ? m[1] + '<' + tag + '>' + m[2] + '</' + tag + '>' + m[3] : stueck;
  }
  // Tags dürfen weder Zeilen noch Tabellenzellen überspannen und keine
  // Zeilenmarker (Liste, Überschrift, Zitat) verschlucken.
  function markiere(text, tag, zeilenanfang) {
    return text.split('\n').map(function (zeile, i) {
      var vorne = '';
      if (i > 0 || zeilenanfang) {
        var m = /^\s*(?:[-*+]\s+|\d+\.\s+|#{1,6}\s+|>\s*)?/.exec(zeile);
        vorne = m[0];
        zeile = zeile.slice(vorne.length);
      }
      // Trennzeile einer Tabelle (|---|:--|): markiert wäre sie keine mehr.
      // Es gilt die neue Fassung, gestrichene Teile entfallen.
      if (/-/.test(zeile) && /^[\s|:-]*$/.test(zeile)) return tag === 'del' ? vorne : vorne + zeile;
      return vorne + zeile.split(/(\|)/).map(function (z) {
        return z === '|' ? z : umschliesse(z, tag);
      }).join('');
    }).join('\n');
  }
  function wortdiff(alt, neu) {
    var a = tokens(alt), n = tokens(neu);
    var stuecke = Diff.diffArrays(a, n);
    // Änderungen, die nur durch Leerzeichen getrennt sind, bilden einen Lauf:
    // erst alles Gestrichene, dann alles Neue — statt Wort um Wort im Wechsel.
    var aus = '', gleich = 0, weg = '', dazu = '', anfang = true;
    function leeren() {
      var rest = /[ \t]*$/.exec(dazu || weg)[0];
      weg = weg.replace(/[ \t]+$/, '');
      dazu = dazu.replace(/[ \t]+$/, '');
      if (weg) aus += markiere(weg, 'del', anfang);
      if (weg && dazu) aus += ' ';
      if (dazu) aus += markiere(dazu, 'ins', anfang && !weg);
      aus += rest;
      weg = dazu = '';
    }
    stuecke.forEach(function (t) {
      var s = t.value.join('');
      if (!weg && !dazu) anfang = aus === '' || aus.slice(-1) === '\n';
      if (t.added) dazu += s;
      else if (t.removed) weg += s;
      else if ((weg || dazu) && /^[ \t]+$/.test(s)) { if (weg) weg += s; if (dazu) dazu += s; }
      else { leeren(); aus += s; gleich += woerter(t.value); }
    });
    leeren();
    var laenge = Math.max(woerter(a), woerter(n)) || 1;
    return { md: aus, aehnlich: gleich / laenge };
  }

  // ---------- Vergleich ----------
  function vergleiche(altText, neuText) {
    var a = bloecke(altText), n = bloecke(neuText);
    var aus = [];
    var weg = [], dazu = [];
    function leeren() {
      var k = Math.min(weg.length, dazu.length);
      for (var i = 0; i < k; i++) {
        var d = wortdiff(weg[i], dazu[i]);
        if (d.aehnlich >= 0.4) aus.push({ art: 'geaendert', md: d.md });
        else { aus.push({ art: 'entfernt', md: weg[i] }); aus.push({ art: 'neu', md: dazu[i] }); }
      }
      weg.slice(k).forEach(function (b) { aus.push({ art: 'entfernt', md: b }); });
      dazu.slice(k).forEach(function (b) { aus.push({ art: 'neu', md: b }); });
      weg = []; dazu = [];
    }
    Diff.diffArrays(a, n).forEach(function (t) {
      if (t.removed) weg = weg.concat(t.value);
      else if (t.added) dazu = dazu.concat(t.value);
      else {
        leeren();
        t.value.forEach(function (b) { aus.push({ art: 'gleich', md: b }); });
      }
    });
    leeren();
    // Kontext für «nur Änderungen»: Nachbarn geänderter Blöcke und alle Überschriften.
    aus.forEach(function (b, i) {
      if (b.art !== 'gleich') return;
      var nachbar = [aus[i - 1], aus[i + 1]].some(function (x) { return x && x.art !== 'gleich'; });
      b.kontext = nachbar || /^#{1,6}\s/.test(b.md);
    });
    return aus;
  }

  // ---------- Darstellung ----------
  var md = null;
  function html(quelle) {
    md = md || window.markdownit({ html: true, linkify: false, typographer: false });
    var h = DOMPurify.sanitize(md.render(quelle));
    return h
      .replace(new RegExp('(<p>)?' + PH_WORTLAUT + '(</p>)?', 'g'),
        '<div class="gl-e-platzhalter">Gesetzeswortlaut — wird beim Build aus der amtlichen Quelle eingesetzt</div>')
      .replace(new RegExp(PH_SHORTCODE, 'g'), '<span class="gl-e-platzhalter">Shortcode</span>');
  }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function seitenUrl(pfad) {
    var p = pfad.replace(/^content/, '').replace(/(_index|index)\.md$/, '').replace(/\.md$/, '/');
    return p.replace(/\/+$/, '/') || '/';
  }
  function fmDiff(alt, neu) {
    if (alt === neu) return null;
    var box = el('details', 'gl-e-fm');
    var n = 0;
    var pre = el('pre');
    Diff.diffLines(alt, neu).forEach(function (t) {
      if (!t.added && !t.removed) return;
      n += t.count || 1;
      var zeilen = t.value.replace(/\n$/, '').split('\n');
      zeilen.forEach(function (z) {
        pre.appendChild(el('span', t.added ? 'gl-e-fm-neu' : 'gl-e-fm-alt', (t.added ? '+ ' : '− ') + z + '\n'));
      });
    });
    box.appendChild(el('summary', null, 'Frontmatter: ' + n + ' Zeile' + (n === 1 ? '' : 'n') + ' geändert'));
    box.appendChild(pre);
    return box;
  }
  function zeigeDatei(d) {
    var sec = el('section', 'gl-e-datei');
    var kopf = el('div', 'gl-e-kopf');
    var art = { added: 'neu', removed: 'gelöscht', renamed: 'umbenannt', modified: 'geändert' }[d.status] || d.status;
    kopf.appendChild(el('span', 'gl-e-status gl-e-status-' + d.status, art));
    kopf.appendChild(el('code', 'gl-e-pfad', d.pfad));
    if (d.status !== 'added') {
      var a = el('a', null, 'veröffentlichte Fassung');
      a.href = seitenUrl(d.pfad);
      kopf.appendChild(a);
    }
    sec.appendChild(kopf);

    var alt = teile(d.alt), neu = teile(d.neu);
    var fm = fmDiff(alt.fm, neu.fm);
    if (fm) sec.appendChild(fm);

    var bl = vergleiche(alt.body, neu.body);
    var zahl = { geaendert: 0, neu: 0, entfernt: 0 };
    var text = el('div', 'gl-e-text');
    bl.forEach(function (b) {
      if (zahl[b.art] != null) zahl[b.art]++;
      var div = el('div', 'gl-e-block gl-e-' + b.art + (b.kontext ? ' gl-e-kontext' : ''));
      div.innerHTML = html(b.md);
      text.appendChild(div);
    });
    var bilanz = [];
    if (zahl.geaendert) bilanz.push(zahl.geaendert + ' geändert');
    if (zahl.neu) bilanz.push(zahl.neu + ' neu');
    if (zahl.entfernt) bilanz.push(zahl.entfernt + ' entfernt');
    kopf.appendChild(el('span', 'gl-e-bilanz',
      bilanz.length ? 'Absätze: ' + bilanz.join(', ') : 'Text unverändert'));
    sec.appendChild(text);
    return sec;
  }
  function zeige(e) {
    wurzel.textContent = '';
    var kopf = el('div', 'gl-e-pr');
    kopf.appendChild(el('span', 'gl-pr-badge', e.zustand));
    var a = el('a', null, '#' + e.nummer + ' ' + e.titel);
    a.href = e.url;
    a.rel = 'noopener';
    kopf.appendChild(a);
    wurzel.appendChild(kopf);

    var schalter = el('label', 'gl-e-schalter');
    var cb = el('input');
    cb.type = 'checkbox';
    cb.addEventListener('change', function () { wurzel.classList.toggle('gl-e-nur', cb.checked); });
    schalter.appendChild(cb);
    schalter.appendChild(document.createTextNode(' Nur Änderungen mit Kontext'));
    wurzel.appendChild(schalter);

    if (!e.dateien.length) wurzel.appendChild(el('p', null, 'Der Pull Request ändert keine Inhalte unter content/.'));
    e.dateien.forEach(function (d) { wurzel.appendChild(zeigeDatei(d)); });
    if (e.weitere) {
      wurzel.appendChild(el('p', 'gl-e-hinweis', e.weitere + ' weitere Datei' + (e.weitere === 1 ? '' : 'en') +
        ' ausserhalb von content/ (z. B. Wortlaut-Daten) sind hier nicht dargestellt.'));
    }
  }
  function fehler(err) {
    var t = err.limit ? 'Die Abfragegrenze von GitHub ist erreicht (60 pro Stunde). Bitte später erneut versuchen.'
      : err.status === 404 ? 'Diesen Pull Request gibt es nicht.'
      : 'Der Entwurf konnte nicht geladen werden (' + err.message + ').';
    wurzel.textContent = '';
    wurzel.appendChild(el('p', 'gl-e-fehler', t));
  }

  function start() {
    var nr = new URLSearchParams(location.search).get('pr');
    if (!nr || !/^\d+$/.test(nr)) return;
    document.getElementById('gl-e-pr').value = nr;
    document.title = 'Entwurf #' + nr + ' – Glossagens';
    wurzel.textContent = 'Lade Pull Request #' + nr + ' …';
    entwurfLaden(nr).then(zeige, fehler);
  }
  // Skripte sind defer: beim Ausführen ist das DOM fertig und die Bibliotheken geladen.
  start();
})();
