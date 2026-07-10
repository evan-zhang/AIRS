"""airs demo command."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from apps.equity_research import run_equity_research
from apps.equity_research.report_exporter import EquityResearchReportExporter


ROOT = Path(__file__).resolve().parents[2]
DEMO_NAMES = {
    "nvidia": ROOT / "demo" / "nvidia.json",
    "tsmc": ROOT / "demo" / "tsmc.json",
    "concord-medical": ROOT / "demo" / "concord-medical.json",
}
DISCLAIMER = "AIRS Demo 仅用于展示研究流程、证据追溯和质量控制，不构成投资建议。"


def run(args: argparse.Namespace) -> dict[str, object]:
    demo_path = DEMO_NAMES[args.name]
    payload = json.loads(demo_path.read_text(encoding="utf-8"))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    result = run_equity_research(payload)
    json_path = output_dir / f"{args.name}-result.json"
    md_path = output_dir / f"{args.name}-report.md"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    EquityResearchReportExporter().write_markdown(result["report"], str(md_path))
    return {
        "exit_code": 0,
        "demo": args.name,
        "json": str(json_path),
        "markdown": str(md_path),
        "message": f"Demo 完成：{args.name}\nJSON: {json_path}\nMarkdown: {md_path}\n免责声明：{DISCLAIMER}",
    }


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("demo", help="运行 AIRS Demo。")
    parser.add_argument("name", choices=sorted(DEMO_NAMES), help="Demo 名称。")
    parser.add_argument("--output-dir", default="demo/output", help="输出目录。")
    parser.set_defaults(func=run)

