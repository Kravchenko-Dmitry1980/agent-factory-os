# Patterns — Index

Architecture patterns extracted from book chapters → `agent-os/08_patterns/`.

## Plans

- [Pattern extraction plan](extraction-plan.md) — backlog + anti-pattern pairing
- [Master extraction plan](../extraction-plan.md)

## Extracted Patterns

→ [08_patterns/index.md](../../08_patterns/index.md)

| Pattern | Status |
|---------|--------|
| generator-loop-pattern | ✅ |
| self-describing-tools | ✅ |
| two-tier-state | ✅ |
| sticky-latch-pattern | ✅ |
| withholding-errors | ✅ |
| fail-closed-defaults | ✅ |
| prompt-cache-as-constraint | ✅ |

## Primary Source Chapters

| Chapter | Patterns introduced |
|---------|---------------------|
| [ch01](../chapters/ch01-architecture.md) | generator loop, self-describing tools |
| [ch02](../chapters/ch02-bootstrap.md) | fast-path, module-level I/O |
| [ch03](../chapters/ch03-state.md) | two-tier state, sticky latch, onChange |
| [ch04](../chapters/ch04-api-layer.md) | prompt cache constraint, watchdog |
| [ch05](../chapters/ch05-agent-loop.md) | withholding, immutable transitions, circuit breakers |
| [ch07](../chapters/ch07-concurrency.md) | speculative execution, input-dependent concurrency |
| [ch09](../chapters/ch09-fork-agents.md) | byte-identical prefix (⬜) |
| [ch11–17](../chapters/index.md) | see extraction plan |

## Anti-Patterns

Fix patterns pair with entries in [09_antipatterns](../../09_antipatterns/index.md) — see [pattern plan § Anti-Pattern Pairing](extraction-plan.md#anti-pattern-pairing).

## Up

- [Research README](../README.md)
