# Phase 3 Impact Review (External Repos)

**Date:** 2026-05-25

## Does any repo change Phase 3.0 scope?

**No.**

Phase 3.0 remains:

- Agent Builder Kit v0.1
- Markdown specs / checklists / templates
- Review Assistant Agent reference
- No code, generator, runtime, factory

## Can any repo be used directly in Phase 3.0?

**No direct adoption.**

- No `npx install` from triaged repos
- No copied SKILL.md or hook/MCP files
- No GitHub Action workflow
- No ruflo / SuperClaude init

## What can influence Phase 3.0 (allowed inspiration only)

| Influence type | Source repos |
|----------------|--------------|
| Skill frontmatter schema | scientific-agent-skills |
| Template type taxonomy | claude-code-templates |
| Review checklist bullets | claude-code-action solutions (MD only) |
| Command grouping labels | SuperClaude (not commands themselves) |
| Change/Spec document shape | agentic-project-management (compare only) |

## What is forbidden in Phase 3.0 because of triage

| Forbidden | Learned from |
|-----------|--------------|
| Runtime adoption | ruflo |
| Swarm / autopilot | ruflo, APM apm-auto |
| GitHub Action automation | claude-code-action |
| MCP/hook bulk import | claude-code-templates, SuperClaude |
| Skill mass install | scientific-agent-skills |
| RAG/self-learning memory | ruflo |
| Template marketplace | claude-code-templates |
| Code copy | all |

## Alignment with existing gates

- [../PHASE_3_START_CONDITIONS.md](../PHASE_3_START_CONDITIONS.md) — unchanged  
- [../phase-2-8/PHASE_3_MINIMAL_SCOPE.md](../phase-2-8/PHASE_3_MINIMAL_SCOPE.md) — unchanged  
- [DO_NOT_ADOPT_NOW.md](DO_NOT_ADOPT_NOW.md) — reinforced
