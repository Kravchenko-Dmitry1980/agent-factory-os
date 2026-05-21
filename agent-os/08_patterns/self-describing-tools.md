# Self-Describing Tools

## Definition

The **self-describing tools pattern** requires each tool to declare its own concurrency safety, permissions, validation, and rendering — avoiding a central orchestrator that knows every tool implementation.

## Key Ideas

- Tool carries: schema, isConcurrencySafe(input), checkPermissions, validateInput, render methods.
- buildTool() spreads fail-closed defaults under tool definition.
- Registry aggregates; orchestrator only partitions and executes.

## Architecture Implications

- Adding tool N+1 requires zero changes to existing tools or pipeline core.
- Input-dependent safety signatures (`Bash` read vs write classification).
- MCP wrappers map annotations to same interface fields.

## Production Implications

- Central god-object orchestrator becomes change bottleneck at 40+ tools.
- Forgotten flag → safe default (serial, write-assumed).

## Related Concepts

- [[tool-runtime]]
- [[fail-closed-defaults]]
- [[concurrency]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch06-tools.md`

## My Notes

