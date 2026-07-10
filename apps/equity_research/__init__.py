"""APP-001 Equity Research App.

DISCLAIMER: APP-001 输出仅用于研究质量控制，不构成投资建议。
"""

from .app import EquityResearchApp, run_equity_research
from .request_parser import ResearchRequest, parse_research_request

DISCLAIMER = "APP-001 输出仅用于研究质量控制，不构成投资建议。"

__all__ = ["EquityResearchApp", "ResearchRequest", "parse_research_request", "run_equity_research"]
