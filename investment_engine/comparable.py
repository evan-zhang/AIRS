"""Comparable analysis component for investment research."""

from __future__ import annotations

from typing import Any


def analyze_comparables(companies: dict[str, Any]) -> dict[str, Any]:
    peers = []
    for idx, company in enumerate(companies["companies"], start=1):
        peers.append(
            {
                "name": company["name"],
                "role": company["role"],
                "quality_score": round(0.62 + idx * 0.04, 2),
                "evidence_refs": [company["evidence_ref"]],
            }
        )
    return {
        "component": "comparable",
        "methodology_refs": ["docs/methodology/valuation.md", "docs/methodology/financial-anomaly.md"],
        "peers": peers,
        "comparison_note": "Comparable 结果仅用于研究排序和证据缺口识别，不构成估值结论或交易建议。",
    }
