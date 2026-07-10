"""Minimal urllib HTTP client for real Connector integrations."""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Any

from .base import RetryPolicy
from .env_config import EnvConfig
from .secret_masking import mask_url


class HTTPClientError(RuntimeError):
    def __init__(self, message: str, *, status_code: int | None = None, retryable: bool = False) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.retryable = retryable


@dataclass
class HTTPResponse:
    url: str
    status_code: int
    headers: dict[str, str]
    text: str

    def json(self) -> dict[str, Any]:
        parsed = json.loads(self.text)
        if not isinstance(parsed, dict):
            raise HTTPClientError("JSON response is not an object", retryable=False)
        return parsed


@dataclass
class HTTPClient:
    connector_id: str
    timeout_seconds: float = 8.0
    retry_policy: RetryPolicy = field(default_factory=RetryPolicy)
    min_interval_seconds: float = 0.0
    user_agent: str = "AIRS Real Data Integration/0.1 contact=airs@example.invalid"
    _last_request_at: float = 0.0

    @classmethod
    def from_env(cls, connector_id: str, retry_policy: RetryPolicy) -> "HTTPClient":
        env = EnvConfig()
        return cls(
            connector_id=connector_id,
            timeout_seconds=env.get_float("AIRS_HTTP_TIMEOUT_SECONDS", 8.0),
            retry_policy=retry_policy,
            min_interval_seconds=env.get_float(f"AIRS_{connector_id.upper()}_RATE_LIMIT_SECONDS", env.get_float("AIRS_RATE_LIMIT_SECONDS", 0.0)),
            user_agent=env.get("AIRS_HTTP_USER_AGENT", "AIRS Real Data Integration/0.1 contact=airs@example.invalid") or "",
        )

    def get(self, url: str, *, headers: dict[str, str] | None = None, params: dict[str, Any] | None = None, secrets: list[str | None] | None = None) -> HTTPResponse:
        full_url = self._url_with_params(url, params or {})
        attempt = 0
        delay = self.retry_policy.initial_delay_seconds
        last_error: HTTPClientError | None = None
        while attempt < self.retry_policy.max_attempts:
            attempt += 1
            self._respect_rate_limit()
            try:
                return self._get_once(full_url, headers=headers or {})
            except HTTPClientError as exc:
                last_error = exc
                if not exc.retryable or attempt >= self.retry_policy.max_attempts:
                    break
                time.sleep(delay)
                delay *= self.retry_policy.backoff_multiplier
        safe_url = mask_url(full_url, secrets or [])
        if last_error:
            raise HTTPClientError(f"{last_error} url={safe_url}", status_code=last_error.status_code, retryable=last_error.retryable) from last_error
        raise HTTPClientError(f"request failed url={safe_url}", retryable=True)

    def _get_once(self, url: str, *, headers: dict[str, str]) -> HTTPResponse:
        safe_headers = {"User-Agent": self.user_agent, "Accept": "*/*", **headers}
        request = urllib.request.Request(url, headers=safe_headers, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                body = response.read().decode(response.headers.get_content_charset() or "utf-8", errors="replace")
                return HTTPResponse(url=url, status_code=response.status, headers=dict(response.headers.items()), text=body)
        except urllib.error.HTTPError as exc:
            retryable = exc.code in {408, 409, 425, 429, 500, 502, 503, 504}
            raise HTTPClientError(f"HTTP {exc.code}", status_code=exc.code, retryable=retryable) from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise HTTPClientError(str(exc), retryable=True) from exc

    def _respect_rate_limit(self) -> None:
        if self.min_interval_seconds <= 0:
            return
        now = time.monotonic()
        wait_for = self.min_interval_seconds - (now - self._last_request_at)
        if wait_for > 0:
            time.sleep(wait_for)
        self._last_request_at = time.monotonic()

    def _url_with_params(self, url: str, params: dict[str, Any]) -> str:
        if not params:
            return url
        clean = {key: value for key, value in params.items() if value is not None}
        query = urllib.parse.urlencode(clean, doseq=True)
        separator = "&" if urllib.parse.urlparse(url).query else "?"
        return f"{url}{separator}{query}"
