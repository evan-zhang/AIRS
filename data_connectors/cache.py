"""In-memory cache manager for Connector Result objects."""
from __future__ import annotations
from dataclasses import dataclass, field
from time import time
from typing import Any
import hashlib, json


@dataclass
class CacheEntry:
    value: Any
    expires_at: float


@dataclass
class CacheManager:
    entries: dict[str, CacheEntry] = field(default_factory=dict)

    def key(self, connector_id: str, version: str, query: dict[str, Any]) -> str:
        raw = json.dumps({"connector_id": connector_id, "version": version, "query": query}, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def get(self, key: str) -> Any | None:
        entry = self.entries.get(key)
        if not entry or entry.expires_at < time():
            self.entries.pop(key, None)
            return None
        return entry.value

    def set(self, key: str, value: Any, ttl_seconds: int) -> None:
        self.entries[key] = CacheEntry(value=value, expires_at=time() + ttl_seconds)
