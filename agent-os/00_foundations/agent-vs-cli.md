# Agent vs CLI

## Definition

A **CLI** is a deterministic function: fixed arguments, fixed behavior, immediate exit. An **agentic CLI** breaks that contract by interpreting natural language, selecting tools dynamically, and looping until completion.

## Key Ideas

- CLI: `grep` does not decide to run `sed`. Agent: model may chain Read → Grep → Edit autonomously.
- CLI contract: one command, one action. Agent contract: prompt → plan → act → evaluate → repeat.
- Agentic systems inherit **non-determinism**, **permission risk**, and **unbounded runtime** by design.

## Architecture Implications

- Permission systems, hooks, and budgets are not optional add-ons — they compensate for broken CLI assumptions.
- Bootstrap must establish **trust boundaries** before reading poisoned environment variables.
- UI must handle **streaming**, **partial results**, and **user interruption** as first-class states.

## Production Implications

- Running arbitrary shell commands without permission resolution is a security catastrophe.
- Users expect sub-300ms startup for CLI-like tools even when the backend is a full agent runtime.
- Observability must trace **turns**, **tool calls**, and **terminal reasons**, not just HTTP requests.

## Related Concepts

- [[what-is-an-agent]]
- [[bootstrap-pipeline]]
- [[permission-modes]]
- [[golden-path]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch02-bootstrap.md`

## My Notes

