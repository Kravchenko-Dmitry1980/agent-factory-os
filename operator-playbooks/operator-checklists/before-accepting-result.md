# Before Accepting Result

Use when AI or demo produced an output you might trust.

- [ ] Trace shows **why** decision was made
- [ ] Critic pass ≠ final approval (if external action)
- [ ] Human approval present if required
- [ ] LLM output treated as untrusted input
- [ ] GUI/visual verification recorded if action was UI
- [ ] No side effect on deny/fail path
- [ ] OUTCOME matches expected (`evaluation/expected-outcomes/`)

**If plausible but unverified → HOLD, do not accept.**
