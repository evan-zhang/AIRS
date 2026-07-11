# AIRS CI Docker Production Verification Report

日期：2026-07-11

范围：QA Sprint 6 CI Docker Production Verification，基于 PR #10、分支 `qa/architecture-stabilization`。

免责声明：本报告仅用于 AIRS 工程质量检查和发布治理，不构成投资建议。

## Objective

本 Sprint 将 Docker Release Gate 从本机迁移到 GitHub Hosted Ubuntu Runner，避免本机 Docker Hub 拉取路径不稳定导致无法验证。

## Workflow

- Workflow file: `.github/workflows/docker-release-gate.yml`
- Runner: GitHub Hosted `ubuntu-latest`
- Trigger: PR #10 / branch `qa/architecture-stabilization`
- Base image: official `docker.io/library/python:3.11-slim`
- Third-party image replacement: not allowed and not configured
- Logs: `docs/testing/logs/ci-docker-release-gate` inside the workflow workspace

## Required Gate Items

- Base image pull
- Base image digest recording
- Docker compose build without cache
- Docker compose startup
- Container health check
- API `/health`
- API authentication
- API body size limit
- API rate limit
- API error redaction
- Container CLI init / validate / demo nvidia
- APP-001 to Core real-data gate
- Real Connector probe
- Container restart recovery
- Compose down/up repeatability
- Runner pytest
- Runner `production_check.py`
- Runner `validate_stable_release.py`
- Runner all `validate_*`
- Runner Production E2E
- Runner Failure Injection

## Current Status

Status: PASS.

Workflow run:

- Workflow URL: `https://github.com/evan-zhang/AIRS/actions/runs/29134097553`
- Run ID: `29134097553`
- Event: `pull_request`
- Commit SHA: `9baf6ffdf41162616294ba011cc1c1a69b8c8650`
- Job: `Docker production verification`
- Job result: `success`
- Started: `2026-07-11T01:09:11Z`
- Completed: `2026-07-11T01:11:35Z`

Base image:

- Source: official `docker.io/library/python:3.11-slim`
- Image ID: `sha256:f29b0d4ca7e6b86c482429892631ffb0d50be331ddadcfba29bb07082f3d0a67`
- Repo digest: `python@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3`
- OS/Architecture: `linux/amd64`
- Third-party image replacement: not used
- Mirror/private registry: not used

Gate results:

- Base image pull: PASS
- Base image digest recording: PASS
- Docker compose build without cache: PASS
- Docker compose startup: PASS
- Container health check: PASS
- API `/health`: PASS
- API authentication: PASS
- API body size limit: PASS
- API rate limit: PASS
- API error redaction: PASS
- Container CLI init / validate / demo nvidia: PASS
- APP-001 to Core real-data gate: PASS
- Real Connector probe: PASS
- Container restart recovery: PASS
- Compose down/up repeatability: PASS
- Runner pytest: PASS
- Runner `production_check.py`: PASS
- Runner `validate_stable_release.py`: PASS
- Runner all `validate_*`: PASS
- Runner Production E2E: PASS
- Runner Failure Injection: PASS

Failure diagnostics artifact: not uploaded because the run succeeded.

## Release Impact

The CI Docker Release Gate passed. AIRS may proceed to human review for `v1.0.0 Stable` approval.
