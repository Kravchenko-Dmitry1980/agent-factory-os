# Claude Code Architecture

## Definition

**Claude Code architecture** is the production TypeScript agent runtime (Anthropic) decomposed into six abstractions — the primary research corpus extracted into Agent-OS atomic notes.

## Key Ideas

- ~2000 files; six abstractions: Query Loop, Tools, Tasks, State, Memory, Hooks.
- Single `query()` path for all entry points.
- Production lessons: cache latches, withholding errors, circuit breakers, bubble permissions.

## Architecture Implications

- Serves as reference implementation for Agent-OS patterns.
- Source chapters map to Agent-OS directories (see mapping below).

## Production Implications

- Patterns validated at fleet scale (hundreds of thousands of developers).
- Feature flags + dead code elimination for internal vs npm builds.

## Chapter → Agent-OS Mapping

| Source | Agent-OS |
|--------|----------|
| ch01 Architecture | 00_foundations, 12_diagrams |
| ch02 Bootstrap | 01_agent-runtime/bootstrap-pipeline |
| ch03 State | 08_patterns/two-tier-state, 00_foundations/stateful-systems |
| ch04 API Layer | 01_agent-runtime/api-layer, 08_patterns/prompt-cache-as-constraint |
| ch05 Agent Loop | 01_agent-runtime/query-loop, 08_patterns/generator-loop-pattern |
| ch06 Tools | 01_agent-runtime/tool-runtime, 03_harness-engineering |
| ch07 Concurrency | 01_agent-runtime/concurrency |
| ch08 Sub-agents | 04_multi-agent/subagents |
| ch09 Fork agents | 07_projects/experiments |
| ch10 Coordination | 04_multi-agent/coordination |
| ch11 Memory | 02_memory |
| ch15 MCP | 05_mcp |

## Related Concepts

- [[six-abstractions]]
- [[what-is-an-agent]]

## Sources

- `Books/claude/ch01-architecture.md` through `Books/claude/ch18-epilogue.md`

## My Notes

