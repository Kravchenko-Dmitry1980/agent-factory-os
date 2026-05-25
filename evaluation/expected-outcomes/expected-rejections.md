# Expected Rejections

Explicit rejection outcomes — distinct from escalation and from silent failure.

---

## Rejection Categories

| Category | Trigger | Terminal event |
|----------|---------|----------------|
| Human reject | Explicit deny | approval_denied, task_failed |
| Governance reject | Policy/provenance | governance_rejection |
| Verification reject | Failed gate | verification_failed |
| LLM reject | Malformed/timeout | llm_malformed_output, llm_timeout |
| Memory reject | Unverified/overflow | memory_write_rejected |
| GUI reject | Mismatch/uncertain | unsafe_action_blocked |
| Promotion reject | Missing evidence | governance_rejection |

---

## Expected Rejection Semantics

```text
REJECT = terminal for this attempt
REJECT ≠ retry forever
REJECT ≠ silent skip
REJECT must appear in audit with reason
```

---

## By Scenario

### Bad Draft / Human Deny

```text
expected decision = DENY
expected event = approval_denied
expected outcome = no publish
expected status = rejected
```

### Malformed LLM

```text
expected decision = REJECT
expected event = llm_malformed_output, verification_failed, governance_rejection
expected outcome = no downstream trust
REMINDER: even valid parse ≠ truth
```

### Missing Provenance (Promotion)

```text
expected decision = REJECT
expected event = governance_rejection
expected outcome = no promotion candidate
```

### Unsupported Claim

```text
expected decision = REJECT
expected event = verification_failed or governance_rejection
expected outcome = human review required or hard stop
```

### Bypass Attempt

```text
expected decision = DENY
expected event = unsafe_action_blocked or verification_failed
expected outcome = publish blocked
```

---

## Rejection vs Escalation

| | Rejection | Escalation |
|---|-----------|------------|
| Automation | stops | stops |
| Human | optional follow-up | required follow-up |
| Typical cause | hard deny, policy | exhaustion, ambiguity |
| Retry | new attempt only with explicit reset | supervisor path |

---

## Fail Criteria (Rejection Handling)

- Rejection without reason string
- Rejection without audit event
- Rejection logged but action still executed
- Rejection converted to warning only
