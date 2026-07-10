"""Semiconductor research example."""

from investment_engine import run_research


REQUEST = {"request_id": "semiconductor", "topic": "半导体", "scope": "半导体设备、材料和先进制程约束研究", "time_horizon": "6-12 months"}


def run():
    return run_research(REQUEST)


if __name__ == "__main__":
    print(run()["final_research_report"])
