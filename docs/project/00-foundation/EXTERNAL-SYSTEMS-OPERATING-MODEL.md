
title: External Systems Operating Model
status: accepted
version: 0.2.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
visibility_note: Public GitHub repository; private external system URLs must not be committed unless intentionally approved.
supersedes: version 0.1.0 external model that used Jira and Confluence as active systems.
-----------------------------------------------------------------------------------------

# External Systems Operating Model

## Purpose

This document defines the active collaboration, delivery, documentation, and records operating model for Monorepo One.

The operating model has been simplified to reduce friction while preserving traceability, verification, documentation discipline, and controlled records.

## Current Active Systems

| System        | Role                                                                                                       | Status |
| ------------- | ---------------------------------------------------------------------------------------------------------- | ------ |
| GitHub        | Source code, issues, PRs, repo docs, ADRs, releases, verification, CI/CD, security configuration           | Active |
| Repo Markdown | Product planning, requirements, architecture, ADRs, delivery docs, quality docs, security docs, AI handoff | Active |
| Nextcloud     | Controlled records, approved exports, release evidence, audit artifacts                                    | Active |

## Deprecated Systems

| System     | Former Role                                  | Current Status              |
| ---------- | -------------------------------------------- | --------------------------- |
| Jira       | Work tracking and delivery workflow          | Deprecated for this project |
| Confluence | Planning hub and human-readable coordination | Deprecated for this project |

## Decision Summary

Jira and Confluence were attempted as part of the initial external system setup.

They are now deprecated because they introduced excessive friction for the current project stage.

Monorepo One will instead use a GitHub-native operating model.

## System-of-Record Rules

### GitHub

GitHub is canonical for:

* source code;
* repository documentation;
* issues;
* labels;
* milestones;
* pull requests;
* branch protection;
* releases;
* CI/CD workflows;
* security scanning configuration;
* ADRs;
* verification scripts;
* repo-resident AI handoff files.

### Repo Markdown

Repo Markdown is canonical for:

* product vision;
* product charter;
* requirements;
* domain model;
* architecture;
* ADRs;
* delivery process;
* quality strategy;
* security strategy;
* records process;
* AI handoff;
* current project state.

Markdown files should be versioned, reviewed, and kept aligned with implementation.

### Nextcloud

Nextcloud is canonical for:

* controlled exported records;
* approved document baselines;
* formal release records;
* audit artifacts;
* signed documents, if any;
* exported PDF/DOCX copies, when needed.

Nextcloud does not replace GitHub for living source documentation.

## Public Repository Safety Rule

The GitHub repository is public.

Therefore:

* do not commit secrets;
* do not commit credentials;
* do not commit private meeting notes;
* do not commit private customer/user data;
* do not commit private Nextcloud URLs unless intentionally approved;
* do not commit historical private Jira or Confluence URLs unless intentionally approved.

Stable public-safe identifiers may be committed.

## Active Traceability Flow

```text
GitHub Issue
→ branch
→ commit(s)
→ pull request
→ verification
→ merge
→ release or documentation update
→ Nextcloud controlled record, when applicable
```

## GitHub Issue Convention

Use GitHub Issues for:

* work packets;
* bugs;
* risks;
* ADR work;
* spikes;
* documentation tasks;
* repo maintenance;
* verification tasks;
* security tasks.

## Branch Naming Convention

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

If an issue does not exist yet, use a clear branch name and create the issue before opening the pull request.

## Commit Convention

Use Conventional Commits.

When tied to a GitHub issue, include:

```text
Refs: #<issue-number>
```

Example:

```text
docs(governance): simplify operating model

Refs: #1
```

## Pull Request Convention

Pull request titles should be concise and include issue references when available.

Example:

```text
[Refs #1] docs(governance): simplify operating model
```

## Labels

The recommended GitHub label taxonomy is:

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

## Minimum Acceptance for the Operating Model

The operating model is accepted when:

* GitHub repository is active;
* GitHub Issues are used for work tracking;
* repo Markdown contains planning and architecture;
* ADR-0006 records the simplification decision;
* Nextcloud remains available for controlled records;
* Jira and Confluence are documented as deprecated;
* no private external URLs are committed.

## Change Control

Any future decision to reintroduce Jira, Confluence, Linear, Plane, Notion, SharePoint, or another external system must be recorded in a new ADR.

The default should remain GitHub-native unless the added tool clearly earns its operational cost.
