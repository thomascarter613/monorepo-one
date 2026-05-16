
title: Planning Deliverable Register
status: draft
version: 0.1.0
created: 2026-05-16
updated: 2026-05-16
project: monorepo-one
---------------------

# Planning Deliverable Register

## Purpose

This register defines the planning and documentation deliverables that should exist before the monorepo proceeds into deeper structure, application scaffolding, service scaffolding, or implementation work.

The register exists to prevent uncontrolled code generation and to keep the repository aligned with governance-first, docs-driven, spec-driven engineering.

## Deliverable Status Values

| Status      | Meaning                                               |
| ----------- | ----------------------------------------------------- |
| Not Started | Deliverable does not exist yet                        |
| Stubbed     | File exists with enough structure to guide completion |
| Draft       | Meaningful content exists but is not final            |
| Review      | Ready for review                                      |
| Accepted    | Accepted as current baseline                          |
| Superseded  | Replaced by a newer deliverable                       |

## Foundation Deliverables

| Deliverable                      | Path                                                             | Status | Canonical System |
| -------------------------------- | ---------------------------------------------------------------- | ------ | ---------------- |
| Repository README                | `README.md`                                                      | Draft  | GitHub           |
| Documentation index              | `docs/README.md`                                                 | Draft  | GitHub           |
| Engineering standard             | `docs/project/00-foundation/ENGINEERING-STANDARD.md`             | Draft  | GitHub           |
| Repository principles            | `docs/project/00-foundation/REPOSITORY-PRINCIPLES.md`            | Draft  | GitHub           |
| External systems operating model | `docs/project/00-foundation/EXTERNAL-SYSTEMS-OPERATING-MODEL.md` | Draft  | GitHub           |
| Planning deliverable register    | `docs/project/00-foundation/PLANNING-DELIVERABLE-REGISTER.md`    | Draft  | GitHub           |

## Product Deliverables

| Deliverable         | Recommended Path                                 | Status      | Canonical System |
| ------------------- | ------------------------------------------------ | ----------- | ---------------- |
| Product vision      | `docs/project/01-product/PRODUCT-VISION.md`      | Not Started | GitHub           |
| Product charter     | `docs/project/01-product/PRODUCT-CHARTER.md`     | Not Started | GitHub           |
| Problem statement   | `docs/project/01-product/PROBLEM-STATEMENT.md`   | Not Started | GitHub           |
| Goals and non-goals | `docs/project/01-product/GOALS-AND-NON-GOALS.md` | Not Started | GitHub           |
| Stakeholders        | `docs/project/01-product/STAKEHOLDERS.md`        | Not Started | GitHub           |
| Success metrics     | `docs/project/01-product/SUCCESS-METRICS.md`     | Not Started | GitHub           |
| Assumptions         | `docs/project/01-product/ASSUMPTIONS.md`         | Not Started | GitHub           |
| Constraints         | `docs/project/01-product/CONSTRAINTS.md`         | Not Started | GitHub           |
| Risks               | `docs/project/01-product/RISKS.md`               | Not Started | GitHub/Jira      |

## Requirements Deliverables

| Deliverable                         | Recommended Path                                              | Status      | Canonical System |
| ----------------------------------- | ------------------------------------------------------------- | ----------- | ---------------- |
| Software Requirements Specification | `docs/project/02-requirements/SRS.md`                         | Not Started | GitHub           |
| Functional requirements             | `docs/project/02-requirements/FUNCTIONAL-REQUIREMENTS.md`     | Not Started | GitHub           |
| Non-functional requirements         | `docs/project/02-requirements/NON-FUNCTIONAL-REQUIREMENTS.md` | Not Started | GitHub           |
| Acceptance criteria                 | `docs/project/02-requirements/ACCEPTANCE-CRITERIA.md`         | Not Started | GitHub           |
| Traceability matrix                 | `docs/project/02-requirements/TRACEABILITY-MATRIX.md`         | Not Started | GitHub           |
| Out of scope                        | `docs/project/02-requirements/OUT-OF-SCOPE.md`                | Not Started | GitHub           |
| Glossary                            | `docs/project/02-requirements/GLOSSARY.md`                    | Not Started | GitHub           |

## Domain Deliverables

| Deliverable         | Recommended Path                                | Status      | Canonical System |
| ------------------- | ----------------------------------------------- | ----------- | ---------------- |
| Domain model        | `docs/project/03-domain/DOMAIN-MODEL.md`        | Not Started | GitHub           |
| Ubiquitous language | `docs/project/03-domain/UBIQUITOUS-LANGUAGE.md` | Not Started | GitHub           |
| Bounded contexts    | `docs/project/03-domain/BOUNDED-CONTEXTS.md`    | Not Started | GitHub           |
| Domain events       | `docs/project/03-domain/DOMAIN-EVENTS.md`       | Not Started | GitHub           |
| State machines      | `docs/project/03-domain/STATE-MACHINES.md`      | Not Started | GitHub           |

## Architecture Deliverables

| Deliverable                | Recommended Path                                             | Status      | Canonical System |
| -------------------------- | ------------------------------------------------------------ | ----------- | ---------------- |
| Architecture overview      | `docs/project/04-architecture/ARCHITECTURE-OVERVIEW.md`      | Not Started | GitHub           |
| System context             | `docs/project/04-architecture/SYSTEM-CONTEXT.md`             | Not Started | GitHub           |
| Container view             | `docs/project/04-architecture/CONTAINER-VIEW.md`             | Not Started | GitHub           |
| Component view             | `docs/project/04-architecture/COMPONENT-VIEW.md`             | Not Started | GitHub           |
| Data architecture          | `docs/project/04-architecture/DATA-ARCHITECTURE.md`          | Not Started | GitHub           |
| Integration architecture   | `docs/project/04-architecture/INTEGRATION-ARCHITECTURE.md`   | Not Started | GitHub           |
| Security architecture      | `docs/project/04-architecture/SECURITY-ARCHITECTURE.md`      | Not Started | GitHub           |
| Observability architecture | `docs/project/04-architecture/OBSERVABILITY-ARCHITECTURE.md` | Not Started | GitHub           |
| Deployment architecture    | `docs/project/04-architecture/DEPLOYMENT-ARCHITECTURE.md`    | Not Started | GitHub           |

## Delivery Deliverables

| Deliverable              | Recommended Path                                       | Status      | Canonical System  |
| ------------------------ | ------------------------------------------------------ | ----------- | ----------------- |
| Delivery operating model | `docs/project/05-delivery/DELIVERY-OPERATING-MODEL.md` | Draft       | GitHub            |
| Jira workflow            | `docs/project/05-delivery/JIRA-WORKFLOW.md`            | Not Started | GitHub/Confluence |
| Issue taxonomy           | `docs/project/05-delivery/ISSUE-TAXONOMY.md`           | Not Started | GitHub/Jira       |
| Branching strategy       | `docs/project/05-delivery/BRANCHING-STRATEGY.md`       | Not Started | GitHub            |
| Commit standard          | `docs/project/05-delivery/COMMIT-STANDARD.md`          | Not Started | GitHub            |
| Pull request standard    | `docs/project/05-delivery/PULL-REQUEST-STANDARD.md`    | Not Started | GitHub            |
| Release strategy         | `docs/project/05-delivery/RELEASE-STRATEGY.md`         | Not Started | GitHub            |
| Change control           | `docs/project/05-delivery/CHANGE-CONTROL.md`           | Not Started | GitHub            |
| Work packet standard     | `docs/project/05-delivery/WORK-PACKET-STANDARD.md`     | Not Started | GitHub            |

## Quality Deliverables

| Deliverable           | Recommended Path                                   | Status      | Canonical System |
| --------------------- | -------------------------------------------------- | ----------- | ---------------- |
| Quality strategy      | `docs/project/06-quality/QUALITY-STRATEGY.md`      | Not Started | GitHub           |
| Testing strategy      | `docs/project/06-quality/TESTING-STRATEGY.md`      | Not Started | GitHub           |
| BDD strategy          | `docs/project/06-quality/BDD-STRATEGY.md`          | Not Started | GitHub           |
| TDD strategy          | `docs/project/06-quality/TDD-STRATEGY.md`          | Not Started | GitHub           |
| Verification strategy | `docs/project/06-quality/VERIFICATION-STRATEGY.md` | Not Started | GitHub           |
| CI/CD strategy        | `docs/project/06-quality/CI-CD-STRATEGY.md`        | Not Started | GitHub           |
| Repo contract         | `docs/project/06-quality/REPO-CONTRACT.md`         | Not Started | GitHub           |
| Quality gates         | `docs/project/06-quality/QUALITY-GATES.md`         | Not Started | GitHub           |

## Security and Records Deliverables

| Deliverable           | Recommended Path                                    | Status      | Canonical System |
| --------------------- | --------------------------------------------------- | ----------- | ---------------- |
| Security strategy     | `docs/project/07-security/SECURITY-STRATEGY.md`     | Not Started | GitHub           |
| Threat model          | `docs/project/07-security/THREAT-MODEL.md`          | Not Started | GitHub           |
| Secret management     | `docs/project/07-security/SECRET-MANAGEMENT.md`     | Not Started | GitHub           |
| Supply-chain security | `docs/project/07-security/SUPPLY-CHAIN-SECURITY.md` | Not Started | GitHub           |
| Access control        | `docs/project/07-security/ACCESS-CONTROL.md`        | Not Started | GitHub           |
| Incident response     | `docs/project/07-security/INCIDENT-RESPONSE.md`     | Not Started | GitHub           |
| Records management    | `docs/project/08-records/RECORDS-MANAGEMENT.md`     | Not Started | GitHub/Nextcloud |
| Document control      | `docs/project/08-records/DOCUMENT-CONTROL.md`       | Draft       | GitHub/Nextcloud |
| Retention policy      | `docs/project/08-records/RETENTION-POLICY.md`       | Not Started | GitHub/Nextcloud |
| DMS integration       | `docs/project/08-records/DMS-INTEGRATION.md`        | Not Started | GitHub/Nextcloud |
| Audit trail           | `docs/project/08-records/AUDIT-TRAIL.md`            | Not Started | GitHub/Nextcloud |

## AI and Handoff Deliverables

| Deliverable             | Path                                 | Status      | Canonical System |
| ----------------------- | ------------------------------------ | ----------- | ---------------- |
| Current state           | `docs/ai/CURRENT_STATE.md`           | Draft       | GitHub           |
| Handoff                 | `docs/ai/HANDOFF.md`                 | Draft       | GitHub           |
| Next steps              | `docs/ai/NEXT_STEPS.md`              | Draft       | GitHub           |
| Open questions          | `docs/ai/OPEN_QUESTIONS.md`          | Draft       | GitHub           |
| External systems status | `docs/ai/EXTERNAL-SYSTEMS-STATUS.md` | Draft       | GitHub           |
| Bootstrap prompt        | `docs/ai/BOOTSTRAP_PROMPT.md`        | Not Started | GitHub           |
| Decisions               | `docs/ai/DECISIONS.md`               | Not Started | GitHub           |
| Working agreements      | `docs/ai/WORKING-AGREEMENTS.md`      | Not Started | GitHub           |
| Context map             | `docs/ai/CONTEXT-MAP.md`             | Not Started | GitHub           |

## Gate Before Slice 3

Slice 3 may proceed only after:

* this register exists;
* external system operating model exists;
* delivery operating model exists;
* document control model exists;
* ADR for the external system is accepted;
* Jira/Confluence/Nextcloud links are recorded outside the public repo;
* traceability loop has been tested at least once.
