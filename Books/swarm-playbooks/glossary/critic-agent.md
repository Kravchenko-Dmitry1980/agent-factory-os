---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Critic Agent

Dedicated agent role that **critiques** executor outputs before human review.

## Limitations (mandatory)

- Does **not** verify truth
- Does **not** replace governance
- Cannot guarantee absence of hallucinations

## In playbooks

- Slug: `critic` (Критик)
- Up to 2 rework rounds per task

## Related

- [critique/critique-limitations.md](../critique/critique-limitations.md)
- [anti-patterns/critic-as-fake-verification.md](../anti-patterns/critic-as-fake-verification.md)
