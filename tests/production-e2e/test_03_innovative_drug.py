from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-03-innovative-drug",
    "title": "创新药管线端到端研究",
    "topic": "Innovative Drug Pipeline",
    "scope": "验证创新药行业催化、风险反证、证据缺口和最终报告分类输出",
    "time_horizon": "24m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "innovative drug pipeline catalyst", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "MRNA", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
