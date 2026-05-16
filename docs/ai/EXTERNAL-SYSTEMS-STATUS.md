
title: External Systems Status
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
jira_project_key: MONO
----------------------

# External Systems Status

## Current Phase

Phase 0: Planning, documentation, and external delivery-system setup.

## GitHub

Status: Created

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
Do not commit secrets, private notes, credentials, customer data, or private external-system URLs.
```

## Jira

Status: Created

Project name:

```text
Monorepo One
```

Project key:

```text
MONO
```

Current known state:

* Jira project exists.
* `MONO-2` opens directly.
* Custom workflow configuration was attempted but deferred.
* Jira is usable as a simple work tracker for now.

## Confluence

Status: Created

Space name:

```text
Monorepo One Engineering
```

Current known state:

* Homepage exists.
* Page tree exists.
* GitHub/Jira/Nextcloud links are recorded in Confluence.

## Nextcloud

Status: Created

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
* Confluence has been updated.
* Jira has been updated.

## Test Record

```text
DMS-TEST-0001 - Monorepo One Records Register Test.txt
```

Purpose:

```text
Verify that Nextcloud can serve as the controlled-records DMS for Monorepo One and can store records linked to GitHub, Jira, and Confluence.
```

## Gate Status Before Slice 3

| Gate                                                | Status      |
| --------------------------------------------------- | ----------- |
| GitHub repository exists                            | Passed      |
| Jira MONO project exists                            | Passed      |
| Jira work item opens directly                       | Passed      |
| Confluence space exists                             | Passed      |
| Confluence page tree exists                         | Passed      |
| Nextcloud Controlled Records area exists            | Passed      |
| Nextcloud test record exists                        | Passed      |
| Repo documentation records external operating model | In Progress |
| ADR records external delivery system                | In Progress |
| Traceability branch/commit/PR references Jira key   | In Progress |

## Next Required Action

Commit the external operating model documentation and reference `MONO-2`.
