# Hermes Desktop Delta Triage (Phase 3.2.2)

**Статус:** research-only — **без** adoption, **без** install/run, **без** Operator Console.

---

## Зачем этот triage

Hermes Desktop переводит экосистему Hermes Agent с CLI-only на **GUI operator layer**: install, chat, profiles, memory, skills, tools, schedules, gateways, provider config.

Это релевантно для Agent-OS как **reference delta** для будущего Operator Console — не как код для копирования.

---

## Почему RU fork

[vakovalskii/hermes-desktop-ru](https://github.com/vakovalskii/hermes-desktop-ru) добавляет:

- русскую локализацию UI (`ru` locale)
- RU-first defaults в setup
- NeuralDeep Hub и Bitrix VibeCode (реализованы через custom endpoint routing)
- GigaChat / YandexGPT — **planned** (упомянуты в README, не найдены в коде)

Полезно для RU-first product direction и будущего provider backlog — **не** для интеграции сейчас.

---

## Правила Phase 3.2.2

| Разрешено | Запрещено |
|-----------|-----------|
| Shallow clone в `source/` | `npm install`, запуск Electron |
| Чтение README, source structure | Adoption, import кода |
| Markdown-отчёты здесь | Operator Console implementation |
| Future backlog | Real provider integration |
| Governance review | Изменение Phase 3.3 scope |

**Код из `source/` не выполнялся.**

---

## Локальные клоны

| Repo | Commit (short) | Path |
|------|----------------|------|
| fathah/hermes-desktop | `075e516` | `source/hermes-desktop/` |
| vakovalskii/hermes-desktop-ru | `2bbe940` | `source/hermes-desktop-ru/` |

---

## С чего читать

| Порядок | Документ |
|---------|----------|
| 1 | [repo-reviews/hermes-desktop.md](repo-reviews/hermes-desktop.md) |
| 2 | [repo-reviews/hermes-desktop-ru.md](repo-reviews/hermes-desktop-ru.md) |
| 3 | [architecture-delta/operator-console-implications.md](architecture-delta/operator-console-implications.md) |
| 4 | [future-backlog/do-not-build-now.md](future-backlog/do-not-build-now.md) |
| 5 | [../governance/phase-3-2-2/FINAL_PHASE_3_2_2_REPORT.md](../../governance/phase-3-2-2/FINAL_PHASE_3_2_2_REPORT.md) |

---

## Что может стать полезным позже

- Operator Console concept (Phase 4+)
- Trace viewer / approval queue UI patterns
- Provider config **governance** lessons (not framework)
- RU-first UX requirements
- Desktop security checklist input

---

## Что не должно влиять на Phase 3.3

Phase 3.3 остаётся: **Real LLM Provider Boundary Plan** (plan only).

Hermes Desktop **не** меняет scope 3.3: no desktop UI, no provider framework, no adoption.

См. [../../governance/phase-3-2-2/PHASE_3_3_IMPACT_REVIEW.md](../../governance/phase-3-2-2/PHASE_3_3_IMPACT_REVIEW.md)
