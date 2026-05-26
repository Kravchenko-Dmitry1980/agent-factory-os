# Option A — LLM Adapter Plan

**Status:** Plan only — **no implementation**

---

## Purpose

A future **LLM adapter boundary** would let Review Assistant obtain draft or critique text from a model **without** treating model output as verified truth. All existing gates remain: verification, human approval, fail-closed, trace.

---

## What it should do (future Phase 3.2-Impl)

| Capability | Description |
|------------|-------------|
| Accept prompt | Task text + prompt type (draft / critique) |
| Return response | Raw + parsed draft or critique |
| Parse response | Structured or plain text extraction |
| Detect malformed output | Unparseable, empty, schema mismatch |
| Handle timeout | Bounded wait; fail-closed |
| Mark uncertainty | Low confidence / ambiguous claims |
| Pass to verification | LLM output is **input** to verification gate |
| Require human approval | Before final delivery — unchanged |

---

## What it must NOT do

- Autonomous action or auto-publish
- Memory writeback or profile learning
- Tool execution from model output
- Multi-model routing or leaderboard
- Agent swarm, RAG, MCP
- Default external API call
- Bypass verification or human approval
- Command/shell execution from LLM text

---

## Future implementation style (when approved)

| Rule | Detail |
|------|--------|
| Location | Separate folder e.g. `prototypes-derived/review-assistant-llm/` or adapter module **adjacent** to thin demo — not under `agent-builder-kit/runtime/` |
| Files | One adapter module + mock; optional real provider behind explicit flag |
| Dependencies | Mock: stdlib only. Real OpenAI: **explicit user approval** + optional dep |
| Modes | `mock` (default), `real` (opt-in flag only) |
| Integration | Thin demo calls adapter; frozen thin v0.1 unchanged unless change proposal |

**Do not implement in Phase 3.2-Plan.**

---

## Mock-first sequence (future)

```text
1. LLM boundary contract (this plan)
2. Mock adapter — deterministic responses
3. Eval: malformed, timeout, uncertain, unsafe
4. Optional real provider — separate approval
5. Freeze adapter v0.1 separately
```

---

## Alignment

- Frozen template: [review-assistant-agent/](../../agent-builder-kit/templates/review-assistant-agent/)
- Thin baseline: [review-assistant-thin/](../../prototypes-derived/review-assistant-thin/)
- Canonical LLM events: `observability/event-taxonomy/canonical-events.md` (`llm_timeout`, `llm_malformed_output`)
- Phase 2 reference: `integrations-real/llm-verification-adapter/` (read-only research)

---

## Diagram

[diagrams/llm-boundary.md](diagrams/llm-boundary.md)
