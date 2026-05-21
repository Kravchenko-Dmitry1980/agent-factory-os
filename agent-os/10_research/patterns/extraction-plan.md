# Patterns — Extraction Plan

Reusable architecture patterns from `Books/claude/` → `agent-os/08_patterns/`.

Patterns describe **how to build**; concepts describe **what exists**.

## Extracted Patterns ✅

| Pattern | Source | Agent-OS note |
|---------|--------|---------------|
| Generator loop | ch01, ch05, ch18 Bet 1 | [generator-loop-pattern](../../08_patterns/generator-loop-pattern.md) |
| Self-describing tools | ch01, ch06, ch18 Bet 3 | [self-describing-tools](../../08_patterns/self-describing-tools.md) |
| Two-tier state | ch03 | [two-tier-state](../../08_patterns/two-tier-state.md) |
| Sticky latch | ch03, ch04 | [sticky-latch-pattern](../../08_patterns/sticky-latch-pattern.md) |
| Withholding errors | ch05 | [withholding-errors](../../08_patterns/withholding-errors.md) |
| Fail-closed defaults | ch06, ch07 | [fail-closed-defaults](../../08_patterns/fail-closed-defaults.md) |
| Prompt cache as constraint | ch04, ch09, ch17, ch18 | [prompt-cache-as-constraint](../../08_patterns/prompt-cache-as-constraint.md) |

## Planned Patterns ⬜

| Pattern file (proposed) | Source (chapter · section) | Notes |
|-------------------------|---------------------------|-------|
| fast-path-dispatch | ch02 · Phase 0 | Narrow argv → dynamic import → exit |
| module-level-io-parallelism | ch02 · Phase 1 | Fire I/O at import evaluation |
| memoized-init | ch02 · init() | Idempotent bootstrap |
| trust-boundary-gating | ch02 · Trust Boundary | Pre/post trust env access |
| centralized-onchange-side-effects | ch03 · onChangeAppState | Diff-based sync |
| dynamic-boundary-prompt | ch04 · System Prompt | Static before, dynamic after |
| dangerous-uncached-section-naming | ch04 · 2^N problem | Loud escape hatch |
| streaming-idle-watchdog | ch04 · Streaming | 90s chunk timeout + fallback |
| immutable-loop-transitions | ch05 · State object | Full state reconstruct on continue |
| layered-context-compression | ch05 · Four layers | Order: budget → snip → micro → collapse → auto |
| circuit-breaker-retries | ch05 · Death spiral | Explicit limits on every retry path |
| input-dependent-concurrency | ch07 · Partition | isConcurrencySafe(input) |
| speculative-tool-execution | ch07 · Streaming executor | Start tools during stream |
| serial-only-context-modifiers | ch07 · Modifiers | Queue in parallel batches |
| attachment-not-description | ch08 · Dynamic prompt | Volatile lists out of tool schema |
| byte-identical-prefix | ch09 · Fork | Thread rendered prompt + exact tools |
| rendered-system-prompt-threading | ch09 · Layer 1 | No re-call getSystemPrompt() |
| use-exact-tools-passthrough | ch09 · Layer 2 | Parent tool array verbatim |
| fork-boilerplate-messages | ch09 · buildForkedMessages | Placeholder tool_results |
| task-output-file-ipc | ch10 · TaskStateBase | outputFile + outputOffset |
| sendmessage-queue-at-round-boundary | ch10 · pendingMessages | Preserve turn structure |
| file-memory-llm-recall | ch11 · Recall | Index + Sonnet selector |
| two-step-memory-write | ch11 · Write path | File + MEMORY.md pointer |
| two-phase-skill-loading | ch12 · Skills | Frontmatter at startup, body on invoke |
| hooks-snapshot-freeze | ch12 · Snapshot Security | Immutable hook config at setup |
| skills-hooks-integration | ch12 · Integration | Skill-declared session hooks |
| double-buffer-terminal-render | ch13 · Double-Buffer | Cell-level dirty tracking |
| pool-based-string-interning | ch13 · Pool Memory | Avoid per-frame GC |
| progressive-enhancement-input | ch14 · Multi-Protocol | Kitty → modifyOtherKeys → legacy |
| discrete-updates-input-batch | ch14 · Key pipeline | One reconcile per read() |
| raw-mode-reference-counting | ch14 · stdin Management | Shared raw mode |
| mcp-tool-wrapping | ch15 · Tool Wrapping | Normalize → truncate → annotate |
| oauth-discovery-chain | ch15 · OAuth | RFC 9728 → 8414 fallbacks |
| in-process-mcp-transport | ch15 · InProcessTransport | queueMicrotask delivery |
| asymmetric-read-write-remote | ch16 · Design philosophy | SSE/WS read, HTTP POST write |
| flush-gate-ordering | ch16 · FlushGate | Queue live writes during history flush |
| bridge-v2-epoch-registration | ch16 · Bridge v2 | /bridge call = registration |
| slot-reservation-8k-64k | ch17 · Slot Reservation | Default 8K, retry 64K |
| api-preconnect | ch17 · API Preconnect | HEAD during init |
| bitmap-search-prefilter | ch17 · Search | 26-bit letter bitmap |
| lazy-schema-deferral | ch17 · Deferred Imports | Zod on first use |
| hooks-over-plugins-isolation | ch18 · Bet 5 | Process isolation vs in-process |

## Anti-Pattern Pairing

Each planned anti-pattern in `09_antipatterns/` should link to its fix pattern:

| Anti-pattern | Fix pattern |
|--------------|-------------|
| infinite-retry-loops | circuit-breaker-retries |
| central-orchestrator-god-object | self-describing-tools |
| cache-busting-sections | prompt-cache-as-constraint |
| scattered-permission-sync | centralized-onchange-side-effects |
| memory-as-crutch | file-memory-llm-recall + taxonomy |
| cache-divergence-recompute (⬜) | byte-identical-prefix |
| object-per-cell-gc (⬜) | pool-based-string-interning |
| post-start-hook-tampering (⬜) | hooks-snapshot-freeze |

## Up

- [Patterns index](index.md)
- [Master extraction plan](../extraction-plan.md)
