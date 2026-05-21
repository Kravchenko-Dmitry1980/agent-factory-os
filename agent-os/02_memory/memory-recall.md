# Memory Recall

## Definition

**Memory recall** is the on-demand selection of relevant memory files for injection into context — via LLM-powered relevance query against frontmatter descriptions, complementing the always-loaded index.

## Key Ideas

- `MEMORY.md` loaded at session start for orientation.
- Sonnet side-query selects up to 5 memories per turn by description match.
- Body loaded only after selection — scan phase reads frontmatter only.
- CLAUDE.md (project) separate from MEMORY.md (user/project observations).

## Architecture Implications

- LLM selector replaces vector similarity — nuance over embedding distance.
- Project-level CLAUDE.md injected via context builder, cached in bootstrap state.
- Memory injection timing coordinated with system prompt dynamic section.

## Production Implications

- Loading all memories exhausts token budget — tiered recall mandatory at scale.
- Bad frontmatter descriptions waste tokens or miss critical rules.
- Relevance query adds latency/cost per turn — bounded by top-K limit.

## Related Concepts

- [[long-term-memory]]
- [[semantic-memory]]
- [[api-layer]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

