#!/usr/bin/env python3
"""Validate RELEASE-001 AIRS Platform 1.0 productization deliverables."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DISCLAIMER = "本验证仅用于 AIRS 工程质量检查，不构成投资建议。"

CLI_FILES = [
    "cli/__init__.py",
    "cli/airs.py",
    "cli/commands/__init__.py",
    "cli/commands/init.py",
    "cli/commands/run.py",
    "cli/commands/demo.py",
    "cli/commands/validate.py",
    "cli/README.md",
]
API_FILES = [
    "api/__init__.py",
    "api/server.py",
    "api/routes/__init__.py",
    "api/routes/research.py",
    "api/routes/workspace.py",
    "api/routes/memory.py",
    "api/routes/health.py",
    "api/README.md",
]
WEB_FILES = [
    "web/index.html",
    "web/new-research.html",
    "web/history.html",
    "web/workspace.html",
    "web/knowledge-graph.html",
    "web/memory.html",
    "web/settings.html",
    "web/static/css/style.css",
    "web/static/js/app.js",
    "web/README.md",
]
DOCKER_FILES = ["docker/Dockerfile", "docker/docker-compose.yml", "docker/README.md"]
CONFIG_FILES = ["config/airs.yaml", "config/airs.stable.yaml", "config/README.md", ".env.example"]
DEMO_FILES = ["demo/nvidia.json", "demo/tsmc.json", "demo/concord-medical.json", "demo/run_demo.py"]
DOC_FILES = [
    "docs/product/overview.md",
    "docs/product/release-notes.md",
    "docs/api/reference.md",
    "docs/api/quickstart.md",
    "docs/deployment/install.md",
    "docs/deployment/docker.md",
    "docs/deployment/quickstart.md",
    "docs/adr/ADR-0015-platform-productization.md",
    "docs/production/RELEASE_001_COMPLETION_REPORT.md",
    "docs/review/RELEASE_001_SELF_REVIEW.md",
]
FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "应买入", "应卖出", "自动交易指令"]


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def validate_files(files: list[str], failures: list[str], *, require_disclaimer: bool = True) -> None:
    for rel in files:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
        if not path.exists():
            continue
        text = read(rel)
        check(len(text.strip()) > 20, f"{rel} has content", f"{rel} content too thin", failures)
        if require_disclaimer and rel.endswith((".md", ".py", ".html", ".yaml", ".example", ".json")):
            check("不构成投资建议" in text, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
        for word in FORBIDDEN:
            check(word not in text, f"{rel} avoids forbidden phrase {word}", f"{rel} contains forbidden phrase {word}", failures)


def validate_cli(failures: list[str]) -> None:
    validate_files(CLI_FILES, failures)
    completed = subprocess.run([sys.executable, "cli/airs.py", "init", "--output", ".airs/validate-productization.yaml", "--force"], cwd=ROOT, text=True, capture_output=True, check=False)
    check(completed.returncode == 0, "CLI init runs", f"CLI init failed: {completed.stderr or completed.stdout}", failures)
    completed = subprocess.run([sys.executable, "cli/airs.py", "demo", "nvidia", "--output-dir", "demo/output/validate-productization"], cwd=ROOT, text=True, capture_output=True, check=False)
    check(completed.returncode == 0, "CLI demo nvidia runs", f"CLI demo failed: {completed.stderr or completed.stdout}", failures)


def validate_api(failures: list[str]) -> None:
    validate_files(API_FILES, failures)
    spec = importlib.util.spec_from_file_location("airs_api_server", ROOT / "api" / "server.py")
    check(spec is not None and spec.loader is not None, "API server import spec loads", "API server import spec failed", failures)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.path.insert(0, str(ROOT))
        spec.loader.exec_module(module)
        check(hasattr(module, "AIRSRequestHandler"), "API server exposes AIRSRequestHandler", "API server missing AIRSRequestHandler", failures)


def validate_web(failures: list[str]) -> None:
    validate_files(WEB_FILES, failures)
    app_js = read("web/static/js/app.js")
    for endpoint in ["/health", "/research", "/workspace", "/memory"]:
        check(endpoint in app_js, f"web app references {endpoint}", f"web app missing {endpoint}", failures)


def validate_docker_config_demo_docs(failures: list[str]) -> None:
    validate_files(DOCKER_FILES + CONFIG_FILES + DEMO_FILES + DOC_FILES, failures)
    compose = read("docker/docker-compose.yml")
    check("8765:8765" in compose, "Docker maps API 8765", "Docker missing API port mapping", failures)
    check("8080:8080" in compose, "Docker maps Web 8080", "Docker missing Web port mapping", failures)
    for rel in ["demo/nvidia.json", "demo/tsmc.json", "demo/concord-medical.json"]:
        try:
            data = json.loads(read(rel))
            check("research_question" in data, f"{rel} has research_question", f"{rel} missing research_question", failures)
        except json.JSONDecodeError as exc:
            check(False, f"{rel} valid JSON", f"{rel} invalid JSON: {exc}", failures)


def validate_governance(failures: list[str]) -> None:
    readme = read("README.md")
    changelog = read("CHANGELOG.md")
    check("AIRS Platform 1.0" in readme and "cli/airs.py" in readme, "README documents platform entrypoints", "README missing platform entrypoints", failures)
    check("RELEASE-001" in changelog and "Platform 1.0 Productization" in changelog, "CHANGELOG documents RELEASE-001", "CHANGELOG missing RELEASE-001", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS RELEASE-001 Productization Validation")
    print("==========================================")
    validate_cli(failures)
    validate_api(failures)
    validate_web(failures)
    validate_docker_config_demo_docs(failures)
    validate_governance(failures)
    print("==========================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    print(f"免责声明：{DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
