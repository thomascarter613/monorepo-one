
title: Current State
status: accepted
version: 0.2.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
---------------------

# Current State

## Project

Monorepo One

## Current Phase

Phase 0: repository foundation and operating system simplification.

## Current Goal

Simplify the active project operating model to GitHub + repo Markdown + Nextcloud.

## Active Operating Model

```text
GitHub = source of truth, issues, PRs, releases, verification, CI/CD
Repo Markdown = planning, requirements, architecture, ADRs, handoff
Nextcloud = controlled records and approved exports
```

## Deprecated Systems

```text
Jira = deprecated
Confluence = deprecated
```

Jira and Confluence were attempted but are no longer part of the active workflow because they created excessive friction.

## Public Repository Rule

The repository is public.

Do not commit:

* secrets;
* credentials;
* private URLs;
* customer data;
* sensitive personal data;
* private operational notes.

## Current Work

Current branch should be:

```text
docs/simplify-operating-model
```

## Current Slice

Simplify external operating model.

## Expected Outputs

* ADR-0006;
* updated external systems operating model;
* updated delivery operating model;
* GitHub workflow document;
* deprecated Jira workflow document;
* updated document control model;
* updated AI current state;
* updated external systems status.

## Next Recommended Action

After this slice is merged, proceed with the root-level repository contract if it has not already been completed.

If the root directory contract is already complete, proceed to the GitHub collaboration baseline:

* issue templates;
* pull request template;
* label taxonomy;
* CODEOWNERS;
* initial CI skeleton.
