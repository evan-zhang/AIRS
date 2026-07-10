from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-07-news-impact",
    "title": "新闻影响分析端到端研究",
    "topic": "News Impact Analysis",
    "scope": "验证新闻事件进入 evidence、KG、scorecard、committee 和 final report 的链路",
    "time_horizon": "3m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "market news impact semiconductor AI", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "SMH", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
