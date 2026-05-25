# Onboarding Workshop (30 min)

Facilitator guide for live session.

---

## Agenda

| Min | Activity |
|-----|----------|
| 0–5 | Present [../README.md](../README.md) — is / is NOT |
| 5–12 | Live run review-loop happy + bypass |
| 12–18 | Open `successful-review-trace.txt` — walk events |
| 18–25 | Run smoke check together |
| 25–30 | Read [../start-here/what-not-to-touch.md](../start-here/what-not-to-touch.md) + Q&A |

---

## Facilitator commands

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python evaluation/scripts/run_demo_smoke_checks.py
```

---

## Key talking points

- Critic != truth
- Fail-closed on bypass
- Smoke is local, not CI

---

## Handout

[../start-here/first-30-minutes.md](../start-here/first-30-minutes.md)
