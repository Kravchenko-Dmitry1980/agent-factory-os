# Real Adapter Scenarios

System under test: `integrations-real/` adapters (mock mode default — no API keys)

Run:

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario uncertain
python integrations-real/telegram-review-gate/minimal-demo.py
python integrations-real/local-queue-worker/minimal-demo.py
python integrations-real/fastapi-review-api/minimal-demo.py
python integrations-real/filesystem-audit-log/minimal-demo.py
```

---

## Scenario: Valid Structured Output Accepted

### System Under Test

`integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy`

### Input

Mock LLM returns schema-valid JSON; verifier accepts structure (not truth).

### Expected Behavior

Parse succeeds; verification passes structurally; decision allow with reminder LLM != truth.

### Expected Event Trace

```
task_started → verification_passed → task_completed
```

### Expected Failure Mode

None — structural pass only.

### Pass Criteria

- Verification: pass
- Reminder that LLM output != truth visible

### Fail Criteria

- Structural pass treated as factual truth
- Missing untrusted_input flag in narrative

### Why This Matters

Adapter accepts format, not content — governance distinction must remain.

---

## Scenario: Malformed Output Rejected

### System Under Test

`integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed`

### Input

Invalid JSON or schema violation from LLM.

### Expected Behavior

Reject; no downstream action.

### Expected Event Trace

```
task_started → llm_malformed_output → verification_failed → governance_rejection
```

Reference: `observability/examples/malformed-llm-trace.txt`

### Expected Failure Mode

Parse/schema reject.

### Pass Criteria

- Decision: reject
- No execute/publish path

### Fail Criteria

- Best-effort parse into action
- Silent fallback to defaults

### Why This Matters

Real I/O exposes parse failures mocks hide.

---

## Scenario: Timeout Rejected

### System Under Test

`integrations-real/llm-verification-adapter/minimal-demo.py --timeout 1` (with slow/mock delay if available)

### Input

LLM call exceeds timeout budget.

### Expected Behavior

Fail-closed reject; no partial trust.

### Expected Event Trace

```
task_started → llm_timeout → verification_failed → governance_rejection
```

### Expected Failure Mode

Timeout deny.

### Pass Criteria

- Timeout event in audit
- No action on timeout

### Fail Criteria

- Infinite wait
- Timeout → use cached guess

### Why This Matters

External APIs are untrusted; hung calls must not block governance.

---

## Scenario: Uncertain Answer Escalated

### System Under Test

`integrations-real/llm-verification-adapter/minimal-demo.py --scenario uncertain`

### Input

LLM returns low-confidence or ambiguous structured response.

### Expected Behavior

Reject or escalate — not auto-approve.

### Expected Event Trace

```
task_started → verification_failed (uncertain) → escalation_triggered|governance_rejection
```

### Expected Failure Mode

Escalation or reject.

### Pass Criteria

- No auto-allow on uncertain
- Human path indicated

### Fail Criteria

- Uncertain → pass
- Confidence score ignored

### Why This Matters

Structured output can still be wrong; uncertainty must fail closed.

---

## Scenario: Telegram Gate Timeout (Real Adapter)

### System Under Test

`integrations-real/telegram-review-gate/minimal-demo.py`

### Input

Approval request; mock timeout (no real Telegram required).

### Expected Behavior

Deny-by-default consistent with prototype.

### Expected Event Trace

```
approval_requested → approval_timeout → unsafe_action_blocked
```

### Pass Criteria

- Mock mode works without token
- Timeout path documented in audit

### Fail Criteria

- Requires live Telegram for basic check
- Timeout allows action

### Why This Matters

Real adapter must preserve prototype governance in mock mode.
