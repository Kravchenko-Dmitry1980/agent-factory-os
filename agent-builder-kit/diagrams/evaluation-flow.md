# Evaluation Flow

```mermaid
flowchart TD
  T[template draft] --> SC[define scenarios]
  SC --> ET[expected traces]
  ET --> PC[pass/fail criteria]
  PC --> TAC[template-acceptance-checklist]
  TAC --> SRC[safety-regression if change]
  SRC --> TRC[trace-review-checklist]
  TRC --> HRC[human-review-checklist]
  HRC --> P3[phase-3-template-review-checklist]
  P3 -->|pass| ACC[accepted]
  P3 -->|fail| T
  ACC --> FRZ[frozen]
```

## Repository links

- Scenarios: `evaluation/scenarios/`
- Quality gates: `evaluation/quality-gates/`
- Kit checklists: [evaluation-checklists/](../evaluation-checklists/README.md)

No benchmark metrics in v0.1.
