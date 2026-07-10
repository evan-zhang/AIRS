"""Innovative drug research example."""

from investment_engine import run_research


REQUEST = {"request_id": "innovative-drug", "topic": "创新药", "scope": "创新药产业链和临床催化剂研究", "time_horizon": "6-12 months"}


def run():
    return run_research(REQUEST)


if __name__ == "__main__":
    print(run()["final_research_report"])
