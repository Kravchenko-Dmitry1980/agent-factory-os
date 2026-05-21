# What Is an Agent

## Definition

An **agent** is a runtime system where a language model generates its own control flow at execution time: it decides which tools to call, in what order, evaluates results, and loops until the task completes or an external constraint stops it.

## Key Ideas

- Unlike a traditional CLI (one command → one action → exit), an agent's "program" is a **loop around an LLM**.
- Tool calls are **side effects**; model reasoning is **control flow**.
- The agent is not a single API call — it is a **stateful execution loop** with message history, permissions, and termination semantics.
- Production agents converge on a small set of abstractions: loop, tools, state, memory, hooks, tasks.

## Architecture Implications

- Design around a **single query loop** that all entry points (REPL, SDK, subagents, headless) share.
- Termination must be **typed** (completed, aborted, budget exhausted, hook stopped) — not implicit.
- Separate **mechanics of model calls** from **orchestration of tool execution**.

## Production Implications

- One loop = one place to add circuit breakers, compaction, and telemetry.
- Divergent code paths for subagents create subtle behavioral bugs — reuse the same loop.
- Security posture is defined by permission modes and hook interceptors, not by the model's intent.

## Related Concepts

- [[agent-vs-cli]]
- [[six-abstractions]]
- [[query-loop]]
- [[harness]]
- [[execution-loops]]

## Sources

- `Books/claude/ch01-architecture.md` — "The Architecture of an AI Agent"
- `Books/claude/ch05-agent-loop.md` — agent loop as center of gravity

## My Notes

