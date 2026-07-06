#!/usr/bin/env python3
"""Check required gate output sections for the solution-design workflow."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


GATE_REQUIREMENTS = {
    0: {
        "file": "outputs/design_input.md",
        "sections": [
            ("项目背景", "Project background"),
            ("方案成熟度", "Solution maturity"),
            ("工艺目标与成功标准", "Process goals and success criteria"),
            ("工艺步骤表", "Process step table"),
            ("外部机构与系统接口清单", "External mechanisms and system interfaces"),
            ("待补资料与追问", "Missing inputs"),
            ("Gate 0 准入结论", "Gate 0 readiness verdict"),
            ("Action Packages", "Action Package"),
        ],
    },
    1: {
        "file": "outputs/design_input.md",
        "sections": [
            ("当前人工/现有流程", "Current workflow"),
            ("操作主体与对象清单", "Actors and objects"),
            ("已知参数与缺失参数", "Known and missing parameters"),
            ("假设锁定与变更记录", "Assumption register"),
            ("事实、假设与决策", "Facts, assumptions, and decisions"),
        ],
    },
    2: {
        "file": "outputs/concept_options.md",
        "sections": [
            ("输入摘要", "Input Summary"),
            ("方案成熟度", "Solution maturity"),
            ("方案", "Option"),
            ("总流程图", "Overall flowchart"),
            ("泳道流程图", "Swimlane flowchart"),
            ("异常流程图", "Exception flowchart"),
            ("数据流图", "Data flow"),
            ("工艺步骤评分表", "Step scoring"),
            ("方案级评分矩阵", "Solution scoring"),
            ("二维 HTML 三视图说明", "2D HTML three-view"),
            ("评审会议输出包", "Review package"),
            ("推荐方向", "Recommended Direction"),
            ("Action Packages", "Action Package"),
        ],
    },
    3: {
        "file": "outputs/risk_review.md",
        "sections": [
            ("范围", "Scope"),
            ("步骤级风险表", "Step risk table", "Risk Table"),
            ("最高优先级风险", "Highest Priority Risks"),
            ("风险评分说明", "Risk scoring"),
            ("验证链接", "Verification Links"),
            ("Action Packages", "Action Package"),
        ],
    },
    5: {
        "file": "outputs/verification_plan.md",
        "sections": [
            ("范围", "Scope"),
            ("验证矩阵", "Verification Matrix"),
            ("步骤级验证覆盖", "Step verification coverage"),
            ("外部机构与接口验证", "External mechanism verification"),
            ("数据记录模板", "Data Recording Template"),
            ("Gate 5 准入结论", "Gate 5 readiness verdict"),
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
