"""Shared helpers for real/mock Connector payloads."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any

from .base import ConnectorConfig, ConnectorRequest
from .secret_masking import mask_mapping

REQUIRED_REAL_FIELDS = [
    "source",
    "url",
    "publication_time",
    "collection_time",
    "trace_id",
    "connector_version",
    "raw_hash",
    "confidence",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def raw_hash(raw: Any) -> str:
    payload = json.dumps(mask_mapping(raw), ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def envelope(config: ConnectorConfig, request: ConnectorRequest, *, url: str, publication_time: str | None, confidence: float, payload: dict[str, Any], mode: str) -> dict[str, Any]:
    safe_payload = mask_mapping(payload)
    return {
        "source": config.source,
        "url": url,
        "publication_time": publication_time or request.timestamp,
        "collection_time": utc_now(),
        "trace_id": request.trace_id,
        "connector_version": config.version,
        "raw_hash": raw_hash(safe_payload),
        "confidence": confidence,
        "mode": mode,
        "payload": safe_payload,
    }
