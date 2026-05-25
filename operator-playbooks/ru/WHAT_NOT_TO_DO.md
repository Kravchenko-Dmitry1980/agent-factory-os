# Чего не делать (RU)

Краткий список для новичка, стажёра и оператора.

---

## Процесс и код

| Не делать | Вместо этого |
|-----------|--------------|
| Патчить вслепую | [ERRORS.md](ERRORS.md) → rollback |
| Создавать новый **framework** / общий runtime | Один демо = один урок |
| Убирать **approval** | Human gate обязателен на риске |
| Доверять **критику** как истине | Verification + человек |
| Доверять **LLM output** как истине | Verify + trace |
| Добавлять **CI/CD** «для удобства» | Ручные evaluation scripts |
| Добавлять **runtime** / MCP server | Freeze Phase 3 |
| Начинать **Phase 3 implementation** без условий | [PHASE_3_START_CONDITIONS.md](../../governance/PHASE_3_START_CONDITIONS.md) |

---

## Папки (не трогать без charter)

- `Books/` — read-only корпус
- `experiments/` — исследования
- `agent-os/` — promotion pipeline
- `prototypes/shared/` — не превращать в платформу
- `evaluation/scripts/` — не ослаблять проверки
- `governance/` — не переписывать политики «под себя»

Полный EN список: [../start-here/what-not-to-touch.md](../start-here/what-not-to-touch.md)

---

## Нарратив (опасно для команды)

- «Демо = production MVP»
- «Phase 3 = фабрика готова»
- «Цифровой двойник в этом спринте»
- «CV агент — первый шаблон»
- «Рой агентов без человека»

См. [PHASE_3_WARNING_RU.md](../../PHASE_3_WARNING_RU.md)

---

## Если давят на скорость

Покажите **bypass-attempt** demo: Published False — это feature, не баг.
