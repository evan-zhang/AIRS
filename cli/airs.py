#!/usr/bin/env python3
"""AIRS Platform 1.0 command line entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

DISCLAIMER = "AIRS 仅用于投资研究流程编排、证据追溯和质量控制，不构成投资建议。"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="airs", description="AIRS Platform 1.0 CLI")
    parser.add_argument("--json", action="store_true", help="以 JSON 输出 CLI 元信息。")
    subparsers = parser.add_subparsers(dest="command", required=True)

    from cli.commands.demo import register as register_demo
    from cli.commands.init import register as register_init
    from cli.commands.run import register as register_run
    from cli.commands.validate import register as register_validate

    register_init(subparsers)
    register_run(subparsers)
    register_demo(subparsers)
    register_validate(subparsers)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = args.func(args)
    if getattr(args, "json", False):
        print(json.dumps({"result": result, "disclaimer": DISCLAIMER}, ensure_ascii=False, indent=2))
    elif isinstance(result, dict) and result.get("message"):
        print(result["message"])
    return int(result.get("exit_code", 0)) if isinstance(result, dict) else 0


if __name__ == "__main__":
    raise SystemExit(main())

