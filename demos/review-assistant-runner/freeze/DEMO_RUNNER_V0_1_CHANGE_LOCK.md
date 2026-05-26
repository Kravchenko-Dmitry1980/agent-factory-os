# Demo Runner v0.1 — Change Lock

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26  
**Effective:** After Phase 3.5.2-Freeze

---

## Locked artifact

`demos/review-assistant-runner/demo_runner.py` — behavior frozen as v0.1.

---

## Required before any change

1. **Change proposal** — what changes and why
2. **UX impact review** — operator confusion risk
3. **No-agent-logic-change review** — confirm `minimal_demo.py` and eval scripts untouched
4. **Real provider policy review** — if item 9 or confirmation flow changes
5. **Transcript safety review** — if `--save-transcript` behavior changes
6. **Validation run** — runner checks + all baseline scripts
7. **Rollback plan** — see [DEMO_RUNNER_V0_1_ROLLBACK_RECORD.md](DEMO_RUNNER_V0_1_ROLLBACK_RECORD.md)
8. **Explicit approval** — governance sign-off

---

## Forbidden without new phase

| Change | Reason |
|--------|--------|
| Add dependencies (click, typer, rich, etc.) | Stdlib-only boundary |
| Add UI / web app / Operator Console | Scope drift |
| Dynamic plugin system / scenario registry | Framework drift |
| Change Review Assistant agent logic | Protected artifact |
| Provider calls by default | Safety boundary |
| Add new menu scenarios | Requires menu baseline update |
| Free-form task input | New product surface |
| Saved session browser | New product surface |
| Runtime / factory behavior | Platform drift |
| Modify protected folders | Governance violation |

Protected folders (do not modify via runner work):

- `prototypes-derived/review-assistant-thin/`
- `evaluation/scripts/`
- `prototypes/`, `integrations-real/`, frozen specs

---

## Allowed without unlocking v0.1

| Change | Condition |
|--------|-----------|
| Navigation markdown updates | Links/status only |
| New freeze docs for v0.2+ | New version, not silent edit |
| Operator transcript files | Local `transcripts/` only |

---

## Version bump rule

Behavior change → new version (e.g. v0.2) + new freeze record. Do not silently mutate v0.1 baseline.
