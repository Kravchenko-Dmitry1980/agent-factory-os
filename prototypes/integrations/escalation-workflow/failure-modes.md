# Escalation — Failure Modes

## Orchestration Drift

Generic retry middleware hides escalation policy. **Mitigation:** explicit counter in workflow file.

## Queue Failure

N/A — single task focus.

## Escalation Failure

Retries continue past ceiling. **Mitigation:** fail-closed stop + ESCALATED status.

## Verification Bypass

Treat low confidence as pass. **Mitigation:** uncertainty routes to retry/escalate.

## Retry Storms

**Scenario:** retry-storm — hits ceiling, escalates, stops.

## Memory Corruption

N/A.

## Approval Bypass

Auto-complete after escalation without human. **Mitigation:** terminal STOP, not COMPLETED.

## Hidden Autonomy

Silent retry forever. **Mitigation:** MAX_RETRIES + audit each attempt.
