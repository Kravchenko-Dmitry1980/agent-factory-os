# Harness

## Definition

A **harness** is the execution envelope around an LLM: it defines how the model interacts with tools, permissions, lifecycle hooks, verification, and feedback — without the model controlling those boundaries directly.

## Key Ideas

- The harness is not the model; it is the **runtime that constrains and amplifies** the model.
- Components: permission modes, PreToolUse/PostToolUse hooks, stop hooks, result budgeting, execution pipeline.
- Harness engineering treats **verification and feedback** as first-class loop phases, not post-hoc checks.
- Subagents inherit the same harness (bubble permissions, shared loop) — not a reduced special case.

## Architecture Implications

- Permission resolution is **mode-based** (plan, default, auto, bubble) — not scattered `if (allowed)` in tools.
- Hooks fire at 27+ lifecycle events and can block, modify, or short-circuit execution.
- Stop hooks run when the model thinks it is done — forcing continuation when verification fails.

## Production Implications

- Auto mode uses a lightweight classifier to approve routine operations semi-autonomously.
- Bubble mode prevents subagents from silently approving destructive actions.
- Hook snapshots are frozen at session start to prevent post-start config tampering.

## Related Concepts

- [[harness-interface]]
- [[execution-verification]]
- [[permission-modes]]
- [[hooks-lifecycle]]
- [[feedback-loops]]

## Sources

- `Books/claude/ch01-architecture.md` — hooks abstraction
- `Books/claude/ch05-agent-loop.md` — stop hooks
- `Books/claude/ch06-tools.md` — 14-step execution pipeline

## My Notes

