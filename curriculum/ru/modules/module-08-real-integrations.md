# Модуль 08 — Реальные интеграции

## Цель

Границы с внешним миром: реальный I/O, но по умолчанию **mock**.

## Простое объяснение

`integrations-real/` учит **один адаптер = один урок**: LLM, очередь, файловый аудит. Режим `--real` только с пониманием рисков. Local-first — без облачной «фабрики».

## Ключевые идеи

- Mock по умолчанию
- Верификация LLM-ответа отдельно от генерации
- Аудит в файл — lineage
- Не смешивать все адаптеры в один runtime на обучении

## Что прочитать

- `integrations-real/README.md`
- `governance/local-first-policy.md`
- [../lessons/lesson-llm-output-is-not-truth.md](../lessons/lesson-llm-output-is-not-truth.md)

## Что запустить

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/local-queue-worker/minimal-demo.py --scenario recovery
python integrations-real/filesystem-audit-log/minimal-demo.py --scenario happy
```

## Упражнение

[../exercises/exercise-detect-bad-llm-output.md](../exercises/exercise-detect-bad-llm-output.md)

## Частые ошибки

- Сразу `--real` на стажировке
- Доверие API-ответу без verify
- «Подключим всё» в одном скрипте

## Контрольные вопросы

1. Зачем mock?
2. Что показывает malformed?
3. Где policy local-first?

## Ожидаемый результат

Студент сравнивает happy и malformed trace.
