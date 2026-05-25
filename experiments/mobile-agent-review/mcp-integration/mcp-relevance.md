# MCP Relevance

Model Context Protocol в контексте MobileAgent / GUI-Owl 1.5.

---

## Where MCP Appears

### 1. GUI-Owl 1.5 Model Capability

v3.5 README highlights:
- Native **tool & MCP calling**
- Top performance on **OSWorld-MCP** and **Mobile-World**

MCP is a **model action type**, not an MCP server implemented in this repo.

### 2. OSWorld-MCP Benchmark (External)

- Repo: [X-PLUG/OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP)
- Eval script referenced: `run_multienv_gui_owl_1_5.py`
- Tests when agent should use GUI vs invoke MCP tools

### 3. Mobile-World (External)

- GUI-Owl 1.5 agent implementation linked externally
- Mobile scenarios with tool + GUI orchestration

---

## What This Repo Does NOT Contain

- No `mcp.json` or MCP server scaffold
- No stdio/SSE transport handlers
- No tool registry matching Agent-OS `05_mcp/` structure

---

## Architectural Implication

MobileAgent v3.5 represents **GUI + MCP hybrid agents** at the **model policy** level:

```
Observation (screen)
    → Model decides: GUI action OR MCP tool call
    → Execute via appropriate adapter
    → Observe result (screen and/or tool output)
```

Contrast with Claude Code: MCP tools are first-class in harness; GUI is not native.

---

## Relation to ToolCUA (External, May 2026)

README links **ToolCUA** — optimizes GUI vs tool path orchestration with RL.

Complementary research line to GUI-Owl MCP capability.

---

## Agent-OS Gap

Current Agent-OS (`agent-os/05_mcp/`) documents protocol from Claude Code perspective.

MobileAgent suggests future section:
- **GUI-MCP hybrid routing** — when to click vs call tool
- **Digital twin bridges** — MCP tools representing device state

Research only — not added to canonical Agent-OS in this experiment.

---

## Bailian / Cloud API

GUI-plus model on Alibaba Bailian may expose MCP-aware inference — cloud-side, not in open-source runners reviewed here.
