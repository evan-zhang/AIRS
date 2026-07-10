"""港股个股 Committee 示例。"""

from .common import run_example


def run():
    return run_example(
        "aic-hk-stock",
        "港股个股研究",
        "company",
        "Portfolio Expert 认为港股流动性、汇率和相关资产暴露需要进入后续风险复核。",
    )
