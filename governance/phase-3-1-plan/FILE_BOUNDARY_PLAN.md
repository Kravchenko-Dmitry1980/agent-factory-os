# File Boundary Plan — Phase 3.1

**Rule:** Do **not** create implementation folders during Phase 3.1-Plan.

---

## Options evaluated

### Option A — `agent-builder-kit/implementations/review-assistant-thin/`

| Pros | Cons |
|------|------|
| Close to Builder Kit and frozen template | Risks conflating **specs** with **runtime** |
| Clear Phase 3 ownership narrative | Invites `implementations/` growth → factory drift |
| Easy cross-link from template README | Kit README says “no runtime” — impl under kit blurs message |

### Option B — `prototypes-derived/review-assistant-thin/` **(recommended)**

| Pros | Cons |
|------|------|
| Clearly **derived** from prototypes, not kit runtime | Less direct visual link to builder-kit template folder |
| Keeps `agent-builder-kit/` **spec-only** | New top-level folder needs README discipline |
| Matches “Learning Lab prototype lineage” | Must document link to frozen template explicitly |
| Reduces factory / platform confusion | |

---

## Recommendation

**Option B:** `prototypes-derived/review-assistant-thin/`

**Reason:** Phase 3.1 proves one frozen template can be implemented safely. Keeping code **outside** `agent-builder-kit/` prevents the kit from becoming a runtime host too early. The implementation **implements** the frozen spec; it does not **become** the kit.

---

## Future folder layout (when implementation starts — not now)

```text
prototypes-derived/
└── review-assistant-thin/          # CREATE ONLY AFTER P1 + GO
    ├── README.md                   # links to frozen template + this plan
    ├── thin_demo.py                # or similar — single entry
    └── scenarios.md                # optional — maps to frozen evaluation.md
```

**Forbidden sibling folders (Phase 3.1):**

```text
prototypes-derived/runtime/
prototypes-derived/factory/
prototypes-derived/shared/
agent-builder-kit/implementations/   # defer unless governance reopens Option A
```

---

## Files that may be created later (implementation phase)

| Path | Allowed |
|------|---------|
| `prototypes-derived/review-assistant-thin/README.md` | yes |
| `prototypes-derived/review-assistant-thin/*.py` | yes — minimal, one entry + optional helpers in same folder |
| `governance/PHASE_3_1_IMPLEMENTATION_REVIEW.md` | yes — after impl |
| New tests under impl folder only | yes — if no changes to `evaluation/scripts/` |

---

## Files that must remain frozen (no semantic edits)

All 12 files under:

`agent-builder-kit/templates/review-assistant-agent/`

(except navigation links via change proposal / sign-off metadata)

Sign-off bundle: append-only for implementation review records.

---

## Protected folders — never modify in Phase 3.1

| Path | Reason |
|------|--------|
| `prototypes/` | Canonical Phase 2 reference demos |
| `integrations-real/` | Real adapters — separate lifecycle |
| `evaluation/scripts/` | Shared harness — do not weaken |
| `observability/examples/` | Canonical trace examples |
| `Books/` | Source corpus |
| `experiments/` | Research perimeter |
| Frozen template body | CHANGE_LOCK applies |

---

## Linking strategy

Impl `README.md` must link:

- Frozen template: `agent-builder-kit/templates/review-assistant-agent/`
- This plan: `governance/phase-3-1-plan/`
- Reference prototype (read-only): `prototypes/review-loop-agent/`

Do **not** import from `prototypes/` as a library — **copy patterns** into impl folder if needed.

---

## Decision record

| Field | Value |
|-------|-------|
| Selected path | `prototypes-derived/review-assistant-thin/` |
| Created | **no** — plan only |
| Revisit Option A | Only via governance change proposal |
