# Trace Regression Examples

Before/after change narratives — manual comparison exercises.

---

## Regression 1: Retry Limit Creep

**Before change:**

```text
retry_triggered retry=1
retry_triggered retry=2
retry_triggered retry=3
retry_exhausted max=3
escalation_triggered
```

**After change (REGRESSION):**

```text
retry_triggered retry=1
...
retry_triggered retry=5
task_completed
```

**Verdict:** FAIL — ceiling removed or increased without governance review.

**Fix:** Revert; file change proposal in `evolution/change-proposals/`.

---

## Regression 2: Auto-Approve Leak

**Before:**

```text
approval_requested actor=human
verification_passed actor=human decision=approve
task_completed
```

**After (REGRESSION):**

```text
verification_passed actor=critic
task_completed actor=publisher
```

**Verdict:** FAIL — human gate removed from trace.

---

## Regression 3: Audit Thinning

**Before:** 6 audit lines with gate names  
**After:** 2 lines — `started`, `done`

**Verdict:** FAIL — observability regression; cannot audit decisions.

See `observability/human-readable-logs/anti-pattern-logging.md`.

---

## Regression 4: LLM Fast Path

**Before:**

```text
llm_malformed_output
verification_failed
governance_rejection
```

**After (REGRESSION):**

```text
task_started
task_completed
```

Malformed scenario now exits 0 without reject events.

**Verdict:** FAIL — verification bypass.

---

## Regression 5: Memory Silent Truncate

**Before:**

```text
memory_write_rejected reason=over_limit
```

**After (REGRESSION):**

```text
(memory write succeeds with truncated content, no event)
```

**Verdict:** FAIL — fail-open on overflow.

---

## How To Use These Examples

1. Pick scenario affected by your change
2. Save baseline trace (copy demo output to `evaluation/reports/` locally — not committed required)
3. Apply change
4. Re-run demo
5. Compare using `trace-diff-checklist.md`
6. If regression → rollback first (`evolution/rollback-thinking/`)
