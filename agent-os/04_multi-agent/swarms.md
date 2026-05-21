# Swarms

## Definition

A **swarm** is a peer-oriented multi-agent topology where named in-process teammates communicate via SendMessage while running concurrently under shared team context.

## Key Ideas

- Agent tool fields: `name`, `team_name`, `mode` for addressable teammates.
- `in_process_teammate` task type with prefix `t`.
- Teammate spawn path when team_name + name both set.
- Parallel agent execution gated by swarm feature flags.

## Architecture Implications

- SendMessage routes to pendingMessages inbox on target task.
- Differs from coordinator: peers vs manager-worker hierarchy.
- Feature-gated schema and agent list attachments preserve prompt cache.

## Production Implications

- Naming collisions avoided by agent name registry in AppState.
- Concurrent teammates multiply API cost — budget at team level.
- Worktree isolation recommended for parallel writes to same repo.

## Related Concepts

- [[coordination]]
- [[subagents]]
- [[synchronization]]

## Sources

- `Books/claude/ch08-sub-agents.md`
- `Books/claude/ch10-coordination.md`

## My Notes

