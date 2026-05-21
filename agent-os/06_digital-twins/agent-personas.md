# Agent Personas

## Definition

An **agent persona** is a configured behavioral profile — system prompt slice, agent definition, permission mode, model tier, and memory context — that shapes how an agent acts in a domain or role.

## Key Ideas

- Built-in personas: Explore, Plan, Verify, general-purpose, fork.
- Custom personas via agent definition frontmatter (loaded at setup).
- Output style, language preference, CLAUDE.md shape persona at project level.
- Coordinator persona slimmed when coordinator system prompt already covers usage.

## Architecture Implications

- Persona = agent definition + tool pool + model + mode + isolation.
- Dynamic AgentTool prompt adapts to available personas and feature flags.
- Persona volatile lists moved to attachments for cache stability.

## Production Implications

- Persona mismatch wastes cost or misses quality bar.
- Digital twin persona should version with git like team memory.
- Multiple personas per project enable role-based delegation.

## Related Concepts

- [[role-systems]]
- [[skill-graphs]]
- [[persistent-identity]]

## Sources

- `Books/claude/ch08-sub-agents.md`

## My Notes

