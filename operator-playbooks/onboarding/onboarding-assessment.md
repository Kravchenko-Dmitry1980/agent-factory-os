# Onboarding Assessment

Self-check or mentor quiz. No automated grading.

---

## Questions

### 1. What is fail-closed?

<details>
<summary>Answer</summary>
When uncertain or a gate fails, the system **denies** action rather than proceeding by default.
</details>

### 2. Why is critic not truth?

<details>
<summary>Answer</summary>
Critic gives **advisory** quality feedback; it can miss facts. Human or verifier must decide. Example: critic pass + human deny in failed-review trace.
</details>

### 3. Why do we need human approval?

<details>
<summary>Answer</summary>
External/high-risk actions need explicit permission and audit. Missing approval must not imply consent.
</details>

### 4. What is a trace?

<details>
<summary>Answer</summary>
Ordered log of events (task_started, approval_requested, etc.) showing **what happened and why**. See `observability/examples/`.
</details>

### 5. What is rollback?

<details>
<summary>Answer</summary>
Revert to last known-good state when a change breaks gates or behavior — before stacking more fixes.
</details>

### 6. What is platform drift?

<details>
<summary>Answer</summary>
Educational demos accrete into an accidental framework/platform, hiding governance and coupling.
</details>

### 7. Why should we not create a framework too early?

<details>
<summary>Answer</summary>
Frameworks obscure which gates run, encourage shared shortcuts, and teach APIs instead of governance invariants.
</details>

---

## Practical check

Run and explain output:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

Pass criteria: explains why Published is False and what bypass means.

---

## Pass threshold (mentor discretion)

- Intern: 6/7 written + practical check
- Developer: all + can run smoke checks
- Lead: all conceptual + can explain repo to stakeholder
