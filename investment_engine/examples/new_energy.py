"""New energy research example."""

from investment_engine import run_research


REQUEST = {"request_id": "new-energy", "topic": "新能源", "scope": "新能源储能、电网和材料约束研究", "time_horizon": "6-12 months"}


def run():
    return run_research(REQUEST)


if __name__ == "__main__":
    print(run()["final_research_report"])
