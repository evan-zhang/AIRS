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

Status: Pending CI run.

This report will be updated after GitHub Actions completes.

## Release Impact

Until the CI Docker Release Gate run completes successfully, AIRS remains not approved for `v1.0.0 Stable`.
