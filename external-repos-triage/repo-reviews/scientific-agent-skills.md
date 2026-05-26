# Repository Review: scientific-agent-skills

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/K-Dense-AI/scientific-agent-skills |
| **Local path** | `external-repos-triage/source/scientific-agent-skills/` |
| **Main purpose** | 138+ scientific/research Agent Skills (agentskills.io standard) for Cursor, Claude Code, Codex |
| **Claimed capabilities** | Domain skills (bio, chem, clinical, imaging, ML), database access docs, multi-step scientific workflows |
| **Primary audience** | Researchers, bio/chem/med developers using AI coding agents |
| **Main language / stack** | Markdown skills (`scientific-skills/*/SKILL.md`), Python examples in docs; install via `npx skills add` |
| **Last inspected** | 2026-05-25 |
| **Commit inspected** | `5bd00bf` |

## What This Repo Is

Каталог **готовых skill-файлов** с YAML frontmatter (`name`, `description`, `license`) и длинными инструкциями — стандарт [Agent Skills](https://agentskills.io/). Каждый skill учит агента работать с конкретной научной библиотекой или базой данных.

## What This Repo Is NOT

- Не governance-слой Agent-OS Lab
- Не проверенный runtime с gates (fail-closed, human approval)
- Не замена curriculum или evaluation
- Не безопасно «установить всё одной командой»

## Most Useful Ideas

- Структура `SKILL.md`: frontmatter + trigger description + requirements + examples
- Доменная группировка (`scientific-skills/<domain>/`)
- Явный **Security Disclaimer** и рекомендация skill-scanner
- Совместимость с Cursor / Claude Code / Codex (как **внешний** формат, не наш)

## Dangerous Ideas

- `npx skills add` — массовая установка без review каждого skill
- Skills с shell/network/package install в инструкциях
- «AI Scientist on desktop» маркетинг (BYOK product) — риск hype
- 138 skills — cognitive overload; supply-chain surface

## Relevance

| Area | Relevance |
|------|-----------|
| Agent-OS | **Low direct** — research corpus only; promotion forbidden |
| Agent Builder Kit | **High structural** — future `skill-template-spec` |
| Cursor / Claude Code | **High** — same skill discovery model |
| Skills ecosystem | **Primary reference** |
| Digital twins | **Low** — not identity/replay |
| CV agents | **Medium later** — imaging/pathology skills exist; need evidence contracts |

## Security / Supply Chain

- Skills = arbitrary instructions to agent
- Community contributions mixed with K-Dense authored
- Weekly scan claimed; user must read each SKILL.md
- Medical/clinical skills — higher harm if misused

## What We Can Learn

- Metadata: `name`, rich `description` (when to trigger / when NOT)
- Per-skill LICENSE reference
- Security.md + scanner workflow
- «Install only what you need» policy

## What We Must Not Copy

- Bulk install command into our repo
- Skill bodies into agent-os without promotion pipeline
- Database API keys patterns without governance
- «Production-ready» claims without our trace/evaluation

## Decision

**STUDY_NOW** (structure and security policy only — **no install**)

## Rationale

Best reference for **future skill template spec** aligned with agentskills.io. High value, manageable risk if we never auto-install.

## Recommended Future Action

Phase 3.1+: draft `skill-template-spec.md` inspired by frontmatter + trigger boundaries; require provenance + allowed/forbidden actions per our SKILL_ECOSYSTEM_SECURITY_REVIEW.
