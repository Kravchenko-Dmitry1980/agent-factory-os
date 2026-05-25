# Memory-Aware Execution

## Definition

**Memory-aware execution** is routing agent work based on memory need and profile — applying recall, bounded injection, and write gates before expensive reasoning paths, not treating memory as always-on context.

## Why It Matters

Blind full-memory injection wastes tokens and adds noise. Execution should match memory depth to task: fast reflex paths skip heavy recall; memory-augmented paths prefetch selectively.

## Architecture Implications

- Classify turn or task: requires user model?, requires cross-session recall?, ephemeral only?
- **Prefetch-before-turn** (concept): background recall when memory-augmented mode selected — merge into Phase 1.3 `memory-recall.md` update, not runtime here.
- [[frozen-memory-snapshot]] supplies static curated layer; dynamic recall is explicit tool/hook, not prompt rebuild.
- [[profile-isolation]] scopes which stores participate.
- [[memory-provider-boundaries]] determines external recall availability.
- Distinct from routing-plane branding — this is harness execution policy.

## Production Implications

- Metrics: memory_hit_rate, recall latency, store utilization vs limits.
- Cap top-k recall results — related Brain OS overfetch risk (research cross-ref only).
- Fail closed when recall returns empty — do not hallucinate user facts.

## Risks

- Over-fetch: retrieving entire history per turn.
- Under-fetch: skipping profile on tasks requiring user preferences.

## Related Concepts

- [[frozen-memory-snapshot]]
- [[memory-recall]]
- [[memory-compaction]]
- [[memory-char-limits]]
- [[memory-provider-boundaries]]
- [[profile-isolation]]

## Related Anti-patterns

- [[unbounded-memory-growth]]
- [[mid-session-memory-injection]]
- [[memory-as-crutch]]

## Related Patterns

- [[frozen-memory-snapshot]]
- [[verification-before-writeback]]

## Upstream Sources

- `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md`
- `Books/brain-os/patterns/memory-aware-routing.md` (stripped)
- `Books/brain-os/anti-patterns/memory-overfetch.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.1
- `governance/PROMOTION_STRATEGY.md`
- `governance/SEMANTIC_DRIFT_ANALYSIS.md`

## Semantic Cluster

memory-governance

## Promotion Metadata

```yaml
maturity: reusable-pattern
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Combines Hermes lifecycle hooks concept with Brain OS memory-need idea; no CAIM/VGP branding.
governance_reference: governance/PROMOTION_STRATEGY.md Source Priority, governance/CANONICAL_DIRECTION.md
```
