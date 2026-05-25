# Phase 3 — Start Conditions

**Purpose:** exact checklist before the **first Phase 3 prompt** (Agent Builder Kit v0.1).

**Phase 2.9 does NOT start Phase 3** — it only makes conditions visible.

---

## Required before Phase 3.0 (any work)

User (Dmitry / lead) **confirms in writing**:

| # | Confirmation |
|---|--------------|
| C1 | Phase 3 = **specs / templates / checklists only** (MD) |
| C2 | **No runtime** in Phase 3.0 |
| C3 | **No agent factory** yet |
| C4 | First template = **Review Assistant Agent** |
| C5 | **No CV** / **no digital twin** in Phase 3.0 |
| C6 | **No code generator** by default |
| C7 | Evaluation + governance docs **referenced** in kit |
| C8 | [PHASE_3_WARNING_RU.md](../PHASE_3_WARNING_RU.md) read |

Technical baseline (re-run before Phase 3 prompt):

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Expect: smoke `PASS=12 FAIL=0`, trace `PASS=6 FAIL=0`.

---

## Required before Phase 3 **implementation** (code / folders)

In addition to C1–C8:

| # | Gate |
|---|------|
| H1 | Mentor pass: operator or developer assessment |
| H2 | Lead pass: project-lead assessment |
| H3 | Architect co-sign: phase-3-readiness assessment |
| H4 | [phase-2-8/PHASE_3_FREEZE_POLICY.md](phase-2-8/PHASE_3_FREEZE_POLICY.md) acknowledged |
| H5 | Explicit user message: «start Phase 3.0 implementation» |

Until H1–H5: **do not create** `agent-builder-kit/` or `.py` stubs.

---

## First Phase 3 deliverables **allowed** (after C1–C8 + user OK)

Only these paths (no other architecture):

```
agent-builder-kit/README.md
agent-builder-kit/template-specs/
agent-builder-kit/safety-gates/
agent-builder-kit/evaluation-checklists/
agent-builder-kit/templates/review-assistant-agent/
governance/PHASE_3_0_BUILDER_KIT_REVIEW.md
```

Optional bilingual RU summary inside kit (user choice).

**Not allowed in first deliverable batch:**

- `agent-builder-kit/runtime/`
- `agent-builder-kit/generator/`
- swarm / twin / CV folders
- new dependencies in `requirements.txt`

---

## Explicit approval required for

| Action | Approver |
|--------|----------|
| Any **Python** code in kit | User |
| Any **generator** | User |
| Any **reusable framework** package | User |
| Any **production** adapter enablement | User + lead |
| CV template spec **implementation** | User — future phase |
| Digital twin template **implementation** | User — future phase |
| Modifying `prototypes/` or `evaluation/scripts/` | User — out of Phase 3 scope |

---

## Quick NO-GO

Stop if prompt asks for:

- LangGraph, MCP server, RAG index
- «Ship MVP», «factory ready»
- Merge all demos into one engine
- Skip smoke for «speed»

Full list: [phase-2-8/PHASE_3_DO_NOT_BUILD_LIST.md](phase-2-8/PHASE_3_DO_NOT_BUILD_LIST.md)

---

## Related

- [phase-2-8/PHASE_3_GO_NO_GO.md](phase-2-8/PHASE_3_GO_NO_GO.md)
- [curriculum/ru/methodology/phase-3-entry-criteria.md](../curriculum/ru/methodology/phase-3-entry-criteria.md)
- [../START_HERE_RU.md](../START_HERE_RU.md)
