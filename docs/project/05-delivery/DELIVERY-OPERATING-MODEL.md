
title: Delivery Operating Model
status: accepted
version: 0.2.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
supersedes: version 0.1.0 Jira-centered delivery model.
-------------------------------------------------------

# Delivery Operating Model

## Purpose

This document defines how work moves through Monorepo One from idea to implementation, verification, merge, and records management.

The active delivery system is now GitHub-native.

## Delivery Principle

Every meaningful change should be traceable.

A change should answer:

* why it is being done;
* what issue or decision authorized it;
* what files changed;
* how it was verified;
* what ADR or requirement it supports;
* whether a controlled record is required.

## Active Delivery Systems

| Concern                   | System               |
| ------------------------- | -------------------- |
| Work tracking             | GitHub Issues        |
| Review gate               | GitHub Pull Requests |
| Source of truth           | GitHub repository    |
| Planning and architecture | Repo Markdown        |
| Controlled records        | Nextcloud            |

## Deprecated Delivery Systems

Jira and Confluence are deprecated for active Monorepo One delivery.

They were attempted during setup but created friction disproportionate to the project stage.

Historical references may remain in old records, but new work should not depend on Jira or Confluence.

## Work Flow

```text
Idea
→ GitHub Issue
→ branch
→ commit(s)
→ pull request
→ verification
→ merge
→ release/update
→ controlled record, if applicable
```

## GitHub Issue Types

Use labels to classify issues.

Recommended type labels:

```text
type:adr
type:bug
type:chore
type:docs
type:feature
type:risk
type:spike
type:work-packet
```

## Area Labels

```text
area:architecture
area:delivery
area:docs
area:governance
area:repo
area:security
area:tooling
area:verification
```

## Phase Labels

```text
phase:0-foundation
phase:1-structure
phase:2-tooling
phase:3-ci
phase:4-first-app
```

## Status Labels

```text
status:ready
status:in-progress
status:blocked
status:verification
status:done
```

Status labels are lightweight. The authoritative state of implementation is the issue, branch, PR, and verification result.

## Branch Naming

Use:

```text
issue-<number>/<type>/<short-description>
```

Examples:

```text
issue-1/docs/simplify-operating-model
issue-2/chore/root-directory-contract
issue-3/ci/add-github-actions-baseline
```

For work that has no issue yet, create the issue before opening the PR.

## Commit Standard

Use Conventional Commits.

Example:

```text
docs(governance): simplify operating model

Refs: #1
```

## Pull Request Standard

A pull request should include:

* summary;
* files/areas changed;
* verification commands run;
* known risks or deferrals;
* linked issue;
* screenshots or outputs when relevant.

## Definition of Ready

A GitHub issue is ready when:

* the goal is clear;
* scope is bounded;
* acceptance criteria are present;
* verification is known;
* dependencies are identified;
* risks are noted;
* the work is small enough for one coherent branch/PR.

## Definition of Done

A work item is done when:

* changes are implemented or documented;
* verification has passed or deferrals are explicit;
* relevant docs are updated;
* ADRs are updated if decisions changed;
* PR has been reviewed by the author at minimum;
* the branch is merged;
* controlled record is created in Nextcloud when required.

## Verification Discipline

At minimum, documentation-only slices should run:

```bash
git diff --check
```

Structure slices should also run their relevant repo verification script.

Tooling/code slices should run the relevant local verification command once stable.

## Controlled Records

A controlled record is required when a document becomes an approved baseline, exported release artifact, signed decision, audit artifact, or release evidence package.

Controlled records are stored in Nextcloud.

## Current Gate

Before implementation-heavy slices, the repository should have:

* simplified operating model documented;
* GitHub workflow documented;
* root directory contract documented;
* repo verification scripts;
* GitHub issue/PR templates;
* CI baseline.
