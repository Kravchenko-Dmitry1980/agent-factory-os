# Reviewer Checklist

Quick checklist for human reviewer before accepting behavioral changes.

---

## Understanding

- [ ] I know which demos/adapters changed
- [ ] I know which governance invariant is at risk
- [ ] Rollback command/path is clear

## Execution

- [ ] Smoke checks run
- [ ] At least one fail-path scenario run (not only happy path)
- [ ] Trace example check script run

## Trace Quality

- [ ] I can explain **why** the workflow ended in that state
- [ ] Gate events are named, not generic errors
- [ ] Human vs critic roles are distinguishable
- [ ] Deny paths show deny events

## Safety

- [ ] No approval → no action still holds
- [ ] Retry ceiling still holds
- [ ] Escalation still triggers at exhaustion
- [ ] Memory writeback still gated
- [ ] GUI/LLM fail paths still reject

## Governance Alignment

- [ ] No new CI/CD artifacts
- [ ] No test framework required
- [ ] Change does not weaken doctrine docs silently

## Verdict

- [ ] PASS — behavior safe, trace adequate
- [ ] FAIL — rollback or fix required
- [ ] DEFER — need human domain judgment (document why)

---

## Reviewer Reminders

1. AI answer looks plausible but may be wrong
2. Critic is not truth
3. Trace must show why decision happened
4. No silent approval
5. No hidden autonomy
