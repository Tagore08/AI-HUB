#!/usr/bin/env bash
set -euo pipefail

PRIVATE="/home/tag01/AI-HUB"
PUBLIC="/home/tag01/AI-HUB-PUBLIC"

[ -d "$PRIVATE/.git" ] || { echo "ERROR: $PRIVATE not a git repo"; exit 1; }
[ -d "$PUBLIC/.git" ]  || { echo "ERROR: $PUBLIC not a git repo"; exit 1; }

echo ">> Wiping public mirror (except .git)..."
find "$PUBLIC" -mindepth 1 -maxdepth 1 ! -name .git ! -name README.md -exec rm -rf {} +

echo ">> Copying safe files..."
for f in AGENTS.md START_HERE.md MAINTENANCE.md SECRETS_POLICY.md .gitignore; do
  [ -f "$PRIVATE/$f" ] && cp "$PRIVATE/$f" "$PUBLIC/"
done
for d in INSTRUCTIONS PROMPTS SCRIPTS; do
  [ -d "$PRIVATE/$d" ] && cp -r "$PRIVATE/$d" "$PUBLIC/"
done
mkdir -p "$PUBLIC/PROJECTS" "$PUBLIC/KNOWLEDGE"
[ -d "$PRIVATE/PROJECTS/TEMPLATES" ] && cp -r "$PRIVATE/PROJECTS/TEMPLATES" "$PUBLIC/PROJECTS/"
[ -f "$PRIVATE/KNOWLEDGE/README.md" ] && cp "$PRIVATE/KNOWLEDGE/README.md" "$PUBLIC/KNOWLEDGE/"
[ -f "$PRIVATE/PUBLIC_README.md" ] && cp "$PRIVATE/PUBLIC_README.md" "$PUBLIC/README.md"

echo ">> Safety scan for secrets..."
if grep -rIE "(api[_-]?key|password|secret|bearer)[[:space:]]*[:=][[:space:]]*['\"]?[A-Za-z0-9_/-]{16,}" "$PUBLIC" --exclude-dir=.git 2>/dev/null; then
  echo "!!! Possible secret found. Aborting."
  exit 2
fi

echo ">> Preview:"
cd "$PUBLIC"
git status --short

echo ""
read -r -p ">> Commit and push to public? [y/N] " ans
case "$ans" in
  y|Y) ;;
  *) echo ">> Aborted."; exit 0 ;;
esac

git add -A
git commit -m "publish $(date +%Y-%m-%d)" || echo ">> Nothing to commit."
git push
echo ">> Done. https://github.com/Tagore08/AI-HUB"
