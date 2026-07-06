#!/usr/bin/env python3
"""Scan a solution-design project input package for file readiness."""

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
        return "directly_readable", "Text or structured project data."
    if suffix in DOCUMENTS:
        return "extract_required", "Extract key process, dimension, table, and requirement content."
    if suffix in IMAGES:
        return "visual_reference", "Useful for equipment appearance, interface, layout, and operation posture; not a substitute for measured dimensions."
    if suffix in VIDEOS:
        return "preprocess_required", "Transcribe or annotate steps, timings, operator actions, objects, and risk moments."
    if suffix in AUDIO:
        return "preprocess_required", "Transcribe into requirements, constraints, decisions, open questions, and action items."
    if suffix in CAD_PREFERRED:
        return "cad_preferred", "Useful geometry evidence; still needs unit, coordinate direction, version, and simplification notes."
    if suffix in CAD_USEFUL_WITH_CONTEXT:
        return "cad_reference", "Needs unit and purpose notes; export STEP when needed."
    if suffix in CAD_NEEDS_EXPORT:
        return "conversion_required", "Export STEP/STP from the native CAD system and add PDF drawings or screenshots when possible."
    return "unknown_or_not_recommended", "Explain source, purpose, and how to open it before using it for solution decisions."


def should_skip(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Project folder to scan")
    args = parser.parse_args()

    root = args.project.resolve()
    if not root.exists():
        print(f"Project does not exist: {root}")
        return 2

    files = [path for path in root.rglob("*") if path.is_file() and not should_skip(path.relative_to(root))]
    if not files:
        print("No input files found.")
        return 1

    print("# File Readiness Report")
    print(f"Project: {root}")
    print()
    print("| File | Category | Processing advice |")
    print("| --- | --- | --- |")

    needs_action = 0
    action_categories = {"conversion_required", "preprocess_required", "unknown_or_not_recommended"}
    for path in sorted(files):
        rel = path.relative_to(root)
        category, advice = classify(path)
        if category in action_categories:
            needs_action += 1
        print(f"| {rel} | {category} | {advice} |")

    print()
    if needs_action:
        print(f"Conclusion: {needs_action} file(s) need conversion, preprocessing, or source confirmation.")
        return 1

    print("Conclusion: Current file types are ready for the next solution-input organization step.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
