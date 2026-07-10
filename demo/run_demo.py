#!/usr/bin/env python3
"""Run AIRS built-in demos."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from apps.equity_research import run_equity_research
from apps.equity_research.report_exporter import EquityResearchReportExporter


DEMOS = {
    "nvidia": ROOT / "demo" / "nvidia.json",
    "tsmc": ROOT / "demo" / "tsmc.json",
    "concord-medical": ROOT / "demo" / "concord-medical.json",
}
DISCLAIMER = "AIRS Demo 仅用于产品演示和研究质量控制，不构成投资建议。"


def run_demo(name: str, output_dir: Path) -> dict[str, str]:
    payload = json.loads(DEMOS[name].read_text(encoding="utf-8"))
    result = run_equity_research(payload)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{name}-result.json"
    md_path = output_dir / f"{name}-report.md"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    EquityResearchReportExporter().write_markdown(result["report"], str(md_path))
    return {"json": str(json_path), "markdown": str(md_path), "disclaimer": DISCLAIMER}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run AIRS demo cases.")
    parser.add_argument("name", choices=sorted(DEMOS))
    parser.add_argument("--output-dir", default="demo/output")
    args = parser.parse_args(argv)
    result = run_demo(args.name, Path(args.output_dir))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

