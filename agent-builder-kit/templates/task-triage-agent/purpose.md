# Task Triage Agent — Purpose

**Status:** SPEC_DRAFT

---

## What Task Triage Agent does

Task Triage Agent helps convert vague incoming work into a structured decision:

```text
task text
  → task type
  → risk level
  → missing information
  → suggested next step
  → human approval requirement
```

It sits **upstream** of implementation, review, and delivery. It classifies and advises; it does not act.

---

## Core responsibilities

| Step | Action |
|------|--------|
| 1 | Read task description and optional context |
| 2 | Validate input for safety and clarity |
| 3 | Classify task type |
| 4 | Assess risk level |
| 5 | Detect missing information |
| 6 | Check execution and orchestrator boundaries |
| 7 | Propose advisory next step |
| 8 | Assess approval and escalation need |
| 9 | Return final triage decision and trace |

---

## Examples of valid use

| Use case | Example task | Expected outcome |
|----------|--------------|-------------------|
| Classify development task | "Add adapter to Review Assistant without breaking mock default" | task_type=implementation, risk=medium, approval_required=true |
| Classify research task | "Compare local LLM options for classification" | task_type=research, suggested_next_step=write comparison memo |
| Detect missing acceptance criteria | "Add feature X" (no criteria) | NEEDS_CLARIFICATION, missing_info includes acceptance criteria |
| Detect provider/security risk | "Enable cloud OpenAI by default in triage" | risk=high, ESCALATE, approval_required=true |
| Suggest planning before implementation | "Implement task triage thin demo" | suggested_next_step=create implementation plan first |
| Recommend escalation for unclear ownership | "Change frozen template" (no owner named) | escalation_required=true, ESCALATE |

---

## Example input

```text
Нужно добавить LLM adapter к Review Assistant, но не сломать mock default.
```

---

## Example output (advisory)

| Field | Example value |
|-------|---------------|
| task_type | implementation |
| priority_class | medium |
| risk_level | medium |
| missing_information | rollback plan, acceptance criteria |
| suggested_next_step | Create implementation plan; verify mock default preserved |
| approval_required | true — medium risk, touches provider boundary |
| escalation_required | false |
| final_triage_decision | TRIAGED |
| trace | See [expected-traces.md](expected-traces.md) |

---

## Value proposition

| Without triage | With triage (advisory) |
|----------------|------------------------|
| Human guesses task type and risk | Structured classification |
| Missing info discovered mid-work | Gaps surfaced early |
| Execution/orchestrator drift hidden | Boundaries enforced at intake |
| Approval need unclear | approval_required explicit |

---

## Relation to Review Assistant

| Dimension | Review Assistant | Task Triage |
|-----------|------------------|-------------|
| Primary input | Review/draft task | Any incoming work task |
| Primary output | Draft + delivery decision | Triage classification |
| Content generation | Yes (draft) | No — classification only |
| Execution | Blocked | Blocked (stronger emphasis) |
| Orchestration | Blocked | Blocked (stronger emphasis) |

Task Triage is complementary — it does not replace Review Assistant and does not auto-start it.
