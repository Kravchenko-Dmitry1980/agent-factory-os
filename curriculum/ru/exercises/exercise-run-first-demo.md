# Упражнение: Первое демо

## Зачем это упражнение

Доказать, что вы можете локально запустить governed workflow и прочитать базовый вывод.

## Время

15 минут

## Шаги

1. Откройте терминал в `C:\Dima\Projects\CURSOR\AGENT`
2. Запустите:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

3. Найдите: Task, Critic verdict, Human decision, Published, Audit
4. Запустите bypass:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

## Ожидаемый результат

Happy: Published True. Bypass: Published False.

## Что наблюдать

- Решение человека на happy path
- Сообщение о блокировке bypass в audit

## Вопросы

1. Критик проверял факты или структуру?
2. Что изменилось между сценариями?

## Критерии успеха

Пересказ happy path в 4 шага; явно сказать, что bypass заблокирован.

## Критерии ошибки

Команда не запускается; не найден audit; считаете, что bypass опубликовал.

Модуль: [../modules/module-00-orientation.md](../modules/module-00-orientation.md)
