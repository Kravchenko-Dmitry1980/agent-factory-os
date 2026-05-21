# MCP Orchestration

## Definition

**MCP orchestration** is how an agent runtime discovers, connects, refreshes, and invokes MCP servers within the query loop — including deferred tool loading and mid-session tool pool updates.

## Key Ideas

- MCP connections initialized in parallel during setup phase.
- Tool pool refresh after tool rounds when servers connect/disconnect.
- Deferred MCP tools: name only until ToolSearch loads schema.
- Monitor_mcp task type watches server health.

## Architecture Implications

- assembleToolPool: deny rules, isEnabled, alphabetical sort within partitions.
- Agent spawn waits for required MCP servers (30s timeout).
- Global cache scope disabled when MCP tools present.

## Production Implications

- Adding MCP server mid-session shifts cache if tools interleaved with built-ins — sort prevents.
- MCP management fast-path in cli.tsx avoids full bootstrap for `mcp list`.
- Dynamic scope allows SDK runtime injection of servers.

## Related Concepts

- [[mcp-protocol]]
- [[query-loop]]
- [[tool-runtime]]

## Sources

- `Books/claude/ch02-bootstrap.md`
- `Books/claude/ch06-tools.md`
- `Books/claude/ch15-mcp.md`

## My Notes

