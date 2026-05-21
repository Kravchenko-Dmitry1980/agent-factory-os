# Execution Loops

## Definition

An **execution loop** is the repeated cycle: prepare context → call model → execute tools → append results → check termination → continue or exit.

## Key Ideas

- The loop is the agent; everything else feeds into or intercepts it.
- Ideal implementation: **async generator** with typed terminal return value.
- Each iteration reconstructs full state object — no partial mutations at continue sites.
- Context passes through **compression layers** before each API call (budget → snip → microcompact → collapse → auto-compact).

## Architecture Implications

- Single `query()` entry for REPL, SDK, subagents, headless — guarantees identical behavior.
- Recoverable errors are **withheld** from yield stream until recovery exhausts.
- Circuit breakers on auto-compact, reactive compact, and max-output recovery prevent infinite loops.

## Production Implications

- Without circuit breakers, one stuck session can burn 250K+ API calls/day.
- Orphaned `tool_use` blocks without `tool_result` break API protocol — safety net required.
- Token budgets use diminishing-returns detection to stop low-value continuations.

## Related Concepts

- [[query-loop]]
- [[generator-loop-pattern]]
- [[context-compression]]
- [[error-recovery-ladder]]
- [[terminal-states]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

