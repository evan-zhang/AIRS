"""Research route handlers."""

from __future__ import annotations

from typing import Any

from apps.equity_research import run_equity_research


DISCLAIMER = "AIRS Research API 仅用于研究流程编排和质量控制，不构成投资建议。"


def _default_payload(path: str, payload: dict[str, Any]) -> dict[str, Any]:
    if path == "/company":
        subject = payload.get("company") or payload.get("symbol") or "NVDA"
        question = payload.get("research_question") or f"分析 {subject} 的财务、估值、供应链和风险"
        return {**payload, "symbol": payload.get("symbol", subject), "research_question": question}
    if path == "/theme":
        theme = payload.get("theme") or "AI compute supply chain"
        return {**payload, "symbol": payload.get("symbol", "NVDA"), "research_question": f"围绕 {theme} 展开主题研究并保留证据链"}
    if path == "/report":
        return {**payload, "research_question": payload.get("research_question", "生成结构化股票研究报告")}
    return payload or {"symbol": "NVDA", "market": "US", "research_question": "分析 NVIDIA 的财务、估值、供应链和风险"}


def handle_research(path: str, payload: dict[str, Any]) -> dict[str, Any]:
    request = _default_payload(path, payload)
    result = run_equity_research(request)
    return {
        "status": result.get("status", "ok"),
        "quality_gate": result.get("quality_gate"),
        "endpoint": path,
        "request_id": result["request"]["request_id"],
        "company": result["company"],
        "result": result,
        "disclaimer": DISCLAIMER,
    }
