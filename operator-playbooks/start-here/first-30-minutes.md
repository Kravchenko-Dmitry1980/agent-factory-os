# First 30 Minutes

A safe, bounded introduction. No prior AI architecture knowledge required.

---

## Goal

Leave with: orientation, one successful demo run, one trace read, one evaluation check, clear "do not touch" list.

**Time:** ~30 minutes

---

## Minute 0–5: Orientation

1. Read [operator-playbooks/README.md](../README.md) — skim "This project is / is NOT"
2. Read [agent-os/doctrine/system-positioning.md](../../agent-os/doctrine/system-positioning.md) — focus on "What Agent-OS IS NOT"

**Checkpoint:** Can you name two things this repo explicitly rejects? (e.g. AGI platform, production orchestration runtime)

---

## Minute 5–15: Run One Demo

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

Read the output. Notice:

- Critic gives advisory pass — not final truth
- Human decision required
- Audit log at the bottom

Optional second run (fail path):

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

Expect: `Published: False` — bypass blocked.

Full commands: [../runbooks/run-prototypes.md](../runbooks/run-prototypes.md)

---

## Minute 15–22: Read One Trace

Open: `observability/examples/successful-review-trace.txt`

Look for:

- Event names (`task_started`, `approval_requested`, `task_completed`)
- OUTCOME line at bottom
- GOVERNANCE summary

Compare mentally with demo audit you just saw.

Guide: [../runbooks/run-observability-examples.md](../runbooks/run-observability-examples.md)

---

## Minute 22–27: Run Evaluation Smoke

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

Expect mostly `PASS`. This is a **local check**, not CI.

If FAIL: see [../troubleshooting/evaluation-fails.md](../troubleshooting/evaluation-fails.md) — do not panic.

---

## Minute 27–30: What Not to Touch

Read: [what-not-to-touch.md](what-not-to-touch.md)

**Minimum takeaway:**

- Do not turn prototypes into a framework
- Do not skip approval gates "temporarily"
- Do not add CI/automation without a new explicit phase

---

## Done?

Next: [first-2-hours.md](first-2-hours.md) or pick [../learning-paths/beginner-path.md](../learning-paths/beginner-path.md)
