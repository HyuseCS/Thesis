#!/usr/bin/env bash
project="${CLAUDE_PROJECT_DIR:-$(pwd)}"
sr="$project/.claude/sr-opus-5.md"

if [ -f "$sr" ] && ! cmp -s "$sr" "$HOME/.claude/sr-opus-5.md"; then
  cat "$sr"
  echo
fi

if [ -f "$project/.claude/handoff.md" ]; then
  echo "# Session handoff"
  echo
  cat "$project/.claude/handoff.md"
fi
exit 0
