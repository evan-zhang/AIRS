"""airs run command."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from apps.equity_research import run_equity_research
from apps.equity_research.report_exporter import EquityResearchReportExporter


DISCLAIMER = "AIRS 研究任务仅用于研究流程编排和质量控制，不构成投资建议。"


def _load_input(args: argparse.Namespace) -> str | dict[str, object]:
    if args.input_json:
        return json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    return {
        "symbol": args.symbol,
        "market": args.market,
        "research_question": args.query,
        "time_range": args.time_range,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    payload = _load_input(args)
    result = run_equity_research(payload)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.markdown:
        EquityResearchReportExporter().write_markdown(result["report"], args.markdown)
    return {
        "exit_code": 0,
        "request_id": result["request"]["request_id"],
        "company": result["company"]["company_name"],
        "output": args.output,
        "markdown": args.markdown,
        "message": "\n".join(
            [
                f"研究任务完成：{result['company']['company_name']}",
                f"Request ID: {result['request']['request_id']}",
                f"JSON: {args.output or '未写入文件'}",
                f"Markdown: {args.markdown or '未写入文件'}",
                f"免责声明：{DISCLAIMER}",
            ]
        ),
    }


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("run", help="运行股票研究任务。")
    parser.add_argument("query", nargs="?", default="分析 NVIDIA 的财务、估值、供应链和风险", help="研究问题。")
    parser.add_argument("--symbol", default="NVDA", help="股票代码。")
    parser.add_argument("--market", default="US", help="市场代码。")
    parser.add_argument("--time-range", default="latest", help="研究时间范围。")
    parser.add_argument("--input-json", help="从 JSON 文件读取完整研究请求。")
    parser.add_argument("--output", help="写入 JSON 结果路径。")
    parser.add_argument("--markdown", help="写入 Markdown 报告路径。")
    parser.set_defaults(func=run)

