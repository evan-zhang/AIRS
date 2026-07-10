# AIRS Production E2E Test Report

免责声明：本报告仅用于 AIRS 工程验证和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

- Version under test: v1.0.0-rc1
- Branch: test/production-e2e-validation
- Generated at: 2026-07-10T11:15:04.638328+00:00
- Overall status: PASS
- Production E2E: 8 PASS / 0 FAIL / 8 total
- Failure Injection: 3 PASS / 0 FAIL / 3 total

## Production E2E Cases

### prod-e2e-01-ai-compute
- Status: PASS
- Test file: `tests/production-e2e/test_01_ai_compute.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-01-ai-compute.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

### prod-e2e-02-semiconductor
- Status: PASS
- Test file: `tests/production-e2e/test_02_semiconductor.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-02-semiconductor.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

### prod-e2e-03-innovative-drug
- Status: PASS
- Test file: `tests/production-e2e/test_03_innovative_drug.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-03-innovative-drug.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

### prod-e2e-04-robotics
- Status: PASS
- Test file: `tests/production-e2e/test_04_robotics.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-04-robotics.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

### prod-e2e-05-new-energy
- Status: PASS
- Test file: `tests/production-e2e/test_05_new_energy.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-05-new-energy.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

### prod-e2e-06-peer-comparison
- Status: PASS
- Test file: `tests/production-e2e/test_06_peer_comparison.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-06-peer-comparison.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

### prod-e2e-07-news-impact
- Status: PASS
- Test file: `tests/production-e2e/test_07_news_impact.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-07-news-impact.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

### prod-e2e-08-memory-learning-regression
- Status: PASS
- Test file: `tests/production-e2e/test_08_memory_learning_regression.py`
- Artifact: `docs/testing/artifacts/production-e2e/prod-e2e-08-memory-learning-regression.json`
- Checks: planner=PASS, runtime=PASS, connectors=PASS, evidence_trace=PASS, knowledge_graph=PASS, scorecard=PASS, committee=PASS, report_taxonomy=PASS, memory=PASS, learning=PASS
- Failure reason: None

## Failure Injection Cases

### failure-connector-timeout
- Status: PASS
- Test file: `tests/failure-injection/test_connector_timeout.py`
- Artifact: `docs/testing/artifacts/failure-injection/failure-connector-timeout.json`
- Expected behavior: RetryPolicy should retry two timeout failures and recover on third attempt.
- Failure reason: None

### failure-runtime-interruption
- Status: PASS
- Test file: `tests/failure-injection/test_runtime_interruption.py`
- Artifact: `docs/testing/artifacts/failure-injection/failure-runtime-interruption.json`
- Expected behavior: Runtime should mark cancelled task, block dependents, and preserve resumable partial state.
- Failure reason: None

### failure-schema-error
- Status: PASS
- Test file: `tests/failure-injection/test_schema_error.py`
- Artifact: `docs/testing/artifacts/failure-injection/failure-schema-error.json`
- Expected behavior: KG validator should intercept malformed schema data before report generation.
- Failure reason: None

## Planner -> Runtime Contract

- Before fix: Planner produced `agent_role` in the task graph while RuntimeCore required `agent_id`; production E2E and failure-injection harnesses carried local `TASK_AGENT_MAP` adapters, so tests could pass while production had no single contract source.
- After fix: `common/contract.py` is the production contract. Planner runtime generation writes `contract_version`, `agent_id`, `input`, and `refs` for each task through `runtime_task_from_planner_task`; RuntimeCore normalizes incoming tasks through the same contract before dispatch.
- Regression posture: E2E and failure-injection harnesses no longer define local agent maps. They call `common.contract` only to preserve test metadata such as `case_id`.

## Evidence Trace Coverage

- Execution Log: stored in each production artifact under `execution_log`.
- Evidence Trace: stored under `evidence_trace` and `airs_evidence_chain`.
- KG State: stored under `kg_state` with validator result.
- Scorecard: stored under `scorecard`.
- Committee Debate: stored under `committee_debate`.
- Final Report: stored under `final_report`.
- Memory Write/Read: stored under `memory_write_read`.
- Learning Feedback: stored under `learning_feedback`.

## Known Issues

See `docs/testing/KNOWN_ISSUES.md`.

## Full Validation Logs

- `scripts/run_production_tests.py`: summarized in `docs/testing/artifacts/production-test-summary.json`.
- `scripts/validate_e2e.py`: `docs/testing/artifacts/validation-logs/validate_e2e.log`.
- Existing `scripts/validate_*.py`: `docs/testing/artifacts/validation-logs/`.

## Integration Notes

- Planner and Runtime now share `common.contract.CONTRACT_VERSION` and `resolve_agent_id`; local test-only mappings were removed from production E2E and failure-injection harnesses.
- `data_connectors/retry.py` remains covered by failure injection and `validate_connectors.py`.
