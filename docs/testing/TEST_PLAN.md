# AIRS Production E2E Test Plan

免责声明：本计划仅用于 AIRS 工程验证和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Scope

Validate AIRS v1.0.0-rc1 production E2E behavior across real module calls, not static examples.

## Required Chain

Each production case must call:

- `planner/engine.py` for research decomposition.
- `runtime/` through `RuntimeCore.run_workflow`.
- `data_connectors/` through registered connectors.
- Evidence generation through `investment_engine` evidence chain output.
- `knowledge_graph/` builder and validator.
- `investment_engine/` report and scorecard generation.
- `committee/` voting and decision recording.
- `workspace/memory.py` write/read.
- `learning/` feedback and memory consolidation.

## Production Cases

1. AI 算力供应链端到端研究
2. 半导体国产替代端到端研究
3. 创新药管线端到端研究
4. 机器人产业链端到端研究
5. 新能源产业端到端研究
6. 两家同行对比端到端研究
7. 新闻影响分析端到端研究
8. Memory/Learning 回归端到端研究

## Failure Injection

- Connector timeout: simulate two timeout failures and verify retry recovery.
- Schema error: inject malformed KG data and verify validator interception.
- Runtime interruption: cancel one task and verify partial state, cancellation event, and blocked dependents.

## Pass Criteria

- All 8 production E2E cases pass every module check.
- Failure-injection cases pass by demonstrating expected interception, retry, or recovery behavior.
- Report artifacts include execution log, evidence trace, KG state, scorecard, committee debate, final report, memory write/read, and learning feedback.
- Final report language separates facts, inferences, assumptions, and opinions.
- No output contains direct recommendation, automatic trading instruction, target price, or return guarantee.

