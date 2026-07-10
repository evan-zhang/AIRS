"""AIRS Investment Research Engine.

The engine orchestrates existing AIRS infrastructure references into a
deterministic research workflow. It is for research quality control only and
does not provide investment advice, trading instructions, target prices, or
return promises.
"""

from .pipeline import InvestmentResearchPipeline, run_research
from .recommendation import DISCLAIMER, classify_statement

__all__ = ["InvestmentResearchPipeline", "run_research", "classify_statement", "DISCLAIMER"]
