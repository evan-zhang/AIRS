"""airs validate command."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DISCLAIMER = "AIRS 验证仅用于工程质量检查，不构成投资建议。"


def run(args: argparse.Namespace) -> dict[str, object]:
    scripts = [ROOT / "scripts" / "validate_productization.py"]
    if args.all:
        scripts = sorted((ROOT / "scripts").glob("validate_*.py"))
    failures: list[str] = []
    for script in scripts:
        print(f"RUN {script.relative_to(ROOT)}")
        completed = subprocess.run([sys.executable, str(script)], cwd=ROOT, check=False)
        if completed.returncode != 0:
            failures.append(str(script.relative_to(ROOT)))
            if args.fail_fast:
                break
    status = "PASS" if not failures else "FAIL"
    return {
        "exit_code": 0 if not failures else 1,
        "status": status,
        "failures": failures,
        "message": f"验证结果：{status}\n失败脚本：{failures or '无'}\n免责声明：{DISCLAIMER}",
    }


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser = subparsers.add_parser("validate", help="运行 AIRS 验证。")
    parser.add_argument("--all", action="store_true", help="运行 scripts/ 下全部 validate_*.py。")
    parser.add_argument("--fail-fast", action="store_true", help="遇到首个失败即停止。")
    parser.set_defaults(func=run)

