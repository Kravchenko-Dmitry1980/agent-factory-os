# Урок: Границы памяти

## Что это?

Память агента **ограничена** (символы/записи) и пополняется только после проверки (verified writeback).

## Почему это важно?

Без границ контекст раздувается, старые ошибки «закрепляются», проверки дорожают.

## Что может пойти не так?

- Overflow без отказа
- Запись до verify
- «Догрузить всё в середине сессии»

## Как это проверить?

Запустите overflow и unverified-writeback; найдите deny в выводе/trace.

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
```

## Какое демо это показывает?

- `prototypes/bounded-memory-agent/`
- `agent-os/doctrine/bounded-memory.md`
