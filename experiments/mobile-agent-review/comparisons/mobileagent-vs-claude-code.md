# MobileAgent vs Claude Code Architecture

Сравнение research source (MobileAgent) с каноническим источником Agent-OS (`Books/claude/`).

---

## Core Loop

| Dimension | Claude Code | MobileAgent (v3 representative) |
|-----------|-------------|--------------------------------|
| Observation | Text messages + tool results | Screenshots (+ optional UI list) |
| Action API | Typed tools (bash, read, edit, …) | Tap/type/swipe via ADB/pyautogui |
| Loop host | Single `query()` async generator | Per-version Python scripts |
| Stop semantics | 10 typed terminal states | Stop/terminate/Finished strings |

---

## Harness Properties

| Feature | Claude Code | MobileAgent |
|---------|-------------|-------------|
| Permission model | CanUseTool, modes | None |
| Hooks | Pre/post tool, stop hooks | None |
| Circuit breakers | Max turns, budget | Partial (replan threshold only) |
| Context compression | 4 layers before API call | History strings + one image |
| Concurrency | Subagents parallel | Sequential multi-agent calls |
| Streaming | SSE to UI | Batch step loop |

---

## Multi-Agent

| Claude Code | MobileAgent v3 |
|-------------|----------------|
| Subagents = separate query() invocations | Roles = prompts or classes sharing InfoPool |
| Isolated context windows | Shared dataclass state |
| Parent orchestrates | Inline orchestrator in run script |

MobileAgent **decomposes cognition** (plan/ act/ reflect); Claude Code **decomposes tasks** (subagents).

---

## Tools vs GUI

Claude Code: world is **code + files + shell**.

MobileAgent: world is **pixels + input events**.

GUI-Owl 1.5 adds **MCP/tool calling** — convergence point toward hybrid harness.

---

## Verification

| Claude Code | MobileAgent |
|-------------|-------------|
| Tool stderr/exit code | Visual A/B/C reflection |
| Lint/test as feedback | Benchmark reward (eval) |
| Withheld errors pattern | Not present |

---

## What Agent-OS Should Import

From MobileAgent (later):
- Visual verification taxonomy (A/B/C)
- InfoPool-style shared GUI state
- GUI-as-environment framing

From Claude Code (already canonical):
- Harness defenses, permissions, terminal states

---

## Sources

- `Books/claude/ch05-agent-loop.md`, `ch06-tools.md`, `ch08-sub-agents.md`
- `Mobile-Agent-v3/mobile_v3/utils/mobile_agent_e.py`
