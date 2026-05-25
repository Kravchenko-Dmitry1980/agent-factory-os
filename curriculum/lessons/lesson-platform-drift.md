# Lesson: Platform Drift

## What is this?

**Platform drift** = educational demos slowly become an accidental "product framework" with shared engines and weakened gates.

## Why does it matter?

Teams maintain the framework instead of governance. New people learn APIs, not safety.

## What can go wrong?

- Shared orchestrator for all demos
- CLI runner + CI before doctrine understood
- "Just one more abstraction"

## How do we check it?

Red flags: growing `prototypes/shared/` without review, universal adapters, pytest replacing human trace review.

`evolution/drift-detection/early-warning-signals.md`

Exercise: [../exercises/exercise-identify-platform-drift.md](../exercises/exercise-identify-platform-drift.md)

## Which demo shows it?

Not one demo — **negative lesson**. Read `evolution/examples/unsafe-shared-runtime.md`
