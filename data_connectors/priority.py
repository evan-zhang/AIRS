"""Connector helper module."""
"""Source Priority Manager."""
from __future__ import annotations

SOURCE_PRIORITY = {
    "official": 1,
    "regulatory": 2,
    "company": 3,
    "exchange": 4,
    "trusted_third_party": 5,
    "public_news": 6,
    "community": 7,
}


class SourcePriorityManager:
    def rank(self, source_type: str) -> int:
        return SOURCE_PRIORITY.get(source_type, 99)

    def sort(self, items: list[dict]) -> list[dict]:
        return sorted(items, key=lambda item: self.rank(item.get("source_type", "")))
