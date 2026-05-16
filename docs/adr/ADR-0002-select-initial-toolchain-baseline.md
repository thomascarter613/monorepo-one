
title: ADR-0002 - Select Initial Toolchain Baseline
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
-------------------

# ADR-0002: Select Initial Toolchain Baseline

## Status

Accepted

## Context

The monorepo needs an initial toolchain before application code is introduced.

The toolchain should support:

* fast local development
* strict TypeScript
* formatting
* linting
* task orchestration
* monorepo project awareness
* Git hook verification
* future CI compatibility

The repository is still in foundation mode, so the selected tools should not force premature application architecture.

## Decision

We will establish the initial toolchain baseline with:

* Bun
* TypeScript
* Biome
* Turborepo
* moon
* Lefthook

## Rationale

Bun provides a fast package manager/runtime and native workspace support.

TypeScript provides static type safety.

Biome provides a unified formatter/linter for supported web project files.

Turborepo provides cache-aware task orchestration for JavaScript and TypeScript projects.

moon provides stronger monorepo project graph, boundary, and long-term repository governance capabilities.

Lefthook provides fast, portable Git hook management.

## Consequences

This introduces several tools before application code exists.

That cost is acceptable because each tool has a narrow responsibility and supports the repo's long-term governance-grade goals.

The risk is tool overlap, especially between Turbo and moon.

That risk is mitigated by ADR-0003, which defines their responsibility split.

## Alternatives Considered

### Bun only

Rejected because package management alone does not provide formatting, linting, task orchestration, project graph governance, or Git hook management.

### pnpm instead of Bun

Rejected for this repository because Bun is the preferred package manager/runtime baseline for this clean-slate monorepo.

### ESLint plus Prettier instead of Biome

Deferred. Biome is simpler for the initial baseline. ESLint may be added later only if framework-specific or rule-specific needs exceed Biome's coverage.

### Turbo only

Rejected because Turbo is excellent for task orchestration but does not fully replace moon's project graph and boundary-governance model.

### moon only

Rejected for the initial JavaScript/TypeScript workflow because Turbo remains a strong and common task orchestration layer for JS/TS monorepos.

## Verification

This decision is verified by:

```bash
bun install
bun run hooks:install
bun run verify
```
