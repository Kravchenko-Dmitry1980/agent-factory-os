# Orchestration Lifecycle (Pattern)

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Стандартизированная последовательность фаз multi-agent execution от постановки цели до публикации/закрытия с явными handoff между planner, executors, critic, and human.

## Operational Context

Canonical flow extracted from swarm prompts:

**goal → planning → decomposition → execution → critique → review → approval → publish**

## Why It Works

- Each phase has clear owner and exit criteria
- Failures localize to phase (bad plan vs bad execution vs bad review)
- Human intervention points are predictable

## Architecture Implications

- Persist phase transitions in run/task records (activity_log)
- Large runs: planning phase ends in `awaiting_plan_approval`
- Executor set configurable (default: all active except strategist + critic)
- Publish is **post-approval** side effect, not automatic terminal state

## Human-in-the-loop Implications

| Phase | Human role |
|-------|--------------|
| goal | Defines objective |
| planning | May approve plan (large runs) |
| execution | Optional: answer `waiting_question` |
| critique | None (automated) |
| review | Mandatory verdict |
| approval | Explicit for external |
| publish | Triggered after approval |

## Failure Modes

- Skipping planning for «speed»
- Critic loop infinite without cap
- Publish wired before review gate
- No recovery if orchestrator fails mid-decomposition

## Related Anti-patterns

- [orchestration-without-contracts.md](../anti-patterns/orchestration-without-contracts.md)
- [prompt-chain-fragility.md](../anti-patterns/prompt-chain-fragility.md)

## Production Constraints

- State machine spec with allowed transitions
- Idempotent phase handlers
- Timeout per phase
- Correlation ID across all phase events

## Sources

- `source/ai-agents-from-scratch.ru.md` — этап 7 (цель → план → исполнение → проверка)
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3 (orchestrator.ts flow)

## Promotion Potential

**SAFE FUTURE PROMOTION** — lifecycle skeleton valuable; must merge with Agent-OS task lifecycle contracts, not replace them.

See also: [lifecycle/orchestration-lifecycle.md](../lifecycle/orchestration-lifecycle.md) for expanded operational doc.
