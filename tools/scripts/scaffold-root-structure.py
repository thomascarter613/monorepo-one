from __future__ import annotations

from pathlib import Path
from textwrap import dedent

TODAY = "2026-05-16"
PROJECT = "monorepo-one"

ROOT_DIRS: dict[str, dict[str, str]] = {
    ".github": {
        "title": "GitHub Configuration",
        "purpose": "GitHub-native repository configuration such as workflows, issue templates, pull request templates, dependabot configuration, code scanning configuration, and repository automation.",
        "rules": "Do not place application source code here. Keep GitHub automation explicit, minimal, and reviewable.",
    },
    ".artifacts": {
        "title": "Local and Generated Artifacts",
        "purpose": "Local/generated artifacts, debug output, temporary reports, verification logs, and generated evidence that should normally not be committed.",
        "rules": "Only README.md is tracked by default. Generated contents should remain ignored unless a specific artifact is intentionally promoted into a controlled record.",
    },
    "apps": {
        "title": "Applications",
        "purpose": "User-facing deployable applications, such as web apps, mobile apps, desktop apps, documentation sites, admin consoles, and portals.",
        "rules": "Apps may depend on packages and contracts. Apps should not contain reusable domain libraries that belong in packages.",
    },
    "assets": {
        "title": "Assets",
        "purpose": "Shared non-code assets such as brand assets, design exports, diagrams, icons, images, and static media that are intentionally versioned.",
        "rules": "Large binary assets should be added deliberately. Generated/transient assets should go under .artifacts or an ignored build output directory.",
    },
    "bin": {
        "title": "Executable Entry Points",
        "purpose": "Small repository-level executable wrappers and command entry points intended to be run directly by developers or automation.",
        "rules": "Prefer thin wrappers here. Substantial implementation should live in tools, packages, or services.",
    },
    "config": {
        "title": "Shared Configuration",
        "purpose": "Shared repository configuration that does not naturally belong to a specific package, app, service, or tool.",
        "rules": "Configuration here should be documented and should avoid secrets. Environment-specific secrets must not be committed.",
    },
    "contracts": {
        "title": "Contracts",
        "purpose": "API contracts, schemas, interface definitions, event contracts, protocol definitions, and other cross-boundary agreements.",
        "rules": "Contracts should be versioned, validated, and treated as source-of-truth artifacts for integration boundaries.",
    },
    "data": {
        "title": "Data",
        "purpose": "Versioned seed data, fixtures, sample datasets, controlled test data, and data documentation.",
        "rules": "Do not commit sensitive data, production data, secrets, or private personal information.",
    },
    "db": {
        "title": "Database",
        "purpose": "Database schemas, migrations, seeds, database tooling, and database-specific documentation.",
        "rules": "Database changes must include migration and rollback considerations once real systems exist.",
    },
    "docs": {
        "title": "Documentation",
        "purpose": "Project documentation, planning, architecture, ADRs, requirements, AI handoff, and implementation guidance.",
        "rules": "Docs are part of the product and must remain aligned with implementation.",
    },
    "governance": {
        "title": "Governance",
        "purpose": "Repository governance policies, engineering standards, review policies, quality policies, and decision/process controls.",
        "rules": "Governance documents should be enforceable where practical and referenced by ADRs or repo-contract checks.",
    },
    "infra": {
        "title": "Infrastructure",
        "purpose": "Infrastructure-as-code, deployment manifests, environment definitions, container orchestration, cloud resources, and platform configuration.",
        "rules": "Infrastructure changes require security, rollback, environment, and operational considerations.",
    },
    "ops": {
        "title": "Operations",
        "purpose": "Operational runbooks, incident response procedures, release operations, backup/restore procedures, and production support materials.",
        "rules": "Operations documentation should be practical, executable, and tied to real systems as they are added.",
    },
    "packages": {
        "title": "Packages",
        "purpose": "Reusable libraries, shared domain modules, UI libraries, SDKs, clients, utilities, and internal packages.",
        "rules": "Packages should have clear ownership, public/internal API boundaries, tests, and dependency discipline.",
    },
    "patches": {
        "title": "Patches",
        "purpose": "Patch files, dependency patches, migration patches, temporary compatibility patches, and patch documentation.",
        "rules": "Patches must be documented with rationale, lifecycle, and removal criteria.",
    },
    "security": {
        "title": "Security",
        "purpose": "Security policies, threat models, security tooling configuration, vulnerability handling docs, and security evidence.",
        "rules": "Do not store secrets here. Security documentation should distinguish policy, implementation, and evidence.",
    },
    "services": {
        "title": "Services",
        "purpose": "Backend services, APIs, workers, daemons, gateways, scheduled jobs, and independently deployable service processes.",
        "rules": "Services may depend on packages and contracts. Services should expose clear operational and API boundaries.",
    },
    "templates": {
        "title": "Templates",
        "purpose": "Reusable templates for docs, ADRs, work packets, issues, pull requests, generated files, and future scaffolding.",
        "rules": "Templates should be complete enough to prevent drift and light enough to stay maintainable.",
    },
    "tools": {
        "title": "Tools",
        "purpose": "Repository automation, scripts, generators, validators, verification tooling, and developer-experience utilities.",
        "rules": "Tools should be safe by default, documented, and usable locally and in CI where practical.",
    },
}

def frontmatter(title: str) -> str:
    return dedent(f"""\
    ---
    title: {title}
    status: accepted
    version: 0.1.0
    created: {TODAY}
    updated: {TODAY}
    project: {PROJECT}
    ---
    """)

def readme_for(dirname: str, meta: dict[str, str]) -> str:
    return dedent(f"""\
    {frontmatter(meta["title"])}
    # {meta["title"]}

    ## Purpose

    {meta["purpose"]}

    ## Repository Role

    This directory is part of the canonical Monorepo One root-level structure.

    ## Rules

    {meta["rules"]}

    ## Current Status

    This directory is established as part of the root repository contract.

    Concrete implementation files will be added in later slices when the relevant capability is introduced.
    """)

for dirname, meta in ROOT_DIRS.items():
    path = Path(dirname)
    path.mkdir(parents=True, exist_ok=True)

    readme = path / "README.md"
    if not readme.exists():
        readme.write_text(readme_for(dirname, meta), encoding="utf-8")

# Ensure .artifacts can track only its README.
gitignore = Path(".gitignore")
if gitignore.exists():
    text = gitignore.read_text(encoding="utf-8")
else:
    text = ""

if ".artifacts/" in text:
    text = text.replace(".artifacts/", ".artifacts/*\n!.artifacts/README.md")
elif ".artifacts/*" not in text:
    text = text.rstrip() + "\n\n# Project artifacts\n.artifacts/*\n!.artifacts/README.md\n"

gitignore.write_text(text.rstrip() + "\n", encoding="utf-8")

# Repository structure document.
Path("docs/project/00-foundation").mkdir(parents=True, exist_ok=True)
Path("docs/project/00-foundation/REPOSITORY-STRUCTURE.md").write_text(dedent(f"""\
---
title: Repository Structure
status: accepted
version: 0.1.0
created: {TODAY}
updated: {TODAY}
project: {PROJECT}
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
  """), encoding="utf-8")

# Repo contract document.

Path("docs/project/06-quality").mkdir(parents=True, exist_ok=True)
Path("docs/project/06-quality/REPO-CONTRACT.md").write_text(dedent(f"""\
------------------------------------------------------------------------

title: Repo Contract
status: accepted
version: 0.1.0
created: {TODAY}
updated: {TODAY}
project: {PROJECT}
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
  """), encoding="utf-8")

# ADR.

Path("docs/adr").mkdir(parents=True, exist_ok=True)
Path("docs/adr/ADR-0005-establish-root-repository-structure.md").write_text(dedent(f"""\
----------------------------------------------------------------------------------------

title: ADR-0005 - Establish Root Repository Structure
status: accepted
version: 0.1.0
created: {TODAY}
updated: {TODAY}
project: {PROJECT}
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
  """), encoding="utf-8")

# Update ADR index.

adr_index = Path("docs/adr/README.md")
if adr_index.exists():
    text = adr_index.read_text(encoding="utf-8")
else:
    text = dedent(f"""
---
title: Architecture Decision Records
status: draft
version: 0.1.0
created: {TODAY}
updated: {TODAY}
project: {PROJECT}
---

# Architecture Decision Records

## ADR Index

| ADR | Title | Status |
| --- | --- | --- |
""")


row = "| ADR-0005 | Establish Root Repository Structure | accepted |"
if row not in text:
    text = text.rstrip() + "\n" + row + "\n"
adr_index.write_text(text, encoding="utf-8")

    # Verification script.

verify = Path("tools/scripts/verify-repo-structure.sh")
verify.write_text(dedent("""
#!/usr/bin/env bash

set -euo pipefail

required_dirs=(
".github"
".artifacts"
"apps"
"assets"
"bin"
"config"
"contracts"
"data"
"db"
"docs"
"governance"
"infra"
"ops"
"packages"
"patches"
"security"
"services"
"templates"
"tools"
)

required_files=(
".github/README.md"
".artifacts/README.md"
"apps/README.md"
"assets/README.md"
"bin/README.md"
"config/README.md"
"contracts/README.md"
"data/README.md"
"db/README.md"
"docs/README.md"
"governance/README.md"
"infra/README.md"
"ops/README.md"
"packages/README.md"
"patches/README.md"
"security/README.md"
"services/README.md"
"templates/README.md"
"tools/README.md"
"docs/project/00-foundation/REPOSITORY-STRUCTURE.md"
"docs/project/06-quality/REPO-CONTRACT.md"
"docs/adr/ADR-0005-establish-root-repository-structure.md"
"tools/scripts/verify-repo-structure.sh"
)

failures=0

for dir in "${required_dirs[@]}"; do
if [[ ! -d "$dir" ]]; then
echo "Missing required directory: $dir"
failures=$((failures + 1))
fi
done

for file in "${required_files[@]}"; do
if [[ ! -f "$file" ]]; then
echo "Missing required file: $file"
failures=$((failures + 1))
fi
done

if grep -R "[https://fie.nl.tab.digital](https://fie.nl.tab.digital)" -n docs README.md tools .github apps assets bin config contracts data db governance infra ops packages patches security services templates 2>/dev/null; then
echo "Private Nextcloud URL found in tracked documentation paths."
failures=$((failures + 1))
fi

if grep -R "appliedinnovationcorp-team.atlassian.net" -n docs README.md tools .github apps assets bin config contracts data db governance infra ops packages patches security services templates 2>/dev/null; then
echo "Private Confluence URL found in tracked documentation paths."
failures=$((failures + 1))
fi

if grep -R "appliedinnovationcorp.atlassian.net" -n docs README.md tools .github apps assets bin config contracts data db governance infra ops packages patches security services templates 2>/dev/null; then
echo "Private Jira URL found in tracked documentation paths."
failures=$((failures + 1))
fi

if [[ "$failures" -ne 0 ]]; then
echo "Repository structure verification failed with $failures failure(s)."
exit 1
fi

echo "Repository structure verification passed"
"""), encoding="utf-8")
verify.chmod(0o755)

# Update root verify if present, but avoid duplicating.

root_verify = Path("tools/scripts/verify.sh")
if root_verify.exists():
    text = root_verify.read_text(encoding="utf-8")
    marker = "bash tools/scripts/verify-repo-structure.sh"
if marker not in text:
    insert = dedent("""\

    say "Checking repository structure"
    bash tools/scripts/verify-repo-structure.sh
    """)
    if "say \"Repository verification passed\"" in text:
        text = text.replace("say \"Repository verification passed\"", insert.strip() + "\n\nsay \"Repository verification passed\"")
    else:
        text = text.rstrip() + "\n\n" + insert.strip() + "\n"
    root_verify.write_text(text, encoding="utf-8")

# Update AI current state.

Path("docs/ai").mkdir(parents=True, exist_ok=True)
Path("docs/ai/CURRENT_STATE.md").write_text(dedent(f"""\
--------------------------------------------------------

title: Current State
status: draft
version: 0.1.0
created: {TODAY}
updated: {TODAY}
project: {PROJECT}
------------------

# Current State

## Project

Monorepo One

## Current Phase

Phase 0: repository foundation and operating system.

## Current Goal

Establish the root-level repository structure contract before implementing applications, services, packages, infrastructure, or CI.

## External Systems

* GitHub repository exists.
* Jira `MONO` project exists.
* Confluence `Monorepo One Engineering` space exists.
* Nextcloud `Controlled Records` area exists.

Private external-system URLs should not be committed to the public GitHub repository.

## Current Work

Current branch should be:

```text
MONO-5/chore/root-directory-contract
```

## Completed Work

* Governance foundation established.
* External delivery and records operating model documented.
* Planning deliverable baseline scaffolded.
* Root directory contract scaffolded.
* Repo structure verification script added.

## Current Verification

Run:

```bash
bash tools/scripts/verify-repo-structure.sh
git diff --check
```

If the full toolchain is stable, also run:

```bash
bun run verify
```

## Next Recommended Action

Open a PR for the root directory contract and reference `MONO-5`.

After this PR is merged, the next recommended slice is the GitHub repository collaboration baseline:

* issue templates;
* pull request template;
* CODEOWNERS;
* initial CI skeleton;
* Dependabot configuration if appropriate.
  """), encoding="utf-8")
