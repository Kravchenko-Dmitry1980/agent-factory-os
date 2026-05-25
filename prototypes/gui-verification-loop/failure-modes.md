# GUI Verification Loop — Failure Modes

## Hallucination

Agent claims screen shows success without reading mock state. **Mitigation:** structured state compare.

## Retry Loops

Infinite click retry on C outcome. **Mitigation:** circuit breaker after 2 C outcomes.

## Missing Verification

Click assumed success on no transport error. **Mitigation:** A/B/C check mandatory before advance.

## Memory Drift

Plan references old screen id. **Mitigation:** observe step refreshes state each loop.

## Unsafe Autonomy

Execute click before verification. **Mitigation:** verify runs on simulated post-state first.

## Missing Escalation

B outcome loops forever. **Mitigation:** replan flag + audit.

## Governance Bypass

Skip verify on "low risk" UI. **Mitigation:** all clicks require A outcome to advance.
