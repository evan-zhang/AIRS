"""Company discovery component for investment research."""

from __future__ import annotations

from typing import Any


COMPANIES = {
    "AI 算力": ["ComputeInfra A", "OpticalLink B", "CoolingSystem C"],
    "创新药": ["BioPipeline A", "ClinicalCRO B", "LicenseOut C"],
    "半导体": ["SemiEquipment A", "Materials B", "FoundryService C"],
    "机器人": ["RobotIntegrator A", "Reducer B", "ServoControl C"],
    "新能源": ["StorageSystem A", "Inverter B", "BatteryMaterial C"],
}


def discover_companies(theme: dict[str, Any]) -> dict[str, Any]:
    topic = theme["topic"]
    companies = COMPANIES.get(topic, ["Company A", "Company B", "Company C"])
    return {
        "component": "company_discovery",
        "methodology_refs": ["docs/methodology/financial-anomaly.md", "docs/methodology/management-quality.md"],
        "connector_refs": ["docs/data-connectors/connector-interface.md"],
        "companies": [
            {"name": name, "role": role, "evidence_ref": f"ev-{idx + 1:02d}"}
            for idx, (name, role) in enumerate(zip(companies, theme["signals"][:3]))
        ],
    }
