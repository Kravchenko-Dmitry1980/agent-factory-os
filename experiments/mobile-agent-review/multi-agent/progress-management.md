# Progress Management

Отслеживание выполнения пользовательского запроса через subgoals и completed content.

---

## v2 Progress Agent

**Prompt:** `get_process_prompt()` in `Mobile-Agent-v2/MobileAgent/prompt.py`

Inputs:
- User instruction
- Action history summaries
- Current screenshot perception

Output:
- **Completed contents** — natural language progress summary
- Fed into next action prompt under `### Progress ###`

Purpose: Decouple "what's done" from raw step list — compresses history for action agent.

---

## v3 Manager Progress Fields

InfoPool tracks:

| Field | Role |
|-------|------|
| `plan` | Numbered subgoals |
| `completed_plan` | Finished subgoals text |
| `progress_status` | Current status narrative |
| `progress_status_history` | Historical status snapshots |
| `current_subgoal` | Active focus for Executor |
| `finish_thought` | Completion rationale |

Manager prompt sections:
- `### Historical Operations ###`
- `### Plan ###`
- `### Last Action ###`
- `### Potentially Stuck! ###` when replan needed

---

## Replan Trigger

```python
err_to_manager_thresh: int = 2  # InfoPool default
error_flag_plan: bool           # set after repeated executor failures
```

When threshold hit → Manager invoked to revise plan, not just retry action.

---

## Task-Specific Plan Hints

Manager injects hardcoded notes for known benchmark quirks:
- `.html` canvas tasks
- Audio Recorder stop icon shape

Pattern: **domain add_info** at manager level vs executor level (`additional_knowledge_manager` vs `additional_knowledge_executor`).

---

## v3.5 / GUI-Owl 1.5

Claims **built-in long-horizon memory** without external workflow:
- MemGUI-Bench leadership cited in README
- Less explicit `completed_plan` string in Python — progress internal to model

---

## Agent-OS Analog

Maps to:
- `agent-os/04_multi-agent/task-state-machine.md`
- Plan/subgoal tracking in orchestration layer
- Distinct from episodic memory (notes) and semantic memory (facts)

---

## Anti-Pattern Link

Progress agent adds LLM call every step → latency cost. v2 README allows disabling memory/reflection for speed — progress still recommended for long tasks.
