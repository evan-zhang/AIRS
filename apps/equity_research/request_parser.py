"""股票研究请求解析。

本模块只把自然语言或字典输入标准化为研究请求，不生成投资建议。
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
import re
from typing import Any
from uuid import uuid4


DISCLAIMER = "仅用于 AIRS 投资研究流程编排和质量控制，不构成投资建议。"

KNOWN_MARKETS = {
    "US": {"nasdaq", "nyse", "us", "美股", "美国"},
    "HK": {"hk", "hkg", "港股", "香港"},
    "TW": {"tw", "tse", "台湾", "台股"},
    "CN": {"cn", "a股", "沪深", "中国"},
}

FOCUS_KEYWORDS = {
    "financial": ["财务", "盈利", "收入", "利润", "cash flow", "financial"],
    "valuation": ["估值", "pe", "ps", "valuation"],
    "industry": ["行业", "竞争", "份额", "industry"],
    "supply_chain": ["供应链", "卡点", "chokepoint", "supply"],
    "catalyst": ["催化", "事件", "catalyst"],
    "risk": ["风险", "risk"],
}

SYMBOL_PATTERN = re.compile(r"\b([A-Z]{1,5}(?:\.[A-Z]{1,3})?|\d{4,6}(?:\.[A-Z]{2})?)\b")


@dataclass(frozen=True)
class ResearchRequest:
    """结构化股票研究请求。"""

    request_id: str
    raw_input: str
    symbol: str | None
    company_name: str | None
    market: str | None
    time_range: str
    research_question: str
    focus_areas: list[str] = field(default_factory=list)
    peer_companies: list[str] = field(default_factory=list)
    risk_preference: str = "balanced"
    language: str = "zh"
    created_at: str = field(default_factory=lambda: date.today().isoformat())
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def parse_research_request(user_input: str | dict[str, Any]) -> ResearchRequest:
    """把用户输入解析为 ResearchRequest。

    支持自然语言字符串或已经结构化的 dict。无法确定的字段保留为空，并交给
    Company Resolver 或后续人工复核处理。
    """

    if isinstance(user_input, dict):
        raw = str(user_input.get("raw_input") or user_input.get("research_question") or user_input)
        symbol = _clean_symbol(user_input.get("symbol"))
        company_name = _clean_text(user_input.get("company_name") or user_input.get("company"))
        market = _infer_market(raw, user_input.get("market"))
        focus_areas = _normalize_focus(user_input.get("focus_areas") or [], raw)
        peers = [str(item).strip() for item in user_input.get("peer_companies", []) if str(item).strip()]
        return ResearchRequest(
            request_id=str(user_input.get("request_id") or f"APP-001-{uuid4().hex[:10].upper()}"),
            raw_input=raw,
            symbol=symbol,
            company_name=company_name,
            market=market,
            time_range=str(user_input.get("time_range") or user_input.get("time_horizon") or "最近12个月"),
            research_question=str(user_input.get("research_question") or raw),
            focus_areas=focus_areas,
            peer_companies=peers,
            risk_preference=str(user_input.get("risk_preference") or "balanced"),
            language=str(user_input.get("language") or "zh"),
        )

    raw = str(user_input).strip()
    symbols = [match.group(1) for match in SYMBOL_PATTERN.finditer(raw)]
    symbol = symbols[0] if symbols else None
    peers = symbols[1:] if len(symbols) > 1 else []
    company_name = _infer_company_name(raw, symbol)
    return ResearchRequest(
        request_id=f"APP-001-{uuid4().hex[:10].upper()}",
        raw_input=raw,
        symbol=symbol,
        company_name=company_name,
        market=_infer_market(raw, None),
        time_range=_infer_time_range(raw),
        research_question=raw or "请生成股票研究报告",
        focus_areas=_normalize_focus([], raw),
        peer_companies=peers,
        risk_preference=_infer_risk_preference(raw),
    )


def _clean_symbol(value: Any) -> str | None:
    if not value:
        return None
    return str(value).strip().upper() or None


def _clean_text(value: Any) -> str | None:
    if not value:
        return None
    return str(value).strip() or None


def _infer_market(raw: str, explicit: Any) -> str | None:
    if explicit:
        token = str(explicit).strip()
        upper = token.upper()
        if upper in KNOWN_MARKETS:
            return upper
        for market, aliases in KNOWN_MARKETS.items():
            if token.lower() in aliases:
                return market
    lowered = raw.lower()
    for market, aliases in KNOWN_MARKETS.items():
        if any(alias in lowered for alias in aliases):
            return market
    if re.search(r"\b[A-Z]{1,5}\b", raw):
        return "US"
    if re.search(r"\b\d{4}\.HK\b|\b\d{5,6}\b", raw):
        return "HK"
    return None


def _infer_company_name(raw: str, symbol: str | None) -> str | None:
    aliases = {
        "NVIDIA": "NVIDIA",
        "英伟达": "NVIDIA",
        "TSMC": "Taiwan Semiconductor Manufacturing Company",
        "台积电": "Taiwan Semiconductor Manufacturing Company",
        "康哲": "China Medical System Holdings",
        "康哲药业": "China Medical System Holdings",
    }
    for alias, name in aliases.items():
        if alias.lower() in raw.lower():
            return name
    if symbol:
        return None
    return raw[:80] if raw else None


def _infer_time_range(raw: str) -> str:
    if "三年" in raw or "3年" in raw:
        return "最近3年"
    if "五年" in raw or "5年" in raw:
        return "最近5年"
    if "季度" in raw or "季报" in raw:
        return "最近4个季度"
    return "最近12个月"


def _normalize_focus(explicit: list[Any], raw: str) -> list[str]:
    focus = {str(item).strip() for item in explicit if str(item).strip()}
    lowered = raw.lower()
    for area, keywords in FOCUS_KEYWORDS.items():
        if any(keyword.lower() in lowered for keyword in keywords):
            focus.add(area)
    return sorted(focus or {"profile", "industry", "financial", "valuation", "risk"})


def _infer_risk_preference(raw: str) -> str:
    lowered = raw.lower()
    if "保守" in lowered or "conservative" in lowered:
        return "conservative"
    if "激进" in lowered or "aggressive" in lowered:
        return "aggressive"
    return "balanced"

