# MCP Integrations

## Definition

**MCP integrations** are production patterns for connecting external systems — OAuth flows, Cross-App Access, enterprise config, IDE extensions, and annotation-based behavior hints.

## Key Ideas

- OAuth 2.0 + PKCE with RFC 9728/8414 discovery chain.
- Cross-App Access (XAA): federated token exchange via IdP.
- Annotation mapping: readOnlyHint → concurrency; destructiveHint → scrutiny.
- Error body normalization for non-compliant OAuth servers (Slack).

## Architecture Implications

- `authServerMetadataUrl` escape hatch when discovery fails.
- Enterprise/managed scopes pre-approved by org policy.
- claudeai scope pre-authorized via web interface.

## Production Implications

- OAuth refresh token errors normalized to `invalid_grant`.
- Trust model: user approves local servers; enterprise trusts centrally.
- Malicious annotations accepted tradeoff — document for security reviews.

## Related Concepts

- [[tool-servers]]
- [[mcp-transports]]
- [[permission-modes]]

## Sources

- `Books/claude/ch15-mcp.md`

## My Notes

