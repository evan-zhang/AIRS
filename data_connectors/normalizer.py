"""Data normalization helpers for Connector Results."""
from __future__ import annotations
from typing import Any
from .base import ConnectorConfig, ConnectorRequest, ConnectorResult, DISCLAIMER


class DataNormalizer:
    def result(self, config: ConnectorConfig, request: ConnectorRequest, data: dict[str, Any], url: str, transformations: list[str] | None = None) -> ConnectorResult:
        return ConnectorResult(
            connector_id=config.connector_id,
            source=config.source,
            source_type=config.source_type,
            url=url,
            timestamp=request.timestamp,
            version=config.version,
            trace_id=request.trace_id,
            data=data,
            traceability={
                "connector": config.connector_id,
                "request_id": request.trace_id,
                "cache_hit": False,
                "transformations": transformations or ["mock_fetch", "normalize"],
            },
            disclaimer=DISCLAIMER,
        )
