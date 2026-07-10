"""Health route handler."""

from __future__ import annotations

import sys


DISCLAIMER = "AIRS Health API 仅用于工程状态检查，不构成投资建议。"


def handle_health() -> dict[str, object]:
    return {
        "status": "ok",
        "service": "airs-api",
        "version": "1.0.0",
        "python": sys.version.split()[0],
        "endpoints": ["GET /health", "GET /workspace", "GET /memory", "POST /research", "POST /company", "POST /theme", "POST /report"],
        "disclaimer": DISCLAIMER,
    }

