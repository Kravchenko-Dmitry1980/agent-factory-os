# Memory Compaction

## Definition

**Memory compaction** is the consolidation of fragmented memory files and index entries — distinct from conversation context compaction but sharing the goal of bounded, efficient retained knowledge.

## Key Ideas

- Conversation compaction (snip, microcompact, auto-compact) shrinks **in-session** message history.
- Memory consolidation merges or prunes memory files when directory grows unwieldy.
- `.consolidate-lock` mtime tracks last consolidation timestamp.
- Both systems avoid unbounded growth without losing critical observations.

## Architecture Implications

- Memory consolidation triggered by heuristics/feature flags (KAIROS/proactive modules).
- Context compaction runs every loop iteration; memory consolidation is batch/offline.
- CLAUDE.md cache in bootstrap breaks circular dependency with auto-mode classifier.

## Production Implications

- Aggressive memory consolidation can lose nuance — taxonomy preserves structure.
- Context compaction circuit breaker prevents runaway API cost; memory lacks same risk profile.
- User can manually delete or edit consolidated files.

## Related Concepts

- [[context-compression]]
- [[long-term-memory]]
- [[memory-recall]]

## Sources

- `Books/claude/ch05-agent-loop.md`
- `Books/claude/ch11-memory.md`

## My Notes

