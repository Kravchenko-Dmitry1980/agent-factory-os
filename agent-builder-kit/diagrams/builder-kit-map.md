# Builder Kit Map

```mermaid
flowchart TB
  subgraph entry [Entry]
    README[README.md]
    RU[RU_SUMMARY.md]
  end

  subgraph specs [Template Specs]
    ATS[agent-template-spec]
    WTS[workflow-template-spec]
    TBS[tool-boundary-spec]
    MBS[memory-boundary-spec]
    HAS[human-approval-spec]
    OTS[observability-trace-spec]
    ECS[evaluation-checklist-spec]
    CPS[change-proposal-spec]
    APS[anti-pattern-checklist-spec]
  end

  subgraph gates [Safety Gates]
    FC[fail-closed]
    VF[verification]
    HA[human-approval]
    MB[memory-boundary]
    TU[tool-use]
    ES[escalation]
    EV[evaluation]
    RB[rollback]
  end

  subgraph ref [Reference Template]
    RA[review-assistant-agent]
  end

  subgraph gov [Governance]
    BP[builder-kit-boundaries]
    NR[no-runtime-policy]
    NF[no-factory-yet-policy]
  end

  README --> specs
  RU --> specs
  specs --> gates
  gates --> RA
  specs --> RA
  gov --> README
```

## Reading order

1. README / RU_SUMMARY
2. template-specs/agent-template-spec
3. safety-gates/
4. templates/review-assistant-agent/
5. evaluation-checklists/
6. governance/ (kit policies)
