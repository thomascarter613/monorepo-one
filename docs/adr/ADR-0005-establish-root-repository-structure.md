----------------------------------------------------------------------------------------

title: ADR-0005 - Establish Root Repository Structure
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
------------------

# ADR-0005: Establish Root Repository Structure

## Status

Accepted

## Context

Monorepo One needs a clear root-level structure before deeper implementation begins.

Without an explicit root contract, the repository is likely to accumulate ambiguous folders, duplicated responsibilities, tool sprawl, and architectural drift.

The repository is intended to support serious, production-grade work across applications, services, packages, infrastructure, contracts, documentation, operations, governance, security, and AI-assisted development.

## Decision

We will establish a canonical root-level directory contract.

The accepted root directories are:

```text
.github/
.artifacts/
apps/
assets/
bin/
config/
contracts/
data/
db/
docs/
governance/
infra/
ops/
packages/
patches/
security/
services/
templates/
tools/
```

Each tracked root directory must include a `README.md` explaining its role.

A verification script will enforce the existence of required root directories and contract files.

## Rationale

This structure separates major concerns:

* deployable applications;
* backend services;
* reusable packages;
* contracts;
* documentation;
* infrastructure;
* operations;
* governance;
* security;
* database assets;
* tools and automation;
* generated artifacts.

The goal is not to fill every directory immediately.

The goal is to establish explicit boundaries before implementation pressure creates accidental structure.

## Consequences

This adds several empty or nearly empty directories early.

That is acceptable because each directory has a documented responsibility and future role.

The risk is perceived over-structure.

That risk is mitigated by keeping each directory documented, empty until needed, and verified by a small repo-contract script.

## Alternatives Considered

### Minimal structure only

Rejected because this monorepo is intentionally governance-grade and expected to evolve across multiple apps, services, packages, contracts, infrastructure, and operational concerns.

### Delay root structure until code exists

Rejected because root-level structure decisions become harder to change once code, tooling, and CI depend on accidental paths.

### Put all planning under docs only

Rejected because docs alone do not provide clear future boundaries for code, infrastructure, data, security, operations, and automation.

## Verification

This ADR is verified by:

```bash
bash tools/scripts/verify-repo-structure.sh
```

Expected result:

```text
Repository structure verification passed
```

## Follow-up Work

* Add GitHub issue and pull request templates.
* Add CI skeleton.
* Add repo-contract tests beyond shell checks.
* Add root ownership and CODEOWNERS.
* Add directory-specific standards as each area becomes active.
