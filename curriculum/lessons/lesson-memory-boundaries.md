# Lesson: Memory Boundaries

## What is this?

**Bounded memory** limits how much context agents keep, and **when** they may write new memory.

## Why does it matter?

Unbounded memory accumulates errors, costs, and stale "facts" that poison future decisions.

## What can go wrong?

- Silent truncate on overflow
- Agent writes unverified "learnings"
- Mid-session memory injection without gate

## How do we check it?

Overflow and unverified scenarios reject; snapshot stays meaningful.

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
```

## Which demo shows it?

`prototypes/bounded-memory-agent/`

Doctrine: `agent-os/doctrine/bounded-memory.md`
