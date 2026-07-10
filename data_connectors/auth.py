"""Authentication Framework for AIRS connectors."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class AuthConfig:
    auth_type: str = "none"
    api_key: str | None = None
    token: str | None = None
    username: str | None = None
    password: str | None = None


class Authenticator:
    """把认证配置转为请求上下文；不会把密钥写入结果。"""

    def headers(self, config: AuthConfig) -> dict[str, str]:
        if config.auth_type == "none":
            return {}
        if config.auth_type == "api_key" and config.api_key:
            return {"X-API-Key": config.api_key}
        if config.auth_type == "bearer_token" and config.token:
            return {"Authorization": f"Bearer {config.token}"}
        if config.auth_type == "basic" and config.username and config.password:
            return {"Authorization": "Basic ***"}
        raise ValueError(f"unsupported or incomplete auth config: {config.auth_type}")
