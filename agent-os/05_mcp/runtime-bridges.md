# Runtime Bridges

## Definition

**Runtime bridges** connect MCP and built-in tool ecosystems to a unified agent harness — wrapping external tools, in-process transports, and provider-agnostic API clients behind one execution pipeline.

## Key Ideas

- MCP → internal Tool interface (Chapter 6 pipeline identical).
- InProcessTransport bridges same-process MCP without subprocess overhead.
- Multi-provider client factory bridges Bedrock/Vertex/Azure/Direct API.
- SDK mode uses stdin/stdout control transport distinct from interactive REPL.

## Architecture Implications

- Type erasure: all provider SDKs cast to uniform Anthropic interface.
- Dynamic import of heavy provider modules — unused paths never load.
- IDE transports bridge editor context into agent tool surface.

## Production Implications

- Bridge layer is where normalization, truncation, and auth attach — keep thin.
- Same 14-step pipeline for built-in and MCP — no special-case security holes.
- In-process servers reduce latency for browser/computer automation tools.

## Related Concepts

- [[mcp-protocol]]
- [[api-layer]]
- [[harness-interface]]

## Sources

- `Books/claude/ch04-api-layer.md`
- `Books/claude/ch15-mcp.md`
- `Books/claude/ch16-remote.md` (remote runtime reference)

## My Notes

