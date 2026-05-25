---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Critique vs Verification

## Mandatory Distinction

| | Critique | Verification |
|---|----------|--------------|
| **Actor** | LLM critic agent | Deterministic checks, grounded retrieval, human, formal eval |
| **Goal** | Improve draft quality heuristically | Establish truth/safety/compliance against spec |
| **Output** | Opinion + rework suggestion | Pass/fail with evidence |
| **Guarantee** | None | Bounded by method (if designed correctly) |
| **In playbooks** | Present | **Absent as first-class system** |

## Statement

**Critique ≠ verification system.**

Playbooks conflate these when stating critic «проверяет на выдумки». That is critique language applied to a verification claim.

## Correct Layering

```
execution → critique (optional, bounded)
         → verification (contracts, tools, evaluators)
         → human review
         → approval
         → publish
```

## Canonical Alignment (reference only)

Agent-OS `verification-before-writeback` and `evaluation-before-writeback` — not imported or modified in this phase.

## Sources

- Implicit gap analysis across both source files

## Related

- [critic-as-fake-verification.md](../anti-patterns/critic-as-fake-verification.md)
- [critique-limitations.md](critique-limitations.md)
