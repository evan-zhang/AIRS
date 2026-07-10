"""AIRS Data Connector base interfaces.

连接器只负责外部数据接入与归一化，不生成投资建议。
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

DISCLAIMER = "仅供 AIRS 工程开发和研究质量控制使用，不构成投资建议。"


@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 3
    initial_delay_seconds: float = 0.1
    backoff_multiplier: float = 2.0


@dataclass(frozen=True)
class CacheStrategy:
    ttl_seconds: int = 300
    allow_stale: bool = False


@dataclass(frozen=True)
class ConnectorConfig:
    connector_id: str
    name: str
    source: str
    source_type: str
    base_url: str
    version: str = "0.1.0"
    priority: str = "trusted_third_party"
    auth_type: str = "none"
    retry_policy: RetryPolicy = field(default_factory=RetryPolicy)
    cache_strategy: CacheStrategy = field(default_factory=CacheStrategy)
    enabled: bool = True


@dataclass(frozen=True)
class ConnectorRequest:
    query: dict[str, Any]
    trace_id: str = field(default_factory=lambda: f"TRACE-{uuid4().hex[:12].upper()}")
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class ConnectorError:
    error_code: str
    message: str
    retryable: bool = False
    trace_id: str | None = None


@dataclass
class ConnectorResult:
    connector_id: str
    source: str
    source_type: str
    url: str
    timestamp: str
    version: str
    trace_id: str
    data: dict[str, Any]
    traceability: dict[str, Any]
    error: ConnectorError | None = None
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        payload = {
            "connector_id": self.connector_id,
            "source": self.source,
            "source_type": self.source_type,
            "url": self.url,
            "timestamp": self.timestamp,
            "version": self.version,
            "trace_id": self.trace_id,
            "data": self.data,
            "traceability": self.traceability,
            "disclaimer": self.disclaimer,
        }
        if self.error:
            payload["error"] = {
                "error_code": self.error.error_code,
                "message": self.error.message,
                "retryable": self.error.retryable,
                "trace_id": self.error.trace_id,
            }
        return payload


@dataclass
class HealthStatus:
    connector_id: str
    status: str
    latency_ms: float
    last_success: str | None = None
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


class BaseConnector(ABC):
    """所有外部数据源 Connector 的抽象基类。"""

    config: ConnectorConfig

    @property
    def connector_id(self) -> str:
        return self.config.connector_id

    @abstractmethod
    def input_schema(self) -> dict[str, Any]:
        """返回输入 Schema。"""

    @abstractmethod
    def output_schema(self) -> dict[str, Any]:
        """返回输出 Schema。"""

    @abstractmethod
    def fetch(self, request: ConnectorRequest) -> ConnectorResult:
        """执行抓取并返回统一 Connector Result。"""

    @abstractmethod
    def normalize(self, raw: dict[str, Any], request: ConnectorRequest) -> ConnectorResult:
        """归一化来源输出。"""

    @abstractmethod
    def health_check(self) -> HealthStatus:
        """返回 Connector 健康状态。"""

    @abstractmethod
    def test_case(self) -> dict[str, Any]:
        """返回最小测试用例。"""

    def error_result(self, request: ConnectorRequest, code: str, message: str, retryable: bool = False) -> ConnectorResult:
        return ConnectorResult(
            connector_id=self.config.connector_id,
            source=self.config.source,
            source_type=self.config.source_type,
            url=self.config.base_url,
            timestamp=request.timestamp,
            version=self.config.version,
            trace_id=request.trace_id,
            data={},
            traceability={"connector": self.config.connector_id, "transformations": [], "cache_hit": False},
            error=ConnectorError(code, message, retryable, request.trace_id),
        )
