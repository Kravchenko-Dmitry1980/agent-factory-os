---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Budget-Aware Orchestration

## Definition

Orchestration layer tracks token/cost per task and run, supports **optional budget cap per run**, and should pause or abort when cap exceeded (enforcement level in playbooks: visibility-first).

## Operational Context

- Fields on `runs` and `tasks` for cost and tokens
- Optional budget on run creation
- Display spend on dashboard per run/task

## Why It Works

- Prevents surprise bills on large swarms + rework loops
- Enables operator tradeoff: quality vs cost per goal
- Surfaces expensive agents/tasks for tuning

## Architecture Implications

- Aggregate cost bottom-up from task completions
- Include critic rework rounds in run total
- Budget check before starting new task or rework round
- Alert event when threshold crossed (80/100%)

## Human-in-the-loop Implications

- Operator sets budget when defining goal
- On exceed: human decides raise limit vs abort vs simplify plan

## Failure Modes

- Budget optional → always ignored
- Costs missing for failed tasks
- Retry loops bypass budget check
- Display-only budget without enforcement

## Sources

- `source/ai-agents-from-scratch.ru.md` — этап 9 (лимит на задачу)
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 4

## Related

- [execution-cost-visibility.md](execution-cost-visibility.md)
- [retry-cost-awareness.md](retry-cost-awareness.md)

## Promotion Potential

**RESEARCH ONLY** — needs enforcement semantics before canonical merge.
