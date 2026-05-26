# Implementation Options — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Option A — Add free-form mode to `demo_runner.py`

Extend frozen Demo Runner with `--free-form` or menu item 16.

| Pros | Cons |
|------|------|
| One UX entry point | **Violates demo-runner-v0.1 freeze** without change proposal |
| Operator finds everything in one script | Runner grows; harder rollback |
| Reuse parsing/summary code | Coupling to frozen artifact |

**Verdict:** **Not recommended** for v1.

---

## Option B — Separate `free_form_cli.py` (recommended)

New path: `demos/review-assistant-freeform/free_form_cli.py`

| Pros | Cons |
|------|------|
| Clean separation from frozen runner | Second script to document |
| Easier rollback | Some code duplication (trace RU maps) |
| Lower risk to demo-runner-v0.1 | Operator learns two entry points |
| Matches Phase 3.5.2 pattern (wrapper, stdlib) | |

**Verdict:** **Recommended.**

---

## Option C — Web UI

Browser form for task input + results.

| Pros | Cons |
|------|------|
| Better UX | **Rejected** — too early, UI platform drift |

**Verdict:** **Reject.**

---

## Option D — Extend `minimal_demo.py` with `--task` flag

Add free-form to agent demo directly.

| Pros | Cons |
|------|------|
| Reuses agent loop | **Modifies frozen agent artifact** |
| | Violates no-agent-logic-change for this track |

**Verdict:** **Reject** unless separate agent phase approved.

---

## Comparison summary

| Option | Freeze-safe | Rollback | Touchability | Recommendation |
|--------|-------------|----------|--------------|----------------|
| A — demo_runner extend | no | hard | high | reject |
| B — separate script | yes | easy | high | **yes** |
| C — web UI | n/a | n/a | highest | reject |
| D — minimal_demo | no | hard | high | reject |

See [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md).
