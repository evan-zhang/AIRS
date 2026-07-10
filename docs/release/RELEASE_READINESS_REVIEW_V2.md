# AIRS Release Readiness Review V2

Review date: 2026-07-10

Scope: QA Sprint 3 Stable Release Remediation review for PR #10 on `qa/architecture-stabilization`.

Disclaimer: This review evaluates software release readiness only. It does not constitute investment advice.

## Executive Summary

QA Sprint 3 materially remediated the most important Stable blockers from `docs/release/RELEASE_READINESS_REVIEW.md`.

The biggest improvement is semantic: AIRS now separates demo/structural PASS from Stable real-data PASS. Mock, SKIP, Fallback, and Unknown sources are explicitly degraded and cannot satisfy the Stable release gate.

Existing local validations pass, but Docker daemon is unavailable in the current environment, so Docker image build, compose startup, and container health check remain unverified.

## Release Decision

Decision: Conditional Approve.

Condition: Do not tag or announce `v1.0.0 Stable` until a human reviewer verifies Docker image build, Docker compose startup, and API container health check in an environment with Docker daemon available.

## 已修复 Blocker

### B1. Production E2E does not prove real production behavior

Status: Fixed for gate semantics.

Evidence:

- `common/release_gate.py`
- `tests/production-e2e/e2e_harness.py`
- `scripts/validate_e2e.py`
- `scripts/validate_stable_release.py`

Result: Production E2E artifacts now carry `stable_release_gate`. Degraded sources cannot be counted as Stable real-data PASS.

### B2. Default platform configuration is demo/mock

Status: Fixed.

Evidence:

- `config/airs.yaml` remains demo/local profile.
- `config/airs.stable.yaml` added as Stable gate profile.
- `config/README.md` explains profile split.

### B3. Runtime is not a true research execution runtime

Status: Mitigated, not fully eliminated.

Evidence:

- CLI/API/App expose `stable_release_gate` and data lineage.
- V2 docs no longer claim Runtime trace alone proves Stable production research.

Remaining: Full Core-driven runtime execution is deferred.

### B4. Internal release documentation is contradictory

Status: Fixed.

Evidence:

- `docs/production/FINAL_REVIEW.md` now points to this V2 review as the final Stable decision.
- `docs/qa/STABLE_RELEASE_REMEDIATION_REPORT.md` and `docs/review/STABLE_RELEASE_SELF_REVIEW.md` record the latest state.

## 剩余 High Risk

### H1/H2/H3. APP/Core/Score runtime consolidation

Status: Remaining risk, accepted for conditional Stable only if release notes keep AIRS positioned as a governed local research workflow platform, not a fully generalized runtime engine.

Reason: APP-001 still constructs parts of Evidence/KG/Score locally, although validators and gate semantics now reduce drift risk.

### H6. Docker runtime verification

Status: Unverified.

Reason: Docker daemon is not available in this environment.

Impact: Stable release must wait for human Docker verification.

## 未验证项目

- Docker image build: not verified because Docker daemon is unavailable.
- Docker compose startup: not verified because Docker daemon is unavailable.
- Docker container `/health`: not verified because Docker daemon is unavailable.
- News real connector with production endpoint: not verified because no `NEWS_API_ENDPOINT` / credentials were supplied.

## Verification Results

Passed:

- `python3 scripts/validate_stable_release.py`
- `AIRS_RUN_REAL_CONNECTOR_PROBE=1 python3 scripts/validate_stable_release.py`
- `python3 scripts/run_production_tests.py`
- `python3 scripts/validate_e2e.py`
- `python3 cli/airs.py init --output .airs/qa-sprint3.yaml --force`
- `python3 cli/airs.py demo nvidia --output-dir demo/output/qa-sprint3`
- `python3 cli/airs.py validate --all`
- `python3 scripts/production_check.py`
- `python3 -m pytest -q`
- API local security checks: 401, 200, 429, 413, invalid JSON redaction
- `AIRS_API_KEY=qa-secret docker compose -f docker/docker-compose.yml config`

Failed / unavailable:

- `docker build -f docker/Dockerfile -t airs-qa-sprint3 .`: unavailable, Docker daemon not reachable.

## 是否允许发布 v1.0.0 Stable

Not yet.

AIRS may proceed to human release review for `v1.0.0 Stable`, but the Stable tag/release should wait until Docker build, compose startup, and container health are verified by a human reviewer in a Docker-enabled environment.

Final answer: AIRS is conditionally ready for Stable after the Docker verification condition is satisfied. It is not approved for automatic Stable release from the current environment.
