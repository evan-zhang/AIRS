from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-01-ai-compute",
    "title": "AI 算力供应链端到端研究",
    "topic": "AI Compute Supply Chain",
    "scope": "验证 AI 服务器供应链卡点、需求证据和反方证据的完整研究链路",
    "time_horizon": "12m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "AI servers supply chain", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "NVDA", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
