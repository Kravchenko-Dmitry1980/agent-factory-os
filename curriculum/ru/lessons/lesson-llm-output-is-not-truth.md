# Урок: Вывод LLM — не истина

## Что это?

Ответ модели — **гипотеза**, даже если JSON валидный и тон уверенный.

## Почему это важно?

Модели придумывают поля, даты и «факты». Структура без verification — декорация.

## Что может пойти не так?

- Автопринятие malformed JSON
- Публикация без второго шага verify
- «Исправим промптом» вместо gate

## Как это проверить?

Сравните happy и malformed; смотрите trace на событие verify fail.

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
```

Пример trace: `observability/examples/malformed-llm-trace.txt`

## Какое демо это показывает?

- `integrations-real/llm-verification-adapter/`
- [../modules/module-03-verification-first.md](../modules/module-03-verification-first.md)
