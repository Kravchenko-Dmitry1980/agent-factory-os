# Memory Provider Boundaries

## Definition

**Memory provider boundaries** define which memory backends may be active simultaneously, what each layer owns, and how external providers relate to built-in curated stores — without mixing conflicting write paths.

## Why It Matters

Multiple external memory backends create tool schema bloat, conflicting writes, and unpredictable recall. Clear boundaries keep memory architecture governable.

## Architecture Implications

- **Built-in curated stores** (bounded agent notes + user profile) remain always active as the canonical local layer.
- **At most one external provider** augments built-in stores — never two competing external backends.
- External providers attach via a defined lifecycle (initialize, prefetch, sync, shutdown) — concept only; no vendor matrix in curated layer.
- Non-primary agent contexts (subagent, scheduled job) should skip provider writes to prevent user-model corruption.
- Provider choice is configuration, not runtime discovery — reject second registration attempts.

## Production Implications

- Document which layer owns what: local curated files vs external semantic recall.
- Fail closed when provider misconfiguration detected (multiple externals, write from blocked context).
- External provider swap requires migration plan — not hot dual-run.

## Risks

- Teams enable external provider without understanding overlap with built-in stores.
- Provider-specific knobs (dialectic depth, async write frequency) promoted as normative config explode operational burden — keep in research tier.

## Related Concepts

- [[memory-char-limits]]
- [[frozen-memory-snapshot]]
- [[profile-isolation]]
- [[subagent-tool-restrictions]]
- [[memory-aware-execution]]

## Related Anti-patterns

- [[unbounded-memory-growth]]
- [[mid-session-memory-injection]]

## Related Patterns

- [[memory-aware-execution]]
- [[verification-before-writeback]]

## Upstream Sources

- `experiments/hermes-agent-review/memory/MEMORY_PROVIDERS.md`
- `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md`
- `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §3

## Governance References

- `PROMOTION_REVIEW.md` §3.1
- `governance/PROMOTION_STRATEGY.md`
- `governance/PROMOTION_LOG.md`

## Semantic Cluster

memory-governance

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: One-external-provider rule and context write boundaries; stripped of 8-provider implementation matrix.
governance_reference: PROMOTION_REVIEW.md §3.1, governance/PROMOTION_STRATEGY.md Memory Provider Boundaries
```
