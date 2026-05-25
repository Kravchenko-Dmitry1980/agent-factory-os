# Architecture Overview

## Назначение

Brain OS — Control Plane между Product Layer и cognitive planes.

## Stack Mapping

| Plane | Маркeting name | Роль |
|-------|----------------|------|
| Memory | CAIM | profile/episodic/semantic/reflection/scenario |
| Cognition | MirrorMind | reasoning orchestration |
| Compute | System-1.5 | speed/cost optimization |
| Policy | VGP2 | strategy/decomposition |
| Product | Sandbox / Recruiter / Test Machine / BS | UI + domain scenarios |

## Pipeline (happy path)

Product → brain-api → classify → route → retrieve memory → select policy → run reasoning → evaluate → trace → writeback

## Maturity

production-relevant (как архитектурная рамка); implementation speculative до OpenAPI + replay.

## Provenance

`source/Brain OS.docx` A.§3; `source/Brain OS MD.docx` §2
