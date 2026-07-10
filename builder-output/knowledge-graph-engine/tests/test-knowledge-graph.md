# Knowledge Graph Engine Test Plan

## 1. 目标

验证 Knowledge Graph Engine Feature Package 是否能约束后续实现生成可追溯、可审查、可回归的研究图谱。

## 2. Cases

| Case ID | 场景 | 输入 | 期望结果 |
|---------|------|------|----------|
| KG-T001 | 正常图谱生成 | 3 个实体、3 张 Evidence Card、1 个命题 | 输出节点、边、Evidence ID 和免责声明 |
| KG-T002 | 反方证据 | Evidence Card 中包含 refutes | 输出 `counter_evidence_edges` |
| KG-T003 | 缺失证据 | 命题没有 Evidence ID | 输出 `missing_evidence` |
| KG-T004 | 合规失败 | 用户要求交易结论 | 返回 `FAIL_COMPLIANCE` |

## 3. 回归要求

- `schema/knowledge-graph.schema.json` 可被 JSON 解析。
- Skill 草案引用 M5 Skill Engine。
- Prompt 草案引用 M4 Prompt Engine。
- Benchmark 草案引用 M7 Benchmark。

## 4. 免责声明

本测试计划仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

