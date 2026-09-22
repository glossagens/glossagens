/**
 * Ladezustand der Volltextsuche — statt „Keine Ergebnisse gefunden" zeigt die
 * Trefferliste, dass der Index noch unterwegs ist, und füllt sich selbst, sobald
 * er da ist.
 *
 * Das Problem: Hextras `flexsearch.js` legt `window.pageIndex` **vor** dem
 * `fetch` an und befüllt es erst, wenn `de.search-data.json` vollständig da ist
 * (17,8 MB roh, 4,6 MB über die Leitung, danach einige Sekunden Parse- und
 * Indexaufbau auf dem Main Thread). Jede Suche in dieser Zeit läuft gegen einen
 * leeren Index und landet in `displayResults([])` — die Suche behauptet also
 * „Keine Ergebnisse gefunden", während sie in Wahrheit noch lädt. Wer „Notwehr"
 * tippt, hält das für eine Antwort und geht wieder.
 *
 * Deshalb zwei Eingriffe, beide ohne Änderung am Theme:
 *
 * 1. **Vorladen vor dem Fokus.** Das Theme startet den Index in seinem
 *    `focus`-Handler. Ein synthetisches `focus`-Event auf ein Suchfeld löst
 *    genau diesen Handler aus, ohne den Tastaturfokus zu verschieben — damit
 *    beginnt der Download bereits, wenn der Zeiger das Feld erreicht
 *    (`pointerenter`), und auf `/kommentar/`, wo das Feld die Seite trägt,
 *    schon in der Leerlaufzeit nach `load`.
 *    Nicht auf jeder Seite in der Leerlaufzeit: 4,6 MB plus mehrere Sekunden
 *    Indexaufbau träfen auch jeden, der nie sucht — auf dem Telefon ist das
 *    spürbar. Der Zeiger-/Fokusauslöser kostet dagegen nichts und kommt in der
 *    Praxis einige hundert Millisekunden vor dem ersten Tastendruck.
 *
 * 2. **Sichtbarer Ladezustand.** Solange der Index leer ist, ersetzt dieses
 *    Skript die Leermeldung durch eine Zeile mit Spinner und trägt sie auch in
 *    `.hextra-search-status` für Screenreader nach. Ein Poller prüft den Index
 *    und stösst die Suche des Themes per erneutem `keyup` an, sobald er steht —
 *    die Liste füllt sich also ohne weiteren Tastendruck.
 *
 * Reihenfolge: `scripts/core.html` bündelt `js/core/*.js` in
 * `resources.Match`-Reihenfolge, `artikel-sprung.js` steht also vor dieser
 * Datei. Beide hängen sich in `DOMContentLoaded` ein, dieser Handler läuft
 * damit hinter dem Theme *und* hinter dem Sprungeintrag und sieht die fertige
 * Liste.
 */
(function () {
  /* Nach dieser Zeit wechselt die Meldung auf „nicht geladen" — der Poller
     läuft aber weiter, damit ein spät eintreffender Index die Liste doch noch
     füllt. 4,6 MB brauchen bei 30 kB/s zweieinhalb Minuten; wer früher aufgibt,
     behauptet einen Fehler, den es nicht gibt. Ganz abgebrochen wird erst nach
     STILLE_MS, damit kein Intervall ewig weiterläuft. */
  const GEDULD_MS = 180000;
  const STILLE_MS = 600000;
  const TAKT_MS = 150;

  let vorgeladen = false;
  let poller = null;

  /* ------------------------------------------------------------------ Zustand */

  /**
   * Trägt der Index schon Dokumente? `reg` ist die Registry der FlexSearch-
   * `Document`-Instanz (Set der vergebenen IDs) — sie ist leer, solange der
   * Aufbau läuft. Fehlt sie in einer künftigen FlexSearch-Version, entscheidet
   * eine Suchprobe: der Präfix „recht" kommt in jedem Kommentar dieses Projekts
   * vor, ein leerer Index liefert dagegen nichts.
   */
  function bestueckt(idx) {
    if (!idx) return false;
    const reg = idx.reg;
    if (reg && typeof reg.size === 'number') return reg.size > 0;
    try {
      return (idx.search('recht', 1) || []).length > 0;
    } catch (e) {
      return false;
    }
  }

  /** 'aus' = noch nicht angestossen, 'laedt' = im Aufbau, 'bereit' = benutzbar. */
  function zustand() {
    if (!window.pageIndex) return 'aus';
    return bestueckt(window.pageIndex) ? 'bereit' : 'laedt';
  }

  /* ----------------------------------------------------------------- Vorladen */

  /** Leitung, auf der 4,6 MB im Hintergrund nicht zu rechtfertigen sind. */
  function leitungTraegt() {
    const c = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (!c) return true;
    if (c.saveData) return false;
    return !/(^|-)([23]g|slow-2g)$/.test(c.effectiveType || '');
  }

  /**
   * Startet den Indexaufbau des Themes über ein synthetisches `focus`-Event.
   * Der Handler des Themes (`init`) hängt sich danach selbst aus, mehrfache
   * Aufrufe sind also harmlos; `vorgeladen` spart nur den Leerlauf.
   */
  function vorladen() {
    if (vorgeladen || zustand() !== 'aus') { vorgeladen = true; return; }
    const feld = document.querySelector('.hextra-search-input');
    if (!feld) return;
    vorgeladen = true;
    feld.dispatchEvent(new Event('focus'));
  }

  /* ------------------------------------------------------------- Ladeanzeige */

  /**
   * Die Liste, in die das Theme gerade schreibt. `flexsearch.js` nimmt dafür
   * die einzige sichtbare `.hextra-search-wrapper` (`getActiveSearchElement`),
   * nicht die Hülle des getippten Feldes — Navbar- und Sidebar-Feld existieren
   * beide im DOM, je nach Breite ist nur eines eingeblendet. Wer hier von
   * `feld.closest(…)` ausgeht, schreibt die Ladezeile in die unsichtbare Liste
   * und lässt die Leermeldung in der sichtbaren stehen.
   */
  function aktiveListe(feld) {
    const sichtbar = Array.from(document.querySelectorAll('.hextra-search-wrapper'))
      .filter(el => el.clientHeight > 0);
    const huelle = sichtbar.length === 1 ? sichtbar[0] : feld.closest('.hextra-search-wrapper');
    return huelle ? huelle.querySelector('.hextra-search-results') : null;
  }

  function statusSetzen(huelle, text) {
    const status = huelle && huelle.querySelector('.hextra-search-status');
    if (status) status.textContent = text;
  }

  function anzeigeEntfernen(liste) {
    liste.querySelectorAll('[data-gl-laden]').forEach(n => n.remove());
  }

  /**
   * Hängt die Ladezeile zuoberst in die Liste — hinter einen etwaigen
   * Sprungeintrag, der schon trägt und deshalb die erste Zeile bleibt.
   */
  function anzeigeSetzen(liste, gescheitert) {
    anzeigeEntfernen(liste);

    const leer = liste.querySelector('.hextra-search-no-result');
    if (leer) leer.remove();

    const zeile = document.createElement('div');
    zeile.className = 'gl-suche-laden' + (gescheitert ? ' gl-suche-laden-fehler' : '');
    zeile.dataset.glLaden = '1';

    if (!gescheitert) {
      const rad = document.createElement('span');
      rad.className = 'gl-suche-spinner';
      rad.setAttribute('aria-hidden', 'true');
      zeile.appendChild(rad);
    }

    const text = document.createElement('span');
    const sprung = liste.querySelector('[data-gl-sprung]');
    text.textContent = gescheitert
      ? 'Der Volltextindex konnte nicht geladen werden.'
      : (sprung
        ? 'Volltextindex wird geladen — der Direktsprung oben trägt schon jetzt.'
        : 'Volltextindex wird geladen — die Trefferliste erscheint, sobald er da ist.');
    zeile.appendChild(text);

    /* Die Ladezeile trägt kein `data-index`: Pfeiltasten und Enter des Themes
       lesen nur solche Knoten und greifen daher weiter auf den Sprungeintrag
       bzw. auf gar nichts — nicht auf diesen Hinweis. */
    const erster = liste.querySelector('li, .hextra-search-prefix');
    if (erster) liste.insertBefore(zeile, erster);
    else liste.appendChild(zeile);

    liste.classList.remove('hx:hidden');
    statusSetzen(liste.closest('.hextra-search-wrapper'), text.textContent);
  }

  /* -------------------------------------------------------------- Nachziehen */

  /**
   * Wartet auf den fertigen Index und lässt das Theme dann erneut suchen. Das
   * erneute `keyup` durchläuft dieselbe Kette wie ein Tastendruck: Theme baut
   * die Trefferliste, `artikel-sprung.js` setzt den Sprungeintrag davor,
   * dieses Skript räumt die Ladezeile ab.
   */
  function nachziehen(feld) {
    if (poller) return;
    const start = Date.now();
    let gemeldet = false;

    poller = setInterval(function () {
      const alter = Date.now() - start;
      const liste = aktiveListe(feld);

      if (zustand() !== 'bereit') {
        /* Lange unterwegs: Meldung wechseln, Poller weiterlaufen lassen — ein
           nachträglich eintreffender Index soll die Liste noch füllen. */
        if (alter > GEDULD_MS && !gemeldet && liste && feld.value) {
          gemeldet = true;
          anzeigeSetzen(liste, true);
        }
        if (alter > STILLE_MS) { clearInterval(poller); poller = null; }
        return;
      }

      clearInterval(poller);
      poller = null;
      if (!liste) return;
      if (!feld.value) { anzeigeEntfernen(liste); return; }

      feld.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
    }, TAKT_MS);
  }

  function pruefen(feld) {
    const liste = aktiveListe(feld);
    if (!liste) return;

    if (!feld.value) { anzeigeEntfernen(liste); return; }

    if (zustand() === 'bereit') { anzeigeEntfernen(liste); return; }

    /* Getippt, bevor das Vorladen griff (Tastaturkürzel, Autofokus): den
       Aufbau jetzt anstossen, sonst wartet die Anzeige auf nichts. */
    vorladen();
    anzeigeSetzen(liste, false);
    nachziehen(feld);
  }

  /* ----------------------------------------------------------------- Bindung */

  document.addEventListener('DOMContentLoaded', function () {
    const felder = document.querySelectorAll('.hextra-search-input');
    if (!felder.length) return;

    document.querySelectorAll('.hextra-search-wrapper').forEach(huelle => {
      huelle.addEventListener('pointerenter', vorladen, { once: true });
      huelle.addEventListener('touchstart', vorladen, { once: true, passive: true });
    });

    felder.forEach(feld => {
      feld.addEventListener('keyup', () => pruefen(feld));
      feld.addEventListener('input', () => pruefen(feld));
    });

    /* Auf /kommentar/ ist die Suche der Zweck der Seite — dort den Index in der
       Leerlaufzeit nach `load` holen, damit das erste Wort sofort trifft. Erst
       nach `load` und mit Nachlauf, damit er sich nicht vor den 15-KB-Sprung-
       index von `artikel-sprung.js` drängt. */
    if (!document.querySelector('.gl-suche .hextra-search-input')) return;
    if (!leitungTraegt()) return;

    const spaeter = () => {
      if (window.requestIdleCallback) requestIdleCallback(vorladen, { timeout: 4000 });
      else setTimeout(vorladen, 1500);
    };
    if (document.readyState === 'complete') setTimeout(spaeter, 800);
    else window.addEventListener('load', () => setTimeout(spaeter, 800), { once: true });
  });
})();
