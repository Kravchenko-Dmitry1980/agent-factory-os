# Unverified GUI Clicks

## Definition

**Unverified GUI clicks** is the failure mode where tap, swipe, or type actions execute without observing UI delta — treating transport success as task progress.

## Why It Matters

Primary production failure for GUI agents. Structured code tools return stdout; GUI feedback is visual and must be explicit in loop contract.

## Architecture Implications

**Failure mode:** Action dispatched → agent assumes success → plan advances on stale screen state.

**Symptoms:**

- Wrong screen after "successful" step
- Repeated actions on unchanged UI
- Disabled reflection for speed in research configs

**Why dangerous:** Errors compound silently; debugging requires full replay; user trust erodes on real devices.

**Mitigation:**

- Mandate [[visual-verification]] A/B/C in [[gui-agent-loop]]
- Never disable verification in production without alternative env reward
- Wait for UI-stable observation, not fixed sleep
- Log verification outcome per step

## Production Implications

- Treat verification as harness requirement, not model optional behavior.
- Monitor C-outcome rate per workflow.

## Risks

- False-A from weak reflector models
- Ignored ADB/transport return codes treated as success

## Related Concepts

- [[visual-verification]]
- [[gui-agent-loop]]
- [[brittle-gui-automation]]
- [[fail-closed-agent-loop]]

## Related Anti-patterns

- [[brittle-gui-automation]]

## Related Patterns

- [[visual-verification]]
- [[fail-closed-agent-loop]]

## Upstream Sources

- `experiments/mobile-agent-review/anti-patterns/unverified-clicks.md`

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
promotion_rationale: Top GUI failure mode with clear mitigation via visual-verification.
governance_reference: PROMOTION_REVIEW.md §4.8, governance/PROMOTION_STRATEGY.md Anti-patterns
```
