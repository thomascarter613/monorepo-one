from __future__ import annotations

from pathlib import Path
from textwrap import dedent

TODAY = "2026-05-16"
PROJECT = "monorepo-one"

DOCS: dict[str, dict[str, object]] = {
    "docs/project/00-foundation/LICENSE-DECISION.md": {
        "title": "License Decision",
        "sections": [
            "Purpose",
            "Current Decision",
            "Options",
            "Risks",
            "Acceptance Criteria",
        ],
        "body": "No open-source license has been selected yet. Because the repository is public, this decision must be resolved deliberately before external reuse is encouraged.",
    },
    "docs/project/00-foundation/DELIVERY-GOVERNANCE.md": {
        "title": "Delivery Governance",
        "sections": [
            "Purpose",
            "Governance Principles",
            "Decision Rights",
            "Work Intake",
            "Review Requirements",
            "Escalation",
            "Acceptance Criteria",
        ],
        "body": "This document defines how delivery decisions are governed across GitHub, Jira, Confluence, and Nextcloud.",
    },
    "docs/project/00-foundation/DEFINITION-OF-DONE.md": {
        "title": "Definition of Done",
        "sections": [
            "Purpose",
            "General Definition of Done",
            "Documentation Definition of Done",
            "Code Definition of Done",
            "Verification Definition of Done",
            "Deferrals",
            "Acceptance Criteria",
        ],
        "body": "A work item is not done merely because files were written. Verification, reviewability, traceability, and documentation alignment are required.",
    },

    "docs/project/01-product/PRODUCT-VISION.md": {
        "title": "Product Vision",
        "sections": ["Purpose", "Vision Statement", "Target Users", "Value Proposition", "Success Indicators", "Open Questions"],
    },
    "docs/project/01-product/PRODUCT-CHARTER.md": {
        "title": "Product Charter",
        "sections": ["Purpose", "Background", "Problem", "Goals", "Non-Goals", "Scope", "Stakeholders", "Constraints", "Risks", "Milestones", "Acceptance Criteria"],
    },
    "docs/project/01-product/PROBLEM-STATEMENT.md": {
        "title": "Problem Statement",
        "sections": ["Purpose", "Problem", "Affected Users", "Current Alternatives", "Impact", "Success Criteria", "Open Questions"],
    },
    "docs/project/01-product/GOALS-AND-NON-GOALS.md": {
        "title": "Goals and Non-Goals",
        "sections": ["Purpose", "Goals", "Non-Goals", "Trade-offs", "Acceptance Criteria"],
    },
    "docs/project/01-product/STAKEHOLDERS.md": {
        "title": "Stakeholders",
        "sections": ["Purpose", "Stakeholder Groups", "Responsibilities", "Decision Rights", "Communication Needs", "Open Questions"],
    },
    "docs/project/01-product/SUCCESS-METRICS.md": {
        "title": "Success Metrics",
        "sections": ["Purpose", "Product Metrics", "Engineering Metrics", "Operational Metrics", "Quality Metrics", "Review Cadence"],
    },
    "docs/project/01-product/ASSUMPTIONS.md": {
        "title": "Assumptions",
        "sections": ["Purpose", "Product Assumptions", "Technical Assumptions", "Operational Assumptions", "Validation Plan"],
    },
    "docs/project/01-product/CONSTRAINTS.md": {
        "title": "Constraints",
        "sections": ["Purpose", "Technical Constraints", "Operational Constraints", "Cost Constraints", "Security Constraints", "Decision Impact"],
    },
    "docs/project/01-product/RISKS.md": {
        "title": "Risks",
        "sections": ["Purpose", "Risk Register", "Risk Ratings", "Mitigations", "Owners", "Review Cadence"],
    },

    "docs/project/02-requirements/SRS.md": {
        "title": "Software Requirements Specification",
        "sections": ["Purpose", "Scope", "Definitions", "Functional Requirements", "Non-Functional Requirements", "Constraints", "Acceptance Criteria", "Traceability"],
    },
    "docs/project/02-requirements/FUNCTIONAL-REQUIREMENTS.md": {
        "title": "Functional Requirements",
        "sections": ["Purpose", "Requirement Format", "Requirements", "Acceptance Criteria", "Traceability"],
    },
    "docs/project/02-requirements/NON-FUNCTIONAL-REQUIREMENTS.md": {
        "title": "Non-Functional Requirements",
        "sections": ["Purpose", "Reliability", "Security", "Performance", "Accessibility", "Observability", "Maintainability", "Portability", "Verification"],
    },
    "docs/project/02-requirements/ACCEPTANCE-CRITERIA.md": {
        "title": "Acceptance Criteria",
        "sections": ["Purpose", "Criteria Format", "Product Acceptance", "Engineering Acceptance", "Verification Acceptance"],
    },
    "docs/project/02-requirements/TRACEABILITY-MATRIX.md": {
        "title": "Traceability Matrix",
        "sections": ["Purpose", "Traceability Rules", "Matrix", "Verification", "Maintenance"],
    },
    "docs/project/02-requirements/OUT-OF-SCOPE.md": {
        "title": "Out of Scope",
        "sections": ["Purpose", "Explicitly Out of Scope", "Deferred", "Rejected", "Reconsideration Criteria"],
    },
    "docs/project/02-requirements/GLOSSARY.md": {
        "title": "Glossary",
        "sections": ["Purpose", "Terms", "Acronyms", "Domain Language", "Maintenance"],
    },

    "docs/project/03-domain/DOMAIN-MODEL.md": {
        "title": "Domain Model",
        "sections": ["Purpose", "Domain Overview", "Core Concepts", "Entities", "Value Objects", "Aggregates", "Services", "Rules", "Open Questions"],
    },
    "docs/project/03-domain/UBIQUITOUS-LANGUAGE.md": {
        "title": "Ubiquitous Language",
        "sections": ["Purpose", "Terms", "Definitions", "Forbidden/Ambiguous Terms", "Maintenance"],
    },
    "docs/project/03-domain/BOUNDED-CONTEXTS.md": {
        "title": "Bounded Contexts",
        "sections": ["Purpose", "Contexts", "Context Map", "Ownership", "Integration Points", "Open Questions"],
    },
    "docs/project/03-domain/DOMAIN-EVENTS.md": {
        "title": "Domain Events",
        "sections": ["Purpose", "Event Naming", "Events", "Producers", "Consumers", "Versioning", "Open Questions"],
    },
    "docs/project/03-domain/STATE-MACHINES.md": {
        "title": "State Machines",
        "sections": ["Purpose", "State Machine Inventory", "States", "Transitions", "Guards", "Side Effects", "Verification"],
    },

    "docs/project/04-architecture/ARCHITECTURE-OVERVIEW.md": {
        "title": "Architecture Overview",
        "sections": ["Purpose", "Architecture Goals", "System Shape", "Major Decisions", "Constraints", "Risks", "Verification"],
    },
    "docs/project/04-architecture/SYSTEM-CONTEXT.md": {
        "title": "System Context",
        "sections": ["Purpose", "Users", "External Systems", "Trust Boundaries", "Context Diagram", "Open Questions"],
    },
    "docs/project/04-architecture/CONTAINER-VIEW.md": {
        "title": "Container View",
        "sections": ["Purpose", "Containers", "Responsibilities", "Interactions", "Deployment Notes", "Open Questions"],
    },
    "docs/project/04-architecture/COMPONENT-VIEW.md": {
        "title": "Component View",
        "sections": ["Purpose", "Components", "Responsibilities", "Dependencies", "Boundaries", "Open Questions"],
    },
    "docs/project/04-architecture/DATA-ARCHITECTURE.md": {
        "title": "Data Architecture",
        "sections": ["Purpose", "Data Stores", "Data Ownership", "Data Classification", "Migrations", "Backups", "Open Questions"],
    },
    "docs/project/04-architecture/INTEGRATION-ARCHITECTURE.md": {
        "title": "Integration Architecture",
        "sections": ["Purpose", "Integration Points", "Protocols", "Contracts", "Failure Modes", "Open Questions"],
    },
    "docs/project/04-architecture/SECURITY-ARCHITECTURE.md": {
        "title": "Security Architecture",
        "sections": ["Purpose", "Trust Boundaries", "Authentication", "Authorization", "Secrets", "Threats", "Controls", "Verification"],
    },
    "docs/project/04-architecture/OBSERVABILITY-ARCHITECTURE.md": {
        "title": "Observability Architecture",
        "sections": ["Purpose", "Logs", "Metrics", "Traces", "Alerts", "Health Checks", "Open Questions"],
    },
    "docs/project/04-architecture/DEPLOYMENT-ARCHITECTURE.md": {
        "title": "Deployment Architecture",
        "sections": ["Purpose", "Environments", "Deployment Targets", "Release Flow", "Rollback", "Operations", "Open Questions"],
    },

    "docs/project/05-delivery/JIRA-WORKFLOW.md": {
        "title": "Jira Workflow",
        "sections": ["Purpose", "Current Workflow", "Intended Workflow", "Labels", "Known Limitations", "Future Hardening"],
    },
    "docs/project/05-delivery/ISSUE-TAXONOMY.md": {
        "title": "Issue Taxonomy",
        "sections": ["Purpose", "Issue Types", "Labels", "Components", "Versions", "Examples"],
    },
    "docs/project/05-delivery/BRANCHING-STRATEGY.md": {
        "title": "Branching Strategy",
        "sections": ["Purpose", "Main Branch", "Feature Branches", "Naming", "Protection", "Examples"],
    },
    "docs/project/05-delivery/COMMIT-STANDARD.md": {
        "title": "Commit Standard",
        "sections": ["Purpose", "Conventional Commits", "Scopes", "Footers", "Examples", "Validation"],
    },
    "docs/project/05-delivery/PULL-REQUEST-STANDARD.md": {
        "title": "Pull Request Standard",
        "sections": ["Purpose", "PR Title", "Description", "Review", "Verification", "Merge Strategy"],
    },
    "docs/project/05-delivery/RELEASE-STRATEGY.md": {
        "title": "Release Strategy",
        "sections": ["Purpose", "Versioning", "Release Notes", "Release Evidence", "Rollback", "Future Work"],
    },
    "docs/project/05-delivery/CHANGE-CONTROL.md": {
        "title": "Change Control",
        "sections": ["Purpose", "Change Classes", "Approval Expectations", "Emergency Changes", "Records", "Audit"],
    },
    "docs/project/05-delivery/WORK-PACKET-STANDARD.md": {
        "title": "Work Packet Standard",
        "sections": ["Purpose", "Work Packet Format", "Acceptance Criteria", "Verification", "Commit Point", "Examples"],
    },

    "docs/project/06-quality/QUALITY-STRATEGY.md": {
        "title": "Quality Strategy",
        "sections": ["Purpose", "Quality Goals", "Quality Gates", "Review", "Metrics", "Continuous Improvement"],
    },
    "docs/project/06-quality/TESTING-STRATEGY.md": {
        "title": "Testing Strategy",
        "sections": ["Purpose", "Test Pyramid", "Unit Tests", "Integration Tests", "Contract Tests", "E2E Tests", "Manual QA"],
    },
    "docs/project/06-quality/BDD-STRATEGY.md": {
        "title": "BDD Strategy",
        "sections": ["Purpose", "Behavior Specifications", "Scenarios", "Acceptance Criteria", "Traceability"],
    },
    "docs/project/06-quality/TDD-STRATEGY.md": {
        "title": "TDD Strategy",
        "sections": ["Purpose", "Red-Green-Refactor", "When to Use TDD", "Test Design", "Verification"],
    },
    "docs/project/06-quality/VERIFICATION-STRATEGY.md": {
        "title": "Verification Strategy",
        "sections": ["Purpose", "Local Verification", "CI Verification", "Manual Verification", "Failure Handling"],
    },
    "docs/project/06-quality/CI-CD-STRATEGY.md": {
        "title": "CI/CD Strategy",
        "sections": ["Purpose", "Pipeline Goals", "Checks", "Security", "Deployment", "Future Hardening"],
    },
    "docs/project/06-quality/REPO-CONTRACT.md": {
        "title": "Repo Contract",
        "sections": ["Purpose", "Required Files", "Required Directories", "Invariants", "Verification"],
    },
    "docs/project/06-quality/QUALITY-GATES.md": {
        "title": "Quality Gates",
        "sections": ["Purpose", "Gate Definitions", "Required Checks", "Deferrals", "Acceptance Criteria"],
    },

    "docs/project/07-security/SECURITY-STRATEGY.md": {
        "title": "Security Strategy",
        "sections": ["Purpose", "Security Principles", "Threats", "Controls", "Verification", "Future Work"],
    },
    "docs/project/07-security/THREAT-MODEL.md": {
        "title": "Threat Model",
        "sections": ["Purpose", "Assets", "Actors", "Trust Boundaries", "Threats", "Mitigations"],
    },
    "docs/project/07-security/SECRET-MANAGEMENT.md": {
        "title": "Secret Management",
        "sections": ["Purpose", "Secret Rules", "Storage", "Rotation", "Local Development", "Incident Handling"],
    },
    "docs/project/07-security/SUPPLY-CHAIN-SECURITY.md": {
        "title": "Supply Chain Security",
        "sections": ["Purpose", "Dependencies", "Lockfiles", "Scanning", "Provenance", "Policy"],
    },
    "docs/project/07-security/ACCESS-CONTROL.md": {
        "title": "Access Control",
        "sections": ["Purpose", "Systems", "Roles", "Least Privilege", "Review Cadence"],
    },
    "docs/project/07-security/INCIDENT-RESPONSE.md": {
        "title": "Incident Response",
        "sections": ["Purpose", "Incident Classes", "Response Flow", "Communication", "Postmortem", "Records"],
    },

    "docs/project/08-records/RECORDS-MANAGEMENT.md": {
        "title": "Records Management",
        "sections": ["Purpose", "Record Classes", "Systems", "Ownership", "Register", "Review"],
    },
    "docs/project/08-records/RETENTION-POLICY.md": {
        "title": "Retention Policy",
        "sections": ["Purpose", "Retention Classes", "Retention Rules", "Deletion/Supersession", "Future Hardening"],
    },
    "docs/project/08-records/DMS-INTEGRATION.md": {
        "title": "DMS Integration",
        "sections": ["Purpose", "Nextcloud Role", "Folder Structure", "Records Register", "Traceability", "Limitations"],
    },
    "docs/project/08-records/AUDIT-TRAIL.md": {
        "title": "Audit Trail",
        "sections": ["Purpose", "Audit Events", "Evidence Sources", "Retention", "Review"],
    },

    "docs/ai/README.md": {
        "title": "AI Context Index",
        "sections": ["Purpose", "Read Order", "Source-of-Truth Rules", "Safety Rules", "Current Files"],
    },
    "docs/ai/BOOTSTRAP_PROMPT.md": {
        "title": "Bootstrap Prompt",
        "sections": ["Purpose", "Instructions for Future AI Sessions", "Read Order", "Operating Constraints", "Current Gate"],
    },
    "docs/ai/DECISIONS.md": {
        "title": "AI-Readable Decisions",
        "sections": ["Purpose", "Decision Log", "ADR References", "Open Decisions"],
    },
    "docs/ai/WORKING-AGREEMENTS.md": {
        "title": "Working Agreements",
        "sections": ["Purpose", "Delivery Agreements", "Documentation Agreements", "Verification Agreements", "Handoff Agreements"],
    },
    "docs/ai/CONTEXT-MAP.md": {
        "title": "Context Map",
        "sections": ["Purpose", "Project Areas", "Canonical Files", "External Systems", "Read Order"],
    },
}

def slug(path: str) -> str:
    return Path(path).stem.lower().replace("_", "-")

def frontmatter(title: str) -> str:
    return dedent(f"""\
    ---
    title: {title}
    status: stubbed
    version: 0.1.0
    created: {TODAY}
    updated: {TODAY}
    project: {PROJECT}
    ---
    """)

def render(path: str, spec: dict[str, object]) -> str:
    title = str(spec["title"])
    sections = list(spec.get("sections", []))
    body = str(spec.get("body", f"This document is a planning stub for **{title}**. It exists to establish the required documentation baseline before deeper monorepo implementation proceeds."))

    parts = [frontmatter(title), f"# {title}\n", "## Status\n\nStubbed.\n", "## Purpose\n\n" + body + "\n"]

    for section in sections:
        if section == "Purpose":
            continue
        parts.append(f"## {section}\n\nTBD. This section must be completed before this document can move from `stubbed` to `draft` or `accepted`.\n")

    parts.append(
        "## Completion Criteria\n\n"
        "This document is complete when:\n\n"
        "- the section content is specific to Monorepo One;\n"
        "- assumptions and unknowns are explicit;\n"
        "- related Jira work items are referenced where appropriate;\n"
        "- related ADRs are referenced where appropriate;\n"
        "- verification or acceptance criteria are included where applicable;\n"
        "- any controlled-record export requirement is identified.\n"
    )

    return "\n".join(parts).rstrip() + "\n"

for file_path, spec in DOCS.items():
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if "status: stubbed" in existing or "status: draft" in existing or "status: accepted" in existing:
            continue
    path.write_text(render(file_path, spec), encoding="utf-8")

# Update the planning register so created docs are no longer marked Not Started.
register = Path("docs/project/00-foundation/PLANNING-DELIVERABLE-REGISTER.md")
if register.exists():
    text = register.read_text(encoding="utf-8")
    for file_path in DOCS:
        if file_path.startswith("docs/project/") or file_path.startswith("docs/ai/"):
            text = text.replace(f"`{file_path}` | Not Started", f"`{file_path}` | Stubbed")
    register.write_text(text, encoding="utf-8")

# Refresh AI state with this phase gate.
current_state = Path("docs/ai/CURRENT_STATE.md")
current_state.parent.mkdir(parents=True, exist_ok=True)
current_state.write_text(dedent(f"""\
---
title: Current State
status: draft
version: 0.1.0
created: {TODAY}
updated: {TODAY}
project: {PROJECT}
---

# Current State

## Project

Monorepo One

## Current Phase

Phase 0: planning, documentation, external delivery system, and governance foundation.

## Current Goal

Establish all planning and documentation deliverables that should exist before proceeding to Slice 3.

## External Systems

- GitHub repository exists.
- Jira `MONO` project exists.
- Confluence `Monorepo One Engineering` space exists.
- Nextcloud `Controlled Records` area exists.

Private external-system URLs should not be committed to the public GitHub repository.

## Current Work

Current branch should be:

```text
MONO-3/docs/planning-deliverable-baseline
````

## Completed Baseline

The repository now has stubs for:

* foundation docs;
* product docs;
* requirements docs;
* domain docs;
* architecture docs;
* delivery docs;
* quality docs;
* security docs;
* records docs;
* AI handoff docs.

## Gate Before Slice 3

Slice 3 remains blocked until:

* this planning baseline is committed;
* the planning deliverable register is accurate;
* the external operating model is committed;
* no private URLs are committed;
* Jira/Confluence are updated with the planning baseline PR;
* the PR is merged into `main`.

## Next Recommended Action

Open a PR for the planning deliverable baseline and reference `MONO-3`.
"""), encoding="utf-8")
