"""Industry research learning example."""
from __future__ import annotations

from .common import run_case


def run() -> dict:
    return run_case("INDUSTRY", "行业研究", "methodology", "scope_drift")


if __name__ == "__main__":
    print(run())

