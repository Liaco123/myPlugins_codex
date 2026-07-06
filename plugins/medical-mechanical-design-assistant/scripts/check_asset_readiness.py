#!/usr/bin/env python3
"""Scan a medical mechanical project input package for file readiness."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


DIRECT_TEXT = {".md", ".txt", ".csv", ".json", ".yaml", ".yml"}
DOCUMENTS = {".pdf", ".docx", ".xlsx", ".xls", ".pptx"}
IMAGES = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}
VIDEOS = {".mp4", ".mov", ".avi", ".mkv", ".wmv", ".m4v"}
AUDIO = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".wma"}
CAD_PREFERRED = {".step", ".stp", ".stl"}
CAD_USEFUL_WITH_CONTEXT = {".dxf", ".dwg", ".obj", ".iges", ".igs", ".x_t", ".x_b"}
CAD_NEEDS_EXPORT = {
    ".sldprt",
    ".sldasm",
    ".prt",
    ".asm",
    ".catpart",
    ".catproduct",
    ".ipt",
    ".iam",
}

IGNORE_DIRS = {"outputs", ".git", ".codex-plugin", "__pycache__"}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def classify(path: Path) -> tuple[str, str]:
    suffix = path.suffix.lower()
    if suffix in DIRECT_TEXT:
        return "可直接读取", "文本/结构化资料"
    if suffix in DOCUMENTS:
        return "可处理但需提取", "建议保留原件，并提取关键尺寸、规格、流程或表格"
    if suffix in IMAGES:
        return "可视觉分析", "适合识别设备外观、接口和操作姿态；不能替代实测尺寸"
    if suffix in VIDEOS:
        return "需预处理", "建议转写、抽关键帧并记录步骤时间"
    if suffix in AUDIO:
        return "需预处理", "建议转写成会议纪要、需求、约束和决策"
    if suffix in CAD_PREFERRED:
        return "CAD优先格式", "可用于几何摘要；仍需单位、坐标方向和版本说明"
    if suffix in CAD_USEFUL_WITH_CONTEXT:
        return "CAD可参考", "需要单位、用途说明，必要时转 STEP"
    if suffix in CAD_NEEDS_EXPORT:
        return "需要转换", "请从原 CAD 软件导出 STEP/STP，并附 PDF 工程图或截图"
    return "未知或不推荐", "请说明来源、用途和打开方式；不要用于工程判断直到确认"


def should_skip(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Project folder to scan")
    args = parser.parse_args()

    root = args.project.resolve()
    if not root.exists():
        print(f"项目不存在: {root}")
        return 2

    files = [path for path in root.rglob("*") if path.is_file() and not should_skip(path.relative_to(root))]
    if not files:
        print("未发现输入文件。")
        return 1

    print("# 文件资料可处理性报告")
    print(f"项目: {root}")
    print()
    print("| 文件 | 分类 | 处理建议 |")
    print("| --- | --- | --- |")

    needs_action = 0
    for path in sorted(files):
        rel = path.relative_to(root)
        category, advice = classify(path)
        if category in {"需要转换", "需预处理", "未知或不推荐"}:
            needs_action += 1
        print(f"| {rel} | {category} | {advice} |")

    print()
    if needs_action:
        print(f"结论: 发现 {needs_action} 个需要转换、预处理或确认的文件。")
        return 1

    print("结论: 当前文件类型均可进入下一步资料整理。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
