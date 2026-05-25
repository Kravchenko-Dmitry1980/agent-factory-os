# CV Agent — Future Decision (Not Phase 3.0)

**Decision:** CV agents are **possible later**; **forbidden** as first Agent Builder Kit template.

First template: **Review Assistant Agent** (text-only).

---

## Why not Phase 3.0 first template

| Factor | Issue |
|--------|-------|
| Image/video evidence | gui-verification is mock — not production CV |
| bbox/mask validation | Not in repo |
| Model confidence | Misleading without calibration |
| Human review | Required — harder to standardize in v0.1 |
| Evidence frames | No storage contract |
| Evaluation | Harder than text smoke |
| Data quality | Out of lab scope |

---

## Allowed in Phase 3

- Future planning note in kit docs
- **CV template requirements list** (contracts below) — MD only
- Link `agent-os/09_antipatterns/unverified-gui-clicks.md`
- No YOLO/medical/video implementation

---

## Not allowed in Phase 3.0

- YOLO agent builder
- Medical image agent
- Production CV pipeline
- Video tracking agent factory
- CV as mandatory kit module

---

## Future CV Agent Template — required contracts (spec-only)

When user approves a future CV phase, template must define:

| Contract | Content |
|----------|---------|
| **Input** | Image/video source, resolution, frame rate limits |
| **Model** | Model id, version, confidence threshold, fail-closed on low confidence |
| **Evidence** | Stored frames, bbox/mask artifacts, hashes |
| **Verification** | Rule: no action on frame without fresh capture; mismatch = deny |
| **Human review** | When human must confirm detection |
| **Output** | Structured result — not raw model JSON as truth |
| **Audit** | Per-frame decision lineage in trace |

---

## Relation to current repo

`prototypes/gui-verification-loop/` teaches **visual verification discipline** — not CV factory.

Use it in curriculum; do not expand into CV builder in Phase 3.0.

---

## Sequencing

1. Review Assistant template (Phase 3.0)
2. Task Triage or Safe Draft (Phase 3.1)
3. GUI verify template enhancement (mock)
4. CV agent template spec (user-approved phase, evidence layer ready)
