"""Filesystem-backed cache for real Connector responses."""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from time import time
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CACHE_DIR = ROOT / ".cache" / "data_connectors"


@dataclass
class PersistentCache:
    cache_dir: Path = DEFAULT_CACHE_DIR

    def __post_init__(self) -> None:
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def key(self, connector_id: str, version: str, query: dict[str, Any]) -> str:
        raw = json.dumps({"connector_id": connector_id, "version": version, "query": query}, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def _path(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"

    def get(self, key: str, ttl_seconds: int) -> dict[str, Any] | None:
        path = self._path(key)
        if not path.exists():
            return None
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            path.unlink(missing_ok=True)
            return None
        if time() - float(payload.get("created_at", 0)) > ttl_seconds:
            path.unlink(missing_ok=True)
            return None
        value = payload.get("value")
        return value if isinstance(value, dict) else None

    def set(self, key: str, value: dict[str, Any]) -> None:
        payload = {"created_at": time(), "value": value}
        self._path(key).write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
