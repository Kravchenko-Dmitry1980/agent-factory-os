# Hidden Coupling Analysis

Coupling that appears only during evolution.

## Patterns

| Pattern | Signal |
|---------|--------|
| **Shared dataclass base** | Edit one workflow, break three |
| **Import between demos** | Circular dependency |
| **Global retry constant** | Unintended scope change |
| **Unified audit schema** | Platform schema creep |
| **Cross-phase shared/ growth** | 2.0 + 2.1 + 2.2 shared merge |

## Detection Questions

1. How many files change for one behavioral tweak?
2. Does change require updating unrelated README?
3. Did `shared/` gain a new module?

## Mitigation

Duplicate 10 lines instead of abstract. See Phase 2.1 [anti-framework-rules](../../prototypes/integrations/governance/anti-framework-rules.md).

## Coupling Budget

One behavioral change → **≤ 2 code files** in prototypes/adapters. Else split proposal.
