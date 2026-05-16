
title: Document Control
status: accepted
version: 0.2.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
dms: nextcloud
supersedes: version 0.1.0 external model that included Jira and Confluence as active systems.
---------------------------------------------------------------------------------------------

# Document Control

## Purpose

This document defines how Monorepo One controls formal documents and records across GitHub, repo Markdown, GitHub Issues/PRs, and Nextcloud.

## Document Classes

| Class             | Description                                                           | Canonical System     |
| ----------------- | --------------------------------------------------------------------- | -------------------- |
| Working Markdown  | Living docs, specs, ADRs, architecture, planning, implementation docs | GitHub               |
| Work Item         | Delivery/task/risk/verification tracking                              | GitHub Issues        |
| Review Artifact   | Review, verification, merge discussion                                | GitHub Pull Requests |
| Controlled Record | Approved/exported/signed/final record copy                            | Nextcloud            |

## Current DMS

The DMS is:

```text
Nextcloud
```

The controlled record area is:

```text
Controlled Records
```

The actual private folder URL is intentionally not committed to this public repository.

## Folder Structure

The controlled records folder uses this structure:

```text
Controlled Records/
├── 00-registers/
├── 01-charters/
├── 02-requirements/
├── 03-architecture/
├── 04-adrs/
├── 05-security/
├── 06-releases/
├── 07-approvals/
├── 08-audits/
└── 09-exports/
```

## Records Register

A records register exists in Nextcloud:

```text
Controlled Records/00-registers/RECORDS-REGISTER.md
```

## Initial Test Record

The initial test record is:

```text
DMS-TEST-0001 - Monorepo One Records Register Test.txt
```

## Minimum Metadata

Each controlled record should include:

* Record ID;
* Title;
* Project;
* Record type;
* Document status;
* Document version;
* Retention class;
* source Git commit or GitHub URL;
* GitHub issue number, if applicable;
* GitHub pull request URL, if applicable;
* effective date, if applicable;
* supersedes, if applicable.

## Record ID Convention

Use this format:

```text
<CLASS>-<YYYY>-<SEQUENCE>
```

Examples:

```text
ADR-2026-0001
REQ-2026-0001
ARCH-2026-0001
REL-2026-0001
AUDIT-2026-0001
```

For test records:

```text
DMS-TEST-0001
```

## Status Values

| Status     | Meaning                    |
| ---------- | -------------------------- |
| Draft      | Work in progress           |
| Review     | Ready for review           |
| Approved   | Accepted controlled record |
| Superseded | Replaced by a newer record |
| Rejected   | Not accepted               |
| Archived   | Retained but inactive      |

## Retention Classes

| Class      | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| Working    | Temporary or draft working record                       |
| Controlled | Important approved project record                       |
| Permanent  | Long-term project record                                |
| Superseded | Retained to preserve history                            |
| Audit      | Evidence of process, verification, approval, or release |

## Public Repository Safety

Because the GitHub repository is public:

* private Nextcloud URLs should not be committed;
* record identifiers may be committed;
* system names may be committed;
* public GitHub URLs may be committed;
* secrets must never be committed.

## Deprecated References

Jira and Confluence are no longer active document-control systems for Monorepo One.

They should not be used for new controlled document workflows.

## Future Hardening

Future improvements may include:

* exported PDF baselines;
* checksums for controlled records;
* release evidence packages;
* signed approvals;
* retention automation;
* backup verification;
* self-hosted Nextcloud migration.
