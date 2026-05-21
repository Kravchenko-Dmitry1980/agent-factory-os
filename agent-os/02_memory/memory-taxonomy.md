# Memory Taxonomy

## Definition

The **memory taxonomy** defines exactly four memory types — user, feedback, project, reference — acting as both category and filter for what the agent may persist across sessions.

## Key Ideas

| Type | Stores |
|------|--------|
| user | Role, goals, expertise, preferences |
| feedback | How to work; corrections and confirmations |
| project | Ongoing context, deadlines, who-is-doing-what |
| reference | Pointers to external systems (URLs, dashboards) |

- Criterion: **not derivable** from current project state or codebase.
- Explicit exclusions: code patterns, git history, CLAUDE.md content, ephemeral tasks.

## Architecture Implications

- Frontmatter `type` field required on every memory file.
- Model instructed to push back on save requests for derivable data.
- Naming convention: `<type>_<topic>.md` (semantic, not enforced in code).

## Production Implications

- Taxonomy validated by evals (0/2 → 3/3 with exclusion-override instruction).
- Without taxonomy, eager model saves everything → stale parallel codebase.
- Description field quality determines recall precision.

## Related Concepts

- [[semantic-memory]]
- [[episodic-memory]]
- [[long-term-memory]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

