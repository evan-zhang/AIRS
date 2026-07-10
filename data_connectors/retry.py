"""Retry and backoff helpers."""
from __future__ import annotations

# Connector retry helper used by production and failure-injection validation.
from time import sleep
from typing import Callable, TypeVar
from .base import RetryPolicy

T = TypeVar("T")


def run_with_retry(fn: Callable[[], T], policy: RetryPolicy) -> T:
    delay = policy.initial_delay_seconds
    last_error: Exception | None = None
    for attempt in range(1, policy.max_attempts + 1):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt == policy.max_attempts:
                break
            sleep(delay)
            delay *= policy.backoff_multiplier
    assert last_error is not None
    raise last_error
