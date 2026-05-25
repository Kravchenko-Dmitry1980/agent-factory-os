# Personality Over Architecture

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

Designing agent systems primarily through **personality-rich system prompts** («характер», «живой тон», role flavor) instead of explicit responsibilities, interfaces, tools, and stop criteria.

## Symptoms

- «Хороший промпт = 80% качества»
- Eight agents differentiated by tone in seed.sql
- Role boundaries blur — Сценарист vs Рилсмейкер overlap
- Behavior changes unpredictably when model updates

## Why It Fails

- Personality does not enforce invariants or tool restrictions
- Hard to test — subjective tone vs objective output schema
- Onboarding new operators requires «feel» not specs
- Conflicts with deterministic routing and policy planes

## Corrective Pattern

- Define role by **inputs, outputs, tools, escalation rules**
- [progressive-autonomy.md](../patterns/progressive-autonomy.md) — start one role with clear IO

## Sources

- `source/ai-agents-from-scratch.ru.md` — этап 5 (характер агента)
- `source/swarm-ai-agents-prompts.ru.md` — Prompt 2 (личности в seed.sql)

## Promotion Potential

**NEVER PROMOTE** — personality may exist in UX copy, not as architecture primitive.
