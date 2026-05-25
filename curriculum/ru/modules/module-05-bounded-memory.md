# Модуль 05 — Ограниченная память

## Цель

Память с лимитами и записью только после проверки.

## Простое объяснение

Bounded memory — не «помнить всё». Снимок памяти фиксируется (frozen snapshot), новое пишется только после verification. Переполнение и непроверенная запись отклоняются.

## Ключевые идеи

- Лимит символов / записей
- Writeback только после verify
- Середина сессии — не место для «догрузить всю историю»
- Память не заменяет проверку фактов

## Что прочитать

- `agent-os/doctrine/bounded-memory.md`
- `agent-os/02_memory/frozen-memory-snapshot.md`
- [../lessons/lesson-memory-boundaries.md](../lessons/lesson-memory-boundaries.md)

## Что запустить

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario happy
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
```

## Упражнение

Связано с [../lessons/lesson-memory-boundaries.md](../lessons/lesson-memory-boundaries.md); повторите happy и overflow.

## Частые ошибки

- Безлимитный контекст «для качества»
- Запись в память до verify
- Память как замена RAG «на всё»

## Контрольные вопросы

1. Что такое frozen snapshot?
2. Что делает сценарий overflow?
3. Почему unverified-writeback блокируется?

## Ожидаемый результат

Студент описывает gate памяти на примере trace overflow.
