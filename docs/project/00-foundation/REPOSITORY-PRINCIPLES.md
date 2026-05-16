
title: Repository Principles
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
-------------------

# Repository Principles

## Principle 1: The Repository Is the Source of Truth

The repository should contain the durable project memory.

Important context should live in files, not only in chat history, issue comments, or informal notes.

## Principle 2: Governance Before Generation

The repository should establish intent, constraints, and decision discipline before uncontrolled code generation.

## Principle 3: Verification Is a Product Feature

A developer should be able to verify the repository state with explicit commands.

If a claim cannot be verified, it should be labeled as an assumption or recommendation.

## Principle 4: Architecture Must Constrain Implementation

Architecture should not be decorative.

It should guide boundaries, dependencies, naming, workflows, testing, and deployment.

## Principle 5: Documentation Must Stay Close to the Work

Documentation should be updated as part of the same work that changes behavior, architecture, tooling, or process.

## Principle 6: Prefer Boring Foundations

Use advanced tools and patterns where they are justified.

Do not introduce complexity before it has a clear purpose.

## Principle 7: Optimize for Handoff

A future contributor or AI assistant should be able to resume work by reading repo-resident context files.

## Principle 8: Small Atomic Commits

Commits should be small, coherent, reviewable, and described with Conventional Commits.

## Principle 9: Explicit Boundaries

The monorepo should clearly distinguish applications, services, packages, tools, infrastructure, contracts, data, docs, governance, and generated artifacts.

## Principle 10: Evolvability Without Chaos

The repository should support future evolution without constant restructuring.
