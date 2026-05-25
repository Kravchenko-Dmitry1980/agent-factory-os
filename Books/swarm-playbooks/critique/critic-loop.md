---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Critic Loop

## Definition

Automated cycle: **executor produces** → **critic evaluates** → **rework or proceed**, repeated up to a **fixed maximum** (playbook: 2 rounds).

## Flow

```
task completed by executor
    → critic verdict
        → pass → next task / review queue
        → fail → rework (increment round)
            → if round < max → re-execute
            → else → escalate to human review/rework
```

## Components

- Critic agent excluded from default executor pool
- Verdict stored on task row
- Orchestrator respects round counter

## Operational Limits

- Max rounds prevent infinite cost
- Critic checks **quality heuristics**, not ground truth
- After cap, human must decide

## Sources

- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3 (orchestrator.ts)
- `source/ai-agents-from-scratch.ru.md` — этап 7

## Related

- [critique-before-publish.md](../patterns/critique-before-publish.md)
- [diagrams/critique-loop.md](../diagrams/critique-loop.md)
- [critique-limitations.md](critique-limitations.md)
