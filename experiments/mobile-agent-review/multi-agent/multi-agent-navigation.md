# Multi-Agent Navigation

Как MobileAgent decompose навигацию по GUI через несколько ролей.

---

## Problem Statement

Long-horizon mobile tasks blow context windows:
- Many screens × rich screenshots
- Lengthy action histories
- Need for plan maintenance

**v2 thesis (NeurIPS 2024):** Multi-agent collaboration improves navigation in long-context scenarios.

---

## v2 — Prompt-Based Agents (Same LLM)

Four roles, four separate chat sessions:

| Role | Function |
|------|----------|
| Action | Next single step on current screen |
| Reflection | Verify last step (A/B/C) |
| Memory | Extract facts to remember |
| Progress | Summarize completed requirements |

Not separate processes — sequential LLM calls with different system prompts.

---

## v3 — Class-Based Agents

| Agent | Responsibility |
|-------|----------------|
| **Manager** | High-level plan, subgoals, replan on stuck |
| **Executor** | Concrete JSON action on current subgoal |
| **ActionReflector** | Post-action verification |
| **Notetaker** | Long-horizon notes (`important_notes`) |

Optional **Grounding** (OSWorld): resolve element descriptions to coordinates.

---

## Navigation Flow

```
User instruction
      ↓
Manager: plan subgoals (first time or replan)
      ↓
Loop:
  Executor: action for current_subgoal
  Execute on device
  Reflector: outcome A/B/C
  Notetaker: optional note extraction
  Manager: update progress / replan if error_flag_plan
      ↓
terminate / answer / Finished
```

---

## Mobile-Agent-E Extensions

Adds **experience navigation**:
- ExperienceRetrieverShortCut / Tips — fetch past successful patterns
- ExperienceReflectorShortCut / Tips — update evolution memory

Self-evolving navigation beyond single session.

---

## v3.5 Shift

README claims multi-agent readiness at **model level**:
- GUI-Owl 1.5 can play planner, executor, verifier, notetaker
- Python orchestration simplified to single VLM loop in `mobile_use/`

**Research note:** Full v3 class framework not ported to v3.5 open-source mobile runner.

---

## PC-Agent Parallel

Desktop `run.py` uses:
- Subtask agent (planning)
- Action, Reflect, Memory, Process agents

Same navigation pattern, different controller (pyautogui).

---

## Key File

`Mobile-Agent-v3/mobile_v3/utils/mobile_agent_e.py` — Manager, Executor, ActionReflector, Notetaker class definitions + InfoPool.
