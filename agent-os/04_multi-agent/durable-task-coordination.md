# Durable Task Coordination

## Definition

**Durable task coordination** is queue-based multi-agent orchestration where tasks persist across agent restarts, support dependency graphs, role pipelines, and human unblock — distinct from ephemeral delegate RPC.

## Why It Matters

Long-running, multi-role, or human-gated work cannot rely on a blocking parent session. Durable coordination separates task state from any single conversation lifetime.

## Architecture Implications

- Task board holds state: ready, running, blocked, completed, failed — not parent message history.
- Dispatcher promotes ready tasks; workers execute in isolated agent instances; verifier and synthesizer roles optional.
- Dependencies and parent-child task links model pipelines (research → implement → review).
- Failure limits auto-block repeat failures — pairs with [[infinite-retry-loops]] mitigation.
- Complement [[kanban-vs-delegate]]: use when delegate decision matrix selects durable path.

Topologies (conceptual):

- Solo worker
- Parallel workers on independent tasks
- Role pipeline
- Fleet (one specialist, many subjects)
- Orchestrator + workers + verifier + synthesizer

## Production Implications

- Human unblock path required for blocked tasks in production workflows.
- Persist audit trail (comments, state transitions) separate from LLM chat logs.
- Do not use durable queue for sub-second parent-blocked lookups.

## Risks

- Queue overhead for trivial tasks.
- Missing failure_limit → stuck retry loops.
- Comment protocol complexity without governance → noisy boards.

## Related Concepts

- [[kanban-vs-delegate]]
- [[task-state-machine]]
- [[coordination]]
- [[subagents]]
- [[fail-closed-agent-loop]]

## Related Anti-patterns

- [[infinite-retry-loops]]
- [[recursive-self-improvement]]

## Related Patterns

- [[fail-closed-agent-loop]]

## Upstream Sources

- `experiments/hermes-agent-review/multi-agent/TASK_ORCHESTRATION.md`
- `experiments/hermes-agent-review/multi-agent/KANBAN.md`
- `experiments/hermes-agent-review/notes/DIGITAL_TWIN_IMPLICATIONS.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.8
- `governance/PROMOTION_LOG.md`
- `governance/NEXT_PHASE_ROADMAP.md`

## Semantic Cluster

orchestration

## Promotion Metadata

```yaml
maturity: reusable-pattern
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Durable coordination primitive at architecture level; comment protocol and DB schema deferred.
governance_reference: PROMOTION_REVIEW.md §6.10, governance/NEXT_PHASE_ROADMAP.md Phase 1.2 Batch B
```
