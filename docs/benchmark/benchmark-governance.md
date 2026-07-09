# Benchmark Governance（Benchmark 治理）

**归属 Milestone**：M7: Benchmark & Production Examples  
**版本**：v0.7.0  
**最后更新**：2026-07-10

**免责声明**：本文档仅用于 AIRS Benchmark 治理和质量控制，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 治理原则

Benchmark 是 AIRS 的质量资产，必须满足：

- 可追溯：每个结论都能追踪到 Evidence Card。
- 可复核：每个评分都能追踪到 M6 Scorecard。
- 可回归：每个用例都能在脚本中被检查。
- 可审计：版本、状态、变更原因和失败记录可保留。
- 合规：所有投资研究输出都必须有免责声明。

## 2. 角色责任

| 角色 | 责任 |
|------|------|
| Code Agent | 创建文件、维护 Schema、编写自检脚本、运行回归 |
| Research Agent | 基于 Benchmark 输入执行研究 |
| Review Agent | 评审 Gold Standard、Evidence Mapping、Score Mapping |
| Verification Agent | 执行 Benchmark 与 Examples 自检，生成结果 |

## 3. 变更治理

允许变更：

- 新增 Benchmark 分类或用例。
- 增强 Gold Standard 的证据边界。
- 增加 Failure Cases。
- 更新 Schema 以支持更完整的回归结果。

受控变更：

- 修改 M2-M6 规则映射。
- 修改 Quality Gate 阈值。
- 修改 Evidence Card 字段要求。
- 修改 Scorecard 聚合逻辑。

受控变更必须有 ADR 或 Completion Report 说明。M7 不应修改 M1-M6 已 PASS 文件，除非出现跨里程碑一致性问题。

## 4. 数据治理

Benchmark 可使用真实感行业场景，但不得伪装为实时投资建议。文档中的公司、行业、政策和数据描述应作为研究样例使用，必须标注证据来源类型、时间范围和不确定性。

Evidence 要求：

- A 级：公司公告、监管文件、官方统计。
- B 级：行业报告、券商研究、权威数据库。
- C 级：主流媒体、公司采访、公开演讲。
- D 级：专家观点、二手引用。
- E 级：不可验证来源，不得作为核心结论依据。

以上等级引用 M3 标准，不在本文件重新定义。

## 5. 质量治理

每个 Benchmark 必须通过以下检查：

- 结构完整：有 ID、分类、方法论、输入、期望输出和失败样例。
- 证据完整：有 Evidence Card 字段映射。
- 评分完整：有 Scorecard 和 Quality Gate 映射。
- 反方完整：有反证或缺失证据说明。
- 合规完整：有免责声明，且不包含交易指令或收益承诺。

## 6. 审计记录

回归结果应记录：

- `benchmark_id`
- `run_id`
- `agent_id`
- `input_version`
- `expected_version`
- `overall_score`
- `quality_gate`
- `failed_checks`
- `evidence_gaps`
- `fix_required`
- `disclaimer`

## 7. 例外处理

若 Benchmark 因外部资料失效无法执行：

1. 标记为 `NEEDS_UPDATE`。
2. 记录失效来源和影响范围。
3. 保留原文件作为审计记录。
4. 新增替代用例或更新证据需求。
5. 重新运行 M7 自检。

## 8. 合规红线

任何 Benchmark 或 Example 一旦缺少免责声明、诱导交易动作、承诺收益或把研究评分表达为投资结论，必须视为强制 `FAIL`。

