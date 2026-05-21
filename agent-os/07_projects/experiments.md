# Experiments

## Definition

The **experiments** project area tracks exploratory agent implementations — feature flags, GrowthBook A/B paths, fork subagents, and prototype harness changes not yet promoted to patterns.

## Key Ideas

- Claude Code uses compile-time `feature()` and runtime GrowthBook experiments.
- Fork subagent experiment: async-only spawns, recursive guard, cache-identical tool defs.
- Experiments isolated by flags — dead code elimination strips unused paths from binary.

## Architecture Implications

- Experiment results feed [[08_patterns]] or [[09_antipatterns]] after validation.
- Keep experiment notes separate from stable concept notes.
- Document flag name, hypothesis, and fleet impact (e.g., cache_creation %).

## Production Implications

- Stale runtime experiments (`CACHED_MAY_BE_STALE`) require session-stable handling.
- Promote to pattern only after production evidence (comments cite incident tickets).

## Related Concepts

- [[adaptive-harness]]
- [[subagents]]
- [[claude-code-architecture]]

## Sources

- `Books/claude/ch08-sub-agents.md` — feature gating
- `Books/claude/ch01-architecture.md` — build system feature flags

## My Notes

