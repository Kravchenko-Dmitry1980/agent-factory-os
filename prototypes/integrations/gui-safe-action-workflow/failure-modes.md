# GUI Safe Action — Failure Modes

## Orchestration Drift

Chaining GUI steps into autonomous loop. **Mitigation:** single action per demo run with explicit gates.

## Queue Failure

N/A.

## Escalation Failure

C-outcome retry without circuit breaker. **Mitigation:** 2-strike stop.

## Verification Bypass

Execute click before visual verify. **Mitigation:** verify runs on simulated state first.

## Retry Storms

Infinite C retries. **Mitigation:** circuit breaker.

## Memory Corruption

Stale screen id in plan. **Mitigation:** observe refreshes each step.

## Approval Bypass

Execute high-risk without approval. **Mitigation:** deny-by-default.

## Hidden Autonomy

Auto-execute on "low risk" without verify. **Mitigation:** all paths require A outcome.
