"""Supply chain learning example."""
from __future__ import annotations

from .common import run_case


def run() -> dict:
    return run_case("SUPPLY", "供应链研究", "investment_engine", "missing_chokepoint_evidence")


if __name__ == "__main__":
    print(run())

