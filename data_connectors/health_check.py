"""Connector health check helpers."""
from __future__ import annotations
from datetime import datetime, timezone
from time import perf_counter
from .base import BaseConnector, HealthStatus


class ConnectorHealthChecker:
    def check(self, connector: BaseConnector) -> HealthStatus:
        start = perf_counter()
        try:
            status = connector.health_check()
            status.latency_ms = round((perf_counter() - start) * 1000, 3)
            return status
        except Exception as exc:  # noqa: BLE001
            return HealthStatus(
                connector_id=connector.connector_id,
                status="FAIL",
                latency_ms=round((perf_counter() - start) * 1000, 3),
                last_success=None,
                error=str(exc),
            )


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
