"""Theme discovery component."""

from __future__ import annotations

from typing import Any


THEME_SIGNALS = {
    "AI 算力": ["GPU 集群", "高速互连", "液冷", "先进封装"],
    "创新药": ["临床管线", "适应症扩展", "医保谈判", "出海授权"],
    "半导体": ["设备国产化", "先进制程", "EDA", "材料"],
    "机器人": ["具身智能", "减速器", "伺服系统", "传感器"],
    "新能源": ["储能", "电网消纳", "锂电材料", "光伏逆变器"],
}


def discover_theme(request: dict[str, Any]) -> dict[str, Any]:
    topic = request["topic"]
    signals = THEME_SIGNALS.get(topic, ["需求变化", "供给约束", "政策催化", "竞争格局"])
    return {
        "component": "theme_discovery",
        "topic": topic,
        "methodology_refs": ["docs/methodology/theme-expansion.md"],
        "prompt_refs": ["prompts/hot-topic/theme-expansion.md"],
        "signals": signals,
        "research_questions": [
            f"{topic} 的需求扩张是否有可验证证据？",
            f"{topic} 的产业链约束是否构成可持续瓶颈？",
            f"{topic} 的风险和反方证据是什么？",
        ],
    }
