# AIRS Production E2E Known Issues

免责声明：本文件仅记录 AIRS 工程验证问题，不构成投资建议。

- Generated at: 2026-07-10T08:53:01.439204+00:00
- Open issue count: 0

## Open Issues

No open production E2E issues were observed in this run.

## Resolved During Validation

### Planner/Runtime task schema gap

- Observed: Planner generated tasks with `agent_role`, while `RuntimeCore` expected `agent_id`.
- Resolution: Added explicit production E2E adapter in `tests/production-e2e/e2e_harness.py` and matching failure-injection adapter in `tests/failure-injection/failure_harness.py`.
- Residual risk: Core modules still have an implicit schema boundary; future production work should promote this adapter into a shared planner-runtime contract if needed.

### Connector retry helper import-order error

- Observed: `data_connectors/retry.py` failed to import because `from __future__ import annotations` was not at the top of the file.
- Resolution: Moved connector helper marker into a comment after the future import.
- Residual risk: None observed after `validate_connectors.py` and failure-injection retry test passed.

### Validation script count regression

- Observed: Adding `scripts/validate_e2e.py` changed the expected count of `validate_*.py` scripts from 22 to 23.
- Resolution: Updated `scripts/validate_learning.py` regression guard to include `validate_e2e.py`.
- Residual risk: Future validation scripts should update the explicit count or migrate the check to a named required-script set.
