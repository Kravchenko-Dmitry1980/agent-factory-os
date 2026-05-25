---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Run (Прогон)

Single end-to-end orchestration instance: one **goal** → plan → tasks → critique → human review.

## States (operational, from Prompt 3)

- planning / executing
- awaiting plan approval (large runs)
- pending human review («на твоей проверке»)
- completed (after human disposition — implied)

## Persistence

- Table: `runs` (goal, status, summary, cost fields)

## Related

- [lifecycle/orchestration-lifecycle.md](../lifecycle/orchestration-lifecycle.md)
