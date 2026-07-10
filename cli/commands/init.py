"""airs init command."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DISCLAIMER = "AIRS 初始化仅创建本地研究配置，不构成投资建议。"


def run(args: argparse.Namespace) -> dict[str, object]:
    target = Path(args.output).expanduser()
    source = ROOT / "config" / "airs.yaml"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and not args.force:
        return {
            "exit_code": 0,
            "path": str(target),
            "message": f"配置已存在：{target}\n使用 --force 可覆盖。\n免责声明：{DISCLAIMER}",
        }
    shutil.copyfile(source, target)
    return {
        "exit_code": 0,
        "path": str(target),
        "message": f"AIRS 配置已初始化：{target}\n免责声明：{DISCLAIMER}",
    }


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("init", help="初始化 AIRS 配置。")
    parser.add_argument("--output", default=".airs/airs.yaml", help="配置输出路径，默认 .airs/airs.yaml。")
    parser.add_argument("--force", action="store_true", help="覆盖已有配置。")
    parser.set_defaults(func=run)

