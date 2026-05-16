
title: ADR-0003 - Define Turbo and Moon Responsibilities
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
-------------------

# ADR-0003: Define Turbo and Moon Responsibilities

## Status

Accepted

## Context

The monorepo will use both Turborepo and moon.

Using both tools without clear boundaries could create duplicated task definitions, confusing workflows, and architecture drift.

The repository needs an explicit responsibility split.

## Decision

Turbo will be used primarily for JavaScript/TypeScript task orchestration.

moon will be used primarily for monorepo project graph, workspace governance, task inheritance, and boundary constraints.

## Responsibility Split

### Turbo Owns

* common JS/TS task execution
* cache-aware task orchestration
* root task pipelines such as build, test, lint, typecheck, and dev
* integration with package scripts

### moon Owns

* workspace project discovery
* project identity and graph governance
* project layer metadata
* project relationship constraints
* future task inheritance across project classes
* long-term monorepo boundary enforcement

## Rule

Do not define the same behavior in both tools unless there is a documented reason.

If a task exists in both Turbo and moon, the documentation must explain which one is canonical for local development, CI, and project governance.

## Consequences

This gives us the benefits of both tools while reducing overlap.

It also creates a responsibility to keep their configurations aligned.

## Verification

This decision is initially verified by:

```bash
bun run verify:turbo
bun run verify:moon
```

Future verification should include a repo contract test that checks for task and project-boundary consistency.
