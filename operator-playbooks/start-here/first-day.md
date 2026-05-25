# First Day

A full orientation day for someone who will work with this repository regularly.

---

## Goal

Navigate all major layers, run representative demos, understand change + evaluation loop, know where to get help.

**Time:** 6–8 hours (with breaks)

---

## Morning: Knowledge Layer (2–3 hr)

| Block | Activity |
|-------|----------|
| Doctrine | Read `agent-os/doctrine/canonical-principles.md`, `verification-first.md`, `fail-closed-execution.md` |
| Patterns | Skim `agent-os/08_patterns/index.md` — pick 2 patterns |
| Anti-patterns | Skim `agent-os/09_antipatterns/index.md` — pick 2 anti-patterns |
| Governance | Read `governance/PROMOTION_STRATEGY.md` intro — how ideas enter agent-os |

Do not try to memorize everything. Focus on **invariants**: verify first, fail closed, bounded memory, human approval.

---

## Midday: Run Everything Once (2 hr)

Follow [../runbooks/run-prototypes.md](../runbooks/run-prototypes.md) — all six core prototypes.

Then one integration workflow:

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario happy
```

Optional real adapter (mock mode):

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
```

Checklists: [../operator-checklists/before-running-demo.md](../operator-checklists/before-running-demo.md)

---

## Afternoon: Observability + Evaluation (1.5 hr)

- Read all six files in `observability/examples/`
- Read `observability/event-taxonomy/canonical-events.md`
- Run all three evaluation scripts
- Skim `evaluation/regression-matrix/regression-matrix.md`

---

## Late Afternoon: Change Discipline (1 hr)

Read:

- [../change-guides/how-to-change-safely.md](../change-guides/how-to-change-safely.md)
- `evolution/README.md`
- [../safety-guides/why-platform-drift-is-dangerous.md](../safety-guides/why-platform-drift-is-dangerous.md)

---

## End of Day: Assessment

Complete [../onboarding/onboarding-assessment.md](../onboarding/onboarding-assessment.md) — self-check, no grading system.

Pick your path:

- Developer → [../learning-paths/ai-architect-path.md](../learning-paths/ai-architect-path.md)
- Cursor user → [../learning-paths/cursor-operator-path.md](../learning-paths/cursor-operator-path.md)
- Intern → [../learning-paths/intern-onboarding-path.md](../learning-paths/intern-onboarding-path.md)
- Lead → [../learning-paths/project-lead-path.md](../learning-paths/project-lead-path.md)

---

## Report Problems

If something fails and you cannot fix in 30 min:

1. Save command + error output
2. Check [../troubleshooting/](../troubleshooting/)
3. Do not patch shared gates blindly
4. Note in local notes or tell project lead — no required ticket system
