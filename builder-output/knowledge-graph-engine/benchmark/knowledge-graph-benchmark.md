# Knowledge Graph Engine Benchmark

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`  

## 1. 研究意图

给定一个供应链卡点研究问题，要求系统把公司、产品、供应链节点、Evidence Card 和核心命题转换成图谱结构。

## 2. Gold Standard

合格输出必须包含：

- 至少 5 个节点，覆盖 entity、evidence、claim、risk。
- 至少 5 条关系边，每条边有 Evidence ID。
- 至少 1 条 refutes 或 counter evidence 边。
- 至少 1 条 missing evidence 说明。
- 明确不确定性和免责声明。

## 3. Evaluation Criteria

| 维度 | 权重 | 通过要求 |
|------|------|----------|
| Evidence Traceability | 0.30 | 每条关键边有 Evidence ID |
| Graph Completeness | 0.20 | 节点和边覆盖核心命题 |
| Counter Evidence | 0.20 | 反方证据被建模 |
| Uncertainty | 0.15 | 缺失证据与不确定性明确 |
| Compliance | 0.15 | 无投资建议或交易指令 |

## 4. Failure Cases

- 关系边没有证据引用。
- 图谱只包含正向证据。
- 缺少免责声明。
- 输出买卖建议、目标价或收益承诺。

## 5. 免责声明

本 Benchmark 仅用于 AIRS 投资研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

