# AIRS Release Readiness Review

Review date: 2026-07-10

Reviewer stance: independent Principal Architect / CTO final release audit. This review does not rely on the project history as proof of correctness and does not treat existing validation PASS results as sufficient evidence for Stable release.

Scope: repository-level release readiness for AIRS v1.0.0 Stable, covering architecture, implementation boundaries, duplicate implementations, runtime behavior, tests, security, performance, documentation consistency, demo-vs-real readiness, and release governance.

Disclaimer: This review evaluates software release readiness only. It does not constitute investment advice.

## Executive Summary

AIRS should not be released as `v1.0.0 Stable` in its current state.

The repository has substantial value as a specification repository, architecture prototype, and local demo platform. It contains broad documentation, validation scripts, CLI/API entry points, a runnable equity research app, mock-capable connectors, E2E harnesses, and release governance files. Existing checks pass:

- `python3 scripts/production_check.py`: `FINAL RESULT: PASS`
- `python3 scripts/validate_release.py`: `RESULT: PASS`
- `python3 -m pytest -q`: `4 passed, 1 skipped`

However, the Stable release decision must be based on production semantics, not only artifact completeness. The dominant risk is that AIRS presents itself as a productized investment research platform while several core paths still behave as specification/demo scaffolding:

- default connector mode is mock (`config/airs.yaml:31-40`);
- Yahoo Finance is explicitly mock-only and returns static AAPL data regardless of requested symbol (`data_connectors/connectors/yahoo_finance.py:34-67`);
- production E2E cases pass while accepting mock connector lineage (`tests/production-e2e/e2e_harness.py:294-301`);
- Runtime agents dispatch synthetic sessions rather than real research agent work (`runtime/task_dispatcher.py:15-29`);
- APP-001 constructs Evidence, KG, and Scorecard locally instead of using a single Core runtime source (`apps/equity_research/analyzer.py:20-154`);
- internal docs conflict: `docs/production/FINAL_REVIEW.md` recommends v1.0.0, while `docs/review/QA_ARCHITECTURE_SELF_REVIEW.md:66-74` and `docs/qa/ARCHITECTURE_STABILIZATION_REPORT.md:121-129` explicitly advise against Stable.

The appropriate release label is `v1.0.0-rc`, `developer preview`, or `v1.0.0 specification release`. It is not ready for `v1.0.0 Stable`.

## Release Decision

Decision: Reject for `v1.0.0 Stable`.

Conditional alternative: approve as `v1.0.0-rc` or `v1.0.0 Specification Repository` if release notes explicitly state that AIRS is not yet a complete production runtime platform and that real-data research is not a hard-gated capability.

## Blocker

### B1. Production E2E does not prove real production behavior

The E2E harness calls real module entrypoints, but it does not require real external data. Connector checks only require fields and disclaimer, not real source validity (`tests/production-e2e/e2e_harness.py:100-111`). The release check accepts any connector lineage if it has real, mock, or skipped sources (`tests/production-e2e/e2e_harness.py:294-301`).

Impact: AIRS can pass "Production E2E" while relying on mock data. This is acceptable for RC, not Stable.

Stable requirement: at least one release-gate E2E case must run in real mode with non-SKIP, non-mock critical sources, and the report must fail or become non-Stable if real data is unavailable.

### B2. Default platform configuration is demo/mock, not stable production

`config/airs.yaml` sets `platform.demo_mode: true` and connector mode to `mock` for the global connector layer and specific sources (`config/airs.yaml:4-40`). This is a clear release-mode mismatch.

Impact: a default install runs as a demo system while top-level docs claim v1.0 Production Release.

Stable requirement: Stable profile must be distinct from demo profile. Default user-facing commands should surface the active data mode and quality gate.

### B3. Runtime is not a true research execution runtime

Runtime dispatches registered agent definitions through `AgentSession` and lifecycle abstractions, but the dispatched tasks do not execute domain research logic. The runtime mostly records state, events, and synthetic outputs (`runtime/core.py:20-26`, `runtime/task_dispatcher.py:15-29`, `runtime/agent_registry.py:35-42`).

Impact: Planner -> Orchestrator -> Runtime can complete without proving that research work was actually executed by runtime agents.

Stable requirement: either downgrade the runtime claim in release materials or make Runtime execute at least one real business task that feeds the final report.

### B4. Internal release documentation is contradictory

`docs/production/FINAL_REVIEW.md:7-13` and `docs/production/FINAL_REVIEW.md:107-109` recommend v1.0.0 release. In contrast, `docs/review/QA_ARCHITECTURE_SELF_REVIEW.md:66-74` says current state should remain RC and not Stable, and `docs/qa/ARCHITECTURE_STABILIZATION_REPORT.md:121-129` says not to directly publish `v1.0.0 Stable`.

Impact: release governance cannot be trusted as a single decision record.

Stable requirement: reconcile release decision documents before tagging Stable.

## High Risk

### H1. APP-001 is Core-assisted, not Core-driven

APP-001 calls Planner, Orchestrator, Runtime, Committee, Memory, and Learning (`apps/equity_research/app.py:34-98`), but the main research output is assembled by app-local `EquityResearchAnalyzer`, which builds its own Evidence Chain, Knowledge Graph, Scorecard, and statement registry (`apps/equity_research/analyzer.py:20-154`).

Risk: future apps may copy this pattern and create multiple incompatible mini-engines.

### H2. Duplicate Evidence / KG / Score implementations

Evidence, KG, and score objects are constructed in at least two places: APP-001 and `investment_engine/pipeline.py` (`investment_engine/pipeline.py:95-148`). The repository also has schemas and builders, but no single source of construction truth.

Risk: schema drift and inconsistent quality gates after release.

### H3. Score Engine is not a stable runtime module

The score methodology exists in docs and schemas, while runtime calculations are embedded in app and engine code (`apps/equity_research/analyzer.py:135-154`, `investment_engine/pipeline.py:129-148`).

Risk: `quality_gate`, `overall_score`, and `confidence_score` may mean different things across modules.

### H4. Real connector behavior silently falls back to mock

News and SEC connectors catch real-mode errors and fallback to mock (`data_connectors/connectors/news.py:66-78`, `data_connectors/connectors/sec_edgar.py:69-81`). Yahoo Finance is mock-only (`data_connectors/connectors/yahoo_finance.py:34-67`).

Risk: users may receive structurally valid reports whose evidence is degraded unless they inspect lineage carefully.

### H5. Validation signal is broad but shallow

The existing validation suite heavily checks existence, disclaimers, imports, and generated artifacts. `validate_e2e.py` validates required fields and report taxonomy, but it does not reject mock production artifacts (`scripts/validate_e2e.py:66-80`).

Risk: "PASS" can be misunderstood as production correctness.

### H6. Security hardening is incomplete for public deployment

The API now defaults to localhost and requires API key for non-local bind (`api/server.py:133-138`), with CORS allowlist and body size checks. But rate limiting, request-level timeout enforcement, access logging policy, deployment profiles, and static Web API-key UX remain incomplete. Existing QA docs also list these as unresolved (`docs/review/QA_ARCHITECTURE_SELF_REVIEW.md:27-30`).

Risk: unsuitable for internet-facing Stable deployment.

### H7. Release artifacts and generated outputs are mixed into source tree

The repository includes `builder-output/`, `demo/output/`, `.cache`, `.pytest_cache`, and many `__pycache__` artifacts. This raises packaging, review, and reproducibility risk.

Risk: release tarball contains generated or local runtime artifacts not intended as source.

## Medium Risk

### M1. Module responsibilities are blurred

APP-001 is both an app and a research engine. Investment Engine is both methodology runner and report generator. Runtime is an execution trace generator more than a task executor. Report Generator exists separately but APP-001 uses its own exporter path.

### M2. Artifact source of truth is unclear

Schemas, templates, prompts, skills, docs, builder templates, and generated outputs all define overlapping concepts. There is no authoritative manifest identifying which files are contracts, generated artifacts, examples, or scaffolds.

### M3. Demo can run while real scenario cannot

`cli demo` and default `cli run` can complete via mock data. A user asking for "latest" or real company research will not necessarily get validated real sources unless the query happens to trigger real mode and the environment is configured.

### M4. API route semantics are thin

The API routes expose health, workspace, memory, and research endpoints, but the platform does not yet provide a production auth model, tenant isolation, persistent job management, or stable async behavior.

### M5. Memory and learning lifecycle is fragmented

Workspace memory, runtime memory, and learning feedback exist as separate local mechanisms. Multi-user isolation, data retention, replay, and deletion semantics are not Stable-grade.

### M6. Test packaging is nonstandard

Production E2E files use `run_case()` harnesses rather than pytest test functions. `pytest` reports only 4 passed / 1 skipped, which does not represent the broader project validation.

### M7. API and Web default relationship is incomplete

The static Web server and API server are started separately. Public API binding can require a key, but the Web path does not yet define a production-safe way to provide that key.

## Low Risk

### L1. Code style and formatting are inconsistent

Several runtime modules compress many statements into single lines (`runtime/core.py`, `runtime/task_dispatcher.py`, `runtime/agent_registry.py`). This does not block RC but reduces maintainability.

### L2. Documentation volume is high relative to executable code

The repository contains many architecture and completion reports. This is useful context, but it increases review cost and can obscure the current truth.

### L3. Generated artifacts inflate release size

`docs/testing/artifacts` and `demo/output` are useful for audit history, but should not be confused with source contracts.

### L4. Version labels are inconsistent in spirit

Some code reports version `0.1.0` for app/engine modules while repository docs claim `v1.0.0`. This may be intentional module versioning, but should be clarified before Stable.

## 建议延期处理的问题

- Full Scorecard runtime module and `ScorecardBuilder`.
- Full Prompt renderer and Skill scheduler.
- Full Benchmark runner with historical regression store.
- Complete Knowledge Graph persistence layer.
- Multi-tenant workspace/memory/learning lifecycle.
- Large-scale benchmark expansion.
- Full public deployment profile with API gateway, observability, rate limiting, and operational runbooks.
- Cleanup of all generated artifacts from repository packaging.

## 建议删除的内容

Delete from the Stable release package or move to generated-artifact storage:

- `demo/output/`
- `__pycache__/` and `*.pyc`
- `.pytest_cache/`
- local `.cache/` contents
- generated E2E artifacts that are not intentionally part of an auditable release bundle

Do not delete source examples, benchmark seeds, schemas, templates, prompts, skills, or docs required for the specification release.

## 建议保留的内容

- Top-level architecture and product docs, after reconciling Stable vs RC language.
- `docs/audit/*`, because they honestly capture remaining architecture debt.
- `docs/qa/ARCHITECTURE_STABILIZATION_REPORT.md`, because it accurately states remaining release risk.
- CLI/API local demo entry points, clearly labeled as local/demo or RC surfaces.
- Connector lineage, degradation notes, and mock/SKIP policy.
- Shared `common/contract.py` and `common/contract_validation.py`.
- Existing production E2E harness, but as RC regression coverage, not Stable proof.

## Release Checklist

Required before Stable:

- [ ] Add a real-mode release gate that fails on mock/SKIP for at least one critical end-to-end case.
- [ ] Split release profiles into demo, rc, and stable.
- [ ] Reconcile `FINAL_REVIEW`, QA self-review, architecture stabilization report, README, ROADMAP, and release notes into one release decision.
- [ ] Decide whether AIRS v1.0.0 is a specification repository or a runtime platform; update public language accordingly.
- [ ] Make Runtime execute at least one real business task that contributes to final report output, or explicitly remove runtime-platform claims.
- [ ] Establish a single source-of-truth manifest for schemas, templates, prompts, skills, examples, and generated artifacts.
- [ ] Define one canonical Evidence/KG/Score construction path or enforce one validator-backed contract across all local builders.
- [ ] Add API rate limiting and public deployment profile, or state that v1.0 Stable is local-only.
- [ ] Remove generated caches and demo outputs from the release package.
- [ ] Add CI that runs the true release gate, not only artifact validation.
- [ ] Update Known Issues so real-data readiness and score/runtime limits are not hidden behind PASS reports.

Acceptable for RC:

- [x] Local CLI demo works.
- [x] Local API can start with safer localhost defaults.
- [x] Mock-mode E2E harness can exercise the structural pipeline.
- [x] Investment advice disclaimers are consistently present.
- [x] Validation scripts provide broad artifact coverage.

## 最终结论

AIRS is close to a credible `v1.0.0-rc` specification and demo release, but not to a `v1.0.0 Stable` platform release.

The key blocker is not missing files. The key blocker is semantic readiness: production tests and product language currently overstate what the runtime and real-data paths prove. The repository can demonstrate an investment research framework and quality-control workflow; it cannot yet guarantee stable real-world operation for production investment research workflows.

AIRS 是否可以发布 v1.0.0 Stable？

No. AIRS should not be released as `v1.0.0 Stable` now. It can be released as `v1.0.0-rc` or `v1.0.0 Specification Release` with explicit limitations.
