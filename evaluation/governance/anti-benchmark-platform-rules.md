# Anti-Benchmark-Platform Rules

Stop if evaluation starts looking like a model or agent benchmark platform.

---

## Forbidden Artifacts

- `leaderboard.json`, model scores, Elo ratings
- Synthetic benchmark datasets for agent comparison
- Automated "agent readiness score"
- Vector/RAG retrieval benchmarks
- Multi-model tournament runners
- Public eval API

---

## Forbidden Language

| Drift phrase | Replace with |
|--------------|--------------|
| "Model A beats Model B" | "Gate behavior unchanged" |
| "Benchmark suite" | "Scenario checklist" |
| "Eval platform" | "Local evaluation notes" |
| "Production QA ready" | "Local behavioral check" |
| "CI gate" | "Human quality gate" |

---

## Allowed Metrics (Minimal)

- PASS / FAIL / NOT_RUN on smoke demos
- Required event present in example trace
- Checklist items checked / unchecked

**Not allowed:** latency percentiles, token cost leaderboards, accuracy@k.

---

## If Benchmark Need Arises

Document in separate experiment — **not** in `evaluation/`. Phase 2.5 protects governance, not model shopping.

---

## Review Trigger

Any PR adding scoring tables across models → reject as scope drift.
