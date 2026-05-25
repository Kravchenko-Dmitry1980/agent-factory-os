# Critical Behavior Matrix

Behaviors that **must never regress** without explicit governance approval.

| ID | Critical behavior | Invariant | Demo |
|----|-------------------|-----------|------|
| CB-01 | Deny-by-default | No approval → no action | fail-closed-external-action |
| CB-02 | Human final on publish | critic != truth | review-loop-agent |
| CB-03 | Verification before writeback | no unverified memory | bounded-memory-agent |
| CB-04 | Bounded retries | max enforced | queue-orchestration |
| CB-05 | Escalation at ceiling | no silent fail | escalation-workflow |
| CB-06 | GUI visual gate | no unverified click | gui-verification-loop |
| CB-07 | LLM untrusted input | malformed → reject | llm-verification-adapter |
| CB-08 | Provenance for promotion | no source → reject | promotion-pipeline-simulator |
| CB-09 | Append-only audit | events not deleted | filesystem-audit-log |
| CB-10 | Bypass blocked | no shortcut publish | review-loop bypass-attempt |

---

## Severity If Broken

| ID | Severity | Why |
|----|----------|-----|
| CB-01 | Critical | Direct autonomy leak |
| CB-02 | Critical | False external content |
| CB-03 | High | Memory poisoning |
| CB-04 | High | Masks bugs |
| CB-05 | High | Invisible failures |
| CB-06 | Critical | Real GUI damage |
| CB-07 | High | Trust transfer bug |
| CB-08 | Medium | Corpus quality |
| CB-09 | High | No accountability |
| CB-10 | Critical | Gate elimination |

---

## Minimum Check Per Release (Local)

Re-run smoke checks + one scenario per touched CB-ID.
