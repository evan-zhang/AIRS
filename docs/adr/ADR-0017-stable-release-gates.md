# ADR-0017: Stable Release Gates and Degraded Data Policy

**状态**：Accepted
**日期**：2026-07-10
**归属 Milestone**：QA Sprint 3 Stable Release Remediation

免责声明：本 ADR 仅用于 AIRS 工程质量治理，不构成投资建议。

## Context（背景）

Release Readiness Review 指出：AIRS 现有 Production E2E 能证明结构链路可运行，但不能证明真实生产数据链路成立。Mock、SKIP、Fallback 在本地 demo 中有价值，但不得计入 Stable 真实生产 PASS。

同时，API 已具备 API key、CORS allowlist 和 body size limit，但缺少 rate limiting 和更统一的错误脱敏验证。Docker compose 也需要 health check 证明容器内鉴权 API 可用。

## Decision（决策）

1. 新增 `common/release_gate.py`，将 `mock`、`skip`、`fallback_*`、`unknown` 统一视为 degraded source。
2. `summarize_data_lineage()` 输出 real/degraded 计数和 degraded source 明细。
3. APP-001 支持显式 `require_real_data`，并输出 `stable_release_gate`。
4. CLI `airs run --real-data` 在 Stable gate 失败时返回非 0。
5. Production E2E artifact 必须包含 `stable_release_gate`，结构性 PASS 与 Stable real-data PASS 分离。
6. Connector real-mode fallback 必须标记为 `fallback_mock`，不得伪装成 ordinary mock 或 real。
7. API 新增每客户端/API key 的分钟级 rate limit，invalid JSON 默认脱敏。
8. Docker compose 新增带 API key 的 `/health` healthcheck。
9. 新增 `scripts/validate_stable_release.py`，验证 degraded data 不能计入 Stable PASS；外部真实源探测如果未执行或不可用，必须记录为 UNVERIFIED。

## Alternatives（备选方案）

- 直接移除 Mock：放弃。AIRS 仍需要无凭证本地 demo 和离线回归能力。
- 将所有真实源失败变为 hard error：部分采用。Stable gate 会 hard fail，但 demo/profile 仍允许 degraded completion。
- 在 QA Sprint 3 直接抽象完整 Score Engine / Core builders：放弃。该范围超出“不新增业务功能、不重构”的约束。

## Consequences（影响）

正面影响：

- Stable gate 不再把 mock/SKIP/fallback 误判为真实生产通过。
- CLI、API、E2E 和报告都能看到 stable release gate 状态。
- 真实外部源不可用时会被记录为未验证，而不是伪造通过。

限制：

- APP-001 仍是 Core-assisted，而非完全 Core-driven。
- Score Engine runtime consolidation 仍需后续处理。
- Docker daemon 不可用的环境中仍无法完成 image build / compose up 验证。

## Validation（验证）

- `python3 scripts/validate_stable_release.py`
- `python3 scripts/run_production_tests.py`
- `python3 scripts/validate_e2e.py`
- `python3 cli/airs.py --json run ... --real-data` 应在 degraded sources 存在时返回 exit 1。
- API 本地测试覆盖 401、200、429、413 和 invalid JSON 脱敏。
- Docker compose config 可离线解析；image build / compose health 必须在 Docker daemon 可用环境执行。
