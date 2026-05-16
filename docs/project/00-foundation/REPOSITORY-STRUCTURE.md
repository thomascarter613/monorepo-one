---
title: Repository Structure
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
---

# Repository Structure

## Purpose

This document defines the canonical root-level structure for Monorepo One.

The goal is to make repository boundaries explicit before applications, services, packages, infrastructure, contracts, or operational systems are implemented.

## Canonical Root Directories

| Directory | Responsibility |
| --- | --- |
| `.github/` | GitHub-native repository configuration and automation |
| `.artifacts/` | Local/generated artifacts and debug outputs, mostly ignored |
| `apps/` | User-facing deployable applications |
| `assets/` | Shared versioned non-code assets |
| `bin/` | Thin executable wrappers and command entry points |
| `config/` | Shared repository-level configuration |
| `contracts/` | API schemas, event contracts, and integration contracts |
| `data/` | Versioned safe seed/sample/test data |
| `db/` | Database schemas, migrations, seeds, and DB tooling |
| `docs/` | Planning, architecture, ADRs, requirements, AI handoff, and documentation |
| `governance/` | Governance policies, standards, and process controls |
| `infra/` | Infrastructure-as-code and platform/deployment definitions |
| `ops/` | Runbooks, operational procedures, release operations, and incident support |
| `packages/` | Reusable internal libraries and shared packages |
| `patches/` | Dependency patches, migration patches, and patch documentation |
| `security/` | Security policies, threat models, and security evidence |
| `services/` | Backend services, APIs, workers, daemons, and scheduled processes |
| `templates/` | Reusable templates for docs, issues, PRs, and scaffolding |
| `tools/` | Repository automation, scripts, generators, and validators |

## Boundary Rules

### Applications

Applications live in `apps/`.

Applications are deployable products or user-facing surfaces.

Applications may depend on `packages/` and `contracts/`.

### Services

Services live in `services/`.

Services are backend processes, APIs, workers, daemons, gateways, or scheduled jobs.

Services may depend on `packages/`, `contracts/`, `db/`, and relevant `config/`.

### Packages

Packages live in `packages/`.

Packages contain reusable code.

Packages should not depend on applications.

### Contracts

Contracts live in `contracts/`.

Contracts define cross-boundary agreements and should be validated when possible.

### Infrastructure

Infrastructure lives in `infra/`.

Infrastructure should not be mixed with application implementation.

### Operations

Operations live in `ops/`.

Operational documentation should be executable, practical, and tied to real systems.

### Governance

Governance lives in `governance/`.

Governance files define standards, review rules, process rules, and policy.

### Tools

Tools live in `tools/`.

Tools should be safe, explicit, and useful locally and in CI.

## Generated Artifacts

Generated/transient artifacts belong in `.artifacts/` unless a specific generated result is intentionally versioned elsewhere.

The `.artifacts/` directory is mostly ignored. Its `README.md` is tracked to document the convention.

## Verification

The root structure is verified with:

```bash
bash tools/scripts/verify-repo-structure.sh
```

## Change Control

Changes to the root directory contract require an ADR update or a new ADR.

Do not add new root-level directories casually.

Each new root-level directory must have:

* a clear owner/purpose;
* a documented boundary;
* a reason it cannot live under an existing root directory;
* verification updates.
