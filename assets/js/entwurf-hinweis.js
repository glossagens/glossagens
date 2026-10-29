/*
 * Balken «Entwurf hängig» auf Kommentar- und Themenseiten: Ändert ein offener
 * Pull Request diese Seite (auf einer Artikelseite auch ihre Unterseiten wie
 * rechtsprechung.md), verweist ein Balken unter dem Titel auf die
 * Entwurfsansicht. Die Liste kommt vom MCP-Worker (/entwuerfe.json, zwei
 * Minuten gecacht); eingebunden in layouts/_partials/custom/head-end.html.
 * Schlägt der Abruf fehl, bleibt die Seite wie sie ist.
 */
(function () {
  'use strict';
  var skript = document.currentScript;
  var worker = skript && skript.getAttribute('data-worker');
  if (!worker) return;

  var hier = decodeURIComponent(location.pathname).replace(/\/?$/, '/');

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function ziel() {
    var b = document.querySelector('.gl-entwurf-balken');
    if (b) return b;
    var h1 = document.querySelector('#content h1');
    if (!h1) return null;
    b = el('div', 'gl-entwurf-balken');
    h1.parentNode.insertBefore(b, h1.nextSibling);
    return b;
  }
  function zeige(treffer) {
    var b = ziel();
    if (!b) return;
    b.textContent = '';
    b.appendChild(el('strong', null, treffer.length === 1 ? 'Entwurf hängig' : treffer.length + ' Entwürfe hängig'));
    b.appendChild(el('span', null, ' — eine noch nicht geprüfte Änderung an dieser Seite liegt vor:'));
    var ul = el('ul');
    treffer.forEach(function (e) {
      var li = el('li');
      var a = el('a', null, 'Nr. ' + e.nr + ': ' + e.titel);
      a.href = '/entwurf/?pr=' + e.nr;
      li.appendChild(a);
      if (e.unterseite) li.appendChild(el('span', 'gl-entwurf-wo', ' (betrifft ' + e.unterseite + ')'));
      ul.appendChild(li);
    });
    b.appendChild(ul);
    b.hidden = false;
  }
  function start() {
    // Nur Artikelseiten eines Kommentars sammeln die Änderungen ihrer Unterseiten.
    var artikel = /^\/kommentar\/[^/]+\/[^/]+\/$/.test(hier);
    fetch(worker.replace(/\/$/, '') + '/entwuerfe.json')
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (d) {
        var treffer = [];
        (d.entwuerfe || []).forEach(function (e) {
          var seiten = e.seiten || [];
          if (seiten.indexOf(hier) >= 0) return treffer.push({ nr: e.nr, titel: e.titel });
          if (!artikel) return;
          var unter = seiten.filter(function (s) { return s.indexOf(hier) === 0; });
          if (unter.length) treffer.push({ nr: e.nr, titel: e.titel, unterseite: unter.map(function (s) {
            return s.slice(hier.length).replace(/\/$/, '');
          }).join(', ') });
        });
        if (treffer.length) zeige(treffer);
      })
      .catch(function () {});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
