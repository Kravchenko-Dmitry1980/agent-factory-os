# Verification Gate

**Question:** Did verification still run before trust transfer (publish, write, execute)?

---

## Checks

- [ ] Critic uncertain → no auto publish
- [ ] Malformed LLM → reject
- [ ] GUI mismatch → block click
- [ ] Unverified memory → no writeback
- [ ] Unsupported promotion claim → reject

## Commands

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python prototypes/gui-verification-loop/minimal-demo.py --scenario mismatch
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario unsupported-claim
```

## Pass

- verification_failed or governance_rejection on fail paths
- verification before task_completed on pass paths

## Fail

- Skip verifier on "fast path"
- Critic pass = final approval
- LLM parse error → continue

## Note

Verification passes **structure**, not **truth**. LLM reminder must remain.
