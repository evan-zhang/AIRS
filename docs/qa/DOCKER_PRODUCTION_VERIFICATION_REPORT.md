# AIRS Docker Production Verification Report

日期：2026-07-11

范围：QA Sprint 4 Docker Production Verification，基于 PR #10、分支 `qa/architecture-stabilization`、提交 `cf1d5ec`。

免责声明：本报告仅用于 AIRS 工程质量检查和发布治理，不构成投资建议。

## QA Sprint 5 Re-run Update

Re-run 时间：2026-07-11

Re-run 基准：

- 分支：`qa/architecture-stabilization`
- PR：#10
- 提交：`5a7528d`
- 目标：Docker Release Gate Re-run

完整日志目录：

- `docs/testing/logs/docker-release-gate-rerun/`

Sprint 5 结论：FAIL。

Docker daemon 仍可用，但 `docker pull python:3.11-slim` 超过 150 秒无进度输出后被终止。本地仍不存在 `python:3.11-slim`，因此没有可记录的基础镜像 digest。由于 Base image pull 是 Stable 放行硬门槛，后续 `docker compose build --no-cache`、`docker compose up -d`、容器 health check、Docker API security、容器内 CLI/APP/Core 和 restart/down-up 验证均未执行，且不得使用旧缓存或未经确认的第三方镜像绕过。

Sprint 5 结果矩阵：

- Base image pull：FAIL
- Base image source：official `docker.io/library/python:3.11-slim`
- Base image digest：Unavailable，镜像未成功拉取且本地未预载
- Docker build：NOT RUN，base image pull failed
- Compose startup：NOT RUN
- Health check：NOT RUN
- API security in Docker：NOT RUN
- CLI / APP / Core in Docker：NOT RUN
- Real Connector in Docker：NOT RUN
- Restart / down-up：NOT RUN
- Host regression：PASS

Sprint 5 对照回归：

- `10-pytest.log`：PASS
- `11-validate-stable-release.log`：PASS
- `12-production-check.log`：PASS
- `13-cli-validate-all.log`：PASS
- `14-production-e2e-failure-injection.log`：PASS

发布影响：QA Sprint 5 未解除 Docker 阻塞项。AIRS 仍不允许发布 `v1.0.0 Stable`。

## Executive Summary

本轮验证确认 Docker daemon 已可用，Compose 配置可解析，主机侧回归、API 安全、CLI、APP-001/Core gate、Real Connector probe、Production E2E 和 Failure Injection 均通过。

唯一未完成的发布阻塞项仍然是 Docker 镜像真实构建：`docker compose build --no-cache` 卡在 `docker.io/library/python:3.11-slim` 元数据/基础镜像拉取阶段。独立 `docker pull python:3.11-slim` 90 秒超时；HTTP 直连 registry endpoint 可返回 Docker registry 401 challenge，说明不是 AIRS Dockerfile 语法或应用代码错误，而是 Docker daemon/registry 拉取路径不可用。

因此，本轮不能把 Docker build、Compose startup、容器 health check 或容器内验证记为 PASS。

## Environment

- Git branch：`qa/architecture-stabilization`
- PR：#10
- Base commit：`cf1d5ec`
- Docker client：28.5.1
- Docker server：28.5.1
- Docker compose：v2.40.2-desktop.1
- Docker daemon：PASS，可通过 `docker info`
- Compose file：`docker/docker-compose.yml`
- 测试 API key：`qa-docker-secret`

完整日志目录：

- `docs/testing/logs/docker-production-verification/`

## Verification Matrix

### 1. Docker version and daemon status

结果：PASS

证据：

- `01-docker-version-daemon.log`
- `docker info` 返回 server version、linux/aarch64、CPU 和 memory 信息。

### 2. Cleanup old containers, networks, volumes, test images

结果：PASS

证据：

- `02-cleanup.log`
- 使用 `AIRS_API_KEY=qa-docker-secret docker compose down --volumes --remove-orphans`
- 删除历史测试镜像命令执行完成。

说明：未设置 `AIRS_API_KEY` 时 Compose 会拒绝解析配置，这是预期安全约束。

### 3. Docker compose build --no-cache

结果：FAIL

命令：

- `AIRS_API_KEY=qa-docker-secret docker compose build --no-cache`

证据：

- `03-compose-build-no-cache.log`
- 日志停在 `load metadata for docker.io/library/python:3.11-slim`
- 该 build 进程长时间无输出，最终被手工终止，退出码 130。

补充诊断：

- `03a-registry-pull-diagnosis.log`：`docker pull python:3.11-slim` 90 秒超时。
- `03b-registry-http-diagnosis.log`：`curl -I https://registry-1.docker.io/v2/` 返回 Docker registry 401 challenge，HTTP 路径可达。
- `03c-compose-build-no-cache-legacy.log`：`DOCKER_BUILDKIT=0 docker compose build --no-cache` 240 秒超时。

根因判断：Docker daemon/registry 拉取路径不可用或极慢，阻塞基础镜像解析。未发现 AIRS Dockerfile 或应用代码缺陷。

### 4. Docker compose up -d

结果：NOT RUN

原因：镜像构建失败，不能启动真实 compose 服务；不得使用旧镜像或缓存伪造 PASS。

### 5. Container status, health check, startup logs, port listening, env loading

结果：NOT RUN

原因：Compose 服务未启动。`docker compose config` 已通过，仅能证明配置可解析，不能证明容器运行。

证据：

- `04-compose-config.log`

### 6. Docker API verification

结果：NOT RUN

未执行项：

- `/health`
- 未鉴权请求拒绝
- 正确 API key 请求成功
- 请求大小限制
- 限流
- 错误脱敏

原因：容器未启动。主机侧对照验证通过，见 `15-host-api-security.log`，但不计入 Docker API PASS。

### 7. In-container CLI / APP / Core / Real Connector

结果：NOT RUN

原因：容器未启动。

主机侧对照验证：

- `16-host-cli-init-demo-validate.log`：PASS
- `17-host-app001-core-realdata-gate.log`：PASS，real-data degraded gate 返回 exit code 1，符合预期。
- `18-real-connector-probe.log`：PASS

这些结果仅作为非容器回归证据，不计入容器内验证 PASS。

### 8. Container restart and service recovery

结果：NOT RUN

原因：Compose 服务未启动。

### 9. docker compose down then up repeatability

结果：NOT RUN

原因：Compose 服务未启动。

### 10. Regression

结果：PASS for host regression

证据：

- `10-pytest.log`：`4 passed, 1 skipped`
- `11-validate-stable-release.log`：PASS
- `12-production-check.log`：PASS
- `13-cli-validate-all.log`：PASS
- `14-production-e2e-failure-injection.log`：PASS

说明：这些验证在主机环境执行。由于 Docker build 失败，不能替代容器级回归。

## Mock / SKIP / Fallback Handling

- Mock、SKIP、Fallback 未计入 Docker production PASS。
- APP-001 real-data gate 在降级数据下返回 `failed_quality_gate`，exit code 1。
- Real Connector probe 通过 `AIRS_RUN_REAL_CONNECTOR_PROBE=1` 执行。
- Docker build 未通过，因此所有容器内项目均保持 NOT RUN，不伪造通过。

## Root Cause

本轮失败根因不是 AIRS 代码，而是 Docker daemon 无法在限定时间内通过自身 registry 拉取路径完成 `python:3.11-slim` 基础镜像解析/下载。

关键证据：

- Docker daemon 已可用。
- Compose 配置可解析。
- HTTPS 到 registry endpoint 可达。
- Docker pull 和 BuildKit/legacy build 都在基础镜像阶段超时。
- 本地不存在 `python:3.11-slim`，不能离线构建。

## Result

- Docker build：FAIL
- Compose startup：NOT RUN
- Health check：NOT RUN
- API security in Docker：NOT RUN
- CLI / APP / Core in Docker：NOT RUN
- Regression on host：PASS

## Release Impact

QA Sprint 4 未解除 Docker verification 阻塞项。

AIRS 不应发布 `v1.0.0 Stable`，直到在 Docker daemon 可以正常拉取基础镜像的环境中重新执行：

- `docker compose build --no-cache`
- `docker compose up -d`
- container health check
- Docker API security checks
- container CLI / APP / Core / Real Connector checks
- restart and down/up repeatability checks
