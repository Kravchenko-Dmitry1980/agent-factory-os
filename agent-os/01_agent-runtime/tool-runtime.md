# Tool Runtime

## Definition

The **tool runtime** is the subsystem that registers tools, validates inputs, resolves permissions, executes calls, budgets results, and returns structured messages to the query loop.

## Key Ideas

- Tool interface: `call()`, `inputSchema`, `isConcurrencySafe()`, `checkPermissions()`, `validateInput()`.
- `buildTool()` applies **fail-closed defaults** (serial, write-assumed, allow passthrough).
- 14-step pipeline: lookup → abort → Zod → semantic → classifier → backfill → PreToolUse → permissions → execute → budget → PostToolUse → messages → errors.
- MCP tools wrapped to identical internal interface after `tools/list`.

## Architecture Implications

- `ToolUseContext` god object threads ~40 fields — pragmatic alternative to 15+ parameters.
- Registry: built-ins first, MCP suffix; sort preserves prompt cache breakpoint.
- Deferred tools (`defer_loading`) require ToolSearch before use.

## Production Implications

- Result budgeting persists oversized output to disk; prevents context death by a thousand cuts.
- BashTool complexity: compound command parsing, sed simulation for safe previews.
- Error classification must be telemetry-safe (no mangled constructor names in minified builds).

## Related Concepts

- [[self-describing-tools]]
- [[fail-closed-defaults]]
- [[permission-modes]]
- [[concurrency]]
- [[mcp-protocol]]

## Sources

- `Books/claude/ch06-tools.md`

## My Notes

