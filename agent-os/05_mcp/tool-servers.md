# Tool Servers

## Definition

**MCP tool servers** are processes or services that expose tools via MCP — local stdio subprocesses, remote HTTP/SSE/WebSocket endpoints, in-process transports, or IDE-integrated servers.

## Key Ideas

- Default transport: stdio (subprocess stdin/stdout JSON-RPC).
- Remote: Streamable HTTP (current), SSE (legacy), WebSocket (rare).
- In-process: `InProcessTransport` — 63 lines, queueMicrotask delivery.
- Config scopes: local, user, project, enterprise, managed, claudeai, dynamic.

## Architecture Implications

- Seven scopes merged with content-based deduplication.
- Local `.mcp.json` requires user approval; enterprise pre-approved.
- Plugin servers suppressed when signature matches manual config.

## Production Implications

- stdio: no network, no auth — ideal for local scripts and DB tools.
- OAuth discovery chain: RFC 9728 → RFC 8414 with fallbacks.
- Slack OAuth error body normalization handles spec violations.

## Related Concepts

- [[mcp-protocol]]
- [[mcp-transports]]
- [[mcp-integrations]]

## Sources

- `Books/claude/ch15-mcp.md`

## My Notes

