# No Agent Logic Change Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — **non-negotiable**

---

## Core rule

Demo Runner **may call** existing scripts.  
Demo Runner **must not change** agent behavior, scenarios, or safety logic.

---

## Demo Runner may

| Action | Detail |
|--------|--------|
| Wrap command | `subprocess.run([sys.executable, path, ...])` |
| Parse output text | Regex/lines for `decision=`, `delivered=`, TRACE |
| Summarize result | Russian operator block |
| Explain trace | Static mapping table |
| Show menu | Fixed scenario list |
| Warn before provider | Confirmation prompt |
| Save transcript | Optional flag — raw + summary |

---

## Demo Runner must not

| Forbidden | Target |
|-----------|--------|
| Change `minimal_demo.py` | Protected |
| Add scenarios | Frozen set only |
| Change decisions | DELIVERED/BLOCKED logic stays in demo |
| Change trace events | Event names emitted by demo only |
| Change approval behavior | Scenario simulation unchanged |
| Change provider behavior | Flags/env passed through only |
| Change safety harness | Eval scripts untouched |
| Patch stdout format in demo | Parse what exists today |
| Monkey-patch imports | No injection into demo process |
| Replace demo with reimplementation | Must subprocess existing file |

---

## Verification (future impl)

| Check | Method |
|-------|--------|
| `minimal_demo.py` unchanged | git diff empty on protected file |
| Same decision for scenario | Compare runner vs direct CLI output |
| Baseline scripts PASS | All 6 eval scripts unchanged results |
| No new files under review-assistant-thin/ | Except README if navigation only |

---

## If logic change needed

Stop. That is **not** Demo Runner scope — separate phase with change proposal for thin v0.4+.

---

## Diagram

See [diagrams/no-logic-change-boundary.md](diagrams/no-logic-change-boundary.md).
