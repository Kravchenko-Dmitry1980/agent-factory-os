# Role Systems

## Definition

**Role systems** assign specialized agent definitions — Explore, Plan, Verify, general-purpose, fork, custom frontmatter agents — each optimizing tool pool, model, permissions, and prompt for a workload shape.

## Key Ideas

- Built-in types: general-purpose, Explore (search), Plan (read-only analysis), Verify (adversarial).
- Custom agents via frontmatter definitions loaded at setup.
- `subagent_type` selects definition; model override optional.
- Feature flags gate which built-ins appear in active agent list.

## Architecture Implications

- Agent list in attachment not tool description — cache stability.
- Permission deny rules filter available agent types per session.
- Required MCP servers block spawn until connected (30s wait).

## Production Implications

- Wrong agent type wastes tokens (Opus for simple grep) or misses depth (Haiku for verify).
- Removing Explore/Plan A/B tested via GrowthBook without binary ship.
- User-defined agents version-controlled in project config.

## Related Concepts

- [[subagents]]
- [[planning]]
- [[verification]]
- [[agent-personas]]

## Sources

- `Books/claude/ch08-sub-agents.md`

## My Notes

