#!/usr/bin/env python3
"""AIRS Platform 1.0 REST API server based on Python stdlib."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from api.routes.health import handle_health
from api.routes.memory import handle_memory
from api.routes.research import handle_research
from api.routes.workspace import handle_workspace


DISCLAIMER = "AIRS API 仅用于投资研究流程编排、证据追溯和质量控制，不构成投资建议。"
DEFAULT_MAX_BODY_BYTES = 1_048_576
LOCAL_HOSTS = {"127.0.0.1", "localhost", "::1"}
RATE_BUCKETS: dict[str, list[float]] = {}


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _security_config() -> dict[str, Any]:
    api_key = os.environ.get("AIRS_API_KEY", "").strip()
    origins = [item.strip() for item in os.environ.get("AIRS_CORS_ALLOW_ORIGINS", "http://localhost:8080,http://127.0.0.1:8080").split(",") if item.strip()]
    return {
        "api_key": api_key,
        "cors_origins": origins,
        "max_body_bytes": int(os.environ.get("AIRS_MAX_BODY_BYTES", str(DEFAULT_MAX_BODY_BYTES))),
        "expose_errors": _env_bool("AIRS_EXPOSE_ERRORS", False),
        "rate_limit_per_minute": int(os.environ.get("AIRS_RATE_LIMIT_PER_MINUTE", "120")),
    }


class AIRSRequestHandler(BaseHTTPRequestHandler):
    server_version = "AIRSHTTP/1.0"

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0") or "0")
        max_body = self.server.security_config["max_body_bytes"]  # type: ignore[attr-defined]
        if length > max_body:
            raise ValueError(f"request body too large: {length} > {max_body}")
        if length == 0:
            return {}
        raw = self.rfile.read(length).decode("utf-8")
        return json.loads(raw) if raw.strip() else {}

    def _send(self, status: int, payload: dict[str, Any]) -> None:
        payload.setdefault("disclaimer", DISCLAIMER)
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        origin = self.headers.get("Origin", "")
        allowed_origins = self.server.security_config["cors_origins"]  # type: ignore[attr-defined]
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        if origin and origin in allowed_origins:
            self.send_header("Access-Control-Allow-Origin", origin)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-AIRS-API-Key")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _authorized(self) -> bool:
        api_key = self.server.security_config["api_key"]  # type: ignore[attr-defined]
        if not api_key:
            return True
        bearer = self.headers.get("Authorization", "")
        header_key = self.headers.get("X-AIRS-API-Key", "")
        return header_key == api_key or bearer == f"Bearer {api_key}"

    def _rate_limited(self) -> bool:
        limit = self.server.security_config["rate_limit_per_minute"]  # type: ignore[attr-defined]
        if limit <= 0:
            return False
        client = self.client_address[0] if self.client_address else "unknown"
        api_key = self.headers.get("X-AIRS-API-Key") or self.headers.get("Authorization") or "anonymous"
        bucket_key = f"{client}:{api_key}"
        now = time.monotonic()
        window_start = now - 60
        bucket = [item for item in RATE_BUCKETS.get(bucket_key, []) if item >= window_start]
        if len(bucket) >= limit:
            RATE_BUCKETS[bucket_key] = bucket
            return True
        bucket.append(now)
        RATE_BUCKETS[bucket_key] = bucket
        return False

    def _send_error(self, status: int, code: str, exc: Exception | None = None) -> None:
        expose = self.server.security_config["expose_errors"]  # type: ignore[attr-defined]
        payload = {"error": code}
        if expose and exc:
            payload["message"] = str(exc)
        self._send(status, payload)

    def do_OPTIONS(self) -> None:  # noqa: N802
        self._send(200, {"status": "ok"})

    def do_GET(self) -> None:  # noqa: N802
        if not self._authorized():
            self._send(401, {"error": "unauthorized"})
            return
        if self._rate_limited():
            self._send(429, {"error": "rate_limited"})
            return
        path = urlparse(self.path).path
        try:
            if path == "/health":
                self._send(200, handle_health())
            elif path == "/workspace":
                self._send(200, handle_workspace())
            elif path == "/memory":
                self._send(200, handle_memory())
            else:
                self._send(404, {"error": "not_found", "path": path})
        except Exception as exc:  # noqa: BLE001
            self._send_error(500, "internal_error", exc)

    def do_POST(self) -> None:  # noqa: N802
        if not self._authorized():
            self._send(401, {"error": "unauthorized"})
            return
        if self._rate_limited():
            self._send(429, {"error": "rate_limited"})
            return
        path = urlparse(self.path).path
        try:
            if path in {"/research", "/company", "/theme", "/report"}:
                self._send(200, handle_research(path, self._read_json()))
            else:
                self._send(404, {"error": "not_found", "path": path})
        except json.JSONDecodeError as exc:
            self._send_error(400, "invalid_json", exc)
        except ValueError as exc:
            self._send_error(413 if "too large" in str(exc) else 400, "invalid_request", exc)
        except Exception as exc:  # noqa: BLE001
            self._send_error(500, "internal_error", exc)

    def log_message(self, fmt: str, *args: object) -> None:
        sys.stderr.write("AIRS API - " + fmt % args + "\n")


def validate_bind_security(host: str) -> None:
    if host in LOCAL_HOSTS:
        return
    if os.environ.get("AIRS_API_KEY", "").strip():
        return
    raise RuntimeError("Refusing non-local bind without AIRS_API_KEY; set an API key or bind to 127.0.0.1")


def run_server(host: str = "127.0.0.1", port: int = 8765) -> None:
    validate_bind_security(host)
    httpd = ThreadingHTTPServer((host, port), AIRSRequestHandler)
    httpd.timeout = float(os.environ.get("AIRS_REQUEST_TIMEOUT_SECONDS", "30"))
    httpd.security_config = _security_config()  # type: ignore[attr-defined]
    print(f"AIRS API listening on http://{host}:{port}")
    print(f"免责声明：{DISCLAIMER}")
    httpd.serve_forever()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run AIRS REST API server.")
    parser.add_argument("--host", default=os.environ.get("AIRS_API_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)
    run_server(args.host, args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
