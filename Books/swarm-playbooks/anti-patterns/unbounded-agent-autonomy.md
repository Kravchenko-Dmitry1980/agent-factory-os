# Unbounded Agent Autonomy

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

Agents retain ability to invoke **external or irreversible tools** without approval boundaries, budget caps, or phase-appropriate restrictions.

## Symptoms

- All tools available to all agents in run
- Critic pass → auto-publish path
- Solo `/task` mode bypasses review gates
- No timeout — agent loops until manual stop

## Why It Fails

- External harm (wrong publish, leaked data, spam)
- Cost runaway on retry loops
- Operator loses control narrative — «agent went rogue»

## Corrective Pattern

- [approval-before-external-action.md](../patterns/approval-before-external-action.md)
- [safe-autonomy.md](../hitl/safe-autonomy.md)
- [budget-aware-orchestration.md](../budget-control/budget-aware-orchestration.md)

## Sources

- Risk implied when Prompt 5 adds direct tasks, Telegram publish, multi-entry points

## Promotion Potential

**NEVER PROMOTE** — canonical systems require fail-closed tool policy.
