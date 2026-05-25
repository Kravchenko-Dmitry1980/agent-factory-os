# Упражнение: Решение об откате

## Зачем это упражнение

Учиться rollback (откат) когда поведение стало небезопасным.

## Время

20 минут

## Шаги

1. Прочитайте `evolution/examples/` (любой пример с missing approval)
2. Сценарий: после изменения в trace нет `approval_requested` на publish path
3. Запишите: rollback да/нет, почему, какие smoke перезапустить
4. Сверьтесь с [../../operator-playbooks/change-guides/how-to-rollback.md](../../operator-playbooks/change-guides/how-to-rollback.md) (если файл есть — иначе how-to-change-safely)

## Ожидаемый результат

Решение: **rollback обязателен** до новых фич.

## Что наблюдать

Отсутствие gate в trace = регрессия governance

## Вопросы

1. Что такое rollback одной фразой?
2. Можно ли «починить» промптом без отката?

## Критерии успеха

Обоснован rollback; перечислены smoke checks.

## Критерии ошибки

«Подождём» при missing approval; путают с redeploy.

Модуль: [../modules/module-11-safe-evolution.md](../modules/module-11-safe-evolution.md)
