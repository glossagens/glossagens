#!/usr/bin/env bash
#
# Lokaler Build-Check: baut die Seite genau so, wie es der GitHub-Runner tut.
#
# Hintergrund: Am 11.08.2026 brach der Deploy sieben Commits lang ab, weil ein
# Template-Ausdruck (`ge $c "0"` in kommentar/articles.html) unter Hugo 0.147.4
# anders auswertet als unter der lokal installierten 0.161.1. Lokal grün, in CI
# rot — der Fehler war nur zu sehen, wenn beide Seiten dieselbe Hugo-Version
# verwenden. Deshalb steht die Version in `.hugo-version`; deploy.yml liest
# dieselbe Datei.
#
# Aufruf: scripts/build-check.sh   (oder automatisch via .githooks/pre-push)

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

# ---------------------------------------------------------------------------
# Submodul-Abgleich
#
# Der Build unten verwendet den lokal ausgecheckten Submodul-Stand; der Runner
# checkt den im Parent-Repo aufgezeichneten Commit aus (deploy.yml:
# submodules: recursive). Laufen die auseinander, baut die CI ein anderes Theme
# als der Check hier — lokal grün, in CI rot.
#
# Am 17.08.2026 genau so passiert: aufgezeichnet war hextra c9feec7, ausgecheckt
# 38d18a5. Der Projekt-Override layouts/_partials/toc.html ruft
# `utils/headings.html` auf, das es erst ab dem neueren Stand gibt — drei
# Deploys in Folge rot, während der lokale Build durchlief.
# ---------------------------------------------------------------------------
if [ -f .gitmodules ]; then
  # `git submodule status` stellt Abweichern ein '+' voran, nicht-initialisierten
  # Submodulen ein '-'. Beides heisst: CI baut etwas anderes als wir hier.
  abweichend="$(git submodule status --recursive | grep '^[+-]' || true)"
  if [ -n "$abweichend" ]; then
    cat >&2 <<EOF

  ✗ Submodul weicht vom aufgezeichneten Stand ab — Push abgebrochen.

$(printf '      %s\n' "$abweichend")

      '+' = anderer Commit ausgecheckt als im Parent-Repo aufgezeichnet
      '-' = nicht initialisiert

      Die CI checkt den aufgezeichneten Commit aus. Der Build unten würde
      deshalb etwas anderes prüfen, als der Runner baut.

      Beheben — den ausgecheckten Stand aufzeichnen:
          git add <submodul-pfad> && git commit
      oder den aufgezeichneten Stand herstellen:
          git submodule update --init --recursive

      Ausnahmsweise überspringen: git push --no-verify

EOF
    exit 1
  fi

  # Unversionierte Änderungen im Submodul erreichen die CI nie — sie sind kein
  # Abbruchgrund (Theme-Anpassungen gehören ohnehin nach layouts/), können aber
  # denselben Fehler verdecken.
  if [ -n "$(git submodule foreach --quiet --recursive 'git status --porcelain')" ]; then
    cat >&2 <<'EOF'

  ⚠️  Unversionierte Änderungen in einem Submodul
      Diese Dateien existieren nur lokal — die CI baut ohne sie.
      Theme-Anpassungen gehören ins Projekt (layouts/ überschreibt themes/).

EOF
  fi
fi

soll="$(tr -d '[:space:]' < .hugo-version)"
ist="$(hugo version | sed -n 's/^hugo v\([0-9.]*\).*/\1/p')"

if [ "$ist" != "$soll" ]; then
  cat >&2 <<EOF

  ⚠️  Hugo-Version weicht von der CI ab
      lokal: ${ist:-unbekannt}      .hugo-version / GitHub Actions: $soll

      Der Build unten prüft dann nicht dasselbe, was der Runner baut —
      versionsabhängige Template-Fehler können durchrutschen.
      Angleichen: passende Hugo-Version installieren, oder .hugo-version
      auf $ist setzen (CI zieht automatisch nach).

EOF
fi

ziel="$(mktemp -d)"
trap 'rm -rf "$ziel"' EXIT

echo "→ hugo --minify (Version $ist)"
if ! hugo --minify --destination "$ziel"; then
  cat >&2 <<'EOF'

  ✗ Build fehlgeschlagen — Push abgebrochen.
    Fehler oben beheben und erneut pushen.
    Ausnahmsweise überspringen: git push --no-verify

EOF
  exit 1
fi

echo "✓ Build ok"
