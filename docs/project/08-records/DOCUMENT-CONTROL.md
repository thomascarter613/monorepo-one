
title: Document Control
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
dms: nextcloud
--------------

# Document Control

## Purpose

This document defines how Monorepo One controls formal documents and records across GitHub, Confluence, Jira, and Nextcloud.

## Document Classes

| Class             | Description                                         | Canonical System |
| ----------------- | --------------------------------------------------- | ---------------- |
| Working Markdown  | Living docs, specs, ADRs, implementation docs       | GitHub           |
| Coordination Page | Human-readable summaries, dashboards, meeting notes | Confluence       |
| Work Item         | Delivery/task/risk/verification tracking            | Jira             |
| Controlled Record | Approved/exported/signed/final record copy          | Nextcloud        |

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

A records register exists in:

```text
Controlled Records/00-registers/RECORDS-REGISTER.md
```

The register tracks controlled records stored in Nextcloud.

## Initial Test Record

The initial test record is:

```text
DMS-TEST-0001 - Monorepo One Records Register Test.txt
```

Purpose:

```text
Verify that Nextcloud can serve as the controlled-records DMS for Monorepo One and can store records linked to GitHub, Jira, and Confluence.
```

## Minimum Metadata

Each controlled record should include:

* Record ID
* Title
* Project
* Record type
* Document status
* Document version
* Retention class
* source Git commit or GitHub URL
* Jira key, if applicable
* Confluence reference, if applicable
* effective date, if applicable
* supersedes, if applicable

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
| Permanent  | Long-term institutional/project record                  |
| Superseded | Retained to preserve history                            |
| Audit      | Evidence of process, verification, approval, or release |

## Public Repository Safety

Because the GitHub repository is public:

* private DMS URLs should not be committed;
* private Confluence URLs should not be committed unless approved;
* private Jira URLs should not be committed unless approved;
* record identifiers may be committed;
* system names may be committed;
* public GitHub URLs may be committed.

## Future Hardening

Future improvements may include:

* stronger metadata automation;
* exported PDF baselines;
* checksums for controlled records;
* release evidence packages;
* signed approvals;
* retention automation;
* backup verification;
* self-hosted Nextcloud migration.
