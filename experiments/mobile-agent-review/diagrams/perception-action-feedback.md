# Perception → Action → Feedback — Diagram

```mermaid
sequenceDiagram
    participant E as Environment
    participant P as Perception
    participant O as Orchestrator
    participant M as Model VLM/LLM
    participant D as Driver ADB/pyautogui
    participant V as Verifier

    E->>P: UI state
    P->>O: screenshot + optional element list
    O->>M: context prompt / InfoPool
    M->>O: action JSON or DSL
    O->>D: parsed action
    D->>E: motor event tap/type/swipe
    E->>P: new screenshot
    P->>V: before/after pair
    V->>M: reflect prompt optional
    M->>V: outcome A/B/C
    V->>O: update error_flag / progress
    O->>M: next step or replan
```

## Data Artifacts per Step

| Stage | Artifact |
|-------|----------|
| Perception | PNG screenshot, clickable_infos[] |
| Reason | Thought, Plan, Action JSON |
| Execute | ADB shell commands |
| Feedback | action_outcomes[], new PNG |
| Memory | important_notes, memory string |

## v3.5 Simplified Path

Verifier may be implicit — model observes new screenshot in next turn without separate Reflector class call.

## Extension: Pre-Op Critic

```mermaid
sequenceDiagram
    participant C as GUI-Critic
    participant O as Orchestrator
    participant M as Model

    O->>M: proposed action
    M->>O: action draft
    O->>C: pre-check screenshot + draft
    C->>O: critique / revise suggestion
    O->>M: execute or revise
```

Not implemented in production loops — research direction only.
