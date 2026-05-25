# Урок: Критик — не истина

## Что это?

**Критик** в демо — роль, которая оценивает черновик (часто структуру/стиль), а не проверяет факты в мире.

## Почему это важно?

«Critic PASS» легко путают с «можно публиковать правду». Это главный тихий сбой review-loop.

## Что может пойти не так?

- Публикация после PASS при ложных фактах
- Удаление human gate «потому что критик строгий»
- Критик как единственная verification

## Как это проверить?

Прочитайте `observability/examples/failed-review-trace.txt`. Найдите: critic pass → human deny или publish block.

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

## Какое демо это показывает?

- review-queue-workflow (approval-denied)
- [../modules/module-02-why-ai-systems-fail.md](../modules/module-02-why-ai-systems-fail.md)
