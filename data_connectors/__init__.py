"""AIRS Data Connector Framework."""
from .base import BaseConnector, CacheStrategy, ConnectorConfig, ConnectorRequest, ConnectorResult, HealthStatus, RetryPolicy
from .env_config import EnvConfig
from .http_client import HTTPClient, HTTPClientError, HTTPResponse
from .persistent_cache import PersistentCache
from .registry import ConnectorRegistry, default_registry
from .secret_masking import mask_mapping, mask_secret, mask_url

__all__ = [
    "BaseConnector",
    "CacheStrategy",
    "ConnectorConfig",
    "ConnectorRequest",
    "ConnectorResult",
    "ConnectorRegistry",
    "EnvConfig",
    "HealthStatus",
    "HTTPClient",
    "HTTPClientError",
    "HTTPResponse",
    "PersistentCache",
    "RetryPolicy",
    "default_registry",
    "mask_mapping",
    "mask_secret",
    "mask_url",
]
