#!/usr/bin/env bash
project="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$project" || exit 0

{
  block="<!-- handoff-facts:start -->
## Facts ($(date '+%Y-%m-%d %H:%M:%S %z'))
- Branch: $(git branch --show-current 2>/dev/null)

Last 5 commits:
\`\`\`
$(git log --oneline -5 2>/dev/null)
\`\`\`

Uncommitted files:
\`\`\`
$(git status --short 2>/dev/null)
\`\`\`
<!-- handoff-facts:end -->"

  file="$project/.claude/handoff.md"
  body=""
  [ -f "$file" ] && body=$(sed '/<!-- handoff-facts:start -->/,/<!-- handoff-facts:end -->/d' "$file")
  if [ -n "$body" ]; then
    printf '%s\n\n%s\n' "$body" "$block" > "$file.tmp"
  else
    printf '%s\n' "$block" > "$file.tmp"
  fi
  mv "$file.tmp" "$file"
} 2>/dev/null
exit 0
