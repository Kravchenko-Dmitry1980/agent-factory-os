# MobileAgent vs Agent-OS

Сравнение с текущим Knowledge OS skeleton (`agent-os/`).

---

## Agent-OS Current State (from CURRENT_STATE_AUDIT)

- 13-section knowledge skeleton
- Canonical source: **Claude Code** (`Books/claude/`)
- Secondary corpus: Code as Agent Harness survey (not yet integrated)
- No GUI/OS agent section in taxonomy yet
- Experiments folder intended for isolated research

---

## Coverage Matrix

| Agent-OS section | MobileAgent relevance |
|------------------|----------------------|
| `00_foundations/` | GUI-as-environment extends execution loop concepts |
| `01_agent-runtime/` | Parallel GUI loop, different observation |
| `02_memory/` | Notetaker, v2 memory, MA-E experience maps to episodic/semantic |
| `03_harness-engineering/` | MobileAgent lacks most mechanisms — negative example |
| `04_multi-agent/` | InfoPool coordination, role systems — strong overlap |
| `05_mcp/` | GUI-Owl 1.5 MCP capability — future bridge |
| `06_digital-twins/` | Cloud phone, emulator twins — high relevance |
| `09_antipatterns/` | Brittle GUI, unverified clicks — new antipatterns |
| `10_research/` | Should ingest MobileAgent as third corpus later |

---

## What Agent-OS Has That MobileAgent Lacks

- Permission modes, hooks lifecycle
- Query loop terminal typing
- MCP protocol documentation
- Golden path sequence diagrams (code-centric)
- Glossary and cross-linked concept graph

---

## What MobileAgent Has That Agent-OS Lacks

- Visual grounding pipeline
- Action verification (A/B/C, GUI-Critic)
- Coordinate space handling
- Platform drivers (ADB, pyautogui, Playwright)
- GUI benchmarks map
- Native VLM agent models (GUI-Owl) — external weights

---

## Taxonomy Decision (Deferred)

Per experiment boundaries: **do not modify Agent-OS taxonomy now**.

Proposed future section (research note only):
```
agent-os/13_gui-agents/   (hypothetical)
  gui-agent-loop.md
  visual-grounding.md
  gui-action-contract.md
  gui-verification.md
```

Or extend `01_agent-runtime/` with GUI modality appendix.

---

## Ingestion Path

1. ✅ `experiments/mobile-agent-review/` — done
2. ⏳ Extract 5–10 canonical notes → `agent-os/10_research/sources.md` entry
3. ⏳ Promote patterns to `08_patterns/` after review
4. ⏳ Add GUI antipatterns to `09_antipatterns/`

---

## Verdict

MobileAgent is **essential complementary corpus** for Agent-OS vision (agents operating computers), not a replacement for Claude Code harness knowledge.
