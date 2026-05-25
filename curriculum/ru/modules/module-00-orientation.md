# Модуль 00 — Ориентация

## Цель

Понять, что это за репозиторий, для кого он и чего он **явно не делает**.

## Простое объяснение

Это **учебная лаборатория** безопасных AI-workflow — не программа, которую выкатывают клиентам. Здесь есть принципы (agent-os), маленькие демо (prototypes) и руководства оператора.

## Ключевые идеи

- Сначала governance (правила), потом «умность»
- Маленькие демо показывают gates; большие платформы их прячут
- Phase 3 (Agent Builder Kit) — **после** обучения, не до

## Что прочитать

- [../README.md](../README.md)
- `agent-os/doctrine/system-positioning.md`
- [../../operator-playbooks/start-here/what-not-to-touch.md](../../operator-playbooks/start-here/what-not-to-touch.md)

## Что запустить

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

## Упражнение

[../exercises/exercise-run-first-demo.md](../exercises/exercise-run-first-demo.md)

## Частые ошибки

- Считать демо production-сервисом
- Начинать с `Books/` вместо curriculum
- Пропустить раздел «чем проект не является»

## Контрольные вопросы

1. Назовите две вещи, которыми проект не является.
2. В какой папке лежат маленькие запускаемые демо?
3. Где лежат ежедневные руководства оператора?

## Ожидаемый результат

Студент за 2 предложения объясняет: «лаборатория безопасных AI-workflow, не развёрнутая AI-платформа».
