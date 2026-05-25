# How to Explain Agents Simply

Use this script:

> An **agent** is a recipe, not a person.  
> Step 1: get task.  
> Step 2: maybe call tools or model.  
> Step 3: **checks** — did output pass rules?  
> Step 4: maybe **human says yes**.  
> Step 5: only then — action.  
> If any check fails → **stop** (fail-closed).

## Analogy

Agent = kitchen with health inspector (verification) and manager sign-off (approval) before serving food (external action).

## Avoid

- Robot with feelings
- "Thinks for itself"
- Swarm of specialists without org chart

## Demo anchor: review-loop-agent — point at audit line by line.
