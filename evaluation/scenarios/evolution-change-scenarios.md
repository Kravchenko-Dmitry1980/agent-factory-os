# Evolution & Change Scenarios

System under test: governance invariants across `prototypes/`, `integrations-real/`, `evolution/`

These are **review scenarios** — not automated tests. Apply before/after any change.

Reference: `evolution/governance-gates/`, `evolution/examples/`

---

## Scenario: Retry Limit Increase Regression

### System Under Test

Any change touching retry constants in queue demos or adapters.

### Input

Diff increases `MAX_RETRIES` or removes exhaustion check.

### Expected Behavior

After change: retry ceiling scenario still stops at original limit unless explicit governance approval.

### Expected Event Trace

Must still include: `retry_exhausted` → `escalation_triggered`

### Expected Failure Mode

If ceiling removed — governance regression.

### Pass Criteria

- Escalation trace unchanged in meaning
- `evolution/examples/unsafe-retry-increase.md` patterns avoided

### Fail Criteria

- Silent retry increase
- Exhaustion event removed from code path

### Why This Matters

Most common "small" change that erodes safety.

---

## Scenario: Auto-Approve Shortcut Regression

### System Under Test

Changes to review-loop, fail-closed, or telegram gate.

### Input

Code path skips `approval_requested` for "internal" or "low risk" actions.

### Expected Behavior

All external/high-risk paths still require approval.

### Expected Event Trace

No publish without `approval_requested` → human decision.

### Expected Failure Mode

Hidden autonomy — see `evolution/examples/accidental-auto-approve.md`

### Pass Criteria

- Bypass scenario still blocks
- Audit chain intact

### Fail Criteria

- New shortcut without gate
- Conditional auto-approve

### Why This Matters

Autonomy leaks through exceptions, not rewrites.

---

## Scenario: Verification Skip Regression

### System Under Test

Changes to LLM adapter or verification gates.

### Input

"Fast path" that skips verifier on cached response.

### Expected Behavior

Malformed and uncertain scenarios still reject.

### Expected Event Trace

`llm_malformed_output` and `verification_failed` still reachable.

### Expected Failure Mode

Verification bypass.

### Pass Criteria

- Malformed scenario still fails after change
- No new default-allow branch

### Fail Criteria

- Trust cache without re-verify
- Remove malformed handling

### Why This Matters

Speed optimizations are the #1 verification killer.

---

## Scenario: Shared Runtime Platform Drift

### System Under Test

New `shared/` modules or cross-demo orchestration.

### Input

Extract "common engine" used by multiple prototypes.

### Expected Behavior

Demos remain independent; no universal runtime.

### Expected Event Trace

N/A — architecture review.

### Expected Failure Mode

Platform emergence — see `evolution/examples/unsafe-shared-runtime.md`

### Pass Criteria

- Each demo runnable alone
- No plugin/registry pattern

### Fail Criteria

- Shared orchestrator
- Demo depends on hidden framework

### Why This Matters

Evaluation must catch framework drift before it becomes "the way we run things."

---

## Scenario: Escalation Removal Regression

### System Under Test

Escalation workflow and queue worker.

### Input

Change maps `retry_exhausted` directly to `task_failed` without escalation.

### Expected Behavior

Human escalation path preserved.

### Expected Event Trace

`retry_exhausted → escalation_triggered` required.

Reference: `evolution/examples/escalation-removal-disaster.md`

### Pass Criteria

- Escalation scenario passes manual review
- No silent terminal fail

### Fail Criteria

- Escalation event deleted
- Supervisor path unreachable

### Why This Matters

Removing escalation makes failures invisible to humans.

---

## Scenario: Observability Regression After Change

### System Under Test

Any code change + `observability/examples/` trace comparison.

### Input

Re-run demo; compare audit output to prior baseline trace.

### Expected Behavior

Critical events still present; no silent gate removal.

### Expected Event Trace

Compare using `evaluation/trace-comparison/trace-diff-checklist.md`

### Expected Failure Mode

Missing events = governance regression.

### Pass Criteria

- Required events still appear
- OUTCOME block still readable

### Fail Criteria

- Fewer audit events with same flow
- Generic logs replace named events

### Why This Matters

If trace cannot explain decision, governance is already broken.
