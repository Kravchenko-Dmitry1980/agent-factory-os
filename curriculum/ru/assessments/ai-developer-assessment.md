# Оценка: AI-разработчик

## Письменные вопросы

10 базовых (см. beginner) плюс:

11. Что такое verification-before-writeback?
12. Какие события ожидаете при escalation?
13. Что изменится, если все демо свести в shared/gates.py?

## Практические задания

- Все 10 упражнений из `../exercises/` (с наставником)
- Объяснить diff trace happy vs malformed LLM
- Назвать gate, который исчез бы при accidental-auto-approve

## Распознавание опасных признаков

- «Кэш промпта важнее gates»
- «Subagent swarm вместо одного gated workflow»
- Promotion markdown в agent-os без review

## Объясни своими словами

Почему маленькое демо лучше большой платформы **для обучения**?

## Критерии pass

10/10 базовых; 8/10 упражнений; понимает impact shared runtime.

## Критерии fail

Предлагает убрать approval; не проходит read-trace; не различает critic и verify.

Трек: [../role-based-tracks/track-ai-developer.md](../role-based-tracks/track-ai-developer.md)
