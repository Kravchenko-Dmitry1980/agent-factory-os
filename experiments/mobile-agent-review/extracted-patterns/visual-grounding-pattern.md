# Visual Grounding Pattern

---

## Pattern Statement

> Bind natural language intent to spatial UI targets through perception pipeline and/or native VLM grounding.

---

## Three Implementations in Repo

### 1. List-Grounded (v1/v2)

```
CV pipeline → [(coord, label), ...] → LLM selects coord or interprets with image
```

**When to use:** Small models, need interpretable candidates  
**Failure mode:** List errors propagate

### 2. Model-Grounded (v3/v3.5)

```
Screenshot → VLM → coordinates or element reference directly
```

**When to use:** Strong GUI-Owl / Qwen-VL  
**Failure mode:** Coordinate space mismatch

### 3. Mark-Grounded (SOM)

```
Screenshot → overlay numbered marks → model picks mark ID → map to coord
```

**When to use:** Dense UIs, web pages  
**Failure mode:** Overlay obscures UI

---

## Supporting Techniques

- `--coor_type qwen-vl` normalization
- `smart_resize` for aspect ratio constraints
- OSWorld Grounding agent for `element_description` strings
- Accessibility tree as non-visual grounding channel

---

## Benchmarks as Grounding Tests

ScreenSpot-v2, ScreenSpot-Pro, OSWorld-G — evaluate pattern quality independent of full task success.

---

## Reuse Recommendation

For Agent-OS GUI track:
1. Define **coord_space** in action schema
2. Support **multi-channel grounding** (VLM primary, a11y fallback)
3. Log grounding confidence if model provides it (GUI-Owl Thinking)
