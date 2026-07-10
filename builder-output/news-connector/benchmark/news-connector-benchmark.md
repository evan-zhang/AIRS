# News Connector Benchmark

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证系统能否把新闻事件转换为规范化事件对象，并为后续事件影响分析提供 Evidence Card 引用、反方来源、缺失证据和不确定性。

## 2. Gold Standard

合格输出必须包含：

- `event_id`、`source`、`published_at`、`normalized_event`。
- 至少 1 个 Evidence ID。
- 事实、解读、推断分开表达。
- 反方来源或缺失证据。
- 合规免责声明。

## 3. Evaluation Criteria

| 维度 | 权重 | 通过要求 |
|------|------|----------|
| Source Traceability | 0.25 | 来源、URL、发布时间完整 |
| Event Normalization | 0.25 | event_type、entities、affected_scope 清晰 |
| Evidence Mapping | 0.20 | 绑定 M3 Evidence 引用 |
| Counter Evidence | 0.15 | 冲突来源或缺失证据明确 |
| Compliance | 0.15 | 无交易建议或收益承诺 |

## 4. Failure Cases

- 来源缺失。
- 把媒体解读当作事实。
- 没有 Evidence ID。
- 缺少反方来源或缺失证据。
- 输出买卖建议、目标价或收益承诺。

## 5. 免责声明

本 Benchmark 仅用于 AIRS 投资研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

