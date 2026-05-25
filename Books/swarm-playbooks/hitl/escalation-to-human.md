---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Escalation to Human

## Definition

Mechanisms that **pause automation** and route control to the operator when the system cannot proceed safely or needs missing input.

## Escalation Triggers (from playbooks)

| Trigger | Status / UX | Operator action |
|---------|-------------|-----------------|
| Large run plan ready | `awaiting_plan_approval` | Approve or edit plan |
| Agent needs input | `waiting_question` | Answer in UI/chat/Telegram |
| Critic rework exhausted | task → review/rework | Human comment |
| Run complete | `pending_human_review` | Approve/rework items |
| Budget exceeded (optional) | should pause | Raise limit or abort — **implicit, not fully spec'd** |
| Tool requires permission | Prompt 0 norm | Confirm install/action |

## Notification Channels

- Dashboard events counter
- Optional Telegram bot (plan ready, run finished)

## Gaps vs Production

- No SLA for `waiting_question`
- No on-call rotation model
- No structured escalation severity

## Sources

- `source/swarm-ai-agents-prompts.ru.md` — Prompts 3–5

## Related

- [human-in-the-loop-approval.md](../patterns/human-in-the-loop-approval.md)
- [human-approval-boundaries.md](human-approval-boundaries.md)
