# Persistent Identity

## Definition

**Persistent identity** is a stable agent or user representation across sessions — session IDs, agent IDs, name registries, and memory scoping that survive process restarts and enable continuity.

## Key Ideas

- Bootstrap: sessionId, parentSessionId, agentId in ToolUseContext.
- Task IDs: prefixed random identifiers with typed prefixes.
- Named swarm agents registered in agentNameRegistry Map.
- Memory directory keyed by sanitized git root path.

## Architecture Implications

- Cost restore guarded by matching persisted sessionId on resume.
- Fork subagents inherit frozen parent system prompt for cache identity.
- Digital twin substrate requires identity keys for memory and skill binding.

## Production Implications

- Session resume/continue launch paths must rehydrate identity consistently.
- Collision-resistant IDs for disk output files (security against symlink attacks).
- Identity without memory is hollow — pair with long-term memory layer.

## Related Concepts

- [[evolving-memory]]
- [[agent-personas]]
- [[long-term-memory]]
- [[subagents]]

## Sources

- `Books/claude/ch03-state.md`
- `Books/claude/ch10-coordination.md`
- `Books/claude/ch11-memory.md`

## My Notes

