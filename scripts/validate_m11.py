#!/usr/bin/env python3
"""Milestone wrapper validation for M11 memory context currently available in AIRS."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def main() -> int:
    failures: list[str] = []
    print("AIRS M11 Memory Context Validation")
    print("==================================")
    required = [
        "docs/runtime/memory-manager.md",
        "runtime/memory_manager.py",
        "workspace/memory.py",
        "docs/production/FEATURE_012_COMPLETION_REPORT.md",
    ]
    for rel in required:
        check((ROOT / rel).exists(), f"{rel} exists", f"missing {rel}", failures)
    runtime_doc = (ROOT / "docs/runtime/memory-manager.md").read_text(encoding="utf-8")
    completion = (ROOT / "docs/production/FEATURE_012_COMPLETION_REPORT.md").read_text(encoding="utf-8")
    check("Memory" in runtime_doc and "Evidence Engine" in runtime_doc, "runtime memory boundary documented", "runtime memory boundary missing", failures)
    check("docs/memory/" in completion and "未发现" in completion, "FEATURE-012 records missing docs/memory context", "FEATURE-012 missing memory gap note", failures)
    check("不构成投资建议" in completion, "FEATURE-012 report has disclaimer", "FEATURE-012 report missing disclaimer", failures)
    print("==================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
