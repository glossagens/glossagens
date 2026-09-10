/**
 * Artikelsprung im Suchfeld — „StGB 70", „Art. 305bis StGB", „or336c" führen
 * direkt auf den Kommentar, statt in einer Volltextliste zu landen.
 *
 * Warum nicht über den FlexSearch-Index: der findet „StGB 70" in jedem Artikel,
 * der die Norm zitiert, und die gesuchte Seite steht irgendwo dazwischen. Die
 * Zuordnung Kürzel + Nummer → Seite ist aber eindeutig und liegt als kleiner
 * Index bereit (`assets/json/artikel-index.json`, rund 15 KB gzip). Er wird in
 * der ersten Leerlaufphase geladen und ist damit lange vor dem 14-MB-Volltext-
 * index da; der Sprung trägt auch dann, wenn dieser gar nicht ankommt (mit
 * blockiertem `search-data.json` gegengeprüft).
 *
 * Zusammenspiel mit dem Theme: Hextras `flexsearch.js` baut die Trefferliste bei
 * jedem `keyup` neu auf. Dieses Skript hängt sich deshalb erst in
 * `DOMContentLoaded` an das Feld — dann steht sein Listener hinter dem des
 * Themes und darf dessen fertige Liste ergänzen. Der Sprungtreffer wird als
 * erster Eintrag eingehängt, die übrigen `data-index` rücken eine Position
 * weiter und `dataset.count` wächst um eins; Pfeiltasten und Enter des Themes
 * lesen genau diese Attribute aus dem DOM und übernehmen den Eintrag dadurch
 * ohne weiteres Zutun.
 */
(function () {
  // {{ $sprungIndex := resources.Get "json/artikel-index.json" | resources.ExecuteAsTemplate "json/artikel-index.json" . }}
  // {{ if hugo.IsProduction }}{{ $sprungIndex = $sprungIndex | minify | fingerprint }}{{ end }}
  const INDEX_URL = '{{ $sprungIndex.RelPermalink }}';

  /* Füllwörter, die zwischen Kürzel und Nummer stehen dürfen. */
  const FUELLWORT = /^(art|artikel|artt|para|abs)$/;
  /* Artikelnummer mit optionalem Zusatz: 70, 305bis, 24a, 66abis, 960e. */
  const NUMMER = /^\d{1,3}[a-zäöüß]*$/;
  /* Nachgestellter Zusatz, falls getrennt getippt: „art 305 bis". */
  const ZUSATZ = /^(bis|ter|quater|quinquies|sexies|septies|octies|novies|decies|[a-z])$/;

  let register = null;   // Kürzel (normalisiert) → Gesetzeseintrag
  let laufend = null;    // laufender fetch, damit nur einmal geladen wird

  function indexLaden() {
    if (laufend) return laufend;
    laufend = fetch(INDEX_URL)
      .then(r => (r.ok ? r.json() : {}))
      .then(json => {
        register = Object.create(null);
        for (const key in json) {
          const gesetz = json[key];
          for (const alias of gesetz.al || [key]) register[alias] = gesetz;
        }
        return register;
      })
      .catch(() => (register = Object.create(null)));
    return laufend;
  }

  /**
   * Zerlegt die Eingabe in Kürzelkandidaten und Artikelnummer. Reihenfolge und
   * Trennzeichen sind gleichgültig: „StGB 70", „Art. 70 StGB", „70 stgb",
   * „stgb70" und „VRG LU 15" führen alle zum selben Ergebnis.
   */
  function zerlegen(eingabe) {
    const roh = (eingabe || '').toLowerCase().replace(/[.,;:_/–—-]/g, ' ').trim();
    if (!roh || roh.length > 40) return null;

    /* „stgb70" auftrennen; „305bis" bleibt zusammen, weil es mit einer Ziffer
       beginnt und die Regel Buchstaben zuerst verlangt. */
    const teile = [];
    for (const t of roh.split(/\s+/).filter(Boolean)) {
      const m = t.match(/^([a-zäöüß]{2,12})(\d{1,3}[a-zäöüß]*)$/);
      if (m) teile.push(m[1], m[2]);
      else teile.push(t);
    }

    let nummer = null;
    const woerter = [];
    for (const t of teile) {
      if (FUELLWORT.test(t)) continue;
      if (nummer === null && NUMMER.test(t)) { nummer = t; continue; }
      /* Zusatz, der getrennt vom Zahlteil steht, wieder anhängen. */
      if (nummer !== null && /^\d+$/.test(nummer) && ZUSATZ.test(t)) { nummer += t; continue; }
      if (/^[a-zäöüß]+$/.test(t)) woerter.push(t);
    }
    if (!woerter.length) return null;

    /* Erst die Wörter zusammen versuchen (kantonal: „vrg lu"), dann einzeln. */
    const kandidaten = [woerter.join('')].concat(woerter);
    return { kandidaten, nummer };
  }

  function treffer(eingabe) {
    if (!register) return null;
    const teile = zerlegen(eingabe);
    if (!teile) return null;

    let gesetz = null;
    for (const k of teile.kandidaten) {
      if (register[k]) { gesetz = register[k]; break; }
    }
    if (!gesetz) return null;
    if (!teile.nummer) return { art: 'gesetz', gesetz: gesetz };

    const artikel = gesetz.a[teile.nummer];
    if (artikel) {
      return {
        art: 'artikel',
        gesetz: gesetz,
        url: gesetz.u + artikel.s + '/',
        titel: artikel.t,
        nummer: teile.nummer
      };
    }
    return { art: 'fehlt', gesetz: gesetz, nummer: teile.nummer };
  }

  function knoten(tag, klasse, text) {
    const el = document.createElement(tag);
    if (klasse) el.className = klasse;
    if (text) el.textContent = text;
    return el;
  }

  /** Ergänzt die vom Theme gebaute Trefferliste um den Sprungeintrag. */
  function einfuegen(feld) {
    const huelle = feld.closest('.hextra-search-wrapper');
    const liste = huelle && huelle.querySelector('.hextra-search-results');
    if (!liste) return;

    /* Eigene Knoten des letzten Durchgangs entfernen — das Theme räumt nur bei
       nicht leerer Eingabe auf, bei „kein Treffer" schreibt es stattdessen. */
    liste.querySelectorAll('[data-gl-sprung]').forEach(n => n.remove());

    const t = treffer(feld.value);
    if (!t) return;

    /* Nicht kommentierter Artikel: nur ein Hinweis mit Weg zur Übersicht. Er
       bleibt bewusst aus der Tastaturnavigation heraus, damit Enter weiterhin
       den besten Volltexttreffer öffnet. */
    if (t.art === 'fehlt') {
      const hinweis = knoten('div', 'gl-sprung-hinweis');
      hinweis.dataset.glSprung = '1';
      hinweis.appendChild(document.createTextNode(
        `Art. ${t.nummer} ${t.gesetz.k} ist noch nicht kommentiert — `));
      const link = knoten('a', null, `Übersicht ${t.gesetz.k}`);
      link.href = t.gesetz.u;
      hinweis.appendChild(link);
      liste.insertBefore(hinweis, liste.firstChild);
      liste.classList.remove('hx:hidden');
      return;
    }

    const leer = liste.querySelector('.hextra-search-no-result');
    if (leer) leer.remove();

    const ziel = t.art === 'artikel' ? t.url : t.gesetz.u;
    const titel = t.art === 'artikel'
      ? `${t.titel} (${t.gesetz.k})`
      : `${t.gesetz.k} — ${t.gesetz.n}`;
    const zeile = t.art === 'artikel'
      ? `Kommentar zu Art. ${t.nummer} ${t.gesetz.k} — Enter öffnet die Seite`
      : 'Artikelübersicht des Erlasses — Enter öffnet die Seite';

    const vorspann = knoten('div', 'hextra-search-prefix gl-sprung-vorspann', 'Direkt zum Kommentar');
    vorspann.dataset.glSprung = '1';

    const eintrag = knoten('li', 'gl-sprung');
    eintrag.dataset.glSprung = '1';
    const link = knoten('a', 'hextra-search-active');
    link.href = ziel;
    link.dataset.index = '0';
    link.appendChild(knoten('div', 'hextra-search-title', titel));
    link.appendChild(knoten('div', 'hextra-search-excerpt', zeile));
    eintrag.appendChild(link);

    /* Bestehende Treffer eine Position nach hinten schieben. */
    const bisher = Array.from(liste.querySelectorAll('a[data-index]'));
    bisher.forEach((el, i) => {
      el.dataset.index = String(i + 1);
      el.classList.remove('hextra-search-active');
    });

    liste.insertBefore(eintrag, liste.firstChild);
    liste.insertBefore(vorspann, eintrag);
    liste.dataset.count = String(bisher.length + 1);
    liste.classList.remove('hx:hidden');

    /* Maus über den Eintrag: Markierung übernehmen, wie es das Theme für seine
       eigenen Zeilen tut. */
    eintrag.addEventListener('mousemove', () => {
      const aktiv = liste.querySelector('a.hextra-search-active');
      if (aktiv && aktiv !== link) aktiv.classList.remove('hextra-search-active');
      link.classList.add('hextra-search-active');
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    const felder = document.querySelectorAll('.hextra-search-input');
    if (!felder.length) return;

    /* Den Sprungindex in einer Leerlaufphase vorladen, statt erst beim Fokus:
       Hextra startet beim Fokus das Laden des Volltextindex, und dessen
       JSON.parse (14 MB) blockiert den Main Thread für einige hundert
       Millisekunden. Wer sofort „StGB 70" tippt und Enter drückt, hätte den
       Sprungeintrag sonst noch nicht auf dem Schirm. 60 KB in der Leerlaufzeit
       kosten dagegen nichts. */
    if (window.requestIdleCallback) requestIdleCallback(indexLaden, { timeout: 3000 });
    else setTimeout(indexLaden, 1200);

    felder.forEach(feld => {
      const auffrischen = () => {
        if (register) { einfuegen(feld); return; }
        indexLaden().then(() => einfuegen(feld));
      };
      feld.addEventListener('focus', auffrischen);
      feld.addEventListener('keyup', auffrischen);
    });
  });
})();
