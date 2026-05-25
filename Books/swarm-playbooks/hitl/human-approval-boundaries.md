---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Human Approval Boundaries

## Definition

Explicit classification of actions into zones: **automated internal**, **automated with critic**, **human review required**, **human approval required for external effect**.

## Boundary Map

| Action class | Automated? | Human? |
|--------------|--------------|--------|
| Draft generation | ✓ | optional review |
| Internal summarization | ✓ | |
| Plan for large run | partial | **approve plan** |
| Critic rework loop | ✓ (capped) | |
| Result visibility | after critic | **review queue** |
| Publish to channel | | **approve** |
| Email/message to client | | **approve** |
| Payment / purchase | | **approve** |
| DB schema migration (tutorial) | | **confirm** (Prompt 0 norm) |

## Operational Rules (from sources)

1. «Где обязательно решает человек» — document at task definition time (ЗАДАЧА.md question 7)
2. «На старте — почти везде» human confirms outputs
3. External actions always confirm — этап 9

## Architecture Implication

Boundaries must be **enforced in tool policy**, not listed only in prompts.

## Sources

- `source/ai-agents-from-scratch.ru.md` — этапы 1, 2, 9
- `source/swarm-ai-agents-prompts.ru.md` — plan approval, review page

## Related

- [approval-before-external-action.md](../patterns/approval-before-external-action.md)
- [safe-autonomy.md](safe-autonomy.md)
