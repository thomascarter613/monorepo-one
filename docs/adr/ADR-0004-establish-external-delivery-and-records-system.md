
title: ADR-0004 - Establish External Delivery and Records System
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
---------------------

# ADR-0004: Establish External Delivery and Records System

## Status

Accepted

## Context

Monorepo One is intended to be a serious, governance-first, high-grade monorepo.

The repository alone is not sufficient for every collaboration and records-management need.

The project needs:

* source control;
* work tracking;
* human-readable planning and coordination;
* controlled records storage;
* traceability between these systems.

## Decision

Monorepo One will use the following external delivery and records system:

| Concern                                           | System     |
| ------------------------------------------------- | ---------- |
| Source code, repo docs, ADRs, verification, CI/CD | GitHub     |
| Work tracking and delivery execution              | Jira       |
| Planning hub and human-readable coordination      | Confluence |
| Controlled records and approved exports           | Nextcloud  |

## Rationale

GitHub is the correct canonical home for source code, repo-resident documentation, ADRs, verification scripts, CI/CD, and release history.

Jira is the correct home for delivery tracking and task execution.

Confluence is the correct home for human-readable coordination pages, dashboards, planning summaries, and cross-system navigation.

Nextcloud is the selected free DMS alternative for controlled records, approved exports, signed/formal document copies, release records, and audit records.

## Public Repository Constraint

The GitHub repository is public.

Therefore, private Jira, Confluence, and Nextcloud URLs should not be committed to the public repo unless intentionally approved.

The repository may document system roles, identifiers, naming conventions, and traceability rules without exposing private URLs.

## Consequences

This creates a more mature operating model than using GitHub alone.

It also introduces coordination overhead because each system has a defined role.

The overhead is acceptable because the project goal is a principal-grade monorepo with durable planning, traceability, verification, and controlled records.

## Alternatives Considered

### GitHub only

Rejected because GitHub alone is not ideal for human-readable planning hubs, delivery boards, and controlled exported document records.

### GitHub plus Jira only

Rejected because it lacks a polished planning and coordination layer and a separate controlled-records store.

### GitHub plus Confluence only

Rejected because it lacks robust delivery tracking and execution state.

### SharePoint Online as DMS

Deferred because the user selected Nextcloud as the free DMS alternative.

### Self-hosted DMS immediately

Rejected for now because self-hosting the DMS would create an infrastructure project before the monorepo foundation is complete.

## Verification

This ADR is verified when:

* GitHub repository exists;
* Jira `MONO` project exists;
* Confluence `Monorepo One Engineering` space exists;
* Nextcloud `Controlled Records` folder exists;
* a test record exists in Nextcloud;
* Confluence links to GitHub, Jira, and Nextcloud;
* Jira records the Nextcloud DMS setup;
* this ADR is committed to GitHub;
* a branch, commit, or pull request references `MONO-2`.

## Follow-up Work

* Create issue taxonomy.
* Create branching strategy.
* Create commit standard.
* Create pull request standard.
* Create Jira workflow documentation.
* Create DMS integration documentation.
* Create repo contract and verification checks.
