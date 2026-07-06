---
name: verification-plan-builder
description: Build measurable verification plans for medical mechanical design concepts, lab equipment fixture changes, analyzer/pipette tooling, embodied intelligence mechanisms, and non-standard medical-related mechanical modifications. Use when Codex needs to turn requirements, concepts, risks, or test notes into verification items with methods, tools, sample sizes, pass criteria, records, and gate status.
---

# Verification Plan Builder

Use this skill to turn design inputs, selected concepts, and risk items into measurable verification work. Verification plans must be executable by an engineer or technician.

Default to Chinese outputs unless the user explicitly requests another language.

## Required Inputs

Prefer these files when present:

- `outputs/design_input.md`
- `outputs/concept_options.md`
- `outputs/risk_review.md`
- `inputs/dimensions.md`
- `inputs/safety_and_risk_boundaries.md`
- `inputs/source_log.md`
- `inputs/cad_index.md`
- `inputs/video_index.md`
- `inputs/audio_index.md`

## Verification Harness

Every verification item must include:

- Requirement or risk link
- What to measure or observe
- Method and setup
- Required tool or fixture
- Sample quantity or repetition count
- Data to record
- Acceptance criteria
- Failure handling
- Owner
- Status
- Whether an external-assist mechanism is required and how that mechanism is verified

Avoid vague criteria such as "works well" or "stable enough". Convert them into dimensions, force, travel, time, error, repeat count, visual defect criteria, contamination criterion, or operator workflow criterion.

When a criterion depends on CAD, video, audio, or vendor documents, include the evidence source and whether it is measured, vendor-published, video-observed, AI-inferred, or pending confirmation.

## Output

Create or update `outputs/verification_plan.md`:

```markdown
# Verification Plan

## Scope
## Assumptions
## Verification Matrix
## Test Setups
## Required Tools And Fixtures
## Data Recording Template
## Gate 5 Readiness Verdict
## Action Packages
```

Verification matrix columns should include: ID, requirement/risk link, method, setup, tool, repetitions, data record, acceptance criteria, owner, status.

## Gate 5 Pass Criteria

Gate 5 passes only when all high-priority risks have a verification item and every verification item has a measurable acceptance criterion.

## Deterministic Checks

Run `python scripts/check_gate.py <project-folder> --gate 5` to check required output sections and risk-to-verification coverage where files are available.
