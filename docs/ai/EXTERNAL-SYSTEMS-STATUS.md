
title: External Systems Status
status: accepted
version: 0.2.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
---------------------

# External Systems Status

## Current Phase

Phase 0: repository foundation and operating system simplification.

## Active Systems

| System        | Status | Role                                                                    |
| ------------- | ------ | ----------------------------------------------------------------------- |
| GitHub        | Active | Source of truth, issues, PRs, docs, ADRs, verification, releases, CI/CD |
| Repo Markdown | Active | Planning, architecture, requirements, decisions, handoff                |
| Nextcloud     | Active | Controlled records and approved exports                                 |

## Deprecated Systems

| System     | Status     | Reason                                               |
| ---------- | ---------- | ---------------------------------------------------- |
| Jira       | Deprecated | Excessive friction for current solo project workflow |
| Confluence | Deprecated | Excessive friction; repo Markdown is preferred       |

## Current Operating Model

Use:

```text
GitHub + repo Markdown + Nextcloud
```

Do not use Jira or Confluence for new active project delivery.

## GitHub

Status: Active.

Repository:

```text
thomascarter613/monorepo-one
```

Visibility:

```text
Public
```

Important note:

```text
Do not commit secrets, credentials, private notes, customer data, sensitive personal data, or private Nextcloud URLs.
```

## Nextcloud

Status: Active.

Provider:

```text
Nextcloud hosted provider
```

Controlled records area:

```text
Controlled Records
```

Current known state:

* Controlled Records folder exists.
* Folder structure exists.
* Test record exists.
* Records register exists.

## Jira

Status: Deprecated.

Jira may remain as a historical setup artifact, but it is not part of the active Monorepo One workflow.

## Confluence

Status: Deprecated.

Confluence may remain as a historical setup artifact, but it is not part of the active Monorepo One workflow.

## Current Gate Before Further Implementation

The simplified operating model should be committed and merged before proceeding with additional repo slices.

## Next Required Action

Commit ADR-0006 and the updated operating model docs.
