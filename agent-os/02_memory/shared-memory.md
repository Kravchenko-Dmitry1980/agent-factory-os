# Shared Memory

## Definition

**Shared memory** is memory accessible across agents, sessions, or team members — via project-scoped directories, team subdirectories, symlinks, and git-committed memory files.

## Key Ideas

- Canonical git root determines shared memory path for all worktrees.
- Team subdirectory (`memory/team/`) for org-shared observations.
- CLAUDE.md in repo is project-shared instruction memory (distinct from user MEMORY).
- Symlinks enable shared team memory without duplication.

## Architecture Implications

- Per-project scoping prevents cross-repo leakage.
- Memory dir created before prompt build (`ensureMemoryDirExists`).
- Shared state in multi-agent: parent holds toolUseId; child writes to outputFile — not shared conversation by default.

## Production Implications

- Git-versioned team memory diffs cleanly in code review.
- Shared memory requires trust — malicious commit could poison agent behavior.
- Worktree isolation agents use separate filesystem copy; memory still shared at git root.

## Related Concepts

- [[long-term-memory]]
- [[subagents]]
- [[evolving-memory]]

## Sources

- `Books/claude/ch11-memory.md`
- `Books/claude/ch08-sub-agents.md` — worktree isolation

## My Notes

