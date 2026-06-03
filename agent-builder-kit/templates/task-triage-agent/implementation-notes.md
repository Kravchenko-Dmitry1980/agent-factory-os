# Task Triage Agent — Implementation Notes

**Status:** SPEC_DRAFT

---

## Current state

**No implementation exists yet.**

This folder contains Markdown specifications only. There is:

- no Python or JavaScript code
- no thin demo in `prototypes-derived/`
- no evaluation script
- no provider boundary
- no runtime or factory

---

## Do not implement from this file

This document describes a **future path** only. Do not write code, create demos, or call providers based on this file without explicit governance approval and sign-off.

---

## Future implementation discipline

Future implementation must follow the same discipline as Review Assistant:

```text
Specs (this template)
  → Freeze / sign-off
  → Plan thin implementation
  → Thin implementation
  → Harden
  → Freeze
```

---

## Recommended future path

| Phase | Activity | Gate |
|-------|----------|------|
| **Phase 3.5-Freeze** | Freeze Task Triage specs v0.1 | Sign-off bundle |
| **Phase 3.6-Plan** | Thin implementation plan | GO/NO-GO — no code |
| **Phase 3.6-Impl** | Thin implementation | Only if approved |
| **Phase 3.6.x** | Harden + eval script | Baseline regression green |
| **Future** | Optional mock/provider | Separate phase |

---

## Thin implementation constraints (future)

When/if approved, thin impl must:

| Constraint | Detail |
|------------|--------|
| Location | `prototypes-derived/task-triage-agent/` — separate folder |
| Deterministic first | Rule-based classifier before any LLM |
| No orchestrator | No routing, queue, delegation |
| No execution | No files, commands, APIs |
| No provider by default | Mock/rules only in first slice |
| Trace required | Match [expected-traces.md](expected-traces.md) |
| Eval script | Mirror Review Assistant check scripts |
| Baseline green | All Review Assistant checks PASS |

---

## Reference chain (do not break)

```text
Review Assistant template (frozen)
  → review-assistant-thin v0.1 / v0.2 / v0.3 (frozen)
  → provider safety harness v0.1 (frozen)
  → Task Triage template (this — SPEC_DRAFT)
  → [future] task-triage thin
```

Task Triage implementation must not modify frozen Review Assistant artifacts.

---

## Pre-implementation checklist

Before any code:

- [ ] Phase 3.5-Freeze complete — specs signed off
- [ ] Phase 3.6-Plan GO/NO-GO = GO
- [ ] Pre-flight baselines PASS
- [ ] Change proposal approved
- [ ] Eval cases from [evaluation.md](evaluation.md) ready
- [ ] Rollback plan documented

---

## Explicit warning

**Do not implement from this file.**

Wait for Phase 3.5-Freeze sign-off and Phase 3.6-Plan approval.
