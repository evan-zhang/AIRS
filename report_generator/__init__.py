"""AIRS Research Report Generator.

本包把 M2 Methodology、M3 Evidence、FEATURE-002 Knowledge Graph、M4 Prompt、M5 Skill
和 M6 Score/Evaluation 输出组合为可追溯的标准研究报告。
"""

from .composer import ReportComposer, SectionComposer
from .evidence_citation import EvidenceCitationBuilder
from .kg_summary import KGSummaryBuilder
from .model import DISCLAIMER, REQUIRED_SECTION_TITLES, ReportSection, ResearchReport
from .pipeline import ReportPipeline
from .score_summary import ScoreSummaryBuilder

__all__ = [
    "DISCLAIMER",
    "REQUIRED_SECTION_TITLES",
    "EvidenceCitationBuilder",
    "KGSummaryBuilder",
    "ReportComposer",
    "ReportPipeline",
    "ReportSection",
    "ResearchReport",
    "ScoreSummaryBuilder",
    "SectionComposer",
]
