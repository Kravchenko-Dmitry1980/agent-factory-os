# Digital Twin — Defer Decision

**Decision:** Digital twins are **NOT** Phase 3.0. **NOT** Phase 3.1 default.

---

## Why defer

Digital twins require capabilities absent from Learning Lab:

| Capability | Repo status |
|------------|-------------|
| Persistent identity | Doctrine only — no runtime |
| Versioned memory | bounded-memory teaches limits — not twin lifecycle |
| Replay | Not implemented |
| Skill graph | graph/ direction only — no DB |
| Long-horizon audit | Trace examples — not years of lineage |
| Human approval on identity changes | Partial via approval demos |
| Rollback of identity state | Evolution docs — not twin rollback |
| Long-term evaluation | Local smoke only |

---

## Allowed in Phase 3

- Mention as **future direction** in kit README
- Map required capabilities (checklist)
- Link `agent-os/06_digital-twins/` as **reading only**
- Curriculum continues to say «not yet»

---

## Not allowed in Phase 3.0

| Forbidden | Reason |
|-----------|--------|
| Digital twin template | Incomplete foundations |
| Digital twin builder | Factory scope |
| Personality clone | Safety + ethics |
| Self-evolving identity | Uncontrolled drift |
| Autonomous profile agent | HITL violation |

---

## When to revisit

After:

1. Review Assistant template accepted
2. Second template (triage or draft) accepted
3. Factory **discussed** but not built
4. User explicitly opens «Digital Twin Phase» with new freeze review

Estimated: **post–Builder Kit v1**, not Phase 3.0.

---

## Risk if not deferred

Stakeholders conflate «agent» with «digital twin» → skip gates → platform drift → NO-GO for safety mission.
