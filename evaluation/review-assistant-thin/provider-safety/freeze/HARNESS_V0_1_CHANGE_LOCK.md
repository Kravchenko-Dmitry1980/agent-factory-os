# Harness v0.1 Change Lock — Provider Safety Harness

**Version:** v0.1  
**Status:** FROZEN  
**Effective:** 2026-05-26

---

## After v0.1 freeze, any change requires

1. **Change proposal** — written scope and rationale
2. **Impact analysis** — effect on Review Assistant v0.3 and baseline scripts
3. **Data safety review** — no real client/project/medical data
4. **Secret safety review** — no API keys, `.env`, or credentials
5. **Evaluation run** — all six validation scripts PASS
6. **Trace comparison** — if agent or trace format affected
7. **Rollback plan** — see [HARNESS_V0_1_ROLLBACK_RECORD.md](HARNESS_V0_1_ROLLBACK_RECORD.md)
8. **Explicit approval** — governance review with PASS / PASS_WITH_NOTES / FAIL

---

## Forbidden without new phase

| Change | Policy |
|--------|--------|
| New case groups (H, I, …) | Requires v0.2 proposal |
| Live provider calls in harness | Phase 3.5+ live harness only |
| Benchmark scores | Forbidden |
| Model rankings / leaderboard | Forbidden |
| pytest migration | Separate phase |
| CI integration | Separate phase |
| Attack corpus import | Red-team platform — forbidden |
| Real private data | Forbidden |
| Real secrets | Forbidden |
| Provider comparison framework | Forbidden |
| Red-team platform expansion | Forbidden |
| Modifying `minimal_demo.py` for harness | Agent behavior lock |

---

## Allowed without full v0.2 (documentation only)

| Change | Condition |
|--------|-----------|
| Typo fixes in freeze docs | No behavior change |
| Navigation links in README | Status/navigation only |
| Governance cross-references | Index updates only |

---

## Version bump guidance

| Change type | Suggested version |
|-------------|-------------------|
| Doc-only, no script change | v0.1 (unchanged) |
| New cases or classifier logic | v0.2+ |
| Live provider integration | Separate harness (e.g. live-harness-v0.1) |
| pytest/CI wrapper | Separate evaluation phase |

---

## Related

- Review Assistant change lock: [V0_3_CHANGE_LOCK.md](../../../../prototypes-derived/review-assistant-thin/freeze/V0_3_CHANGE_LOCK.md)
- Phase 3.4 plan preconditions: [PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md](../../../../governance/phase-3-4-plan/PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md)
