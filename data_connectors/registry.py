"""Connector Registry for AIRS Data Connector Framework."""
from __future__ import annotations
from dataclasses import dataclass, field
from .base import BaseConnector


@dataclass
class ConnectorRegistry:
    connectors: dict[str, BaseConnector] = field(default_factory=dict)

    def register(self, connector: BaseConnector) -> None:
        if not connector.config.enabled:
            raise ValueError(f"connector disabled: {connector.connector_id}")
        self.connectors[connector.connector_id] = connector

    def get(self, connector_id: str) -> BaseConnector:
        try:
            return self.connectors[connector_id]
        except KeyError as exc:
            raise KeyError(f"unknown connector: {connector_id}") from exc

    def list_ids(self) -> list[str]:
        return sorted(self.connectors)

    def health(self) -> dict[str, dict]:
        return {cid: connector.health_check().to_dict() for cid, connector in self.connectors.items()}


def default_registry() -> ConnectorRegistry:
    from .connectors import AlphaVantageConnector, GitHubConnector, NewsConnector, RSSConnector, SECEdgarConnector, YahooFinanceConnector
    registry = ConnectorRegistry()
    for connector in [SECEdgarConnector(), YahooFinanceConnector(), AlphaVantageConnector(), NewsConnector(), GitHubConnector(), RSSConnector()]:
        registry.register(connector)
    return registry
