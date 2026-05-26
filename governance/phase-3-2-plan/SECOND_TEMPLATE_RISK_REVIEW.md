# Second Template Risk Review — Phase 3.2

**Decision:** Second template **postponed**

---

## Why second template is postponed

| Risk | Impact |
|------|--------|
| Increases template surface | Duplicate acceptance, freeze, eval cycles |
| Increases governance burden | Two specs to keep aligned with kit |
| Creates factory illusion | "Catalog of agents" → pressure for generator |
| Dilutes Review Assistant hardening | Focus split before LLM boundary proven |
| Requires new acceptance criteria | Full template-spec compliance again |
| Pushes toward runtime | Triage/routing templates need orchestration |
| Duplication | Safe Content Draft ≈ Review Assistant variant |

---

## Option B candidate risks (summary)

| Candidate | Primary risk |
|-----------|--------------|
| Task Triage Agent | Orchestrator / router runtime |
| Safe Content Draft Agent | Duplicate Review Assistant |
| Meeting Summary Review Agent | Domain creep + LLM dependency without boundary |

---

## When second template becomes allowed

All required:

1. **Review Assistant LLM boundary safe** (mock-first at minimum) OR explicit user decision to skip LLM permanently
2. **Evaluation extended** — thin + LLM checks stable PASS
3. **Template review process stable** — first template freeze/sign-off mature
4. **No runtime/factory drift** — no shared engine extracted
5. **User explicitly approves** — e.g. «Start Phase 3.x second template spec»

Recommended order: **second template spec-only (Markdown)** before second impl.

---

## Recommended first second template (future)

**Task Triage Agent** — **spec only**, advisory routing, no execution — if user wants catalog expansion without LLM.

Not recommended next: Meeting Summary (needs LLM + PII); Safe Content Draft (duplicate).

---

## Link to decision

[RECOMMENDED_NEXT_STEP.md](RECOMMENDED_NEXT_STEP.md) — Option A first.
