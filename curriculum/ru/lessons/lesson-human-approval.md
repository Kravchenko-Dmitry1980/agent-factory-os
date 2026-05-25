# Урок: Одобрение человеком

## Что это?

Человек **явно** разрешает действие с последствиями (публикация, внешний API, платёж).

## Почему это важно?

Автономия без governance масштабирует ошибки. Человек — gate, а не «тормоз для слабых моделей».

## Что может пойти не так?

- Снятие approval для «внутренних» задач
- Auto-approve по таймауту
- Критик заменяет человека

## Как это проверить?

Сравните approved vs no-approval; в trace ищите human_decision / approval_denied.

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/integrations/telegram-review-gate/minimal-demo.py --scenario happy
```

## Какое демо это показывает?

- fail-closed-external-action
- telegram-review-gate
- review-loop-agent (human step)
