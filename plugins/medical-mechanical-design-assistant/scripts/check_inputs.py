#!/usr/bin/env python3
"""Check medical mechanical design project input completeness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


LEVEL_REQUIREMENTS = {
    1: [
        ("inputs/photos", "directory_or_file"),
        ("inputs/meeting_notes", "directory_or_file"),
        ("inputs/target_action.md", "file"),
        ("inputs/dimensions.md", "file"),
    ],
    2: [
        ("inputs/photos", "directory_or_file"),
        ("inputs/videos", "directory_or_file"),
        ("inputs/dimensions.md", "file"),
        ("inputs/manuals", "directory_or_file"),
        ("inputs/constraints.md", "file"),
    ],
    3: [
        ("inputs/photos", "directory_or_file"),
        ("inputs/videos", "directory_or_file"),
        ("inputs/dimensions.md", "file"),
        ("inputs/manuals", "directory_or_file"),
        ("inputs/constraints.md", "file"),
        ("inputs/cad", "directory_or_file"),
        ("inputs/tolerances.md", "file"),
        ("inputs/materials.md", "file"),
        ("inputs/manufacturing_constraints.md", "file"),
        ("inputs/verification_standards.md", "file"),
    ],
}

COMMON_RECOMMENDED = [
    "inputs/project_brief.md",
    "inputs/equipment_list.md",
    "inputs/material_list.md",
    "inputs/workflow_steps.md",
    "inputs/cad_index.md",
    "inputs/video_index.md",
    "inputs/audio_index.md",
    "inputs/source_log.md",
    "inputs/safety_and_risk_boundaries.md",
    "inputs/existing_issues.md",
    "inputs/interfaces.md",
]


def has_content(path: Path, mode: str) -> bool:
    if mode == "file":
        return path.is_file() and path.stat().st_size > 0
    if path.is_file():
        return path.stat().st_size > 0
    if path.is_dir():
        return any(child.is_file() and child.stat().st_size > 0 for child in path.rglob("*"))
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Project folder to check")
    parser.add_argument("--level", type=int, choices=(1, 2, 3), default=1)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    root = args.project.resolve()
    missing = []
    present = []

    for rel_path, mode in LEVEL_REQUIREMENTS[args.level]:
        path = root / rel_path
        if has_content(path, mode):
            present.append(rel_path)
        else:
            missing.append(rel_path)

    recommended_missing = [
        rel_path for rel_path in COMMON_RECOMMENDED if not has_content(root / rel_path, "file")
    ]

    result = {
        "project": str(root),
        "level": args.level,
        "pass": not missing,
        "present": present,
        "missing_required": missing,
        "missing_recommended": recommended_missing,
    }

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        status = "PASS" if result["pass"] else "FAIL"
        print(f"Input completeness level {args.level}: {status}")
        if missing:
            print("Missing required inputs:")
            for item in missing:
                print(f"- {item}")
        if recommended_missing:
            print("Missing recommended inputs:")
            for item in recommended_missing:
                print(f"- {item}")

    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
