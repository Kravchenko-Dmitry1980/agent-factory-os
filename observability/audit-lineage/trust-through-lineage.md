# Trust Through Lineage

## Question

> Can we defend this decision to an auditor?

## Requires

- Complete chain from source to outcome
- Explicit rejection reasons
- No silent state jumps

## Promotion Trust

`governance/PROMOTION_STRATEGY.md` pipeline visible as:

```
source → review → scan → governance → integrate | reject
```

Each stage = auditable event.

## Failure Trust

When blocked:

```
unsafe_action_blocked
escalation_triggered
governance_rejection
```

Auditor sees **prevented harm**, not silent deny.

## Without Lineage

Trust collapses to "the model said so" — unacceptable for governed systems.
