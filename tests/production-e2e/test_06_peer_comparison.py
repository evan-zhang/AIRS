from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-06-peer-comparison",
    "title": "两家同行对比端到端研究",
    "topic": "Peer Comparison: AI Compute Leaders",
    "scope": "验证两家同行对比中的证据链、可比分析、委员会异议和最终报告边界",
    "time_horizon": "12m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "AI compute peer comparison", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "AMD", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
