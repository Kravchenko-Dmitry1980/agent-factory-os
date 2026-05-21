# MCP Transports

## Definition

**MCP transports** are the communication channels between MCP client and server — eight configurations spanning local stdio, remote HTTP/SSE/WS, in-process, IDE, and proxy types.

## Key Ideas

| Transport | Use case |
|-----------|----------|
| stdio | Local subprocess (default) |
| http | Remote Streamable HTTP |
| sse | Legacy remote SSE |
| ws | Bidirectional WebSocket |
| sdk | Control messages over stdin/stdout |
| InProcessTransport | Same-process server (Chrome, Computer Use) |
| sse-ide / ws-ide | IDE extension integration |
| claudeai-proxy | Via Claude.ai infrastructure |

## Architecture Implications

- Fetch wrapper stack: timeout → step-up detection → base fetch.
- `ws-ide` splits Bun vs Node WebSocket implementations.
- InProcessTransport: queueMicrotask prevents stack overflow; close cascades to peer.

## Production Implications

- Choose stdio for local tools; http for remote services.
- Legacy SSE still widely deployed despite http recommendation.
- Proxy and IDE transports ecosystem-specific — not portable to all agents.

## Related Concepts

- [[tool-servers]]
- [[runtime-bridges]]
- [[mcp-protocol]]

## Sources

- `Books/claude/ch15-mcp.md`

## My Notes

