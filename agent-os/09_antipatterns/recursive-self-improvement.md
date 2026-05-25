# Recursive Self-Improvement

## Definition

**Recursive self-improvement** (ungoverned) is the failure mode where agents spawn child agents, rewrite skills/memory, or adapt policy without depth limits, human gates, or rollback — causing cost explosion and uncontrolled drift.

## Why It Matters

Delegation and self-modifying skills are powerful; without guards they become runaway feedback loops unsuitable for production.

## Architecture Implications

**Failure mode:** Subagent spawns subagent; curator auto-deletes content; adaptation service mutates policy without eval.

**Symptoms:**

- Exponential delegate depth or fan-out
- Skill catalog churn without archive policy
- User model drift from unscoped writes

**Why dangerous:** Unbounded cost; irreversible knowledge loss; policy drift without audit trail.

**Mitigation:**

- [[subagent-tool-restrictions]] — block recursive delegation
- [[memory-provider-boundaries]] — non-primary contexts skip writes
- Defer uncontrolled adaptation (research tier); require approval + rollback + offline eval before any policy learning
- Archive-over-delete for agent-created procedural content (curator governance — Phase 1.3)
- Step and depth budgets on all orchestration primitives

## Production Implications

- Hard caps on delegate depth and concurrent children.
- No auto-delete of agent-authored skills in production.
- Separate research experiments from production memory/skill paths.

## Risks

- Marketing "self-improving agent" without governance invariants.
- MA-E-style experience tips without eval gate (research-only upstream).

## Related Concepts

- [[subagent-tool-restrictions]]
- [[subagents]]
- [[progressive-skill-disclosure]]
- [[verification-before-writeback]]
- [[infinite-retry-loops]]

## Related Anti-patterns

- [[infinite-retry-loops]]
- [[central-orchestrator-god-object]]

## Related Patterns

- [[subagent-tool-restrictions]]
- [[verification-before-writeback]]
- [[progressive-skill-disclosure]]

## Upstream Sources

- `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §9, §11
- `Books/brain-os/anti-patterns/uncontrolled-adaptation.md` (research — reject promotion)

## Governance References

- `PROMOTION_REVIEW.md` §3.2
- `governance/CANONICAL_DIRECTION.md`
- `governance/SEMANTIC_DRIFT_ANALYSIS.md`

## Semantic Cluster

orchestration

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Governance-first anti-pattern; adaptation-service explicitly excluded from promotion.
governance_reference: PROMOTION_REVIEW.md §7.3, governance/CANONICAL_DIRECTION.md speculative list
```
