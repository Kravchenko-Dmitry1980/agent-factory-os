# Free-Form CLI — Non-Goals

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Interactive Free-Form CLI is NOT

| Non-goal | Clarification |
|----------|---------------|
| Chatbot product | No multi-turn product chat |
| ChatGPT clone | No open-ended conversation UI |
| Autonomous agent | No self-directed task execution |
| Execution engine | No publish, send, write, deploy |
| Orchestrator | No multi-agent routing |
| Workflow system | No DAG / steps engine |
| Task manager | No backlog / assign / track |
| Runtime / factory | No platform layer |
| Provider manager | No router, no fallback chain |
| Memory system | No writeback, no RAG store |
| Production UI | Terminal lab tool only |
| Operator Console | Explicit backlog item (Phase 3.2.2 triage) |
| Task Triage implementation | Specs only (separate artifact) |

---

## What it IS

**A controlled operator input mode for Review Assistant demo.**

Purpose: type lab-safe task text → see gates → read Russian explanation → exit.

---

## Anti-patterns to reject in future impl

| Anti-pattern | Why forbidden |
|--------------|---------------|
| «Just add chat loop» | Becomes product chat |
| «Store last 10 tasks» | Session/memory drift |
| «Auto-call LM Studio if mock fails» | Hidden provider |
| «Merge into demo_runner.py» | Bloats frozen runner |
| «Reuse Task Triage specs as runtime» | Specs ≠ implementation |
| «Allow any input length» | DoS / secret leak risk |

---

## If someone asks for more

Redirect to:

- **Demo Runner v0.1** — predefined scenarios (frozen)
- **Phase 3.6-Plan** — Task Triage thin impl (future)
- **Operator Console** — research backlog, not this phase

See [FREE_FORM_CLI_SCOPE.md](FREE_FORM_CLI_SCOPE.md).
