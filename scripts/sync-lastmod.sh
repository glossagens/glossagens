#!/usr/bin/env bash
# sync-lastmod.sh — Setzt lastmod in Frontmatter auf das Datum des letzten Git-Commits der Datei
# Aufruf: ./scripts/sync-lastmod.sh [datei_oder_verzeichnis...]
# Ohne Argumente: alle .md unter content/kommentar/

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

TARGETS=("${@:-content/kommentar/}")
CHANGED=0

sync_file() {
  local file="$1"
  local git_date
  git_date=$(git log -1 --format="%cs" -- "$file" 2>/dev/null) || return 0
  [[ -z "$git_date" ]] && return 0

  local current_lastmod
  current_lastmod=$(awk '/^lastmod:/ { gsub(/[":]/, "", $2); print $2; exit }' "$file") || true

  if [[ "$current_lastmod" == "$git_date" ]]; then
    return 0
  fi

  # Update lastmod in frontmatter using awk for reliability
  awk -v newdate="$git_date" '
    /^lastmod:/ { print "lastmod: \"" newdate "\""; next }
    { print }
  ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"

  CHANGED=$((CHANGED + 1))
  echo "  $file: ${current_lastmod:-<none>} → $git_date"
}

echo "Syncing lastmod from git history..."
while IFS= read -r f; do
  sync_file "$f"
done < <(find "${TARGETS[@]}" -name "*.md" -type f)

echo "Done. $CHANGED file(s) updated."