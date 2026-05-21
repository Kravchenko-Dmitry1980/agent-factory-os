# Skill Graphs

## Definition

A **skill graph** is the structured map of an agent's capabilities — tools, MCP servers, custom agent definitions, Cursor skills, and feature-gated behaviors — and their dependencies and activation conditions.

## Key Ideas

- Tool pool = built-ins + MCP + deferred tools discovered via ToolSearch.
- Agent definitions loaded at setup with frontmatter metadata.
- Feature flags and GrowthBook experiments gate skill availability.
- Skills as markdown instructions (Cursor) parallel tool reuse pattern in memory.

## Architecture Implications

- assembleToolPool and getAllBaseTools are skill registry sources.
- Required MCP servers declare dependencies on external skills.
- Dynamic schema omits skills model cannot currently invoke.

## Production Implications

- Skill graph drift when plugins connect mid-session — refresh tool pool each turn.
- Document skill dependencies for digital twin reproducibility.
- Future: explicit skill graph DB; today: config files + registries.

## Related Concepts

- [[role-systems]]
- [[agent-personas]]
- [[mcp-orchestration]]

## Sources

- `Books/claude/ch02-bootstrap.md`
- `Books/claude/ch06-tools.md`
- `Books/claude/ch08-sub-agents.md`

## My Notes

