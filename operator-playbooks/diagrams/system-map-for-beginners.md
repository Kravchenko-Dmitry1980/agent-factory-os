# System Map for Beginners

```mermaid
flowchart TB
    subgraph learn [Learn — read]
        AO[agent-os/doctrine]
        GOV[governance]
    end
    subgraph try [Try — run locally]
        PT[prototypes]
        INT[prototypes/integrations]
        IR[integrations-real mock]
    end
    subgraph understand [Understand — observe]
        OBS[observability/examples]
        EVA[evaluation/scripts]
    end
    subgraph change [Change — carefully]
        EVO[evolution/change-proposals]
        OP[operator-playbooks]
    end
    AO --> PT
    GOV --> PT
    PT --> INT
    INT --> IR
    PT --> OBS
    OBS --> EVA
    EVO --> OP
    OP --> PT
```

**Start arrow:** `operator-playbooks/start-here/start-here.md`

**Do not start in:** `Books/` (source corpus), `experiments/` (research)

---

## One-line layer summary

| Folder | Beginner description |
|--------|---------------------|
| agent-os | What we believe about safe agents |
| prototypes | Tiny demos proving those beliefs |
| observability | Example logs of good/bad behavior |
| evaluation | Check demos still behave |
| evolution | How to change without breaking gates |
| operator-playbooks | How humans navigate all of this |
