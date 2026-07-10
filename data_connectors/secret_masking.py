"""Secret masking helpers for Connector runtime output."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

SECRET_KEY_HINTS = ("key", "token", "secret", "password", "authorization", "api_key")


def mask_secret(value: str | None) -> str | None:
    """Return a display-safe representation of a secret value."""

    if value is None:
        return None
    if len(value) <= 8:
        return "***"
    return f"{value[:4]}...{value[-4:]}"


def mask_url(url: str, secrets: Sequence[str | None] = ()) -> str:
    masked = url
    for secret in secrets:
        if secret:
            masked = masked.replace(secret, mask_secret(secret) or "***")
    return masked


def mask_mapping(payload: Any) -> Any:
    """Recursively mask values whose key names look like credentials."""

    if isinstance(payload, Mapping):
        safe: dict[str, Any] = {}
        for key, value in payload.items():
            if any(hint in str(key).lower() for hint in SECRET_KEY_HINTS):
                safe[str(key)] = mask_secret(str(value)) if value is not None else None
            else:
                safe[str(key)] = mask_mapping(value)
        return safe
    if isinstance(payload, list):
        return [mask_mapping(item) for item in payload]
    if isinstance(payload, tuple):
        return tuple(mask_mapping(item) for item in payload)
    return payload
