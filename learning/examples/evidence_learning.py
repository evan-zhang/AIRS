"""Evidence learning example."""
from __future__ import annotations

from .common import run_case


def run() -> dict:
    return run_case("EVIDENCE", "证据链研究", "evidence", "source_traceability_gap")


if __name__ == "__main__":
    print(run())

