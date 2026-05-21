# Evolving Memory

## Definition

**Evolving memory** is the continuous update of an agent's cross-session knowledge through write, edit, consolidate, and recall cycles — treating memory as observations that change over time, not authoritative database state.

## Key Ideas

- Write: FileWrite + index update in MEMORY.md.
- Update: FileEdit existing memory; no internal versioning.
- Consolidation prunes/merges when directory grows.
- Recall: LLM selector surfaces relevant files per turn.

## Architecture Implications

- Memory competes with CLAUDE.md — project instructions vs user observations.
- Team symlink shared memory for org-level evolution.
- KAIROS daily logs as optional high-granularity episodic stream.

## Production Implications

- Files communicate epistemological status: notes, not gospel.
- User edits stale memory directly — twin reflects human correction.
- RAG-ready: atomic files with frontmatter map cleanly to future embedding pipelines.

## Related Concepts

- [[long-term-memory]]
- [[episodic-memory]]
- [[self-revision]]
- [[memory-compaction]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

