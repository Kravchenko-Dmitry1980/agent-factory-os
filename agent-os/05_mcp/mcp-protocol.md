# MCP Protocol

## Definition

The **Model Context Protocol (MCP)** is an open JSON-RPC 2.0 specification for tool discovery (`tools/list`) and invocation (`tools/call`) between an agent client and a tool server.

## Key Ideas

- Contract: tool name, description, JSON Schema inputs — nothing else required.
- Client responsibilities: transport, auth, config merge, name normalization, wrapping.
- Wrapped MCP tools use same internal Tool interface as built-ins.
- Fully qualified name: `mcp__{serverName}__{toolName}`.

## Architecture Implications

- Built-ins sorted before MCP in tool pool — preserves prompt cache breakpoint.
- Description truncated at 2048 chars — OpenAPI dumps reached 15K tokens/tool.
- Schema passthrough; errors at call time not registration time.

## Production Implications

- Malicious server can lie on readOnlyHint — accepted trust boundary (user opted in).
- MCP presence disables global prompt cache scope (user-specific tool defs).
- Dedup by server signature not name — same URL/command = same server.

## Related Concepts

- [[tool-servers]]
- [[mcp-transports]]
- [[runtime-bridges]]
- [[tool-runtime]]

## Sources

- `Books/claude/ch15-mcp.md`

## My Notes

