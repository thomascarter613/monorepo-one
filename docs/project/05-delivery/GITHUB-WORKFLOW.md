
title: GitHub Workflow
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
---------------------

# GitHub Workflow

## Purpose

This document defines the GitHub-native workflow for Monorepo One.

GitHub is the active work tracking, review, and source-control system for the project.

## Work Item Flow

```text
GitHub Issue
→ branch
→ commit(s)
→ pull request
→ verification
→ merge
→ issue close
→ Nextcloud controlled record, if applicable
```

## Issues

Use GitHub Issues for:

* features;
* bugs;
* documentation tasks;
* repo maintenance;
* ADR work;
* risks;
* spikes;
* work packets;
* verification tasks;
* security tasks.

## Issue Template Expectations

Each meaningful issue should capture:

* goal;
* context;
* acceptance criteria;
* verification;
* affected area;
* risks or deferrals;
* related docs or ADRs.

## Labels

Recommended labels:

```text
type:adr
type:bug
type:chore
type:docs
type:feature
type:risk
type:spike
type:work-packet

phase:0-foundation
phase:1-structure
phase:2-tooling
phase:3-ci
phase:4-first-app

status:ready
status:in-progress
status:blocked
status:verification
status:done

area:architecture
area:delivery
area:docs
area:governance
area:repo
area:security
area:tooling
area:verification
```

## Milestones

Recommended milestones:

```text
v0.0-governance-foundation
v0.1-repo-operating-system
v0.2-first-runnable-skeleton
v0.3-quality-and-ci-baseline
v1.0-initial-stable-monorepo
```

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

## Commit Naming

Use Conventional Commits.

Examples:

```text
docs(governance): simplify operating model
chore(repo): establish root directory contract
ci(github): add verification workflow
```

When tied to an issue, include:

```text
Refs: #<issue-number>
```

## Pull Requests

PR titles should be concise and traceable.

Examples:

```text
[Refs #1] docs(governance): simplify operating model
[Refs #2] chore(repo): establish root directory contract
```

PR descriptions should include:

```text
## Summary

## Files Changed

## Verification

## Risks / Deferrals

## Traceability
```

## Merge Strategy

Prefer squash merge for small atomic slices.

The squash commit should preserve the Conventional Commit summary and issue reference.

## Rules for Public Repository Safety

Do not commit:

* secrets;
* credentials;
* tokens;
* private Nextcloud URLs;
* private customer/user data;
* sensitive personal data;
* private operational notes.

## Future Hardening

Future slices should add:

* issue templates;
* pull request template;
* CODEOWNERS;
* branch protection;
* required CI checks;
* Dependabot configuration;
* secret scanning guidance;
* CodeQL or equivalent code scanning after code exists.
