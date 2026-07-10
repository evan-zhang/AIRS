"""Environment and .env configuration for real Connector integrations."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_FILE = ROOT / ".env"


class EnvConfig:
    """Small .env reader that never writes or logs secret values."""

    def __init__(self, env_file: str | Path | None = None) -> None:
        self.env_file = Path(env_file) if env_file else DEFAULT_ENV_FILE
        self._file_values = self._read_env_file(self.env_file)

    def _read_env_file(self, path: Path) -> dict[str, str]:
        if not path.exists():
            return {}
        values: dict[str, str] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
        return values

    def get(self, key: str, default: str | None = None) -> str | None:
        return os.environ.get(key, self._file_values.get(key, default))

    def get_int(self, key: str, default: int) -> int:
        value = self.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default

    def get_float(self, key: str, default: float) -> float:
        value = self.get(key)
        if value is None:
            return default
        try:
            return float(value)
        except ValueError:
            return default

    def mode_for(self, connector_id: str) -> str:
        specific = self.get(f"AIRS_{connector_id.upper()}_MODE")
        return (specific or self.get("AIRS_CONNECTOR_MODE", "mock") or "mock").strip().lower()

    def real_enabled(self, connector_id: str, query: dict[str, Any] | None = None) -> bool:
        query_mode = str((query or {}).get("mode", "")).strip().lower()
        if query_mode in {"real", "mock"}:
            return query_mode == "real"
        return self.mode_for(connector_id) == "real"

    def endpoint_for(self, key: str, default: str) -> str:
        return self.get(key, default) or default
