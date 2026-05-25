# Training Curriculum (Phase 2.7)

**Status:** Educational methodology — not code, not Agent Factory, not production platform.

## Languages

- English version: current curriculum root
- Russian version: [ru/](ru/)

---

## What This Curriculum Teaches

How to design and operate **safe AI workflows**: verification, human approval, bounded memory, fail-closed execution, readable traces, local evaluation, and safe change — using this repository as the textbook and laboratory.

---

## Who It Is For

| Audience | Track |
|----------|-------|
| Complete beginner | [role-based-tracks/track-intern.md](role-based-tracks/track-intern.md) |
| AI developer | [role-based-tracks/track-ai-developer.md](role-based-tracks/track-ai-developer.md) |
| Cursor operator | [role-based-tracks/track-cursor-operator.md](role-based-tracks/track-cursor-operator.md) |
| Project lead | [role-based-tracks/track-project-lead.md](role-based-tracks/track-project-lead.md) |
| AI architect | [role-based-tracks/track-ai-architect.md](role-based-tracks/track-ai-architect.md) |

---

## What the Student Will Learn

- What an AI agent **actually is** (workflow + tools + gates — not magic)
- Why AI systems fail silently
- How to verify before trusting output
- How to use human approval correctly
- How to read traces and detect bad behavior
- How to run local evaluation checks
- How to change systems without breaking gates
- How to avoid platform drift
- When the team is ready for Phase 3 (Agent Builder Kit)

---

## What the Student Will NOT Learn Yet

- Model training or fine-tuning
- Building autonomous swarms without gates
- Production deployment at scale
- RAG / vector pipelines
- AGI or "replace the human" narratives
- Digital twin factory (Phase 3+)
- Agent Factory implementation (Phase 3 — criteria first)

---

## Why We Start Small

Large platforms hide mistakes. Small demos (~200 lines) show **exactly which gate ran**. You learn governance by seeing it, not by reading hype.

---

## Why We Avoid Hype

Hype skips verification. This curriculum teaches:

- **Critic ≠ truth**
- **LLM output ≠ truth**
- **"It runs" ≠ safe**

Safe AI workflow matters because plausible wrong output is the default failure mode — not crashes.

---

## This Curriculum Is NOT

- A course about AGI
- A course about building autonomous swarms
- A course about replacing humans
- A course about production platforms
- A course about model training

---

## This Curriculum IS

- A course about **safe AI workflow design**
- A course about **AI-agent architecture basics**
- A course about **verification**
- A course about **governance**
- A course about **safe system evolution**

---

## How to Navigate

| Start here | Then |
|------------|------|
| [course-map.md](course-map.md) | Full ladder Level 0–10 |
| [student-guides/student-start-here.md](student-guides/student-start-here.md) | Student entry |
| [modules/module-00-orientation.md](modules/module-00-orientation.md) | First module |
| [../operator-playbooks/start-here/first-30-minutes.md](../operator-playbooks/start-here/first-30-minutes.md) | Hands-on 30 min |

Governance review: [../governance/PHASE_2_7_CURRICULUM_REVIEW.md](../governance/PHASE_2_7_CURRICULUM_REVIEW.md)

---

## Relation to Other Phases

```
Phase 2.6  operator-playbooks  → how to operate day-to-day
Phase 2.7  curriculum          → how to teach and learn systematically
Phase 3    Agent Builder Kit   → only after phase-3-entry-criteria met
```

Entry criteria: [methodology/phase-3-entry-criteria.md](methodology/phase-3-entry-criteria.md)
