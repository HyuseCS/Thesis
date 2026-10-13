---
name: handoff
description: Write the session handoff to .claude/handoff.md so the next session starts where this one stopped. Run at the end of a session or when the user says they are done.
---

# /handoff

## In the main session

The `handoff` agent cannot see this conversation. Collect these from this session's work, in plain
short sentences, and spawn the `handoff` agent with them:

- Goal: what this stretch of work is for.
- Where we are: the files and sections in progress (for example `outputs/hojaji-2026.md §3`).
- Decisions made, each with its why.
- Open questions, each with who decides.
- Blockers, or "none".
- Next step: the exact next action, with the command or file.

When the agent returns, reply with the next step in one line.

## In the `handoff` agent

Write `<project>/.claude/handoff.md`. Keep the facts block between `<!-- handoff-facts:start -->`
and `<!-- handoff-facts:end -->` if one exists (a hook maintains it). Replace everything above it.

Use only the notes you were given. Check that each file path you write exists. Follow `AGENTS.md`
for any claim about a paper: keep the citation key and the location cite (`Sec. 3.4`, `Fig. 3`).

```markdown
# Handoff — <YYYY-MM-DD HH:MM>

## Goal
<what this stretch of work is for>

## Where we are
<files and sections in progress>

## Decisions made
- D1. <decision> (<why>)

## Open questions
- Q1. <question> (<who decides>)

## Blockers
- <blocker or "none">

## Next step
<the exact next action, with the command or file>
```

Then make sure `<project>/.gitignore` has `.claude/handoff.md`. Report the next step in one line.
