---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Orchestrator

Agent role that receives a **goal**, produces a **plan**, assigns **tasks** to executors, aggregates results, and produces a **summary** for human review.

## In playbooks

- Slug: `strategist` (Стратег)
- Excluded from default executor pool during runs
- Distinct from conversational chat mode

## Operational note

Orchestrator ≠ control plane. No routing contracts or trace records in sources.

## Related

- [glossary/run.md](run.md)
- [patterns/orchestration-lifecycle.md](../patterns/orchestration-lifecycle.md)
