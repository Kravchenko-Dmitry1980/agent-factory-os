# Recommended Next Step — Phase 3.2

**Date:** 2026-05-26

---

## Recommended next phase

# Phase 3.2 — LLM Adapter Boundary (mock-first)

**Planning:** approved in Phase 3.2-Plan  
**Implementation:** **not started** — requires explicit user approval

---

## Do next

1. **Plan LLM boundary** — contract, failure modes, trace, eval, security (this folder)
2. **Future impl (when approved):** mock-first LLM adapter adjacent to Review Assistant thin
3. **Test** malformed / timeout / uncertain / unsafe output in mock mode
4. **Keep** human approval mandatory before delivery
5. **Keep** no runtime / no factory
6. **Extend** evaluation with LLM boundary checks (new script or extend thin check — only with approval, do not modify existing scripts without gate)
7. **Freeze** adapter separately after PASS review

---

## Do NOT do next

| Forbidden | Reason |
|-----------|--------|
| Second template | Postponed — see Option B review |
| Factory / runtime / generator | Phase 3 scope lock |
| Production API / Telegram / FastAPI | Out of scope |
| RAG / MCP / multi-agent | Frozen |
| Default OpenAI/API calls | Mock-first; explicit flag + approval for real |
| Modify frozen thin v0.1 without change proposal | Impl freeze |
| Universal provider framework | Platform drift |

---

## Recommended path (sequential)

```text
Phase 3.2-Plan     ← this decision (Markdown)
Phase 3.2-Impl     ← mock LLM adapter only (future, explicit start)
Phase 3.2-Review   ← eval + freeze adapter v0.1
Phase 3.3-Plan     ← second template OR real provider (user choice)
```

---

## User prompt required for implementation

> «Start Phase 3.2 mock LLM adapter for Review Assistant.»

Plus [PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md).

---

## Alternative (not recommended now)

**Option B — Second template spec-only** — defer until after LLM boundary mock is safe or user explicitly skips LLM and requests second template plan instead.

---

## Verdict

**CONDITIONAL_GO_FOR_LLM_ADAPTER_PLAN** — proceed with planning docs; implementation gated.

See [FINAL_PHASE_3_2_PLAN_REPORT.md](FINAL_PHASE_3_2_PLAN_REPORT.md)
