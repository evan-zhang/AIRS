"""Memory route handler."""

from __future__ import annotations

from runtime.memory_manager import MemoryManager


DISCLAIMER = "AIRS Memory API 仅用于研究过程记忆展示，不构成投资建议。"


def handle_memory() -> dict[str, object]:
    memory = MemoryManager()
    memory.remember("release-001", "platform_status", {"status": "productized", "version": "1.0.0"})
    return {"status": "ok", "memory": memory.recall("release-001"), "disclaimer": DISCLAIMER}

