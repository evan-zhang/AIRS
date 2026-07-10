"""Committee and report learning example."""
from __future__ import annotations

from .common import run_case


def run() -> dict:
    return run_case("COMMITTEE", "Committee 与 Report 改进", "committee", "decision_record_gap")


if __name__ == "__main__":
    print(run())

