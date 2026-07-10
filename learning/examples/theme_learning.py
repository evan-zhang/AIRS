"""Theme research learning example."""
from __future__ import annotations

from .common import run_case


def run() -> dict:
    return run_case("THEME", "主题研究", "prompt", "weak_counter_argument")


if __name__ == "__main__":
    print(run())

