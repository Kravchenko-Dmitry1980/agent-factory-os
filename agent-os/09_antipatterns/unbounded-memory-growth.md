# Unbounded Memory Growth

## Definition

**Unbounded memory growth** is allowing curated or episodic memory stores to expand without hard limits, consolidation policy, or write gates — leading to noise, cost, and stale parallel state.

## Why It Matters

Memory without bounds becomes a junk drawer. Retrieval quality drops; prompt injection cost rises; agents stop reading live sources.

## Architecture Implications

**Failure mode:** Every turn appends facts → store grows → injection or recall returns irrelevant history.

**Symptoms:**

- Memory files exceed context budget
- Agent repeats outdated architecture "facts"
- No consolidation workflow when "full"

**Why dangerous:** Combines [[memory-as-crutch]] with operational cost explosion; external providers amplify write volume.

**Mitigation:**

- [[memory-char-limits]] with reject-or-consolidate on overflow
- [[memory-provider-boundaries]] — single external backend, scoped writes
- [[verification-before-writeback]] before persisting agent-generated memory
- Periodic human audit of curated stores

## Production Implications

- Alert on store size thresholds (~80% of limit).
- Taxonomy filters: exclude derivable codebase facts.

## Risks

- Soft limits without enforcement silently truncate.
- Auto-summarize entire history into memory without eval gate.

## Related Concepts

- [[memory-char-limits]]
- [[memory-as-crutch]]
- [[memory-taxonomy]]
- [[memory-provider-boundaries]]
- [[verification-before-writeback]]

## Related Anti-patterns

- [[memory-as-crutch]]
- [[mid-session-memory-injection]]

## Related Patterns

- [[memory-char-limits]]
- [[verification-before-writeback]]
- [[memory-aware-execution]]

## Upstream Sources

- `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §1
- `Books/brain-os/anti-patterns/memory-overfetch.md` (retrieval risk — research)

## Governance References

- `PROMOTION_REVIEW.md` §3.2
- `governance/PROMOTION_LOG.md`

## Semantic Cluster

memory-governance

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Boundedness anti-pattern; Hermes char-limit evidence, Brain OS overfetch cross-ref only.
governance_reference: PROMOTION_REVIEW.md §3.2, governance/PROMOTION_STRATEGY.md
```
