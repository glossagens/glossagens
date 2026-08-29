/**
 * TOC Follow — hält den aktiven Gliederungspunkt in der Sichtbarkeit.
 *
 * Hextra hebt den aktuellen Abschnitt zwar hervor (js/core/toc-scroll.js setzt
 * `hextra-toc-active`), scrollt die TOC-Spalte aber nicht mit. Bei den langen
 * Kommentarartikeln — Art. 66a StGB hat 40 Überschriften — überläuft die Liste
 * die Spaltenhöhe, und die Hervorhebung liegt für die untere Hälfte des Textes
 * ausserhalb des sichtbaren Bereichs.
 *
 * Ergänzt wird deshalb nur das Nachführen: ein MutationObserver auf das
 * class-Attribut der TOC-Links; wandert die Markierung aus dem Sichtfenster des
 * Scroll-Containers, wird dieser (und nur dieser, nicht die Seite) nachgezogen.
 *
 * Liegt in assets/js/core/, weil scripts/core.html per
 * `resources.Match "js/core/*.js"` bündelt — Projekt- und Theme-Assets sind
 * dabei dieselbe Union.
 */
document.addEventListener("DOMContentLoaded", function () {
  const toc = document.querySelector(".hextra-toc");
  if (!toc) return;

  const container = toc.querySelector(".hextra-scrollbar");
  if (!container) return;

  // Kein Überlauf, kein Nachführen nötig.
  if (container.scrollHeight <= container.clientHeight + 1) return;

  if (!("MutationObserver" in window)) return;

  const margin = 48; // Sicherheitsabstand zu Ober- und Unterkante

  function follow(link) {
    const linkBox = link.getBoundingClientRect();
    const boxBox = container.getBoundingClientRect();

    const overTop = linkBox.top - (boxBox.top + margin);
    const overBottom = linkBox.bottom - (boxBox.bottom - margin);

    let delta = 0;
    if (overTop < 0) delta = overTop;
    else if (overBottom > 0) delta = overBottom;
    if (delta === 0) return;

    const smooth = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    container.scrollBy({ top: delta, behavior: smooth ? "smooth" : "auto" });
  }

  const observer = new MutationObserver(function (mutations) {
    for (const m of mutations) {
      const el = m.target;
      if (el.classList && el.classList.contains("hextra-toc-active")) {
        follow(el);
        return;
      }
    }
  });

  observer.observe(toc, {
    attributes: true,
    attributeFilter: ["class"],
    subtree: true,
  });
});
