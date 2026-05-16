
title: Delivery Operating Model
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
jira_project_key: MONO
----------------------

# Delivery Operating Model

## Purpose

This document defines how work moves through Monorepo One from idea to implementation, verification, merge, and record keeping.

## Delivery Principle

Every meaningful change should be traceable.

A change should answer:

* Why is this being done?
* What work item authorized it?
* What files changed?
* How was it verified?
* What decision or requirement does it support?
* What record should preserve the outcome?

## Current Toolchain of Work

| Concern                     | System     |
| --------------------------- | ---------- |
| Work tracking               | Jira       |
| Source and technical truth  | GitHub     |
| Human-readable coordination | Confluence |
| Controlled records          | Nextcloud  |

## Current Jira Reality

The Jira project key is:

```text
MONO
```

The intended workflow is:

```text
Backlog → Ready → In Progress → In Review → Verification → Done
```

However, custom workflow configuration was deferred because work item visibility became unreliable.

The current accepted operational workflow is the simpler Jira default workflow, supplemented by labels, GitHub PRs, and verification discipline.

## Required Traceability Fields

For each meaningful work item, capture:

* Jira key
* summary
* work type
* component or area
* acceptance criteria
* verification method
* related GitHub branch
* related pull request
* related ADR, if any
* related Confluence page, if any
* related Nextcloud record, if any

## Branching Convention

```text
MONO-123/<type>/<short-description>
```

Examples:

```text
MONO-2/docs/external-operating-model
MONO-8/adr/repository-structure-contract
MONO-12/chore/verification-script
```

## Commit Convention

Use Conventional Commits.

Example:

```text
docs(delivery): document external operating model

Refs: MONO-2
```

## Pull Request Convention

Pull request titles should include the Jira key.

Example:

```text
[MONO-2] docs(delivery): document external operating model
```

## Definition of Ready

A work item is ready when:

* the goal is clear;
* scope is bounded;
* acceptance criteria are present;
* verification is known;
* dependencies are identified;
* risks are noted;
* the work is small enough for one coherent branch/PR.

## Definition of Done

A work item is done when:

* implementation or documentation is complete;
* verification has passed or deferrals are documented;
* relevant docs are updated;
* ADRs are created or updated if decisions changed;
* GitHub branch/commit/PR references the Jira key;
* Confluence is updated when coordination visibility is needed;
* Nextcloud record is created when a controlled record is required;
* the work is merged or otherwise formally closed.

## Current Gate Before Slice 3

Slice 3 remains blocked until:

* external operating model is documented;
* planning deliverable register is documented;
* document control model is documented;
* ADR for the external delivery/records system is accepted;
* one traceability loop has been proven.
