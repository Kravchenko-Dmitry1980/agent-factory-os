# Verification Before Writeback

## Definition

**Verification before writeback** is the gate requiring successful evaluation or verification before persisting memory, skills, or procedural updates — preventing unverified agent output from becoming durable state.

## Why It Matters

Writeback without verification pollutes long-lived stores with hallucinations, task ephemera, and failed-attempt residue. Durable layers need higher evidence bar than chat messages.

## Architecture Implications

```
EXECUTE → VERIFY → (pass) → WRITEBACK → (fail) → discard | retry | escalate
```

Applies to:

- Curated memory adds/replaces ([[memory-char-limits]] stores)
- Skill creation or modification ([[progressive-skill-disclosure]] corpus)
- Cross-session episodic promotion (selective, not raw chat dump)

- Aligns with [[visual-verification]] for GUI modality and [[verification]] for code/hook modality.
- Subagents should not writeback to shared stores — see [[subagent-tool-restrictions]].
- Evaluation may be automated (tests, reflector A/B/C) or human gate for high-risk domains.

## Production Implications

- Explicit writeback API rejects unverified payloads.
- Audit log: what verified, what rejected, which gate failed.
- Reduces [[unbounded-memory-growth]] and [[memory-as-crutch]] severity.

## Risks

- Verification bypass "for speed" in development propagates to production.
- Over-strict gates block legitimate learning — tune per store type.

## Related Concepts

- [[verification]]
- [[visual-verification]]
- [[memory-aware-execution]]
- [[fail-closed-agent-loop]]
- [[memory-char-limits]]

## Related Anti-patterns

- [[unbounded-memory-growth]]
- [[recursive-self-improvement]]
- [[mid-session-memory-injection]]

## Related Patterns

- [[fail-closed-agent-loop]]
- [[memory-aware-execution]]

## Upstream Sources

- `Books/brain-os/patterns/evaluation-before-writeback.md` (stripped)
- `experiments/mobile-agent-review/extracted-patterns/action-verification-pattern.md`
- `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md`

## Governance References

- `PROMOTION_REVIEW.md` §5.5
- `governance/PROMOTION_STRATEGY.md`
- `governance/SEMANTIC_DRIFT_ANALYSIS.md`

## Semantic Cluster

verification

## Promotion Metadata

```yaml
maturity: reusable-pattern
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Brain OS idea promoted without plane/event contract; paired with MobileAgent verify semantics.
governance_reference: governance/PROMOTION_STRATEGY.md Contracts default, governance/CANONICAL_DIRECTION.md Phase 1.3 Brain OS strip
```
