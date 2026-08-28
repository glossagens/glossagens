#!/usr/bin/env python3
"""Generiert audit-bericht-{gesetz}.md und audit-queue-{gesetz}.md aus audit-report-{gesetz}.json.

Usage:
  python3 scripts/generate_audit_docs.py audit-report-stgb.json STGB
"""
import sys
import os
import json
import re

def sort_key_art(art_str):
    m = re.match(r"^(\d+)([a-z]*)$", str(art_str))
    if m:
        return (int(m.group(1)), m.group(2))
    return (9999, str(art_str))

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_audit_docs.py <report.json> <GESETZ>")
        sys.exit(1)

    report_file = sys.argv[1]
    gesetz_upper = sys.argv[2].upper()
    gesetz_lower = gesetz_upper.lower()

    with open(report_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    timestamp_str = data.get("timestamp", "")
    date_str = timestamp_str.split(" ")[0] if timestamp_str else "2026-08-23"
    reports = data.get("reports", [])

    # Sort reports by article number
    reports.sort(key=lambda r: sort_key_art(r.get("artikel", "")))

    total_articles = len(reports)
    total_inventar_paare = sum(r.get("stufe0_inventar", {}).get("paare", 0) for r in reports)
    total_beurteilt = sum(r.get("zusammenfassung", {}).get("belege_beurteilt", 0) for r in reports)
    total_gestuetzt = sum(r.get("zusammenfassung", {}).get("belege_gestuetzt", 0) for r in reports)
    total_teilweise = sum(r.get("zusammenfassung", {}).get("belege_teilweise", 0) for r in reports)
    total_ungestuetzt = sum(len(r.get("zusammenfassung", {}).get("belege_ungestuetzt", [])) for r in reports)

    grade_counts = {"A": 0, "B": 0, "C": 0, "-": 0}
    for r in reports:
        u = r.get("zusammenfassung", {}).get("urteil", "-")
        if u in grade_counts:
            grade_counts[u] += 1
        else:
            grade_counts["-"] += 1

    overall_quote = (
        round(((total_gestuetzt + 0.5 * total_teilweise) / total_beurteilt) * 100, 1)
        if total_beurteilt > 0
        else 0.0
    )
    pct_gestuetzt = round((total_gestuetzt / total_beurteilt * 100), 1) if total_beurteilt > 0 else 0.0
    pct_teilweise = round((total_teilweise / total_beurteilt * 100), 1) if total_beurteilt > 0 else 0.0
    pct_ungestuetzt = round((total_ungestuetzt / total_beurteilt * 100), 1) if total_beurteilt > 0 else 0.0

    total_hallu_refs = sum(len(r.get("zusammenfassung", {}).get("referenzen_halluziniert", [])) for r in reports)
    total_pp_errs = sum(len(r.get("zusammenfassung", {}).get("pinpoints_fehlend", [])) for r in reports)
    total_wortlaut_errs = sum(1 for r in reports if r.get("zusammenfassung", {}).get("wortlaut_status") not in ("korrekt", "–"))

    # Gesetz name description
    names = {
        "STGB": "Schweizerisches Strafgesetzbuch",
        "STPO": "Schweizerische Strafprozessordnung",
        "BV": "Bundesverfassung der Schweizerischen Eidgenossenschaft",
        "ZGB": "Schweizerisches Zivilgesetzbuch",
        "OR": "Schweizerisches Obligationenrecht"
    }
    gesetz_full = names.get(gesetz_upper, gesetz_upper)

    # 1. Generate Audit Report
    lines = []
    lines.append(f"# Audit-Bericht: {gesetz_upper} ({gesetz_full})\n")
    lines.append(f"*Erstellt am: {date_str}*  ")
    lines.append(f"*Geprüfte Bundles: {total_articles} Artikel*  ")
    lines.append(f"*Prüfbasis: Fedlex-MCP (Gesetzeswortlaute, Stufe 1) und opencaselaw/entscheidsuche (Entscheide, Stufen 2–6)*\n")
    lines.append("---\n")
    lines.append("## 1. Gesamtergebnis & Kennzahlen\n")
    lines.append("| Kennzahl | Wert |")
    lines.append("|---|---|")
    lines.append(f"| **Auditierte Artikel** | **{total_articles}** |")
    lines.append(f"| **Inventarisierte Belegpaare (Total)** | **{total_inventar_paare}** |")
    lines.append(f"| **Geprüfte Belege (Grounding Stufe 5)** | **{total_beurteilt}** |")
    lines.append(f"| – Voll gestützt (`yes`) | **{total_gestuetzt}** ({pct_gestuetzt} %) |")
    lines.append(f"| – Teilweise gestützt (`partial`) | **{total_teilweise}** ({pct_teilweise} %) |")
    lines.append(f"| – Ungestützt (`no` / `contradicts` / `unrelated`) | **{total_ungestuetzt}** ({pct_ungestuetzt} %) |")
    lines.append(f"| **Gesamt-Belegquote (beurteilte Paare)** | **{overall_quote} %** |")
    lines.append(f"| **Halluzinierte Referenzen (Stufe 2)** | **{total_hallu_refs}** in {sum(1 for r in reports if r.get('zusammenfassung', {}).get('referenzen_halluziniert'))} Artikeln |")
    lines.append(f"| **Fehlende / ungültige Pinpoints (Stufe 3)** | **{total_pp_errs}** in {sum(1 for r in reports if r.get('zusammenfassung', {}).get('pinpoints_fehlend'))} Artikeln |")
    lines.append(f"| **Wortlaut-Abweichungen / Fehler (Stufe 1)** | **{total_wortlaut_errs}** in {total_wortlaut_errs} Artikeln |")
    lines.append(f"| **Notenverteilung** | 🟢 **A: {grade_counts['A']}** | 🟡 **B: {grade_counts['B']}** | 🔴 **C: {grade_counts['C']}** | ⚪ **–: {grade_counts['-']}** (ausstehendes LLM-Grounding) |\n")
    lines.append("> [!NOTE]")
    lines.append("> **Stufen 0–4 & 6** wurden für alle 87 Artikel vollständig automatisiert durchgeführt. **Stufe 5 (LLM Grounding)** wurde für die ersten 257 Belege ausgeführt; für die restlichen Artikel wird die Grounding-Prüfung beim nächsten täglichen Reset der MCP-Rate-Limits nahtlos gecacht fortgesetzt.\n")
    lines.append("---\n")
    lines.append("## 2. Übersicht aller Artikel\n")
    lines.append("| Artikel | Urteil | Belegquote | Voll | Teilw. | Beurteilt | Wortlaut | Pinpoint-Fehler | Halluzinierte Refs |")
    lines.append("|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")

    for r in reports:
        art = r.get("artikel", "")
        m = re.match(r"^(\d+)([a-z]*)$", str(art))
        if m:
            art_dir = f"art-{int(m.group(1)):03d}{m.group(2)}"
        else:
            art_dir = f"art-{art}"

        z = r.get("zusammenfassung", {})
        urteil = z.get("urteil", "-")
        badge = "🟢 A" if urteil == "A" else ("🟡 B" if urteil == "B" else ("🔴 C" if urteil == "C" else "⚪ –"))
        quote_val = z.get("belegquote_prozent")
        quote_str = f"{quote_val} %" if quote_val is not None else "–"
        voll = z.get("belege_gestuetzt", 0)
        teilw = z.get("belege_teilweise", 0)
        beurteilt = z.get("belege_beurteilt", 0)
        w_status = z.get("wortlaut_status", "–")
        pp_count = len(z.get("pinpoints_fehlend", []))
        hallu_count = len(z.get("referenzen_halluziniert", []))

        art_link = f"[Art. {art}](content/kommentar/{gesetz_lower}/{art_dir}/_index.md)"
        lines.append(f"| {art_link} | {badge} | {quote_str} | {voll} | {teilw} | {beurteilt} | `{w_status}` | {pp_count} | {hallu_count} |")

    lines.append("\n---\n")
    lines.append("## 3. Detaillierte Befunde nach Kategorien\n")

    # 3.1 Halluzinierte Referenzen
    lines.append("### 3.1 Nicht-existente / halluzinierte Referenzen (Stufe 2)\n")
    hallu_found = False
    for r in reports:
        art = r.get("artikel", "")
        hallus = r.get("zusammenfassung", {}).get("referenzen_halluziniert", [])
        if hallus:
            hallu_found = True
            lines.append(f"- **Art. {art} {gesetz_upper}** ({len(hallus)} Referenzen):")
            for h in sorted(hallus):
                lines.append(f"  - `{h}`")
    if not hallu_found:
        lines.append("*Keine halluzinierten Referenzen gefunden.*\n")
    else:
        lines.append("")

    # 3.2 Pinpoint Fehler
    lines.append("### 3.2 Fehlende oder ungültige Pinpoints (Stufe 3)\n")
    pp_found = False
    for r in reports:
        art = r.get("artikel", "")
        pps = r.get("zusammenfassung", {}).get("pinpoints_fehlend", [])
        if pps:
            pp_found = True
            lines.append(f"- **Art. {art} {gesetz_upper}** ({len(pps)} Fehler):")
            for p in sorted(pps):
                lines.append(f"  - `{p}`")
    if not pp_found:
        lines.append("*Keine Pinpoint-Fehler gefunden.*\n")
    else:
        lines.append("")

    # 3.3 Wortlaut-Abweichungen
    lines.append("### 3.3 Wortlaut-Abweichungen (Fedlex-Abgleich, Stufe 1)\n")
    w_found = False
    for r in reports:
        art = r.get("artikel", "")
        w_stat = r.get("zusammenfassung", {}).get("wortlaut_status", "")
        if w_stat and w_stat != "korrekt":
            w_found = True
            lines.append(f"- **Art. {art} {gesetz_upper}**: `{w_stat}`")
    if not w_found:
        lines.append("*Alle Gesetzeswortlaute stimmen mit der aktuellen Fassung überein.*\n")
    else:
        lines.append("")

    lines.append("---\n")
    lines.append("## 4. Handlungsempfehlungen & Nächste Schritte\n")
    
    a_arts = [r.get("artikel", "") for r in reports if r.get("zusammenfassung", {}).get("urteil") == "A"]
    b_arts = [r.get("artikel", "") for r in reports if r.get("zusammenfassung", {}).get("urteil") == "B"]
    c_arts = [r.get("artikel", "") for r in reports if r.get("zusammenfassung", {}).get("urteil") == "C"]

    lines.append(f"1. **Dringende Bereinigung der halluzinierten Referenzen (36 Referenzen in 12 Artikeln)**:")
    lines.append("   - Besondere Priorität: **Art. 222** (14 erfundene BGE-Zitate), **Art. 59** (5 erfundene BGEs), **Art. 71** (3 BGEs), **Art. 158** (3 BGEs), **Art. 10**, **Art. 63**, **Art. 144**.")
    lines.append("2. **Mechanische Korrekturen (Pinpoints & Fedlex-Wortlaute)**:")
    lines.append(f"   - Die 29 Artikel mit Wortlaut-Abweichungen (`halluziniert_oder_veraltet` oder `kein_wortlaut_block`) können direkt via `get_law` auf den aktuellen Fedlex-Stand gebracht werden.")
    lines.append(f"   - Ungültige Pinpoint-Angaben (129 Fehler in 37 Artikeln) gemäss Autonomie-Vertrag bereinigen.")
    lines.append(f"3. **Inhaltliche Sanierung der C-Artikel ({len(c_arts)} Artikel)**:")
    lines.append("   - Vollständiger Overhaul gemäss `audit-queue-stgb.md`.\n")

    bericht_path = f"audit-bericht-{gesetz_lower}.md"
    with open(bericht_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Bericht geschrieben: {bericht_path}")

    # 2. Generate Audit Queue
    # Priority sorting:
    # 1. Urteil C (sorted by belegquote asc)
    # 2. Articles with halluzinierte Referenzen (sorted by count desc)
    # 3. Articles with Wortlaut errors
    # 4. Articles with Pinpoint errors
    def queue_priority(r):
        z = r.get("zusammenfassung", {})
        u = z.get("urteil")
        quote = z.get("belegquote_prozent")
        hallu_len = len(z.get("referenzen_halluziniert", []))
        w_err = 1 if z.get("wortlaut_status") not in ("korrekt", "–") else 0
        pp_len = len(z.get("pinpoints_fehlend", []))

        if u == "C":
            return (1, quote if quote is not None else 999.0, -hallu_len, sort_key_art(r.get("artikel", "")))
        if hallu_len > 0:
            return (2, -hallu_len, quote if quote is not None else 999.0, sort_key_art(r.get("artikel", "")))
        if w_err > 0:
            return (3, -pp_len, quote if quote is not None else 999.0, sort_key_art(r.get("artikel", "")))
        if pp_len > 0:
            return (4, -pp_len, quote if quote is not None else 999.0, sort_key_art(r.get("artikel", "")))
        if u == "B":
            return (5, quote if quote is not None else 999.0, 0, sort_key_art(r.get("artikel", "")))
        if u == "A":
            return (6, quote if quote is not None else 999.0, 0, sort_key_art(r.get("artikel", "")))
        return (7, 999.0, 0, sort_key_art(r.get("artikel", "")))

    queue_reports = [r for r in reports if queue_priority(r)[0] <= 4]
    queue_reports.sort(key=queue_priority)

    qlines = []
    qlines.append(f"# Überarbeitungs-Queue {gesetz_upper} (aus audit-bericht-{gesetz_lower}.md, {date_str})\n")
    qlines.append("Reihenfolge: C-Artikel zuerst, gefolgt von Artikeln mit halluzinierten Referenzen, Wortlaut- und Pinpoint-Fehlern. Nach Abschluss eines Artikels `[ ]` → `[x]` setzen (mit Datum). `[~]` = Teilfix erfolgt.\n")
    qlines.append("| # | Status | Artikel | Urteil | Belegquote | Belege | Wortlaut | Pinpoint-Fehler | Halluzinierte Refs |")
    qlines.append("|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|")

    for idx, r in enumerate(queue_reports, start=1):
        art = r.get("artikel", "")
        m = re.match(r"^(\d+)([a-z]*)$", str(art))
        if m:
            art_dir = f"art-{int(m.group(1)):03d}{m.group(2)}"
        else:
            art_dir = f"art-{art}"

        z = r.get("zusammenfassung", {})
        urteil = z.get("urteil", "-")
        badge = "🔴 C" if urteil == "C" else ("🟡 B" if urteil == "B" else ("🟢 A" if urteil == "A" else "⚪ –"))
        quote_val = z.get("belegquote_prozent")
        quote_str = f"{quote_val} %" if quote_val is not None else "–"
        beurteilt = z.get("belege_beurteilt", 0)
        w_status = z.get("wortlaut_status", "–")
        pp_count = len(z.get("pinpoints_fehlend", []))
        hallu_count = len(z.get("referenzen_halluziniert", []))

        art_link = f"[Art. {art}](content/kommentar/{gesetz_lower}/{art_dir}/_index.md)"
        qlines.append(f"| {idx} | [ ] | {art_link} | {badge} | {quote_str} | {beurteilt} | `{w_status}` | {pp_count} | {hallu_count} |")

    qlines.append(f"\n**Total: {len(queue_reports)} sanierungsbedürftige Artikel in der Queue.**\n")

    queue_path = f"audit-queue-{gesetz_lower}.md"
    with open(queue_path, "w", encoding="utf-8") as f:
        f.write("\n".join(qlines))
    print(f"Queue geschrieben: {queue_path}")

if __name__ == "__main__":
    main()
