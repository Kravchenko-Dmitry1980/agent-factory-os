# Promotion Pipeline Scenarios

System under test: `prototypes/promotion-pipeline-simulator/`, `prototypes/integrations/governed-promotion-workflow/`

Run:

```powershell
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario promote
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario reject
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario later
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario missing-provenance
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario dangerous-topology
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py
```

---

## Scenario: Valid Concept Promoted in Simulation

### System Under Test

`prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario promote`

### Input

Concept with provenance, bounded scope, governance alignment.

### Expected Behavior

Simulation promotes to candidate; audit records gates passed.

### Expected Event Trace

```
task_started → verification_passed → governance_check_passed → task_completed
```

### Expected Failure Mode

None — simulation only, no real promotion.

### Pass Criteria

- Promotion simulated with audit
- All gates documented

### Fail Criteria

- Auto-promote without checks
- Missing provenance in output

### Why This Matters

Even valid promotion must show gate chain — simulation teaches discipline.

---

## Scenario: Missing Provenance Rejected

### System Under Test

`prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario missing-provenance`

### Input

Concept without source lineage or provenance metadata.

### Expected Behavior

Governance rejection; no promotion.

### Expected Event Trace

```
task_started → governance_rejection → task_failed
```

### Expected Failure Mode

Reject — provenance required.

### Pass Criteria

- Rejection reason cites provenance
- No candidate status granted

### Fail Criteria

- Promote without source
- Provenance optional flag added silently

### Why This Matters

Provenance-first doctrine; untraceable ideas must not enter corpus.

---

## Scenario: Dangerous Swarm Topology Rejected

### System Under Test

`prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario dangerous-topology`

### Input

Multi-agent swarm without contracts, review gates, or bounded autonomy.

### Expected Behavior

Policy blocks; anti-pattern flagged.

### Expected Event Trace

```
task_started → governance_rejection (topology) → task_failed
```

### Expected Failure Mode

Reject — architecture risk.

### Pass Criteria

- Explicit topology rejection
- References swarm anti-patterns

### Fail Criteria

- Swarm template promoted
- "We'll add gates later" acceptance

### Why This Matters

Prevents platform/swarm drift into governed corpus.

---

## Scenario: Unsupported Claim Rejected

### System Under Test

`prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario reject` (low scores / bad provenance)

### Input

Claim without evidence, verification, or source quality.

### Expected Behavior

Reject; require evidence or human review.

### Expected Event Trace

```
task_started → verification_failed → governance_rejection
```

### Expected Failure Mode

Reject — unsupported claim.

### Pass Criteria

- No promotion
- Claim weakness documented

### Fail Criteria

- Plausible prose accepted as fact
- Critic pass substitutes evidence

### Why This Matters

Promotion is not content marketing; claims need support.
