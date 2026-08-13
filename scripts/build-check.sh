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
