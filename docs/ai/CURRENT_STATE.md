--------------------------------------------------------

title: Current State
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
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
