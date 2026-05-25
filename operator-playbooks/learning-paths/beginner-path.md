# Beginner Path

---

## Goal

Understand what this repo is, run demos safely, read traces, avoid dangerous mistakes.

## Estimated Time

4–6 hours over 1–2 days

---

## What to Read

1. [../start-here/first-30-minutes.md](../start-here/first-30-minutes.md)
2. [../start-here/what-not-to-touch.md](../start-here/what-not-to-touch.md)
3. [../../agent-os/doctrine/system-positioning.md](../../agent-os/doctrine/system-positioning.md)
4. [../safety-guides/why-fail-closed-matters.md](../safety-guides/why-fail-closed-matters.md)
5. [../safety-guides/why-critic-is-not-truth.md](../safety-guides/why-critic-is-not-truth.md)

---

## What to Run

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python evaluation/scripts/run_demo_smoke_checks.py
```

---

## What to Avoid

- Reading all of `Books/` on day one
- Changing prototype code
- Adding automation scripts
- Treating critic pass as approval

---

## Expected Outcome

- Can explain repo purpose in 2 sentences
- Can run review-loop demo and read audit
- Knows where traces and troubleshooting live

---

## Checkpoint Questions

1. Is this a production deployment platform? (No)
2. What does fail-closed mean?
3. Where is `successful-review-trace.txt`?
4. What command runs smoke checks?

See [../onboarding/onboarding-assessment.md](../onboarding/onboarding-assessment.md)
