# GUI Agent Loop

## Definition

The **GUI agent loop** is an embodied execution cycle: observe screen → reason about next step → execute GUI action → verify feedback → update progress — repeating until terminal state or step budget exhaustion.

## Why It Matters

Code-centric query loops assume structured tool results (stdout, files). GUI agents operate on pixels and layout; without an explicit loop contract, teams treat clicks as fire-and-forget side effects.

## Architecture Implications

```
SCREEN → REASON → ACTION → FEEDBACK → UPDATE → (repeat | STOP)
```

| Stage | Responsibility |
|-------|----------------|
| Screen | Capture observation (screenshot, accessibility tree, or hybrid) |
| Reason | Plan next action from goal + history + memory |
| Action | Parse intent → execute via platform adapter |
| Feedback | New observation + verification outcome |
| Update | Progress, error flags, episodic scratch |

- Treat GUI as **modality extension** of agent runtime — parallel golden path to code [[query-loop]], not replacement.
- Single action per turn reduces compounding grounding errors.
- [[visual-grounding]] binds intent to coordinates; [[visual-verification]] validates feedback.
- Platform adapters (mobile, desktop, browser) sit behind action contract — not in curated architecture core.

## Production Implications

- Step budget and circuit breaker on repeated verification failures required.
- Separate "action succeeded" from "task succeeded" in loop state.
- Never disable verification stage in production without alternative reward signal.

## Risks

- Monolithic VLM end-to-end loops hide verification semantics.
- Sleep-based sync instead of observation-driven wait → flaky automation.

## Related Concepts

- [[visual-grounding]]
- [[visual-verification]]
- [[query-loop]]
- [[error-recovery-ladder]]
- [[verification]]

## Related Anti-patterns

- [[unverified-gui-clicks]]
- [[brittle-gui-automation]]

## Related Patterns

- [[fail-closed-agent-loop]]

## Upstream Sources

- `experiments/mobile-agent-review/extracted-patterns/screen-reason-action-feedback-loop.md`
- `Books/agents/` (harness survey framing — research catalog)

## Governance References

- `PROMOTION_REVIEW.md` §4.1
- `governance/PROMOTION_LOG.md`
- `governance/SEMANTIC_LINKING_AUDIT.md`

## Semantic Cluster

gui-modality

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Core GUI harness primitive; no ADB/runtime scripts or version-specific controllers.
governance_reference: PROMOTION_REVIEW.md §4.1, governance/CANONICAL_DIRECTION.md Phase 1.2
```
