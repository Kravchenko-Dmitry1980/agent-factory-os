---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Retry Cost Awareness

## Definition

Every **automated retry** (critic rework, planning retry, task timeout retry) has measurable marginal cost — operators must account for retry loops in budget and autonomy design.

## Cost Multipliers (from playbooks)

| Mechanism | Max iterations | Cost effect |
|-----------|----------------|-------------|
| Critic rework | 2 rounds | up to 3× executor+critic per task |
| Planning retry | mentioned in Prompt 4 | extra orchestrator calls |
| Agent timeout retry | per-agent timeout | unbounded if misconfigured |
| Test batch (`tests:batch`) | limit flag | N scenarios × critic |

## Rules

1. Cap rework rounds explicitly
2. Include retries in run budget aggregation
3. Surface retry count in UI per task
4. Failed tasks should not retry infinitely silently

## Failure Modes

- «Fix quality» by increasing retries → cost explosion
- Test batch run without budget guard
- Retry without changing input → identical failure

## Sources

- `source/swarm-ai-agents-prompts.ru.md` — Prompts 3–5

## Related

- [budget-aware-orchestration.md](budget-aware-orchestration.md)
- [critic-loop.md](../critique/critic-loop.md)

## Promotion Potential

**RESEARCH ONLY** — document retry policy in contracts before promotion.
