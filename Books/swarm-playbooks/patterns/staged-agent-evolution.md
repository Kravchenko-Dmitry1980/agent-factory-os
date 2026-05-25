# Staged Agent Evolution

---
classification: reusable-pattern
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Definition

Evolution path for agent systems through **discrete stages**: tools → single agent → multi-agent chat → orchestrated runs → platform features — each stage gated by verification checkpoints.

## Operational Context

Playbook prompt sequence maps to stages:

| Stage | Capability |
|-------|------------|
| 0 | Environment + project skeleton |
| 1 | DB, backend, dashboard, one agent (Стратег) |
| 2 | All agents as 1:1 chat personas |
| 3 | Orchestrated runs + critic + review |
| 4 | Content factory, budget, closed loop |
| 5 | Multi-project, knowledge, tests |
| 6 | Documentation hardening |

## Why It Works

- Each stage adds one complexity dimension
- «Не переходи к следующему промту, пока текущий шаг не заработал»
- Reduces big-bang integration failures

## Architecture Implications

- Schema migrations incremental (`migrate.sql`)
- Features behind implicit stage — not all tables day one
- Backward compatible: chat mode works when runs disabled

## Human-in-the-loop Implications

- Human validates each stage via checklist / smoke test
- Operator controls when to invoke Prompt N+1

## Failure Modes

- Skipping stages (jump to Prompt 3 without stable Prompt 1)
- Adding platform features before core run lifecycle stable
- Stage success = «compiles» not « meets task criteria »

## Related Anti-patterns

- [premature-agent-swarm.md](../anti-patterns/premature-agent-swarm.md)
- [tutorial-driven-architecture.md](../anti-patterns/tutorial-driven-architecture.md)

## Production Constraints

- Environment promotion: dev stages ≠ prod feature parity without gates
- Automated stage acceptance tests
- Rollback per stage via migrations + feature flags

## Sources

- `source/ai-agents-from-scratch.ru.md` — этапы 0–10
- `source/swarm-ai-agents-prompts.ru.md` — Prompts 0–6 structure

## Promotion Potential

**SAFE FUTURE PROMOTION** — onboarding/maturity model; not a runtime architecture.
