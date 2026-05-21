# Long-Term Memory

## Definition

**Long-term memory** in agent systems is durable knowledge across sessions — stored as human-readable files, scoped per project, with LLM-powered relevance selection rather than vector RAG infrastructure.

## Key Ideas

- Files on disk (Markdown + YAML frontmatter), not vector DB — human-readable, editable, git-friendly.
- Scoped to git repository root; worktrees share canonical memory directory.
- Two tiers: `MEMORY.md` index always loaded; individual files on-demand (up to 5/turn).
- Model writes via standard FileWrite/FileEdit — no special memory API.

## Architecture Implications

- Four-type taxonomy filters what is worth remembering (user, feedback, project, reference).
- Excludes derivable info (code patterns, git history) to keep model grounded in codebase.
- Consolidation and team memory via symlinks and shared directories.

## Production Implications

- Zero infrastructure: works offline, no schema migrations.
- Stale memory corrected with editor or `rm` — user agency over agent knowledge.
- Wrong taxonomy → memory as crutch instead of reading live code.

## Related Concepts

- [[semantic-memory]]
- [[episodic-memory]]
- [[memory-recall]]
- [[memory-compaction]]
- [[evolving-memory]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

