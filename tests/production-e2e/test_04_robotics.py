from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-04-robotics",
    "title": "机器人产业链端到端研究",
    "topic": "Robotics Supply Chain",
    "scope": "验证机器人核心零部件、下游需求和风险反证的完整链路",
    "time_horizon": "12m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "humanoid robotics supply chain", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "TSLA", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
