# Kanban vs Delegate

## Definition

**Kanban vs delegate** is the decision framework for choosing between ephemeral parent-blocked delegation and durable queue-based orchestration — matching multi-agent primitive to workflow duration, resumability, and human-in-the-loop needs.

## Why It Matters

Using the wrong primitive causes blocked parents on long work, or heavy queue overhead on simple subtasks. Explicit primitive choice prevents orchestration misuse.

## Architecture Implications

| Dimension | Delegate | Durable queue (Kanban-style) |
|-----------|----------|------------------------------|
| Parent blocking | Yes — parent waits for summary | No — work persists independently |
| Survives restart | No | Yes |
| Human mid-task input | Poor fit | Good fit |
| Scheduled unattended | Poor fit | Cron-style complement |
| Multiple roles over lifetime | Poor fit | Pipeline / fleet topologies |
| Latency for quick answer | Best fit | Overhead unjustified |

- Both may share the same underlying agent runtime — primitive differs in coordination layer, not model.
- Delegate returns summary-only to parent; queue uses board state, comments, and role handoffs.
- See [[durable-task-coordination]] for persistent queue semantics.

## Production Implications

- Decision checklist at task creation: blocking?, durable?, human gate?, scheduled?
- Instrument primitive misuse (long delegate chains, kanban for one-shot lookups).
- Default concurrent delegate limits prevent cost explosion — separate from queue worker pools.

## Risks

- Teams standardize on one primitive for all workloads.
- Kanban adopted without failure limits → infinite retry on stuck tasks.

## Related Concepts

- [[durable-task-coordination]]
- [[subagents]]
- [[subagent-tool-restrictions]]
- [[task-state-machine]]
- [[coordination]]

## Related Anti-patterns

- [[infinite-retry-loops]]
- [[recursive-self-improvement]]

## Related Patterns

- [[fail-closed-agent-loop]]

## Upstream Sources

- `experiments/hermes-agent-review/multi-agent/TASK_ORCHESTRATION.md`
- `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §6–7
- `Books/claude/ch08-sub-agents.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.8
- `governance/PROMOTION_LOG.md`
- `governance/SEMANTIC_LINKING_AUDIT.md`

## Semantic Cluster

orchestration

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Fills major multi-agent gap; architecture decision matrix only, no Kanban DB schema.
governance_reference: PROMOTION_REVIEW.md §3.8, governance/CANONICAL_DIRECTION.md Phase 1.2
```
