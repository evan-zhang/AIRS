# AIRS Config

免责声明：AIRS 配置中心仅用于研究流程编排、Connector、缓存、Workspace 和 Demo 模式管理，不构成投资建议。

`config/airs.yaml` 是 Platform 1.0 的本地 demo/profile 配置文件，默认允许 Mock Connector，用于无凭证环境的结构验证和演示。

`config/airs.stable.yaml` 是 Stable 发布门禁 profile，默认要求 real connector mode。Stable 发布不得把 Mock、SKIP、Fallback 计入真实生产 PASS。

配置文件覆盖：

- `platform`：版本与 Demo 模式。
- `workspace`：研究资产目录。
- `cache`：缓存开关、路径和 TTL。
- `api` / `web`：服务端口。
- `connectors`：Mock / Real Connector 模式。
- `models`：模型提供方占位配置，默认标准库规则编排。
- `secrets`：环境变量名称，不保存真实密钥。
- `compliance`：免责声明与禁止输出。

本文件不保存真实 API Key。请复制 `.env.example` 为 `.env` 后在本地填写密钥。
