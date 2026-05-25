# Coordination Patterns

Как агенты координируются без message bus или RPC.

---

## Pattern 1: Shared Mutable State (InfoPool)

**Used in:** v3 mobile, Mobile-Agent-E

```python
@dataclass
class InfoPool:
    instruction: str
    plan: str
    action_history: list
    action_outcomes: list
    important_notes: str
    error_flag_plan: bool
    ...
```

- All agents receive `InfoPool` read-only in prompts
- Orchestrator mutates pool after each agent returns
- **No** agent-to-agent direct messaging

**Pros:** Simple, debuggable, single process  
**Cons:** Tight coupling, god-object tendency

---

## Pattern 2: Multi-Chat Same Model (v2, PC)

- Separate chat history per role (`init_chat`, `init_reflect_chat`, …)
- Orchestrator passes strings between stages
- State in Python variables: `memory`, `completed_content`, `error_flag`

Same LLM, different conversations — simulates specialization cheaply.

---

## Pattern 3: Single VLM Loop (v3.5)

- Coordination internalized in GUI-Owl 1.5 weights
- External state minimal: screenshot sequence + instruction
- Closest to **monolithic agent** at code level

---

## Pattern 4: Hierarchical PC (PC-Agent)

```
Subtask agent → decomposes desktop task
     ↓
Action agent → low-level mouse/keyboard
     ↓
Reflect / Memory / Process
```

Explicit **hierarchy** for complex PC workflows (ICLR 2025 WS paper focus).

---

## Pattern 5: Experience Sidecar (MA-E)

```
Main loop (Manager/Operator/Reflector/Notetaker)
     ↔
ExperienceRetriever / ExperienceReflector
     ↔
Persistent tips/shortcuts store
```

Cross-episode coordination — rare in other versions.

---

## Orchestration Timing

Typical v3 step order:

1. Manager (conditional — skip if plan stable)
2. Executor
3. Device execute + sleep
4. Reflector
5. Notetaker (if `--notetaker True`)
6. Update InfoPool → loop

Manager re-entry on `error_flag_plan` or subgoal completion.

---

## Comparison to Agent-OS Multi-Agent

| Aspect | MobileAgent | Agent-OS (Claude-derived) |
|--------|-------------|----------------------------|
| Coordination | Shared dataclass / vars | Subagents, separate query() |
| Isolation | None (same process) | Subagent context isolation |
| Permissions | None | CanUseTool, hooks |
| Parallelism | Sequential only | Concurrent subagents (ch07) |

---

## Extractable Pattern

**"Shared pool + role-specific prompts"** — lightweight alternative to full subagent processes for GUI loops with tight screenshot feedback requirements.
