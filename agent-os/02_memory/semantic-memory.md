# Semantic Memory

## Definition

**Semantic memory** stores stable factual knowledge about users, projects, and references — meanings and constraints that persist across sessions and guide behavior without re-derivation each turn.

## Key Ideas

- Types: **user** (role, expertise), **project** (ongoing work context), **reference** (external bookmarks).
- Frontmatter `description` field is the relevance signal for LLM selector.
- Index entries in `MEMORY.md` capped ~150 chars — table of contents, not content dump.

## Architecture Implications

- `scanMemoryFiles()` reads first 30 lines for frontmatter only during recall scan.
- Absolute dates required in project memories ("Thursday" → ISO date).
- Team memory subdirectory with shared `MEMORY.md`.

## Production Implications

- Vague descriptions cause false positives/negatives in relevance selection.
- User can inspect `~/.claude/projects/<slug>/memory/` directly.
- Eval-validated pushback when user asks to save derivable lists.

## Related Concepts

- [[long-term-memory]]
- [[memory-taxonomy]]
- [[memory-recall]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

