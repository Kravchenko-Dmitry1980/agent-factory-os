# Change Lock — Review Assistant Thin v0.2

After v0.2 freeze, any change to **frozen implementation files** (see [V0_2_IMPLEMENTATION_MANIFEST.md](V0_2_IMPLEMENTATION_MANIFEST.md)) requires:

1. **Change proposal** — what/why/impact
2. **Impact analysis** — scenarios affected (all 10), spec alignment
3. **Security review** — especially if touching LLM boundary
4. **Evaluation run** — all 4 check scripts (thin, llm mock, smoke, trace)
5. **Trace comparison** — before/after vs [V0_2_SCENARIO_BASELINE.md](V0_2_SCENARIO_BASELINE.md)
6. **Rollback plan** — [V0_2_ROLLBACK_RECORD.md](V0_2_ROLLBACK_RECORD.md)
7. **Explicit approval** — user/lead message

---

## Forbidden without new phase

| Change | Why blocked |
|--------|-------------|
| Real OpenAI / Anthropic / external API | Scope expansion; requires Phase 3.3+ approval |
| Provider abstraction framework | Platform drift |
| Model router / registry | Platform drift |
| RAG / MCP / CV / digital twin | Out of scope |
| Persistent memory | Template v0.1 forbids |
| Second agent / second template | Phase 3 scope |
| Runtime / factory / generator | Explicitly excluded |
| Auto-publish | Safety violation |
| Hidden tool execution from LLM output | Safety violation |
| Interactive CLI approval | Separate approval |
| Telegram / FastAPI service | Production adapter |
| Shared framework extraction | Platform drift |

---

## v0.2-specific lock

| Item | Rule |
|------|------|
| Mock LLM boundary | Frozen — change only via proposal |
| 5 LLM mock scenarios | Frozen expected decisions and events |
| llm_boundary.md | Frozen with impl |
| Real provider | **Not approved** — mock remains default |

---

## Allowed without unfreeze (non-semantic)

- Typo fixes in docs (no behavior change)
- Navigation links and freeze metadata append
- Governance reviews and validation record updates
- Evaluation script baseline string updates if trace format typo-only

---

## Frozen spec

`agent-builder-kit/templates/review-assistant-agent/` — **separate** CHANGE_LOCK. Do not edit spec to match impl drift.

---

## Version history

| Version | Baseline |
|---------|----------|
| v0.1 | 5 scenarios, no LLM — [CHANGE_LOCK.md](CHANGE_LOCK.md) |
| v0.2 | 10 scenarios, mock LLM — this file |

Semantic behavior change after v0.2 → v0.3 + new freeze record.
