---
title: ADR-0006 - Simplify Operating Model
status: accepted
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
---

# ADR-0006: Simplify Operating Model

## Status

Accepted

## Context

Monorepo One initially attempted to establish an external operating model using GitHub, Jira, Confluence, and Nextcloud.

The intent was sound:

- GitHub for source code, repo documentation, ADRs, pull requests, releases, verification, and CI/CD.
- Jira for work tracking.
- Confluence for human-readable planning and coordination.
- Nextcloud for controlled records and approved exports.

However, during setup, Jira and Confluence introduced friction disproportionate to the current project stage.

The project is currently a solo, clean-slate, governance-first monorepo. At this stage, the operating system must be lightweight, reliable, and directly connected to repository progress.

A process that looks enterprise-grade but slows or blocks execution is not principal-grade. Principal-grade engineering requires the simplest operating model that preserves traceability, verification, maintainability, and forward progress.

## Decision

Monorepo One will simplify its active operating model.

The active systems are now:

| Concern | Active System |
| --- | --- |
| Source code | GitHub |
| Work tracking | GitHub Issues |
| Review and verification gate | GitHub Pull Requests |
| Planning and architecture | Repo-resident Markdown |
| Decisions | Repo-resident ADRs |
| Handoff and AI context | Repo-resident Markdown |
| Controlled records and approved exports | Nextcloud |

Jira and Confluence are deprecated for this project.

They may remain as historical setup artifacts, but they are no longer part of the active delivery workflow.

## Rationale

This decision reduces operational friction while preserving the important engineering outcomes:

- traceability;
- reviewability;
- repo-resident source of truth;
- controlled records;
- documentation discipline;
- verification discipline;
- AI/human handoff readiness.

GitHub already supports issues, labels, milestones, pull requests, discussions if needed, releases, branch protection, code scanning, secret scanning, and CI/CD.

For the current stage, GitHub plus repo Markdown is sufficient and more coherent.

Nextcloud remains valuable because controlled exported records are a different class of artifact than living Markdown source documents.

## Consequences

### Positive Consequences

- Less tool friction.
- Fewer context switches.
- Simpler work tracking.
- Stronger repository-centered workflow.
- Easier AI/human handoff.
- Lower administrative burden.
- Better alignment with solo/principal execution.

### Negative Consequences

- Less enterprise-style work-management structure.
- No Jira workflow customization.
- No Confluence dashboard/page tree as active planning hub.
- GitHub Issues must carry enough metadata through labels, milestones, and issue templates.
- Repo Markdown must remain disciplined and well organized.

### Mitigation

We will mitigate the loss of Jira/Confluence by using:

- GitHub issue templates;
- GitHub labels;
- GitHub milestones;
- pull request templates;
- ADRs;
- repo-resident planning docs;
- repo-resident handoff files;
- Nextcloud records register for controlled exports.

## Deprecated Systems

### Jira

Jira is deprecated for active project delivery.

Historical references may remain in prior records, but new work should be tracked in GitHub Issues.

### Confluence

Confluence is deprecated for active planning and coordination.

Planning and architecture should be kept in repo-resident Markdown.

## Active System-of-Record Rules

### GitHub

GitHub is canonical for:

- source code;
- branches;
- commits;
- pull requests;
- issues;
- milestones;
- releases;
- CI/CD;
- repo documentation;
- ADRs;
- verification scripts;
- security configuration;
- AI handoff files.

### Repo Markdown

Repo Markdown is canonical for:

- product planning;
- requirements;
- architecture;
- domain model;
- delivery process;
- quality strategy;
- security strategy;
- records process;
- handoff;
- ADRs.

### Nextcloud

Nextcloud is canonical for:

- controlled exported records;
- approved document baselines;
- formal release evidence packages;
- signed documents, if any;
- audit artifacts.

Nextcloud does not replace GitHub as the source for living Markdown docs.

## New Traceability Flow

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

If no GitHub issue exists yet, use a clear branch name and create the issue before opening the pull request.

## Commit Convention

Use Conventional Commits.

When tied to an issue, include a footer:

```text
Refs: #123
```

Example:

```text
docs(governance): simplify operating model

Refs: #1
```

## Pull Request Convention

Use:

```text
[Refs #123] type(scope): summary
```

Example:

```text
[Refs #1] docs(governance): simplify operating model
```

If the work intentionally has no issue yet, use:

```text
docs(governance): simplify operating model
```

## Verification

This ADR is verified when:

* Jira is no longer documented as active delivery infrastructure;
* Confluence is no longer documented as active planning infrastructure;
* GitHub Issues are documented as active work tracking;
* repo Markdown is documented as active planning/architecture source of truth;
* Nextcloud remains documented as controlled-records storage;
* private external URLs are not committed;
* the updated operating model is committed and merged.

## Follow-Up Work

* Add GitHub issue templates.
* Add pull request template.
* Add label taxonomy.
* Add milestone plan.
* Add CODEOWNERS.
* Add GitHub Actions CI baseline.
* Add repo-contract verification for issue/PR templates.
