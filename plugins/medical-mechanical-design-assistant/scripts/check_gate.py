#!/usr/bin/env python3
"""Check required gate output sections for the design workflow."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


GATE_REQUIREMENTS = {
    0: {
        "file": "outputs/design_input.md",
        "sections": [
            ("Project background", "项目背景"),
            ("Target action or mechanical function", "目标动作", "流程确认"),
            ("Hard constraints and no-change boundaries", "硬约束", "硬约束和不可改边界"),
            ("Safety, contamination, and sample integrity boundaries", "安全、污染和样品完整性边界"),
            ("Open questions", "开放问题"),
            ("Gate 0 readiness verdict", "Gate 0 Readiness Verdict"),
            ("Action package", "Action Packages"),
        ],
    },
    1: {
        "file": "outputs/design_input.md",
        "sections": [
            ("Project background", "项目背景"),
            ("Equipment, consumables, and interfaces", "设备、耗材和接口"),
            ("Known dimensions and missing dimensions", "已知尺寸和缺失尺寸"),
            ("Assumptions", "假设"),
            ("Open questions", "开放问题"),
        ],
    },
    2: {
        "file": "outputs/concept_options.md",
        "sections": [
            ("Input Summary", "输入摘要"),
            ("Option", "方案"),
            ("Comparison Matrix", "对比矩阵"),
            ("Recommended Direction", "推荐方向"),
            ("Action Packages", "Action Package"),
        ],
    },
    3: {
        "file": "outputs/risk_review.md",
        "sections": [
            ("Scope", "范围"),
            ("Risk Table", "风险表"),
            ("Highest Priority Risks", "最高优先级风险"),
            ("Verification Links", "验证链接"),
            ("Action Packages", "Action Package"),
        ],
    },
    5: {
        "file": "outputs/verification_plan.md",
        "sections": [
            ("Scope", "范围"),
            ("Verification Matrix", "验证矩阵"),
            ("Required Tools And Fixtures", "所需工具和夹具"),
            ("Data Recording Template", "数据记录模板"),
            ("Gate 5 Readiness Verdict", "Gate 5 Readiness Verdict"),
            ("Action Packages", "Action Package"),
        ],
    },
}

ACTION_FIELDS = [
    ("Goal",),
    ("Input materials",),
    ("Execution steps",),
    ("Required files",),
    ("Required tools",),
    ("Deliverables",),
    ("Acceptance criteria",),
    ("Risks",),
    ("Owner",),
    ("Due date",),
    ("Status",),
]


def contains_heading_or_label(text: str, section: str) -> bool:
    escaped = re.escape(section)
    patterns = [
        rf"^#+\s+.*{escaped}.*$",
        rf"^\s*[-*]?\s*{escaped}\s*:",
    ]
    return any(re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE) for pattern in patterns)


def contains_any_heading_or_label(text: str, section: str | tuple[str, ...]) -> bool:
    aliases = section if isinstance(section, tuple) else (section,)
    return any(contains_heading_or_label(text, alias) for alias in aliases)


def section_name(section: str | tuple[str, ...]) -> str:
    if isinstance(section, tuple):
        return " / ".join(section)
    return section


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Project folder to check")
    parser.add_argument("--gate", type=int, choices=sorted(GATE_REQUIREMENTS), required=True)
    args = parser.parse_args()

    root = args.project.resolve()
    requirement = GATE_REQUIREMENTS[args.gate]
    output_file = root / requirement["file"]

    if not output_file.is_file():
        print(f"Gate {args.gate}: FAIL")
        print(f"Missing output file: {requirement['file']}")
        return 1

    text = output_file.read_text(encoding="utf-8")
    missing_sections = [
        section for section in requirement["sections"] if not contains_any_heading_or_label(text, section)
    ]
    missing_action_fields = [
        field for field in ACTION_FIELDS if "Action Package" in text and not contains_any_heading_or_label(text, field)
    ]

    if missing_sections or missing_action_fields:
        print(f"Gate {args.gate}: FAIL")
        for section in missing_sections:
            print(f"Missing section: {section_name(section)}")
        for field in missing_action_fields:
            print(f"Missing action package field: {section_name(field)}")
        return 1

    print(f"Gate {args.gate}: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
