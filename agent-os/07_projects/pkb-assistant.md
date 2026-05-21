# PKB Assistant

## Definition

**PKB Assistant** (Personal Knowledge Base) is a project slot for an agent that maintains, retrieves, and connects atomic notes — aligned with Agent-OS structure and Obsidian/Cursor workflows.

## Key Ideas

- Maps directly to this repository's atomic note contract.
- Memory taxonomy + file-based storage over vector RAG for human editability.
- Future RAG: embed notes with stable section headers for chunk quality.

## Architecture Implications

- Read/write via file tools; index files as navigation graphs.
- Link extraction from `Related Concepts` wikilinks.
- Compaction = note merging/decomposition policies, not conversation snip.

## Production Implications

- Scale to 10K+ notes requires strict one-concept-per-file discipline.
- Git as version history for knowledge evolution.

## Related Concepts

- [[long-term-memory]]
- [[self-revision]]
- [[memory-taxonomy]]

## Sources

- Agent-OS project registry (placeholder)

## My Notes

