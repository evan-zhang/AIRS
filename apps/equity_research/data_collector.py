"""股票研究数据收集计划与 Connector 调用。"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from data_connectors import ConnectorRequest, default_registry

from .company_resolver import CompanyInfo
from .request_parser import ResearchRequest


DISCLAIMER = "Connector 数据仅用于研究质量控制；真实数据不可用时必须标注 SKIP 或降级，不构成投资建议。"


@dataclass
class DataCollectionBundle:
    plan: list[dict[str, Any]]
    connector_results: list[dict[str, Any]]
    evidence_cards: dict[str, dict[str, Any]]
    degradation_notes: list[str] = field(default_factory=list)
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "plan": self.plan,
            "connector_results": self.connector_results,
            "evidence_cards": self.evidence_cards,
            "degradation_notes": self.degradation_notes,
            "disclaimer": self.disclaimer,
        }


class EquityDataCollector:
    """按公司研究需求生成数据采集计划并调用可用 Connector。"""

    def __init__(self) -> None:
        self.registry = default_registry()

    def collect(self, request: ResearchRequest, company: CompanyInfo) -> DataCollectionBundle:
        plan = self.build_plan(request, company)
        results: list[dict[str, Any]] = []
        notes: list[str] = []
        for item in plan:
            try:
                connector = self.registry.get(item["connector_id"])
                result = connector.fetch(ConnectorRequest(item["query"])).to_dict()
                if result.get("data", {}).get("mode") == "mock":
                    notes.append(f"{item['connector_id']} 使用 Mock 降级数据，不能冒充真实外部数据。")
                if result.get("error"):
                    notes.append(f"{item['connector_id']} 返回错误：{result['error']['message']}")
                results.append(result)
            except Exception as exc:  # noqa: BLE001
                notes.append(f"{item['connector_id']} SKIP：{exc}")
                results.append(
                    {
                        "connector_id": item["connector_id"],
                        "source": "SKIP",
                        "url": "SKIP",
                        "timestamp": item["purpose"],
                        "version": "unknown",
                        "trace_id": "SKIP",
                        "data": {"mode": "skip", "reason": str(exc)},
                        "traceability": {"plan_item": item},
                        "disclaimer": DISCLAIMER,
                    }
                )
        evidence = self._to_evidence_cards(request, company, results)
        return DataCollectionBundle(plan=plan, connector_results=results, evidence_cards=evidence, degradation_notes=notes)

    def build_plan(self, request: ResearchRequest, company: CompanyInfo) -> list[dict[str, Any]]:
        query_name = company.company_name if company.resolver_status != "NEED_REVIEW" else request.raw_input
        mode = "real" if _requires_real_data(request) else "mock"
        return [
            {
                "connector_id": "yahoo_finance",
                "purpose": "价格与基础行情占位；若为 Mock 必须降级。",
                "query": {"symbol": company.symbol, "range": request.time_range, "mode": mode},
                "evidence_category": "financial_market_data",
            },
            {
                "connector_id": "news",
                "purpose": "公司新闻与催化事件；真实新闻 API 不可用时降级。",
                "query": {"query": query_name, "language": request.language, "limit": 5, "mode": mode},
                "evidence_category": "news",
            },
            {
                "connector_id": "sec_edgar" if company.market == "US" else "rss",
                "purpose": "监管披露或公开 RSS 来源；不可用时标注 SKIP/Mock。",
                "query": {"symbol": company.symbol, "query": query_name, "limit": 5, "mode": mode},
                "evidence_category": "filing_or_public_feed",
            },
            {
                "connector_id": "rss",
                "purpose": "行业与供应链公开资料补充。",
                "query": {"feed_url": "https://news.google.com/rss/search?q=" + query_name.replace(" ", "+"), "limit": 5, "mode": mode},
                "evidence_category": "industry",
            },
        ]

    def _to_evidence_cards(self, request: ResearchRequest, company: CompanyInfo, results: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
        cards: dict[str, dict[str, Any]] = {}
        for index, result in enumerate(results, start=1):
            evidence_id = f"APP001-EV-{index:02d}"
            mode = result.get("data", {}).get("mode", "mock_or_static")
            confidence = 0.35 if mode in {"mock", "skip"} else 0.70
            cards[evidence_id] = {
                "evidence_id": evidence_id,
                "title": f"{company.company_name} {result.get('connector_id', 'connector')} 数据",
                "category": "connector_result",
                "source": result.get("source", "UNKNOWN"),
                "source_type": result.get("source_type", "UNKNOWN"),
                "url": result.get("url", "SKIP"),
                "publication_time": result.get("timestamp"),
                "collection_time": result.get("timestamp"),
                "confidence": confidence,
                "evidence_level": "L3" if mode in {"mock", "skip"} else "L2",
                "supports": [{"statement_id": "fact-data-availability", "statement": "研究流程已记录该数据源的可用性与追溯字段。"}],
                "refutes": [{"statement_id": "assumption-real-data-complete", "statement": "若结果为 Mock 或 SKIP，则反驳真实数据完整可用的假设。"}],
                "missing_evidence": ["真实财务明细", "公司公告原文", "可复核行业数据"],
                "weight": confidence,
                "traceability": result.get("traceability", {}),
                "data_mode": mode,
                "version": result.get("version", "unknown"),
                "statement_type": "Fact" if mode not in {"mock", "skip"} else "Assumption",
                "disclaimer": "仅供研究参考，不构成投资建议",
            }
        cards["APP001-EV-COUNTER-01"] = {
            "evidence_id": "APP001-EV-COUNTER-01",
            "title": "反方证据占位：数据源不足可能削弱结论",
            "category": "counter_evidence",
            "source": "AIRS governance",
            "source_type": "internal_quality_control",
            "url": "docs/data-connectors/real-data-integration.md",
            "publication_time": request.created_at,
            "collection_time": request.created_at,
            "confidence": 0.65,
            "evidence_level": "L2",
            "supports": [],
            "refutes": [{"statement_id": "opinion-high-conviction", "statement": "证据不充分时不得输出高确信度结论。"}],
            "missing_evidence": ["真实数据源凭证", "人工复核"],
            "weight": 0.65,
            "traceability": {"module": "apps/equity_research/data_collector.py"},
            "version": "0.1.0",
            "statement_type": "Fact",
            "disclaimer": "仅供研究参考，不构成投资建议",
        }
        return cards


def _requires_real_data(request: ResearchRequest) -> bool:
    if request.require_real_data:
        return True
    raw = request.raw_input.lower()
    return "production" in raw or "real_data" in raw or "真实数据" in raw
