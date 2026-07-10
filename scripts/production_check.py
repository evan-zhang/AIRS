#!/usr/bin/env python3
"""Run all AIRS production validation scripts and summarize results."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

VALIDATORS = [
    "scripts/validate_m1.py",
    "scripts/validate_m2.py",
    "scripts/validate_evidence.py",
    "scripts/validate_prompt.py",
    "scripts/validate_skill.py",
    "scripts/validate_score.py",
    "scripts/validate_evaluation.py",
    "scripts/validate_benchmark.py",
    "scripts/validate_examples.py",
    "scripts/validate_release.py",
]


def run_validator(rel: str) -> tuple[bool, str]:
    path = ROOT / rel
    if not path.exists():
        return False, f"missing validator: {rel}"
    completed = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = completed.stdout.strip()
    return completed.returncode == 0, output


def main() -> int:
    print("AIRS Production Check")
    print("=====================")
    results: list[tuple[str, bool]] = []

    for rel in VALIDATORS:
        print(f"\n--- Running {rel} ---")
        passed, output = run_validator(rel)
        print(output)
        results.append((rel, passed))
        print(f"--- {rel}: {'PASS' if passed else 'FAIL'} ---")

    print("\n=====================")
    print("Summary")
    failed = [rel for rel, passed in results if not passed]
    for rel, passed in results:
        print(f"{'PASS' if passed else 'FAIL'}: {rel}")

    if failed:
        print("FINAL RESULT: FAIL")
        for rel in failed:
            print(f"- {rel}")
        return 1

    print("FINAL RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
