# Exercise: Run First Demo

## Purpose

Prove you can run a governed workflow locally and read basic output.

## Time

15 minutes

## Steps

1. Open terminal in `C:\Dima\Projects\CURSOR\AGENT`
2. Run:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

3. Find: Task, Critic verdict, Human decision, Published, Audit section
4. Run bypass scenario:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

## Expected Result

Happy: Published True. Bypass: Published False.

## What To Observe

- Human decision on happy path
- Bypass blocked message or audit action

## Questions

1. Did critic verify facts or structure?
2. What changed between scenarios?

## Pass Criteria

Can narrate happy path in 4 steps; states bypass was blocked.

## Fail Criteria

Cannot run command; cannot find audit; thinks bypass published.

Module: [../modules/module-00-orientation.md](../modules/module-00-orientation.md)
