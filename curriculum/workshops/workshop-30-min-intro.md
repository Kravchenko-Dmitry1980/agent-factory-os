# Workshop: 30-Minute Intro

## Audience

Complete beginners, stakeholders curious about the lab.

## Duration

30 minutes

## Goal

Orientation + one demo + one trace + smoke check — no code changes.

## Agenda

| Min | Activity |
|-----|----------|
| 0–5 | [../README.md](../README.md) — is / is NOT |
| 5–12 | Live demo review-loop happy + bypass |
| 12–18 | `observability/examples/successful-review-trace.txt` |
| 18–25 | `python evaluation/scripts/run_demo_smoke_checks.py` |
| 25–30 | [../start-here/what-not-to-touch.md](../operator-playbooks/start-here/what-not-to-touch.md) Q&A |

## Files to Open

- curriculum/README.md
- observability/examples/successful-review-trace.txt

## Commands to Run

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python evaluation/scripts/run_demo_smoke_checks.py
```

## Discussion Questions

1. Is this a product you deploy?
2. Why block bypass?
3. What is a trace?

## Expected Learning Outcome

Participant can find start-here and run one demo alone.

Mirror: [../operator-playbooks/onboarding/onboarding-workshop-30-min.md](../operator-playbooks/onboarding/onboarding-workshop-30-min.md)
