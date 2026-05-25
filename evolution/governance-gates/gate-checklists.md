# Gate Checklists

Use before merging governed code changes.

## Promotion Gate

- [ ] Follows `governance/PROMOTION_STRATEGY.md`
- [ ] No stage skipping
- [ ] Provenance documented
- [ ] Not direct experiment → agent-os copy

## Approval Gate

- [ ] External actions still require explicit approve
- [ ] Timeout = deny-by-default unchanged
- [ ] Fingerprint binding preserved (Telegram/external)

## Verification Gate

- [ ] critic still advisory only
- [ ] LLM output still ≠ truth
- [ ] GUI A/B/C before execute
- [ ] Malformed output still rejects

## Escalation Gate

- [ ] MAX_RETRIES documented
- [ ] `escalation_triggered` on ceiling
- [ ] No silent drop after exhaustion

## Rollback Gate

- [ ] Rollback steps written
- [ ] Revert command/path known
- [ ] Failure scenarios pass after rollback test

## Observability Gate

- [ ] Canonical events still map
- [ ] Example trace updated if user-visible
- [ ] No metric-only failure signaling added

## All Gates Pass?

Proceed. Any fail → rollback or reject change.
