#!/usr/bin/env python3
"""Validate AIRS FEATURE-004 Data Connector Framework deliverables."""
from __future__ import annotations
import importlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [
    "docs/data-connectors/connector-architecture.md",
    "docs/data-connectors/connector-lifecycle.md",
    "docs/data-connectors/connector-interface.md",
    "docs/data-connectors/source-priority.md",
    "docs/data-connectors/connector-governance.md",
]
CORE = [
    "data_connectors/__init__.py",
    "data_connectors/registry.py",
    "data_connectors/base.py",
    "data_connectors/auth.py",
    "data_connectors/rate_limiter.py",
    "data_connectors/cache.py",
    "data_connectors/retry.py",
    "data_connectors/normalizer.py",
    "data_connectors/priority.py",
    "data_connectors/health_check.py",
    "data_connectors/README.md",
]
CONNECTORS = {
    "data_connectors/connectors/sec_edgar.py": "SECEdgarConnector",
    "data_connectors/connectors/yahoo_finance.py": "YahooFinanceConnector",
    "data_connectors/connectors/alpha_vantage.py": "AlphaVantageConnector",
    "data_connectors/connectors/news.py": "NewsConnector",
    "data_connectors/connectors/github.py": "GitHubConnector",
    "data_connectors/connectors/rss.py": "RSSConnector",
}
SCHEMAS = [
    "schemas/connectors/connector.schema.json",
    "schemas/connectors/datasource.schema.json",
    "schemas/connectors/connector-result.schema.json",
]
TEMPLATES = [
    "templates/connectors/connector-template.md",
    "templates/connectors/connector-config-template.yaml",
    "templates/connectors/connector-test-template.md",
    "templates/builder/feature-request-data-connector-framework.yaml",
]
BUILDER_PACKAGE = [
    "builder-output/data-connector-framework/ISSUE.md",
    "builder-output/data-connector-framework/ADR.md",
    "builder-output/data-connector-framework/FEATURE_SPEC.md",
    "builder-output/data-connector-framework/skill/data-connector-framework-skill.md",
    "builder-output/data-connector-framework/prompt/data-connector-framework-prompt.md",
    "builder-output/data-connector-framework/schema/data-connector-framework.schema.json",
    "builder-output/data-connector-framework/tests/test-data-connector-framework.md",
    "builder-output/data-connector-framework/benchmark/data-connector-framework-benchmark.md",
    "builder-output/data-connector-framework/PR_CHECKLIST.md",
    "builder-output/data-connector-framework/RELEASE_NOTES.md",
]
REPORTS = [
    "docs/adr/ADR-0004-data-connector-framework.md",
    "docs/production/FEATURE_004_COMPLETION_REPORT.md",
    "docs/review/FEATURE_004_SELF_REVIEW.md",
]
REQUIRED_TERMS = ["CONFIG", "INPUT_SCHEMA", "OUTPUT_SCHEMA", "ERROR_HANDLING", "RETRY_POLICY", "CACHE_STRATEGY", "health_check", "TEST_CASE"]
TRACE_FIELDS = ["source", "url", "timestamp", "version", "trace_id", "traceability"]
FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为", "应买入", "应卖出"]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_text(rel: str, failures: list[str], min_size: int = 120, disclaimer: bool = True) -> str:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return ""
    text = read(rel)
    check(len(text) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    if disclaimer:
        check("免责声明" in text and "不构成投资建议" in text, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for word in FORBIDDEN:
        check(word not in text, f"{rel} avoids forbidden expression: {word}", f"{rel} contains forbidden expression: {word}", failures)
    return text


def validate_json(rel: str, failures: list[str]) -> dict:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        check(True, f"{rel} is valid JSON", f"{rel} invalid JSON", failures)
        return data
    except json.JSONDecodeError as exc:
        check(False, f"{rel} is valid JSON", f"{rel} invalid JSON: {exc}", failures)
        return {}


def validate_static(failures: list[str]) -> None:
    for rel in DOCS:
        text = validate_text(rel, failures, min_size=500)
        for term in ["Connector", "Source", "Trace", "Evidence"]:
            check(term in text, f"{rel} references {term}", f"{rel} missing {term}", failures)
    for rel in CORE:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
        if path.exists() and rel.endswith((".py", ".md")):
            text = read(rel)
            check("Connector" in text or "connector" in text, f"{rel} contains connector logic", f"{rel} missing connector logic", failures)
    for rel in SCHEMAS:
        data = validate_json(rel, failures)
        blob = json.dumps(data, ensure_ascii=False)
        for field in ["source", "url", "timestamp", "version", "trace_id", "不构成投资建议"]:
            check(field in blob, f"{rel} contains {field}", f"{rel} missing {field}", failures)
    for rel in TEMPLATES:
        validate_text(rel, failures, min_size=80, disclaimer=rel.endswith(".md") or rel.endswith(".yaml"))
    for rel in BUILDER_PACKAGE:
        if rel.endswith(".json"):
            validate_json(rel, failures)
        else:
            validate_text(rel, failures, min_size=220)
    for rel in REPORTS:
        validate_text(rel, failures, min_size=500)


def validate_connectors(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    from data_connectors import ConnectorRequest, default_registry
    registry = default_registry()
    check(set(registry.list_ids()) == {"alpha_vantage", "github", "news", "rss", "sec_edgar", "yahoo_finance"}, "default registry has six connectors", "default registry missing connectors", failures)
    for rel, cls in CONNECTORS.items():
        text = validate_text(rel, failures, min_size=1000, disclaimer=False)
        for term in REQUIRED_TERMS:
            check(term in text, f"{rel} declares {term}", f"{rel} missing {term}", failures)
        module_name = rel[:-3].replace("/", ".")
        module = importlib.import_module(module_name)
        connector = getattr(module, cls)()
        test = connector.test_case()
        result = connector.fetch(ConnectorRequest(test["input"])).to_dict()
        for field in TRACE_FIELDS:
            check(field in result and result[field] is not None, f"{rel} result has {field}", f"{rel} result missing {field}", failures)
        check("不构成投资建议" in result.get("disclaimer", ""), f"{rel} result has disclaimer", f"{rel} result missing disclaimer", failures)
        check(connector.health_check().status == "PASS", f"{rel} health check PASS", f"{rel} health check failed", failures)
        bad = connector.fetch(ConnectorRequest({})).to_dict()
        check("error" in bad and bad["error"]["error_code"] == "INPUT_VALIDATION_ERROR", f"{rel} handles input error", f"{rel} missing input error handling", failures)


def validate_consistency(failures: list[str]) -> None:
    schema_readme = read("schemas/README.md")
    changelog = read("CHANGELOG.md")
    check("schemas/connectors/" in schema_readme and "connector-result.schema.json" in schema_readme, "schemas/README documents connector schemas", "schemas/README missing connector schemas", failures)
    check("FEATURE-004" in changelog and "Data Connector Framework" in changelog, "CHANGELOG documents FEATURE-004", "CHANGELOG missing FEATURE-004", failures)
    for rel in ["docs/data-connectors/connector-architecture.md", "docs/data-connectors/connector-interface.md"]:
        text = read(rel)
        for term in ["Source", "URL", "Timestamp", "Version", "Trace ID", "Traceability"]:
            check(term in text, f"{rel} aligns with Evidence trace field {term}", f"{rel} missing Evidence trace field {term}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-004 Data Connector Framework Validation")
    print("====================================================")
    validate_static(failures)
    validate_connectors(failures)
    validate_consistency(failures)
    print("====================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
