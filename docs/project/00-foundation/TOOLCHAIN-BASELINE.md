---
title: Toolchain Baseline
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
---

# Toolchain Baseline

## Purpose

This document records the initial root-level toolchain baseline for the monorepo.

The goal is to establish a small, coherent tooling foundation before application, service, package, infrastructure, or CI implementation begins.

## Selected Initial Tools

| Concern | Tool |
| --- | --- |
| Package manager and runtime | Bun |
| TypeScript compiler | TypeScript |
| Formatting and linting | Biome |
| JavaScript/TypeScript task orchestration | Turborepo |
| Monorepo project graph and boundary governance | moon |
| Git hook management | Lefthook |

## Responsibility Boundaries

### Bun

Bun is the package manager and JavaScript runtime baseline.

Bun owns:

- dependency installation
- lockfile generation
- workspace installation
- root package scripts

### TypeScript

TypeScript owns static type verification.

The root TypeScript configuration is intentionally strict.

### Biome

Biome owns formatting and linting for supported file types.

Biome is configured to ignore unknown file types so that Markdown-heavy documentation does not block the initial verification baseline.

### Turborepo

Turborepo owns JavaScript/TypeScript task orchestration and cache-aware task execution.

Turbo will become more useful after apps, services, and packages are added.

### moon

moon owns long-term monorepo structure, project graph awareness, task inheritance, and boundary governance.

Moon is introduced now but used conservatively until real projects exist.

### Lefthook

Lefthook owns local Git hook execution.

The initial pre-commit hook runs repository verification.

## Current Verification Command

```bash
bun run verify
```

## Current Limitations

This slice does not yet add:

* applications
* services
* packages
* CI workflows
* test framework
* root directory contract checker
* security scanning
* Docker or infrastructure tooling

Those belong in later slices.

## Acceptance Criteria

This slice is accepted when:

* dependencies install successfully
* `bun.lock` exists
* `bun run verify` passes
* Lefthook validates successfully
* the commit message hook accepts Conventional Commit messages
