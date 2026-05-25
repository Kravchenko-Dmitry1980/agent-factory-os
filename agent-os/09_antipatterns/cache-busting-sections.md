# Cache-Busting Sections

## Definition

**Cache-busting sections** are prompt or tool definition changes that invalidate server-side prefix cache — often from runtime conditionals before the static boundary, dynamic tool descriptions, or mid-session MCP reordering.

## Key Ideas

- Runtime boolean before static boundary → 2^N cache variants.
- Dynamic agent list in tool description → ~10.2% fleet cache_creation.
- Flat sort of built-in + MCP tools shifts built-in positions when MCP changes.

## Architecture Implications

- Use DANGEROUS_ prefix + reason for uncached sections.
- Attachments for volatile lists; static tool descriptions.
- Sort built-ins and MCP separately; concat built-ins first.

## Production Implications

- Well-intentioned engineer can double fleet cost invisibly.
- Code review gate on system prompt diffs near boundary marker.

## Related Concepts

- [[prompt-cache-as-constraint]]
- [[sticky-latch-pattern]]
- [[mid-session-memory-injection]]
- [[frozen-memory-snapshot]]

## Sources

- `Books/claude/ch04-api-layer.md`
- `Books/claude/ch08-sub-agents.md`

## My Notes

