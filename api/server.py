#!/usr/bin/env python3
"""AIRS Platform 1.0 REST API server based on Python stdlib."""

from __future__ import annotations

import argparse
import json
import sys
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


class AIRSRequestHandler(BaseHTTPRequestHandler):
    server_version = "AIRSHTTP/1.0"

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length == 0:
            return {}
        raw = self.rfile.read(length).decode("utf-8")
        return json.loads(raw) if raw.strip() else {}

    def _send(self, status: int, payload: dict[str, Any]) -> None:
        payload.setdefault("disclaimer", DISCLAIMER)
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:  # noqa: N802
        self._send(200, {"status": "ok"})

    def do_GET(self) -> None:  # noqa: N802
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
            self._send(500, {"error": "internal_error", "message": str(exc)})

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        try:
            if path in {"/research", "/company", "/theme", "/report"}:
                self._send(200, handle_research(path, self._read_json()))
            else:
                self._send(404, {"error": "not_found", "path": path})
        except json.JSONDecodeError as exc:
            self._send(400, {"error": "invalid_json", "message": str(exc)})
        except Exception as exc:  # noqa: BLE001
            self._send(500, {"error": "internal_error", "message": str(exc)})

    def log_message(self, fmt: str, *args: object) -> None:
        sys.stderr.write("AIRS API - " + fmt % args + "\n")


def run_server(host: str = "0.0.0.0", port: int = 8765) -> None:
    httpd = ThreadingHTTPServer((host, port), AIRSRequestHandler)
    print(f"AIRS API listening on http://{host}:{port}")
    print(f"免责声明：{DISCLAIMER}")
    httpd.serve_forever()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run AIRS REST API server.")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)
    run_server(args.host, args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

