# Оценка: начинающий

## Письменные вопросы

Ответьте своими словами (2–4 предложения каждый).

1. Что такое fail-closed?
2. Почему критик не является истиной?
3. Почему вывод LLM не равен правде?
4. Зачем нужен человек в контуре?
5. Что такое trace?
6. Что такое rollback?
7. Что такое platform drift?
8. Почему нельзя слишком рано делать framework?
9. Что делает workflow безопасным?
10. Когда нужно передавать задачу человеку?

Сверка с наставником: [../../operator-playbooks/onboarding/onboarding-assessment.md](../../operator-playbooks/onboarding/onboarding-assessment.md)

## Практические задания

1. [../exercises/exercise-run-first-demo.md](../exercises/exercise-run-first-demo.md) — pass
2. [../exercises/exercise-read-trace.md](../exercises/exercise-read-trace.md) — pass

## Распознавание опасных признаков

Что опасно? Почему?

- A) Убрать human approval для внутренних документов
- B) Читать observability/examples
- C) Увеличить retries без proposal
- D) Запускать smoke после изменения

**Ответы:** A и C опасны.

## Объясни своими словами

Объясните другу за 60 секунд, что это за репозиторий, **без** слов «AI-платформа».

## Критерии pass

- 7/10 письменных ответов достаточны (судья — наставник)
- Оба практических задания pass
- Red flags: 2/2 верно
- Самостоятельно: review-loop happy + bypass

## Критерии fail

Не запускаете демо; критик = истина; не можете определить trace; одобряете A или C.
