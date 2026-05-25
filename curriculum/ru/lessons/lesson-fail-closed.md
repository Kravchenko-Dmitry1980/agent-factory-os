# Урок: Fail-closed

## Что это?

**Fail-closed** — поведение «при сомнении не делать опасное действие»: остановка, deny, запись в trace с причиной.

## Почему это важно?

Без fail-closed система «угадывает» и выполняет отправку, публикацию или платёж при неполных данных. Это хуже падения — потому что выглядит как успех.

## Что может пойти не так?

- Таймаут трактуют как одобрение
- «Критик не уверен — но попробуем»
- Bypass в обход human gate
- Exit code 0 при Published False

## Как это проверить?

Сравните сценарии no-approval / uncertain / rejected. В trace должны быть gate + reason + исход deny.

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
```

## Какое демо это показывает?

- `prototypes/fail-closed-external-action/`
- `prototypes/review-loop-agent/` (bypass-attempt)
- Доктрина: `agent-os/doctrine/fail-closed-execution.md`
