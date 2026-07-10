from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-08-memory-learning-regression",
    "title": "Memory/Learning 回归端到端研究",
    "topic": "Memory Learning Regression",
    "scope": "验证 Memory 写入读取、Learning feedback 和跨模块 source_ref 可追溯",
    "time_horizon": "6m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "investment research learning feedback", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "AAPL", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
