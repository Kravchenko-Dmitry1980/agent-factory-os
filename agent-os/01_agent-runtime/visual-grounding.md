# Visual Grounding

## Definition

**Visual grounding** is the architectural step that binds natural-language intent to spatial UI targets — via perception pipelines, native VLM coordinates, or marked overlay references.

## Why It Matters

GUI actions require coordinates or element references. Ungrounded actions produce wrong-pixel taps and silent task failure.

## Architecture Implications

Three grounding strategies (choose by model capability and UI density):

| Strategy | Mechanism | Typical failure |
|----------|-----------|-----------------|
| List-grounded | Detected elements → LLM selects target | List errors propagate |
| Model-grounded | VLM returns coordinates directly | Coordinate space mismatch |
| Mark-grounded (SOM) | Numbered overlays → mark ID → coord map | Overlay obscures UI |

Cross-cutting requirements:

- **Coordinate space normalization** — declare space in action schema (normalized vs absolute pixels).
- **Multi-channel fallback** — accessibility tree when vision insufficient (conceptual; no OS-specific API).
- Log grounding confidence when model provides it.

## Production Implications

- Never treat OCR/element lists as ground truth without verification.
- Regression tests on resolution and DPI variants for normalized coords.
- Grounding quality metrics independent of full task success (benchmark spot tests).

## Risks

- Legacy OCR-list pipelines promoted as default despite known inaccuracy.
- Mixed coordinate spaces across loop turns.

## Related Concepts

- [[gui-agent-loop]]
- [[visual-verification]]
- [[error-recovery-ladder]]

## Related Anti-patterns

- [[brittle-gui-automation]]
- [[unverified-gui-clicks]]

## Related Patterns

- [[fail-closed-agent-loop]]

## Upstream Sources

- `experiments/mobile-agent-review/extracted-patterns/visual-grounding-pattern.md`
- `experiments/mobile-agent-review/perception/visual-grounding.md`

## Governance References

- `PROMOTION_REVIEW.md` §4.2
- `governance/PROMOTION_LOG.md`

## Semantic Cluster

gui-modality

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Foundational GUI perception concept; stripped of GroundingDINO/OCR pipeline implementation.
governance_reference: PROMOTION_REVIEW.md §4.2, governance/PROMOTION_STRATEGY.md GUI concepts
```
