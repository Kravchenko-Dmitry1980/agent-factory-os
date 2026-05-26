# Change Lock — Review Assistant Thin v0.1

Any change to **frozen implementation files** (see [IMPLEMENTATION_MANIFEST.md](IMPLEMENTATION_MANIFEST.md)) requires:

1. **Change proposal** — what/why/impact
2. **Impact analysis** — scenarios affected, spec alignment
3. **Evaluation run** — 5 scenarios + `check_review_assistant_thin.py` + Phase 2 smoke/trace
4. **Trace comparison** — before/after vs [SCENARIO_BASELINE.md](SCENARIO_BASELINE.md)
5. **Rollback plan** — [ROLLBACK_RECORD.md](ROLLBACK_RECORD.md)
6. **Explicit approval** — user/lead message

---

## Forbidden without new phase

| Change | Why blocked |
|--------|-------------|
| LLM API | Scope expansion |
| Interactive CLI approval | Separate approval |
| Telegram / FastAPI | Production adapter |
| Persistent memory | Template v0.1 forbids |
| Runtime / factory / second agent | Phase 3.1 scope |
| Shared framework extraction | Platform drift |

---

## Allowed without unfreeze (non-semantic)

- Typo fixes in docs (no behavior change)
- Navigation links
- Freeze/evaluation metadata append
- `evaluation/scripts/check_review_assistant_thin.py` baseline string updates if trace format typo-only

---

## Frozen spec

`agent-builder-kit/templates/review-assistant-agent/` — **separate** CHANGE_LOCK. Do not edit spec to match impl drift.

---

## Version bump

Semantic behavior change → v0.2 + new freeze record.
