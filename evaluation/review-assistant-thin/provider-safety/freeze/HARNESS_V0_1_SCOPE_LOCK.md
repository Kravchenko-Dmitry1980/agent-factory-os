# Harness v0.1 Scope Lock — Provider Safety Harness

**Version:** v0.1  
**Status:** FROZEN  
**Effective:** 2026-05-26

---

## In scope (frozen)

| Item | Detail |
|------|--------|
| Fixed 16 synthetic cases | Groups A–G; see [HARNESS_V0_1_CASE_MATRIX.md](HARNESS_V0_1_CASE_MATRIX.md) |
| Local deterministic safety classification | v0.3-aligned rules in harness script |
| No network | Default run makes no HTTP/API calls |
| No provider calls | No LM Studio, OpenAI, Anthropic, or other providers |
| No secrets | Synthetic strings only; fake placeholder in F02 |
| No real data | No client/project/medical/repo content |
| PASS/FAIL only | No scores, rankings, or leaderboard |
| Review Assistant v0.3 assumptions | Parse → safety → verification → approval → deliver/block |

---

## Out of scope (frozen exclusion)

| Item | Reason |
|------|--------|
| Model benchmark | Not a quality test |
| Leaderboard | No model ranking |
| Provider comparison | No A/B provider scoring |
| Live prompt-injection testing | Requires separate opt-in phase |
| Production QA | Local harness only |
| pytest / CI | Manual script only |
| Red-team platform | No exploit corpus |
| Second agent / template | Single harness scope |
| RAG / MCP | Not in scope |
| RU provider testing | GigaChat, YandexGPT — separate phase |
| Cloud provider testing | OpenAI, Anthropic — separate phase |
| Operator Console | Backlog item |

---

## Strictly forbidden without new phase

| Action | Policy |
|--------|--------|
| Adding provider calls to harness | Requires Phase 3.5+ live harness proposal |
| Adding real prompts against live model | Opt-in phase only |
| Adding attack corpus | Red-team platform — forbidden |
| Adding scoring / ranking | Benchmark — forbidden |
| Adding CI integration | Separate governance decision |
| Adding pytest migration | Separate governance decision |
| Adding provider framework | Forbidden by project doctrine |
| Modifying `minimal_demo.py` for harness cases | Agent behavior lock |

---

## Scope boundary diagram

```text
┌─────────────────────────────────────────┐
│  Provider Safety Harness v0.1 (FROZEN)  │
│  • 16 synthetic cases                   │
│  • local classification                 │
│  • PASS/FAIL                            │
└─────────────────────────────────────────┘
          │ assumes rules aligned with
          ▼
┌─────────────────────────────────────────┐
│  Review Assistant Thin v0.3 (FROZEN)    │
│  • minimal_demo.py unchanged            │
│  • mock default + opt-in real provider  │
└─────────────────────────────────────────┘
```

---

## Related governance

- [phase-3-4-plan/RECOMMENDED_HARNESS_SCOPE.md](../../../../governance/phase-3-4-plan/RECOMMENDED_HARNESS_SCOPE.md)
- [phase-3-4-plan/NO_BENCHMARK_POLICY.md](../../../../governance/phase-3-4-plan/NO_BENCHMARK_POLICY.md)
- [phase-3-4-plan/NO_RED_TEAM_PLATFORM_POLICY.md](../../../../governance/phase-3-4-plan/NO_RED_TEAM_PLATFORM_POLICY.md)
