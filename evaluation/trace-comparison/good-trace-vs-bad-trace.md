# Good Trace vs Bad Trace

Educational pairs — learn to spot governance in traces.

---

## Example 1: Happy Review (GOOD)

```text
[19:56:59] task_started         actor=queue
[19:56:59] verification_passed  actor=critic      advisory=true
[19:56:59] approval_requested   actor=human       required=true
[19:56:59] verification_passed  actor=human       decision=approve
[19:56:59] task_completed       actor=publisher
OUTCOME status=completed
GOVERNANCE gates_passed=3 escalated=no
```

**Why good:** Human gate visible; critic marked advisory; completion last.

---

## Example 1b: Critic-Only Publish (BAD)

```text
[19:56:59] task_started         actor=queue
[19:56:59] verification_passed  actor=critic
[19:56:59] task_completed       actor=publisher
OUTCOME status=completed
```

**Why bad:** No approval_requested; critic treated as final authority.

---

## Example 2: Approval Denied (GOOD)

```text
[19:57:10] approval_requested   actor=human
[19:57:11] approval_denied      actor=human       reason=critic_disagreement
[19:57:11] task_failed          actor=system
OUTCOME status=rejected
```

**Why good:** Human disagreement captured; no publish.

Source: `observability/examples/failed-review-trace.txt`

---

## Example 2b: Silent Reject (BAD)

```text
[19:57:10] task_started
[19:57:11] task_failed          actor=system      reason=error
```

**Why bad:** Cannot tell if human, critic, or bug caused failure.

---

## Example 3: Escalation (GOOD)

```text
[19:57:09] retry_exhausted      actor=system      max=3
[19:57:09] escalation_triggered actor=supervisor
[19:57:09] unsafe_action_blocked actor=gate
OUTCOME status=escalated escalated=yes
```

**Why good:** Ceiling visible; escalation explicit; auto-complete blocked.

---

## Example 3b: Silent Exhaustion (BAD)

```text
[19:57:09] task_failed          actor=worker
OUTCOME status=failed
```

**Why bad:** Retries invisible; escalation missing; looks like simple error.

---

## Example 4: LLM Malformed (GOOD)

```text
[20:02:18] llm_malformed_output actor=verifier
[20:02:18] verification_failed  actor=verifier    untrusted_input=true
[20:02:18] governance_rejection actor=gate
REMINDER: LLM output != truth
```

**Why good:** Untrusted input explicit; no downstream execute.

---

## Example 4b: Parse And Pray (BAD)

```text
[20:02:18] task_started         actor=llm
[20:02:18] task_completed       actor=workflow
```

**Why bad:** Malformed handling invisible; looks like success.

---

## Quick Visual Checklist

| Good trace has | Bad trace lacks |
|----------------|-----------------|
| Named gate events | Generic "error" |
| Actor attribution | Anonymous failures |
| OUTCOME + GOVERNANCE | Exit code only |
| Deny reason | Silent block |
| advisory=true on critic | Critic as truth |
