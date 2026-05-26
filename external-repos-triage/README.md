# External Repos Triage (Phase 2.10)

**Статус:** только исследование — **без** внедрения, **без** запуска, **без** установки.

---

## Зачем этот этап

Перед Phase 3 (Agent Builder Kit v0.1 — только MD specs) мы смотрим **внешние** репозитории про skills, Claude Code, оркестрацию и PM-агентов — чтобы понять, **чему учиться**, а не **что копировать**.

---

## Правила безопасности

| Разрешено | Запрещено |
|-----------|-----------|
| Shallow clone `--depth 1` в `source/` | `npm install`, `pip install`, `uv sync` |
| Чтение README, SKILL.md, docs | Запуск скриптов, Actions, MCP, демо |
| Markdown-отчёты в этом каталоге | Копирование кода в agent-os / prototypes |
| | Установка skills/templates в проект |
| | Submodule / adoption |

**Ничего из `source/` не выполнялось** в Phase 2.10.

---

## С чего читать

| Порядок | Документ |
|---------|----------|
| 1 | [../governance/phase-2-10/FINAL_PHASE_2_10_REPORT.md](../governance/phase-2-10/FINAL_PHASE_2_10_REPORT.md) |
| 2 | [../governance/phase-2-10/REPO_PRIORITY_MATRIX.md](../governance/phase-2-10/REPO_PRIORITY_MATRIX.md) |
| 3 | [repo-reviews/](repo-reviews/) — по одному файлу на репо |
| 4 | [comparison/repo-comparison.md](comparison/repo-comparison.md) |
| 5 | [useful-patterns/](useful-patterns/) · [dangerous-patterns/](dangerous-patterns/) |

---

## Локальные клоны (`source/`)

| Repo | Commit (short) | Path |
|------|----------------|------|
| scientific-agent-skills | 5bd00bf | `source/scientific-agent-skills/` |
| agentic-project-management | 67b954d | `source/agentic-project-management/` |
| ruflo | 60f37f2 | `source/ruflo/` |
| SuperClaude_Framework | 226c45c | `source/SuperClaude_Framework/` |
| claude-code-action | 787c5a0 | `source/claude-code-action/` |
| claude-code-templates | a8f3752 | `source/claude-code-templates/` |
| hermes-desktop | 075e516 | `source/hermes-desktop/` |
| hermes-desktop-ru | 2bbe940 | `source/hermes-desktop-ru/` |

> Phase 3.2.2: Hermes Desktop triage — [hermes-desktop-delta/](hermes-desktop-delta/README.md). **Code not executed.**

---

## Hermes Desktop delta (Phase 3.2.2)

| Doc | Purpose |
|-----|---------|
| [hermes-desktop-delta/README.md](hermes-desktop-delta/README.md) | Triage index |
| [hermes-desktop-delta/repo-reviews/](hermes-desktop-delta/repo-reviews/) | Upstream + RU fork reviews |
| [../governance/phase-3-2-2/FINAL_PHASE_3_2_2_REPORT.md](../governance/phase-3-2-2/FINAL_PHASE_3_2_2_REPORT.md) | Final report |

Research-only — no adoption, no Operator Console build.

> Клоны большие (особенно templates, ruflo). Для git рассмотрите `external-repos-triage/source/` в `.gitignore` — отчёты в `repo-reviews/` и `governance/phase-2-10/` самодостаточны.

---

## Связь с Phase 3

Phase 3.0 **не меняется**: только markdown specs, Review Assistant template, без runtime.

Влияние внешних репо — **структурное вдохновение** (формат skill, taxonomy шаблонов), не adoption.

См. [../governance/phase-2-10/PHASE_3_IMPACT_REVIEW.md](../governance/phase-2-10/PHASE_3_IMPACT_REVIEW.md)
