"""Company research learning example."""
from __future__ import annotations

from .common import run_case


def run() -> dict:
    return run_case("COMPANY", "公司研究", "report", "evidence_gap")


if __name__ == "__main__":
    print(run())

