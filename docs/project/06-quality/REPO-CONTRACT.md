------------------------------------------------------------------------

title: Repo Contract
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
------------------

# Repo Contract

## Purpose

The repo contract defines structural invariants for Monorepo One.

A repository invariant is a rule that should remain true unless deliberately changed by an accepted decision.

## Current Contract Scope

This first repo contract covers root-level structure only.

Future versions will add checks for:

* package metadata;
* workspace membership;
* TypeScript project references;
* ADR frontmatter;
* documentation frontmatter;
* CI workflows;
* security configuration;
* ownership files;
* generated contract validation.

## Required Root Directories

The following directories must exist:

```text
.github
.artifacts
apps
assets
bin
config
contracts
data
db
docs
governance
infra
ops
packages
patches
security
services
templates
tools
```

## Required Root Documentation

Each tracked root directory must include a `README.md` explaining its role.

Required README files:

```text
.github/README.md
.artifacts/README.md
apps/README.md
assets/README.md
bin/README.md
config/README.md
contracts/README.md
data/README.md
db/README.md
docs/README.md
governance/README.md
infra/README.md
ops/README.md
packages/README.md
patches/README.md
security/README.md
services/README.md
templates/README.md
tools/README.md
```

## Required Contract Files

```text
docs/project/00-foundation/REPOSITORY-STRUCTURE.md
docs/project/06-quality/REPO-CONTRACT.md
docs/adr/ADR-0005-establish-root-repository-structure.md
tools/scripts/verify-repo-structure.sh
```

## Verification

Run:

```bash
bash tools/scripts/verify-repo-structure.sh
```

Expected result:

```text
Repository structure verification passed
```

## Change Rule

If this contract changes, update:

* this file;
* `docs/project/00-foundation/REPOSITORY-STRUCTURE.md`;
* `tools/scripts/verify-repo-structure.sh`;
* ADR index or a new ADR if the change is material.
