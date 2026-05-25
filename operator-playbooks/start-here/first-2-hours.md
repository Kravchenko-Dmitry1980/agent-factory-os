# First 2 Hours

Build on the 30-minute intro with breadth across demos, traces, and safety concepts.

---

## Goal

Run 3–4 demos, read 2 traces, understand fail-closed + approval, run full evaluation status.

**Time:** ~2 hours

---

## Hour 1: Core Demos

Run in order (15 min each including reading output):

```powershell
# 1. Review loop (already done in 30-min — optional repeat)
python prototypes/review-loop-agent/minimal-demo.py --scenario happy

# 2. Fail-closed external action
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval

# 3. Bounded memory
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow

# 4. Queue retries
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
```

After each run, read the audit section. Ask: **what would happen if this gate were removed?**

Scenario guides: [../scenario-guides/](../scenario-guides/)

---

## Hour 1:30 — Traces

Read both:

- `observability/examples/failed-review-trace.txt` — human catches critic mistake
- `observability/examples/escalation-trace.txt` — retries stop, escalation happens

Use: [../runbooks/run-observability-examples.md](../runbooks/run-observability-examples.md)

---

## Hour 1:45 — Safety (Short Reads)

Skim these (5 min each):

- [../safety-guides/why-critic-is-not-truth.md](../safety-guides/why-critic-is-not-truth.md)
- [../safety-guides/why-fail-closed-matters.md](../safety-guides/why-fail-closed-matters.md)

---

## Hour 2 — Evaluation

```powershell
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

Read: [../runbooks/run-evaluation-checks.md](../runbooks/run-evaluation-checks.md)

---

## Checkpoint Questions

1. What happens when approval is missing in fail-closed demo?
2. What event appears when retries hit the ceiling?
3. Why is critic pass not enough to publish?

Answers: [../onboarding/onboarding-assessment.md](../onboarding/onboarding-assessment.md)

---

## Next

[first-day.md](first-day.md) or role-specific [../learning-paths/](../learning-paths/)
