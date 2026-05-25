# Модуль 03 — Сначала проверка

## Цель

Проверять **до** доверия, публикации и записи в память.

## Простое объяснение

Verification-first — правило: не публиковать и не запоминать, пока нет проверки (факты, экран, структура — по типу задачи). Красивый ответ LLM — гипотеза, не факт.

## Ключевые идеи

- Структура JSON ≠ правда
- GUI: смотреть экран до клика
- Проверка отдельна от критика
- Ошибка проверки → stop (fail-closed)

## Что прочитать

- `agent-os/doctrine/verification-first.md`
- `agent-os/08_patterns/verification-before-writeback.md`
- [../lessons/lesson-llm-output-is-not-truth.md](../lessons/lesson-llm-output-is-not-truth.md)
- [../lessons/lesson-visual-verification.md](../lessons/lesson-visual-verification.md)

## Что запустить

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python prototypes/gui-verification-agent/minimal-demo.py --scenario outcome-b
```

## Упражнение

[../exercises/exercise-detect-bad-llm-output.md](../exercises/exercise-detect-bad-llm-output.md)

## Частые ошибки

- Считать валидный JSON доказательством
- Пропускать visual check для GUI
- Путать критика с верификатором

## Контрольные вопросы

1. Чем verification отличается от critic?
2. Когда нужна visual verification?
3. Что делать при malformed LLM output?

## Ожидаемый результат

Студент называет шаг проверки до publish для своего сценария.
