# Subagent Tool Restrictions

## Definition

**Subagent tool restrictions** are explicit blocklists and scoped toolsets applied to child agent instances — preventing recursive delegation, memory corruption, and gateway side effects from isolated workers.

## Why It Matters

Subagents run with fresh context and summary-only return. Unrestricted tools let children mutate global state the parent cannot observe, causing silent corruption and unbounded delegation depth.

## Architecture Implications

Typical blocklist categories (conceptual — adapt per harness):

| Restricted capability | Reason |
|----------------------|--------|
| Recursive delegation | Depth and cost explosion |
| Memory writes | Task ephemera pollutes user model |
| Clarification / ask-user | Child must work from passed context |
| Outbound messaging / gateway | Side effects invisible to parent |
| Profile-scoped stores | Writes belong to primary context only |

- Parent must pass complete context in delegation payload — restriction does not compensate for empty context.
- Parallel child limit is a separate concurrency guard from tool blocklist.
- Align with [[memory-provider-boundaries]] agent-context tagging (non-primary skips writes).

## Production Implications

- Audit subagent tool pools per agent definition template.
- Log blocked tool attempts for security review.
- Bubble / headless permission modes mandatory for unattended children.

## Risks

- Over-restriction blocks legitimate isolated research tasks.
- Under-restriction → memory and messaging corruption.

## Related Concepts

- [[subagents]]
- [[kanban-vs-delegate]]
- [[profile-isolation]]
- [[memory-provider-boundaries]]
- [[fail-closed-agent-loop]]
- [[permission-modes]]

## Related Anti-patterns

- [[recursive-self-improvement]]

## Related Patterns

- [[fail-closed-agent-loop]]
- [[memory-aware-execution]]

## Upstream Sources

- `experiments/hermes-agent-review/multi-agent/SUBAGENTS.md`
- `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §4, §9
- `Books/claude/ch08-sub-agents.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.8
- `governance/PROMOTION_LOG.md`

## Semantic Cluster

orchestration

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Extends subagents.md with explicit safety boundaries; no framework-specific blocklist code.
governance_reference: PROMOTION_REVIEW.md §3.8, governance/PROMOTION_STRATEGY.md
```
