# Упражнение: Change proposal

## Зачем это упражнение

Менять систему через документ, а не «быструю правку».

## Время

30 минут

## Шаги

1. Прочитайте `evolution/change-proposals/change-template.md`
2. Сценарий: увеличить MAX_RETRIES с 3 до 5 в учебном workflow
3. Заполните шаблон: цель, риск, gates затронуты, smoke до/после, rollback план
4. **Код не менять** — только proposal (с наставником)

## Ожидаемый результат

Заполненный proposal с явным rollback.

## Что наблюдать

Риски: retry storm, слабее escalation

## Вопросы

1. Какие trace изменятся?
2. Кто одобряет proposal?

## Критерии успеха

Все секции шаблона заполнены; риск retry назван.

## Критерии ошибки

Пустой rollback; «просто поменяем в коде».

Модуль: [../modules/module-11-safe-evolution.md](../modules/module-11-safe-evolution.md)
