
title: Engineering Standard
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
-------------------

# Engineering Standard

## Standard

This repository should be built to a production-grade engineering standard.

Production-grade means the work is:

* maintainable
* testable
* secure
* observable
* documented
* accessible where user interfaces exist
* reproducible
* reviewable
* evolvable
* operationally supportable

## Default Delivery Discipline

Work should proceed through small, atomic, reviewable slices.

Each meaningful slice should include:

* goal
* files changed
* verification command
* expected result
* commit point
* Conventional Commit message
* known risks or deferrals

## Definition of Done

A work item is not done merely because files were written.

A work item is done when the applicable checks pass, including:

* formatting
* linting
* typechecking
* tests
* build
* contract validation
* security checks
* documentation updates
* repository invariant checks

If verification has not been run, the work should be described as drafted, not complete.

## Architecture Discipline

Architecture should be explicit and documented.

Major decisions should be captured as ADRs.

Patterns such as DDD, BDD, TDD, clean architecture, hexagonal architecture, event-driven architecture, CQRS, and policy-as-code should be used only when they solve real problems and earn their complexity.

## Verification Discipline

Verification should be available locally and in CI.

The repository should eventually provide a single top-level verification command that proves the repo is healthy.

Until that exists, each slice should provide manual verification steps.

## Security Discipline

Security is a first-class concern.

The repository should avoid committing secrets and should eventually include:

* dependency scanning
* secret scanning
* static analysis
* least-privilege configuration
* secure defaults
* threat modeling for consequential systems
