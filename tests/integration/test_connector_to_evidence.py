from __future__ import annotations

from data_connectors.base import ConnectorRequest
from data_connectors.connectors.rss import RSSConnector
from data_connectors.real_payload import REQUIRED_REAL_FIELDS
from investment_engine import run_research
from knowledge_graph.builder import KnowledgeGraphBuilder
from knowledge_graph.model import EvidenceBinding
from knowledge_graph.validator import KnowledgeGraphValidator


def test_connector_to_evidence_to_kg_to_report_chain() -> None:
    connector = RSSConnector()
    result = connector.fetch(ConnectorRequest({"feed_url": "https://example.com/feed.xml", "limit": 1})).to_dict()
    for field in REQUIRED_REAL_FIELDS:
        assert result["data"].get(field) is not None

    evidence = {
        "evidence_id": "ev-connector-01",
        "source": result["source"],
        "url": result["url"],
        "trace_id": result["trace_id"],
        "connector_version": result["version"],
        "statement_type": "Fact",
        "content": "Connector result preserved traceable source metadata.",
        "confidence": result["data"]["confidence"],
    }
    builder = KnowledgeGraphBuilder(
        graph_id="kg-connector-integration",
        title="Connector Integration KG",
        research_question="Can connector output move into evidence and report layers?",
        methodology_refs=["docs/methodology/evidence-chain.md"],
        evidence_cards={evidence["evidence_id"]: evidence},
    )
    builder.add_node(
        {
            "node_id": "connector-result",
            "node_type": "evidence",
            "label": "Traceable connector result",
            "source_refs": [f"connector-trace:{result['trace_id']}"],
            "confidence": 0.7,
            "evidence_bindings": [EvidenceBinding("ev-connector-01", "claim-01", "supports", "medium").to_dict()],
        }
    )
    builder.add_node(
        {
            "node_id": "claim",
            "node_type": "claim",
            "label": "AIRS can bind connector output into KG nodes.",
            "source_refs": ["ev-connector-01"],
            "confidence": 0.7,
            "evidence_bindings": [EvidenceBinding("ev-connector-01", "claim-01", "supports", "medium").to_dict()],
        }
    )
    builder.add_edge(
        {
            "edge_id": "edge-connector-claim",
            "from_node": "connector-result",
            "to_node": "claim",
            "relation_type": "supports",
            "evidence_refs": ["ev-connector-01"],
            "missing_evidence": ["real source freshness check"],
            "confidence": 0.7,
        }
    )
    validation = KnowledgeGraphValidator().validate(builder.build())
    assert validation.passed, validation.errors

    report = run_research({"request_id": "connector-chain", "topic": "Connector integration", "scope": "Evidence to KG to Report", "time_horizon": "current"})
    assert "final_research_report" in report
    assert "不构成投资建议" in report["final_research_report"]
