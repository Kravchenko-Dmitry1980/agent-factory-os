# Урок: Визуальная проверка

## Что это?

Перед кликом в GUI агент **смотрит экран** (скриншот/состояние) и сверяет ожидание — visual verification.

## Почему это важно?

Координаты и селекторы ломаются; «кликнул — значит правильно» — типичный обман.

## Что может пойти не так?

- Клик без проверки кадра
- Ложный PASS по старому скриншоту
- Игнор outcome-b (неверный экран)

## Как это проверить?

Сценарий outcome-b должен блокировать или отличаться от happy в trace.

```powershell
python prototypes/gui-verification-agent/minimal-demo.py --scenario outcome-b
```

Пример: `observability/examples/unsafe-gui-action-trace.txt`  
Антипаттерн: `agent-os/09_antipatterns/unverified-gui-clicks.md`

## Какое демо это показывает?

- `prototypes/gui-verification-agent/`
