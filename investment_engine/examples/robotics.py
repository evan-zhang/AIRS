"""Robotics research example."""

from investment_engine import run_research


REQUEST = {"request_id": "robotics", "topic": "机器人", "scope": "机器人产业链和关键零部件卡点研究", "time_horizon": "6-12 months"}


def run():
    return run_research(REQUEST)


if __name__ == "__main__":
    print(run()["final_research_report"])
