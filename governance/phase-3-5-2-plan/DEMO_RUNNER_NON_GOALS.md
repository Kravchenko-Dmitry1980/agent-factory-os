# Demo Runner — Non-Goals

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Demo Runner **is not** any of the following. It is **only** a human-friendly wrapper for existing demo scenarios.

---

## Demo Runner is NOT

| Not this | Why |
|----------|-----|
| **Agent runtime** | Does not execute agent loop — calls existing demo |
| **Framework** | No plugin API, no extensibility layer |
| **Orchestrator** | Does not route tasks or start agents |
| **Provider manager** | Does not configure models — passes through env + flags |
| **Testing framework** | Not pytest replacement — wraps existing checks |
| **Benchmark** | No scoring leaderboard |
| **Red-team tool** | Harness stays separate |
| **Project management tool** | No queues, tickets, assignments |
| **Operator Console** | Backlog — separate product vision |
| **Chat product** | No conversational UI |
| **Production UI** | Lab operator aid only |
| **Scenario engine** | No dynamic scenario generation |
| **Generator / factory** | No “create new demos from template” |
| **Second agent** | Not Task Triage |
| **Documentation generator** | Summarizes run output, not full doc pipeline |

---

## Demo Runner IS

| Is this | Detail |
|---------|--------|
| **Wrapper** | subprocess to frozen scripts |
| **Translator** | TRACE → Russian key events |
| **Menu** | Fixed list, numbered choices |
| **Operator aid** | Reduces friction for demos and learning |
| **Additive UX** | Raw stdout still visible or captured in transcript |

---

## Red flags (stop impl if appearing)

- “Let’s add scenarios in the runner”
- “Let’s patch minimal_demo for nicer output”
- “Let’s auto-run real provider on startup”
- “Let’s use rich/typer for better menu”
- “Let’s make it a platform for all agents”

→ Rollback per [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md).

---

## One-line definition

**Human-friendly shell around frozen Review Assistant Thin demos — nothing more.**
