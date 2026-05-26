# Research-Only Decisions

**None of these repositories merge into Agent-OS now.**  
**None are Phase 3.0 implementation dependencies.**

| Repo | Decision | Allowed use | Forbidden use | Future revisit |
|------|----------|-------------|---------------|----------------|
| scientific-agent-skills | STUDY_NOW | Read SKILL.md structure; security.md | npx install; copy skills | Phase 3.1 skill spec |
| claude-code-templates | STUDY_NOW | Taxonomy sampling | npx install; MCP/hooks | Phase 3.1 metadata |
| agentic-project-management | STUDY_LATER | Read planning templates | apm init; apm-auto | Phase 4 PM template |
| SuperClaude_Framework | STUDY_LATER | commands.md structure | pip install; personas | Phase 4 operator map |
| claude-code-action | FREEZE | Read security/solutions MD | Add workflow YAML | Phase 5+ CI pilot |
| ruflo | FREEZE | Anti-pattern teaching | Any init/install | Unlikely |

## Global rule

`external-repos-triage/source/` is **quarantine** — not imported by prototypes, curriculum, or agent-os.
