#!/usr/bin/env bash
# post-commit hook: Synchronisiert lastmod in Frontmatter mit Git-Commit-Datum
# Nur auf .md-Dateien angewendet, die im Commit geändert wurden

COMMIT_DATE=$(git log -1 --format="%cs")
STAGED_MD_FILES=$(git diff-tree --no-commit-id --name-only -r HEAD -- '*.md')

if [[ -z "$STAGED_MD_FILES" ]]; then
  exit 0
fi

CHANGED=0
for file in $STAGED_MD_FILES; do
  # Nur Dateien unter content/kommentar/ bearbeiten
  [[ "$file" != content/kommentar/* ]] && continue
  [[ ! -f "$file" ]] && continue

  # Hole das Datum des letzten Commits, das diese Datei geändert hat
  FILE_DATE=$(git log -1 --format="%cs" -- "$file")

  # Aktualisiere lastmod im Frontmatter
  if grep -q '^lastmod:' "$file"; then
    CURRENT=$(awk '/^lastmod:/ { gsub(/[":]/, "", $2); print $2; exit }' "$file")
    if [[ "$CURRENT" != "$FILE_DATE" ]]; then
      awk -v newdate="$FILE_DATE" '/^lastmod:/ { print "lastmod: \"" newdate "\""; next } { print }' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
      CHANGED=$((CHANGED + 1))
    fi
  elif grep -q '^date:' "$file"; then
    awk -v newdate="$FILE_DATE" '/^date:/ { print; print "lastmod: \"" newdate "\""; next } { print }' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    CHANGED=$((CHANGED + 1))
  fi
done

if [[ $CHANGED -gt 0 ]]; then
  git add -A
  git commit --amend --no-edit --no-verify
fi