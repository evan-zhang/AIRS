from e2e_harness import run_production_case


CASE = {
    "case_id": "prod-e2e-02-semiconductor",
    "title": "半导体国产替代端到端研究",
    "topic": "Semiconductor Localization",
    "scope": "验证半导体设备与材料链条中的证据采集、KG 整合和委员会审议",
    "time_horizon": "18m",
    "connectors": [
        {"connector_id": "news", "query": {"query": "semiconductor equipment localization", "language": "zh"}},
        {"connector_id": "yahoo_finance", "query": {"symbol": "ASML", "range": "1d"}},
    ],
    "expectations": {"min_evidence_cards": 5},
}


def run_case():
    return run_production_case(CASE)
