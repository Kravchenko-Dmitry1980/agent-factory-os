# AGENT Repository

Engineering knowledge operating system for AI agents.

## Start Here

| Audience | Entry |
|----------|-------|
| **Russian (recommended for lab)** | **[START_HERE_RU.md](START_HERE_RU.md)** → [QUICKSTART_RU.md](QUICKSTART_RU.md) |
| English / knowledge OS | **[agent-os/README.md](agent-os/README.md)** — overview, philosophy, lifecycle |
| Operators | [operator-playbooks/README.md](operator-playbooks/README.md) · [operator-playbooks/ru/](operator-playbooks/ru/) |
| Students | [curriculum/README.md](curriculum/README.md) · [curriculum/ru/](curriculum/ru/) |
| Phase 3 gate | [governance/PHASE_3_START_CONDITIONS.md](governance/PHASE_3_START_CONDITIONS.md) · [PHASE_3_WARNING_RU.md](PHASE_3_WARNING_RU.md) |
| Phase 3.0 kit | [agent-builder-kit/README.md](agent-builder-kit/README.md) · [agent-builder-kit/RU_SUMMARY.md](agent-builder-kit/RU_SUMMARY.md) |

## Structure

```
agent-os/
├── 00_foundations/      Core concepts
├── 01_agent-runtime/    Loop, tools, concurrency
├── 02_memory/           Memory systems
├── 03_harness-engineering/
├── 04_multi-agent/
├── 05_mcp/
├── 06_digital-twins/
├── 07_projects/
├── 08_patterns/
├── 09_antipatterns/
├── 10_research/
├── 11_glossary/
├── 12_diagrams/
└── templates/
```

## Source Corpora

**Books/** is the **source layer** — canonical, read-only corpora.  
**agent-os/** is the **curated knowledge layer** — atomic notes, patterns, research catalog.

- [Books/claude/](Books/claude/) — Claude Code architecture corpus (18 markdown chapters)
- [Books/agents/](Books/agents/) — Code as Agent Harness survey corpus (PDF + converted chapters)

Preservation policy: [agent-os/10_research/sources.md](agent-os/10_research/sources.md)

**Research layer:** [agent-os/10_research/](agent-os/10_research/README.md) — catalog, extraction plans, chapter index stubs

Extracted atomic notes: `agent-os/00–09/` (partial, per extraction plan)

## Conventions

- kebab-case filenames
- One concept per markdown file
- Required sections: Definition, Key Ideas, Architecture Implications, Production Implications, Related Concepts, Sources, My Notes
- Wikilinks `[[concept-name]]` for Obsidian/Cursor graph navigation
