# Missing Idempotency

## Problem

Повтор task_id → duplicate events/trace pollution

## Fix

Idempotent handlers keyed by task_id; dedup event_id

## Gap

Source заявляет NFR, **не даёт** algorithm

## Maturity

production-relevant

## Provenance

`source/Brain OS.docx` B NFR; I.§5
