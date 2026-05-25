# Why AI Needs Review

AI systems generate **plausible** text, code, and decisions. Plausible ≠ correct.

---

## The problem

- Models fill gaps with confident-sounding guesses
- Errors don't look like errors — they look like normal output
- Speed encourages skipping verification

---

## What we do instead

1. **Verification gate** — check structure, sources, or tests before trust
2. **Human approval** — for external or high-risk actions
3. **Trace** — record why a decision happened
4. **Fail-closed** — when unsure, stop

---

## Operator rule

Never ship AI output to users, files, or APIs because "it read well."

Run review-loop demo:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
```

Doctrine: `agent-os/doctrine/verification-first.md`
