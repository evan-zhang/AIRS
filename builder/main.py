#!/usr/bin/env python3
"""AIRS Builder main entrypoint.

Reads a YAML feature request and generates a complete Feature Package under
builder-output/<feature-slug>/.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - fallback is covered by integration use.
    yaml = None

from registry import all_artifacts


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "builder-output"
REQUIRED_FIELDS = [
    "feature_id",
    "feature_name",
    "feature_summary",
    "business_goal",
    "user_scenarios",
    "dependencies",
    "constraints",
    "expected_outputs",
    "risk_level",
]
RISK_LEVELS = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
DISCLAIMER = "本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug or "feature-package"


def minimal_yaml_load(text: str) -> dict[str, Any]:
    """Parse the simple YAML shape used by Builder request templates."""

    result: dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not raw_line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"')
            if value:
                result[key] = value
                current_key = None
            else:
                result[key] = []
                current_key = key
            continue
        if current_key and line.strip().startswith("- "):
            item = line.strip()[2:].strip().strip('"')
            result[current_key].append(item)
    return result


def load_request(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text)
    else:
        data = minimal_yaml_load(text)
    if not isinstance(data, dict):
        raise ValueError("Feature Request must be a YAML object.")
    return data


def validate_request(data: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_FIELDS if not data.get(field)]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    risk_level = str(data["risk_level"]).upper()
    if risk_level not in RISK_LEVELS:
        raise ValueError(f"risk_level must be one of {', '.join(sorted(RISK_LEVELS))}")
    if not isinstance(data["expected_outputs"], list) or not data["expected_outputs"]:
        raise ValueError("expected_outputs must be a non-empty list.")


def normalize(data: dict[str, Any]) -> dict[str, Any]:
    feature_name = str(data["feature_name"])
    slug = slugify(str(data.get("feature_slug") or feature_name))
    context = dict(data)
    context["feature_slug"] = slug
    context["package_path"] = f"builder-output/{slug}"
    context["risk_level"] = str(data["risk_level"]).upper()
    context["disclaimer"] = DISCLAIMER
    for key in ("user_scenarios", "dependencies", "constraints", "expected_outputs"):
        value = context.get(key, [])
        if isinstance(value, str):
            value = [value]
        context[key] = value
        context[f"{key}_markdown"] = "\n".join(f"- {item}" for item in value)
        context[f"{key}_json"] = json.dumps(value, ensure_ascii=False, indent=2)
    return context


def render_template(template_text: str, context: dict[str, Any]) -> str:
    rendered = template_text
    for key, value in context.items():
        if isinstance(value, (list, dict)):
            value = json.dumps(value, ensure_ascii=False, indent=2)
        rendered = rendered.replace("{{" + key + "}}", str(value))
    return rendered


def generate_package(context: dict[str, Any]) -> Path:
    package_dir = OUTPUT_ROOT / context["feature_slug"]
    package_dir.mkdir(parents=True, exist_ok=True)
    for artifact in all_artifacts():
        template_path = ROOT / artifact.template
        if not template_path.exists():
            raise FileNotFoundError(f"Missing template: {artifact.template}")
        output_path = package_dir / artifact.output_path(context["feature_slug"])
        output_path.parent.mkdir(parents=True, exist_ok=True)
        rendered = render_template(template_path.read_text(encoding="utf-8"), context)
        if artifact.is_json:
            json.loads(rendered)
        output_path.write_text(rendered, encoding="utf-8")
    return package_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate AIRS Feature Package from YAML request.")
    parser.add_argument("feature_request", help="Path to Feature Request YAML.")
    args = parser.parse_args(argv)

    try:
        request_path = Path(args.feature_request)
        if not request_path.is_absolute():
            request_path = ROOT / request_path
        data = load_request(request_path)
        validate_request(data)
        context = normalize(data)
        package_dir = generate_package(context)
    except Exception as exc:  # noqa: BLE001 - CLI should report concise errors.
        print(f"RESULT: FAIL - {exc}", file=sys.stderr)
        return 1

    print(f"RESULT: PASS")
    print(f"Generated Feature Package: {package_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
