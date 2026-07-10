from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-05-new-energy",
    "title": "新能源产业端到端研究",
    "topic": "New Energy Chain",
    "scope": "验证新能源需求、供给瓶颈、价格证据缺口和学习反馈",
    "time_horizon": "18m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "new energy storage supply chain", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "ENPH", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
