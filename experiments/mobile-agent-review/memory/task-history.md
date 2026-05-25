# Task History

Как история действий представлена и используется в loop.

---

## v2 History Fields

| Variable | Content |
|----------|---------|
| `summary_history` | Natural language operation summaries |
| `action_history` | Parsed Action strings |
| `last_summary`, `last_action` | Most recent step |
| `completed_content` | Progress agent output |

Injected in action prompt as:
```
Step-1: [Operation: ...; Action: Tap (x,y)]
```

---

## v3 InfoPool History

| Field | Content |
|-------|---------|
| `summary_history` | Action descriptions |
| `action_history` | Serialized actions |
| `action_outcomes` | A/B/C or reflector outputs |
| `error_descriptions` | Failure explanations |
| `progress_status_history` | Manager status over time |

Used by Manager, Executor, Reflector prompts — full cross-agent visibility.

---

## Image History

Typically **not** all past screenshots kept in context:
- Last before/after pair for reflection
- Current screenshot for action
- v3.5 may annotate screenshot with recent action overlay (`annotate_screenshot`)

Compression strategy: **textual history + one fresh image** — analogous to Agent-OS context compression.

---

## Benchmark Trajectory Logs

Eval runs save trajectories externally:
- Google Drive links in v3 README for AndroidWorld GUI-Owl / MA3
- Web benchmark `output_dir` with step screenshots

Useful for offline analysis, not runtime memory.

---

## History Length Risks

- Unbounded list growth in long tasks
- No automatic summarization middleware (unlike Claude Code 4-layer compression)
- Manager replan partially mitigates via `completed_plan` abstraction

---

## Extractable Pattern

**Dual-track history:**
1. **Fine-grained:** action_history (machine-oriented)
2. **Coarse-grained:** progress_status / completed_plan (plan-oriented)

Agent-OS could adopt similar split for GUI modality without storing every screenshot.
