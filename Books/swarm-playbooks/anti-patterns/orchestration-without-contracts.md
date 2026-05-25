# Orchestration Without Contracts

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

Multi-agent orchestration implemented as **ad hoc prompt chains and DB statuses** without explicit contracts for tasks, routing decisions, traces, events, and tool boundaries.

## Symptoms

- Tasks described in natural language only
- No task envelope schema; handoffs implicit in orchestrator prompt
- activity_log without correlation to contract IDs
- Tool permissions defined in code paths, not policy
- Cannot replay or diff runs deterministically

## Why It Fails

- Integration breaks silently when prompts change
- No fail-closed routing — orchestrator improvises
- Governance and audit impossible at scale
- Team cannot evolve components independently

## Corrective Pattern

- Agent-OS contracts layer (reference only — not modified in this phase)
- [orchestration-lifecycle.md](../patterns/orchestration-lifecycle.md) as ops skeleton pending contracts

## Sources

- Implicit across `source/swarm-ai-agents-prompts.ru.md` — orchestrator.ts, tasks table without formal envelope

## Promotion Potential

**NEVER PROMOTE** — orchestration patterns here are **operational hints**, not canonical substitutes.
