"""AI compute research example."""

from investment_engine import run_research


REQUEST = {"request_id": "ai-compute", "topic": "AI 算力", "scope": "AI 算力产业链卡点研究", "time_horizon": "6-12 months"}


def run():
    return run_research(REQUEST)


if __name__ == "__main__":
    print(run()["final_research_report"])
