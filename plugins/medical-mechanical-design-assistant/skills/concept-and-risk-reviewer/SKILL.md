---
name: concept-and-risk-reviewer
description: Generate multiple constrained mechanical concept options and preliminary risk/FMEA review for medical mechanical design, embodied intelligence mechanisms, lab automation, analyzer accessories, pipette fixtures, non-standard jigs, and equipment modifications. Use when Codex needs concept comparison, failure modes, safety concerns, contamination/sample integrity checks, or early design critique before CAD.
---

# Concept And Risk Reviewer

Use this skill after design inputs are organized. Generate multiple options, then challenge them against medical mechanical constraints. Do not present any option as final or verified.

Default to Chinese outputs unless the user explicitly requests another language.

## Required Inputs

Prefer `outputs/design_input.md`. If absent, inspect available `inputs/` files and clearly label any assumptions.

If equipment model numbers, CAD files, videos, or audio are present, verify that they have been indexed in `inputs/source_log.md`, `inputs/cad_index.md`, `inputs/video_index.md`, or `inputs/audio_index.md`. Do not treat unconfirmed web search results, native CAD files, or video observations as measured facts.

## Concept Harness

Every concept option must include:

- Structure principle
- Motion/action path
- Installation and positioning method
- Interface with original equipment
- Consumable/sample interaction
- Expected effect on original equipment performance
- External-assist mechanisms needed beyond the robot body, such as clamps, rotary cap openers, door openers, nests, guides, pipetting/dosing modules, filtration modules, conveyors, or tool changers
- Manufacturing method
- Assembly method
- Cleaning and maintenance method
- Likely failure modes
- Verification method
- Key unknowns

## Risk Harness

Check at least these risk families:

- Contamination and cleanability
- Sample loss, carryover, or result interference
- Positioning error and tolerance stack-up
- Clamping, slipping, loosening, or wear
- Overload, jamming, pinch, collision, or fatigue
- Misuse, operator confusion, and accessibility
- Consumable compatibility
- Cleaning/disinfection material compatibility
- Power loss or emergency stop state
- Maintenance and replacement errors
- Original equipment warranty, calibration, or service impact

## Output

Create or update `outputs/concept_options.md`:

```markdown
# Concept Options

## Input Summary
## Option 1: <name>
## Option 2: <name>
## Option 3: <name>
## Comparison Matrix
## External Assist Mechanism List
## Recommended Direction
## Rejected Ideas
## Assumptions
## Open Questions
## Action Packages
```

Create or update `outputs/risk_review.md`:

```markdown
# Preliminary Risk Review

## Scope
## Risk Table
## Highest Priority Risks
## Verification Links
## Residual Concerns
## Engineer Review Notes
## Action Packages
```

Risk table columns should include: hazard, cause, effect, detection, mitigation, verification item, owner, status.

## Decision Rule

Recommend the concept that best preserves sample integrity, equipment safety, reliability, manufacturability, maintainability, and verification clarity. If evidence is insufficient, recommend the next test or measurement instead of choosing.

For mobile dual-arm robot projects, explicitly separate:

- Tasks likely feasible with the robot body, arms, end effectors, and navigation.
- Tasks requiring external fixed fixtures or active mechanisms.
- Tasks that should remain manual until evidence supports automation.
