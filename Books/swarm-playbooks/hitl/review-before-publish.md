---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Review Before Publish

## Definition

No artifact reaches a **publish** or **external send** integration until it has passed the human **review queue** and explicit **approval** for that action class.

## Workflow

1. Run completes automated phases → status «на твоей проверке»
2. Operator opens `/review` — reads summary + task outputs
3. Per item: **Одобрить** or **На доработку** (+ comment)
4. Only approved items eligible for publish API / calendar publish button
5. Approved publication may trigger closed loop (draft → content plan)

## Why Separate from Critique

| Stage | Actor | Purpose |
|-------|-------|---------|
| Critique | Critic LLM | Filter obvious issues, bounded rework |
| Review | Human | Accountability, brand, legal, nuance |
| Publish | Integration | Irreversible external effect |

## Failure Modes

- Skipping review because critic passed
- Publishing from calendar without checking approval chain
- Auto-draft creation confused with publish approval

## Sources

- `source/swarm-ai-agents-prompts.ru.md` — Prompt 3, 4

## Related

- [review-gate.md](../patterns/review-gate.md)
- [critique-vs-verification.md](../critique/critique-vs-verification.md)
