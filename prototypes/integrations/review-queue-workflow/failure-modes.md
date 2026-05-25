# Review Queue — Failure Modes

## Orchestration Drift

**Risk:** Queue becomes generic job platform. **Mitigation:** in-memory FIFO, single worker, no registry.

## Queue Failure

**Risk:** Lost or double-processed tasks. **Scenario:** `queue-corruption` — detect and stop.

## Escalation Failure

**Risk:** Retry exhaustion silently drops task. **Mitigation:** ESCALATED status + audit.

## Verification Bypass

**Risk:** Publish after critic pass only. **Mitigation:** human approval gate.

## Retry Storms

**Risk:** Infinite rework. **Mitigation:** MAX_REWORK = 2, then escalate.

## Memory Corruption

N/A — stateless draft per task.

## Approval Bypass

**Risk:** Direct publish call. **Mitigation:** publish checks approval flag.

## Hidden Autonomy

**Risk:** Auto-approve on critic pass. **Mitigation:** human gate always required.

## Standard Categories

- **Hallucination:** critic passes wrong draft — human must catch
- **Missing verification:** skip human → publish denied
- **Governance bypass:** blocked in publish()
