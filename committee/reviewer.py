"""Committee 委员会复核角色。"""

from __future__ import annotations

from typing import Any

from .role_registry import DISCLAIMER


class EvidenceReviewer:
    role_id = "evidence_reviewer"

    def challenge(self, session: dict[str, Any]) -> dict[str, Any]:
        evidence = session.get("evidence_review", {})
        gaps = evidence.get("gaps", ["需要补足原始来源、时间戳和反方证据。"])
        return {
            "role_id": self.role_id,
            "challenge_type": "evidence_integrity",
            "challenge": "证据链必须引用 M3 Evidence Card 和 Evidence Chain，且每个关键命题至少有支持证据和反方证据。",
            "gaps": gaps,
            "pass": not gaps,
            "disclaimer": DISCLAIMER,
        }


class DevilsAdvocate:
    role_id = "devils_advocate"

    def challenge(self, session: dict[str, Any]) -> dict[str, Any]:
        return {
            "role_id": self.role_id,
            "challenge_type": "counter_argument",
            "challenge": "若结论依赖单一景气假设、单一数据源或单一路径外推，必须降级为有条件研究结论。",
            "alternative_explanations": ["周期补库存", "政策节奏变化", "竞争扩产", "数据样本偏差"],
            "pass": True,
            "disclaimer": DISCLAIMER,
        }
