# Swarm Playbooks — Operational Corpus

Изолированная **operational / instructional** база знаний, извлечённая из двух playbook-источников о сборке multi-agent систем с HITL.

## Что это

**Не canonical architecture.** Не governance layer. Не production reference.

Это контролируемая экстракция **операционной мудрости** для:

- поэтапного внедрения агентов (MVP → orchestration → review)
- HITL и approval gates
- critique loops (с явными ограничениями)
- queue-backed execution и budget awareness

## Источники (immutable)

| Файл | Описание |
|------|----------|
| `source/ai-agents-from-scratch.ru.md` | Универсальный 11-этапный гайд «с нуля» |
| `source/swarm-ai-agents-prompts.ru.md` | Промты для сборки «Роя из 8 агентов» |

Файлы в `source/` **не редактировать**. Provenance — в `*.provenance.md`.

## Границы корпуса

### Является

- operational patterns и anti-patterns
- lifecycle и HITL guidance
- critique limitations (обязательно)
- promotion candidates review (без auto-promote)

### Не является

- частью `agent-os/` (curated canonical layer)
- частью `governance/`
- runtime-кодом или install tutorial
- заменой architecture specs в `Books/brain-os/`

## Как читать

1. **`index.md`** — навигация
2. **`review/source-analysis.md`** — сильные/слабые стороны источников
3. **`lifecycle/orchestration-lifecycle.md`** — канонический операционный lifecycle
4. **`patterns/`** — reusable operational patterns
5. **`anti-patterns/`** — operational dangers
6. **`governance/corpus-positioning.md`** — позиционирование относительно Agent-OS

## Metadata (все extracted notes)

```yaml
classification: reusable-pattern | beginner-tutorial | operational-guidance | non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
```

## Phase

**SWARM-EXTRACTION** — operational knowledge isolation and refinement.  
**NOT** architecture promotion, taxonomy expansion, or governance rewriting.
