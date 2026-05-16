---
title: External Systems Operating Model
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
jira_project_key: MONO
visibility_note: Public GitHub repository; private external system URLs must not be committed unless intentionally approved.
---

# External Systems Operating Model

## Purpose

This document defines how Monorepo One uses external collaboration, delivery, planning, and records systems.

The goal is to ensure that work is traceable from idea to implementation to verification to controlled record without relying on hidden chat history or informal memory.

## Current External Systems

| System | Name / Identifier | Role | URL Handling |
| --- | --- | --- | --- |
| GitHub | `thomascarter613/monorepo-one` | Canonical source code, repo docs, ADRs, branches, commits, pull requests, releases, CI/CD, verification history | Public URL may be referenced |
| Jira | `MONO` | Delivery tracking, work items, risks, task state, execution planning | Private URL stored in Confluence/Jira, not committed to public repo |
| Confluence | `Monorepo One Engineering` | Human-readable planning hub, coordination pages, dashboards, summaries | Private URL stored in Confluence/Jira, not committed to public repo |
| Nextcloud | Controlled Records | Controlled records, approved exports, signed/formal document copies, release/audit records | Private folder URL stored in Confluence/Jira, not committed to public repo |

## System-of-Record Rules

### GitHub

GitHub is canonical for:

- source code
- repository documentation
- ADRs
- branches
- commits
- pull requests
- releases
- CI/CD definitions
- verification scripts
- repo-resident AI handoff files

If a decision affects code, architecture, tooling, verification, repository structure, or delivery discipline, it must be reflected in GitHub.

### Jira

Jira is canonical for:

- work items
- delivery state
- work sequencing
- execution tracking
- risks requiring active follow-up
- traceability between planned work and implementation

Jira work item keys should appear in branch names, pull request titles, and commit footers where practical.

### Confluence

Confluence is canonical for:

- human-readable planning hub
- navigation across systems
- project coordination
- dashboard-style summaries
- meeting notes
- non-canonical summaries of repo docs
- links to private system URLs

Confluence may summarize GitHub documents, but GitHub remains canonical for implementation-affecting technical records.

### Nextcloud

Nextcloud is canonical for:

- controlled exported records
- approved document baselines
- signed documents
- formal document copies
- release records
- audit records

Nextcloud should not replace GitHub as the canonical source for Markdown documentation, ADRs, source code, or verification logic.

## Privacy and Public Repository Rule

The GitHub repository is public.

Therefore:

- Do not commit secrets.
- Do not commit credentials.
- Do not commit private meeting notes.
- Do not commit private customer/user data.
- Do not commit private Jira, Confluence, or Nextcloud URLs unless explicitly approved.
- Use stable identifiers such as `MONO`, `Monorepo One Engineering`, and `Controlled Records` in public repo docs.

## Traceability Convention

A normal work item should flow like this:

```text
Jira work item
→ Git branch
→ commit(s)
→ pull request
→ verification
→ merge
→ Confluence summary/update
→ Nextcloud controlled record, when applicable
```

## Naming Conventions

### Jira Key

```text
MONO-123
```

### Branch

```text
MONO-123/<type>/<short-description>
```

Examples:

```text
MONO-2/docs/external-operating-model
MONO-7/adr/package-manager-decision
MONO-12/chore/repo-contract
```

### Commit Footer

```text
Refs: MONO-123
```

### Pull Request Title

```text
[MONO-123] docs(scope): concise summary
```

## Minimum Acceptance for the External System

The external system is accepted when:

* GitHub repository exists.
* Jira `MONO` project exists.
* At least one Jira work item opens directly.
* Confluence `Monorepo One Engineering` space exists.
* Nextcloud `Controlled Records` area exists.
* A test record exists in Nextcloud.
* Confluence links to GitHub, Jira, and Nextcloud.
* Jira records the DMS setup link/comment.
* Repo documentation records this operating model.
* A test branch/commit/PR references a Jira key.

## Current Known Limitations

* Jira custom workflow configuration was attempted but deferred because work item visibility became unreliable.
* Jira is currently accepted as usable with its simpler/default workflow.
* Detailed workflow states will be represented through labels, PR review, verification docs, and future workflow hardening.
* Nextcloud metadata discipline is currently lightweight and folder/register based.
* Formal retention automation is deferred.

## Gate Before Slice 3

Slice 3 must not begin until this operating model is committed and linked from Jira/Confluence.
