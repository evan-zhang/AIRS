"""公司识别与代码解析。"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .request_parser import ResearchRequest


DISCLAIMER = "公司识别结果仅用于研究流程编排，不构成投资建议。"

COMPANY_DIRECTORY: dict[str, dict[str, str]] = {
    "NVDA": {
        "symbol": "NVDA",
        "company_name": "NVIDIA Corporation",
        "market": "US",
        "exchange": "NASDAQ",
        "industry": "Semiconductors",
        "sector": "Information Technology",
        "currency": "USD",
    },
    "TSM": {
        "symbol": "TSM",
        "company_name": "Taiwan Semiconductor Manufacturing Company Limited",
        "market": "US",
        "exchange": "NYSE ADR",
        "industry": "Semiconductors",
        "sector": "Information Technology",
        "currency": "USD",
    },
    "2330.TW": {
        "symbol": "2330.TW",
        "company_name": "Taiwan Semiconductor Manufacturing Company Limited",
        "market": "TW",
        "exchange": "TWSE",
        "industry": "Semiconductors",
        "sector": "Information Technology",
        "currency": "TWD",
    },
    "0867.HK": {
        "symbol": "0867.HK",
        "company_name": "China Medical System Holdings Limited",
        "market": "HK",
        "exchange": "HKEX",
        "industry": "Pharmaceuticals",
        "sector": "Healthcare",
        "currency": "HKD",
    },
    "CMS": {
        "symbol": "0867.HK",
        "company_name": "China Medical System Holdings Limited",
        "market": "HK",
        "exchange": "HKEX",
        "industry": "Pharmaceuticals",
        "sector": "Healthcare",
        "currency": "HKD",
    },
}

ALIASES = {
    "NVIDIA": "NVDA",
    "英伟达": "NVDA",
    "TSMC": "TSM",
    "台积电": "2330.TW",
    "康哲药业": "0867.HK",
    "康哲": "0867.HK",
    "CHINA MEDICAL SYSTEM": "0867.HK",
}


@dataclass(frozen=True)
class CompanyInfo:
    symbol: str
    company_name: str
    market: str
    exchange: str
    industry: str
    sector: str
    currency: str
    resolver_status: str
    traceability: dict[str, Any]
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def resolve_company(request: ResearchRequest | dict[str, Any]) -> CompanyInfo:
    """解析股票代码或公司名称，返回公司基础信息。

    本地目录只承担路由作用。未命中时返回 NEED_REVIEW，不伪造成真实公司资料。
    """

    req = request if isinstance(request, ResearchRequest) else ResearchRequest(**request)
    symbol = (req.symbol or "").upper()
    key = symbol if symbol in COMPANY_DIRECTORY else _alias_key(req.company_name or req.raw_input)
    if key and key in COMPANY_DIRECTORY:
        data = COMPANY_DIRECTORY[key]
        return CompanyInfo(**data, resolver_status="RESOLVED_LOCAL_DIRECTORY", traceability={"resolver": "apps/equity_research/company_resolver.py", "input": req.to_dict()})
    fallback_symbol = symbol or "UNRESOLVED"
    return CompanyInfo(
        symbol=fallback_symbol,
        company_name=req.company_name or fallback_symbol,
        market=req.market or "UNKNOWN",
        exchange="UNKNOWN",
        industry="UNKNOWN",
        sector="UNKNOWN",
        currency="UNKNOWN",
        resolver_status="NEED_REVIEW",
        traceability={"resolver": "apps/equity_research/company_resolver.py", "input": req.to_dict(), "gap": "本地公司目录未命中，需要真实数据源或人工确认。"},
    )


def _alias_key(text: str) -> str | None:
    upper = text.upper()
    for alias, key in ALIASES.items():
        if alias.upper() in upper:
            return key
    return None

