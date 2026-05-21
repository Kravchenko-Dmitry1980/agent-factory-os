# Central Orchestrator God Object

## Definition

The **central orchestrator god object** anti-pattern concentrates per-tool knowledge (concurrency, permissions, rendering) in one module that must be updated for every new tool — scaling linearly in merge conflicts and bugs.

## Key Ideas

- Symptom: orchestrator switch statements on tool names.
- Opposite: self-describing tools + generic 14-step pipeline.
- ToolUseContext god object is pragmatic; central tool logic is not.

## Architecture Implications

- Registry + partition + pipeline stays generic.
- Tool-specific logic lives in tool module only.
- MCP wrapping applies uniform pipeline without MCP branches in core.

## Production Implications

- Team velocity collapses as tool count grows past ~20.
- Security audits cannot reason about per-tool checks scattered in orchestrator.

## Related Concepts

- [[self-describing-tools]]
- [[tool-runtime]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch06-tools.md`

## My Notes

