# FEATURE-008 Completion Report: Investment Research Engine

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Scope

FEATURE-008 已交付统一 Investment Research Engine，基于 M1-M7 与 M8 基础设施，编排 Runtime、Orchestrator、Workspace、Data Connectors、Methodology、Skill、Prompt、Evidence、Knowledge Graph、Score 和 Report。

## Delivered Artifacts

- `builder/requests/feature-request-investment-research-engine.yaml`
- `builder-output/investment-research-engine/`
- `docs/investment-engine/`
- `docs/orchestrator/orchestrator-architecture.md`
- `investment_engine/`
- `investment_engine/examples/` 五个研究案例
- `schemas/investment/`
- `templates/investment/`
- `scripts/validate_investment_engine.py`
- `docs/adr/ADR-0008-investment-research-engine.md`
- `docs/review/FEATURE_008_SELF_REVIEW.md`

## Validation

`scripts/validate_investment_engine.py` 覆盖 FEATURE-008 静态文件、五个可执行案例、Recommendation 四类语句、禁止表达、基础设施引用和 16 个既有回归脚本。

已运行 17 个 `validate_*` 脚本，全部 PASS：

- validate_m1.py
- validate_m2.py
- validate_evidence.py
- validate_prompt.py
- validate_skill.py
- validate_score.py
- validate_evaluation.py
- validate_benchmark.py
- validate_examples.py
- validate_release.py
- validate_builder.py
- validate_knowledge_graph.py
- validate_report_generator.py
- validate_connectors.py
- validate_runtime.py
- validate_workspace.py
- validate_investment_engine.py

## Compliance

Engine 只用于研究流程编排和质量控制，不构成投资建议。所有输出保留免责声明，不输出确定性交易建议、目标价、收益承诺或自动化交易动作。

## Known Gaps

- 示例使用 deterministic mock evidence，不接入真实外部行情或新闻。
- Score Card 为最小可运行质量评分，不是生产级投资评分模型。
- Report Generator 集成以模板和结构化文本为主，后续可接入 `report_generator.ReportPipeline` 做完整渲染。
