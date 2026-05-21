# Prompt Cache as Constraint

## Definition

**Prompt cache as constraint** treats server-side prompt caching as an architectural invariant that shapes prompt ordering, section naming, tool pool sorting, header latching, and MCP placement — not an optional optimization toggle.

## Key Ideas

- Static/dynamic boundary in system prompt — global vs per-session cache scopes.
- DANGEROUS_ prefix for cache-breaking sections with mandatory reason param.
- 2^N rule: runtime conditionals before boundary multiply cache variants.
- Built-ins before MCP in tool list — cache breakpoint after last built-in.

## Architecture Implications

- Design prompts for prefix stability across turns and sessions.
- Move volatile tool/agent lists to attachment messages.
- Disable global scope when MCP tools present (user-specific defs).

## Production Implications

- Single misplaced section can double fleet prompt processing cost.
- Code review checklist: boundary placement for every new prompt section.

## Related Concepts

- [[sticky-latch-pattern]]
- [[api-layer]]
- [[cache-busting-sections]]

## Sources

- `Books/claude/ch04-api-layer.md`
- `Books/claude/ch06-tools.md`

## My Notes

