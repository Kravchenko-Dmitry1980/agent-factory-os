# Review Loop — Failure Modes

## Hallucination

**Risk:** Draft contains fabricated claims; critic approves confidently.

**Mitigation:** Critic is not verification — human must review. Demo: critic can pass bad drafts; human is the evidence gate.

**Anti-pattern:** `critic-as-fake-verification`

## Retry Loops

**Risk:** Uncapped rework between executor and critic.

**Mitigation:** Max 2 rework rounds, then escalate.

## Missing Verification

**Risk:** Publish immediately after critic pass.

**Mitigation:** Fail-closed — publish API rejects without `human_decision=approve`.

## Memory Drift

**Risk:** Critic and executor share biased context, rubber-stamp each other.

**Mitigation:** Separate roles in architecture; critic must not have publish tools.

## Unsafe Autonomy

**Risk:** Auto-publish on high score.

**Mitigation:** No score threshold for publish in demo code.

## Missing Escalation

**Risk:** `uncertain` verdict treated as pass.

**Mitigation:** Fail-closed block until human inspects.

## Governance Bypass

**Risk:** Direct call to `publish()` skipping review.

**Mitigation:** `publish()` checks approval token; demo includes bypass-attempt scenario.
