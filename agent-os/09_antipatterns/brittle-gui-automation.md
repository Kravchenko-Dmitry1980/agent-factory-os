# Brittle GUI Automation

## Definition

**Brittle GUI automation** aggregates failure modes where GUI harnesses rely on fragile assumptions — inaccurate perception, fixed sleeps, hardcoded hints, or unguarded device actions — producing flaky or unsafe behavior.

## Why It Matters

Research reference implementations expose patterns worth learning and pitfalls worth avoiding. Cataloging brittleness prevents naive port to production.

## Architecture Implications

| Failure mode | Symptom | Mitigation |
|--------------|---------|------------|
| OCR-list as ground truth | Wrong-pixel taps | [[visual-grounding]] + verify |
| Absolute pixels on variable layout | Cross-device miss | Normalized coordinate space |
| Hardcoded eval hints in planner | Benchmark overfit | Remove task-specific hints |
| Platform driver assumptions | Silent prerequisite fail | Explicit capability checks |
| Sleep-based sync | Flaky on slow UI | Observation-driven wait |
| No permission layer | Unsafe real-device actions | Confirm gates for destructive ops |
| Monolithic per-version scripts | Fixes don't propagate | Shared adapter boundary |

**Why dangerous:** Flakiness masquerades as model weakness; security gaps on real devices; maintenance cost explodes across versions.

## Production Implications

- Treat research GUI stacks as pattern sources, not hardened runtimes.
- Permission layer mandatory before production device control.

## Risks

- Copying research sleep/sync defaults into production harness.

## Related Concepts

- [[unverified-gui-clicks]]
- [[visual-grounding]]
- [[visual-verification]]
- [[gui-agent-loop]]

## Related Anti-patterns

- [[unverified-gui-clicks]]

## Related Patterns

- [[visual-grounding]]
- [[visual-verification]]

## Upstream Sources

- `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md`

## Governance References

- `PROMOTION_REVIEW.md` §4.8
- `governance/PROMOTION_LOG.md`

## Semantic Cluster

gui-modality

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Aggregates seven GUI failure modes with mitigations; no runtime script references.
governance_reference: PROMOTION_REVIEW.md §4.8, governance/PROMOTION_STRATEGY.md
```
