---
# Neues Thema: hugo new themen/{slug}/_index.md   (Verzeichnisname = stabiler Slug)
title: "{{ replace .File.Dir "themen/" "" | replaceRE "/$" "" | replaceRE "-" " " | title }}"
date: {{ now.Format "2006-01-02" }}
lastmod: {{ now.Format "2006-01-02" }}
description: ""
tags: []
# grundlage | institution | verfahren | rechtsfolgen | kantonsvergleich (data/themen/typen.yaml)
typ: ""
# Das Wichtigste in Kürze, 2–3 Sätze. bger-update entscheidet daraus, ob das Thema zu einem Urteil passt.
kurz: ""
# Schlüssel aus data/sachgebiete/ (bger.yaml, eigene.yaml), so genau wie möglich — Untergebiet vor Sachgebiet.
sachgebiete: []
# Die ausgelegten Normen; art dreistellig wie das Verzeichnis (art-007, art-336c).
normen:
  # - { gesetz: or, art: art-336c }
# Für Themen ohne passendes BGer-Sachgebiet (Methodik): Begriffe, über die bger-update das Thema findet.
stichworte: []
agent_verified: false
revisions:
  - date: {{ now.Format "2006-01-02" }}
    by: ""
    model: ""
    mcp_verified: false
    note: "Erstfassung"
---

<!-- Jede ##/###-Überschrift mit festem Anker {#id}: bger-update verlinkt darauf. -->

## Überblick {#ueberblick}
