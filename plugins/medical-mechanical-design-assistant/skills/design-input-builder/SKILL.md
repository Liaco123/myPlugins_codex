---
name: design-input-builder
description: Build a structured design input package for early-stage medical mechanical design, embodied intelligence mechanisms, lab equipment fixture changes, pipette/assay/analyzer adaptations, or non-standard tooling. Use when Codex needs to organize project background, requirements, constraints, interfaces, photos/videos/manuals, dimensions, safety boundaries, open questions, and gate readiness before concept generation.
---

# Design Input Builder

Use this skill to convert raw project material into a traceable design input package. Treat AI as a drafting and checking assistant, not as the engineering approver.

Default to Chinese outputs unless the user explicitly requests another language.

## Workflow

1. Inspect the project folder and identify available inputs:
   - `inputs/project_brief.md`
   - `inputs/equipment_list.md`
   - `inputs/material_list.md`
   - `inputs/workflow_steps.md`
   - `inputs/photos/`
   - `inputs/videos/`
   - `inputs/manuals/`
   - `inputs/meeting_notes/`
   - `inputs/dimensions.md`
   - `inputs/cad_index.md`
   - `inputs/video_index.md`
   - `inputs/audio_index.md`
   - `inputs/source_log.md`
   - `inputs/safety_and_risk_boundaries.md`
   - `inputs/existing_issues.md`
   - `inputs/interfaces.md`
2. If the user has not prepared an input package, use `$project-intake-guide` first to request and classify materials.
3. Classify readiness level:
   - Level 1 concept exploration: photos, meeting notes, target action, rough dimensions.
   - Level 2 feasibility concept: photos, operation video, key dimensions, equipment/consumable specifications, constraint list.
   - Level 3 executable design: Level 2 plus CAD/STEP, tolerances, material requirements, manufacturing constraints, verification standards.
4. Create or update `outputs/design_input.md` with these sections:
   - Project background
   - Intended clinical/lab workflow context
   - Target action or mechanical function
   - User and operator interaction
   - Equipment, consumables, and interfaces
   - Known dimensions and missing dimensions
   - Hard constraints and no-change boundaries
   - Safety, contamination, and sample integrity boundaries
   - Robot platform and external-assist mechanism assumptions
   - Manufacturing, assembly, cleaning, and maintenance constraints
   - Assumptions
   - Source and evidence summary
   - Open questions
   - Gate 0 readiness verdict
   - Action package list
5. Separate facts, assumptions, and decisions. Never turn an assumption into a requirement without labeling it.
6. If inputs are insufficient for the requested level, produce a missing-input list instead of inventing details.
7. If CAD, video, audio, or vendor model numbers are supplied, state whether they are direct evidence, need preprocessing, need conversion, or need source confirmation.

## Gate 0 Pass Criteria

Gate 0 passes only when the project has enough evidence for the requested level and every missing item is either resolved or explicitly accepted as a risk by the engineer.

## Action Package Format

Every recommended next step must use this format:

```markdown
### Action Package: <task name>
- Goal:
- Input materials:
- Execution steps:
- Required files:
- Required tools:
- Deliverables:
- Acceptance criteria:
- Risks:
- Owner:
- Due date:
- Status:
```

## Deterministic Checks

Run `python scripts/check_inputs.py <project-folder> --level <1|2|3>` when a project folder exists. Use the script result to support, not replace, engineering judgment.
