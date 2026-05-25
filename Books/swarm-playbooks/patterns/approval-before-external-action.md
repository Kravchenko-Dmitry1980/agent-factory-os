# Approval Before External Action

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Any action with **irreversible or public external effect** (publish, send message, payment, API mutation) requires explicit human approval after automated stages complete.

## Operational Context

- «Обязательное подтверждение человеком для действий «наружу»»
- Telegram publish via button/API after calendar approval
- External tools (send to client, post to channel) gated

## Why It Works

- Fail-closed default for highest-risk operations
- Aligns automation benefit (draft speed) with human accountability (release)

## Architecture Implications

- Tool taxonomy: `internal` vs `external` with policy enforcement
- External tools check run/task approval state before execution
- Two-person rule optional for sensitive domains
- Publish endpoints return 403 if approval missing

## Human-in-the-loop Implications

- Clear UX distinction: «save draft» vs «publish»
- Operator knows exactly what will happen externally before confirm
- Rejection returns artifact to rework, not silent drop

## Failure Modes

- Agent calls external API through undclassified tool
- Approval on wrong environment (staging vs prod channel)
- Time-delayed publish without re-confirmation
- Bypass via `/task` solo mode without review

## Related Anti-patterns

- [unbounded-agent-autonomy.md](../anti-patterns/unbounded-agent-autonomy.md)
- [automation-without-review.md](../anti-patterns/automation-without-review.md)

## Production Constraints

- Policy engine (not prompt honor system) for external tools
- Audit log of external actions with approver identity
- Kill switch for publish integrations

## Sources

- `source/ai-agents-from-scratch.ru.md` — этап 9
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 4 (publish telegram), Prompt 3 (review before release)

## Promotion Potential

**SAFE FUTURE PROMOTION** — strong safety pattern; align with Agent-OS fail-closed defaults and tool restrictions for subagents.
