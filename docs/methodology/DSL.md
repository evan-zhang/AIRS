# Methodology DSL（方法论描述语言）

**归属 Milestone**：M2 Methodology Core  
**适用范围**：用于结构化描述 AIRS Methodology Layer 中的方法论，供 Prompt、Skill、Schema、Benchmark 和 Score 后续复用。  
**免责声明**：Methodology DSL 仅描述研究流程和质量要求，不构成投资建议、交易指令或价格预测。

## 1. 设计目标

Methodology DSL 的目标是把方法论文档从自由文本转化为可验证、可映射、可执行的结构化描述。它不替代 Markdown 文档，而是为后续自动检查、Prompt 生成、Skill 编排和 Benchmark 映射提供稳定字段。

## 2. 核心原则

- **可追溯**：每个结论必须能追溯到输入、证据、反证和置信度规则。
- **可执行**：Workflow 必须能被 Research Agent 拆成步骤。
- **可评审**：Review Agent 能检查必需证据、反证和失败场景。
- **可扩展**：M3-M8 可在不破坏 16 节结构的前提下增加字段。
- **合规优先**：所有投资相关输出必须带免责声明，并禁止荐股、交易和价格预测。

## 3. 顶层结构

```yaml
methodology:
  id: supply-chain-chokepoint
  name: Supply Chain Chokepoint Analysis
  zh_name: 供应链卡脖子分析
  version: 0.2.0
  milestone: M2
  disclaimer_required: true
  sections:
    purpose: ...
    theory: ...
    background: ...
    applicable_scenarios: ...
    non_applicable_scenarios: ...
    inputs: ...
    outputs: ...
    workflow: ...
    required_evidence: ...
    counter_evidence: ...
    failure_cases: ...
    confidence: ...
    benchmark_mapping: ...
    future_prompt_mapping: ...
    future_skill_mapping: ...
    future_score_mapping: ...
```

## 4. 字段规范

- `id`：必填，使用小写短横线命名，必须与文件名主体一致。
- `name`：必填，英文方法论名称。
- `zh_name`：必填，中文方法论名称。
- `version`：必填，语义化版本；M2 初始版本为 `0.2.0`。
- `milestone`：必填，当前为 `M2`。
- `disclaimer_required`：必填，投资研究方法论必须为 `true`。
- `sections`：必填，必须包含 16 个标准字段，字段不得为空。

## 5. Section 语义

| DSL 字段 | 对应 Markdown Section | 说明 |
|----------|------------------------|------|
| `purpose` | Purpose | 方法论解决什么研究问题 |
| `theory` | Theory | 理论基础和分析假设 |
| `background` | Background | AIRS 项目中的背景和必要性 |
| `applicable_scenarios` | Applicable Scenarios | 适用触发条件 |
| `non_applicable_scenarios` | Non-applicable Scenarios | 不适用和拒绝边界 |
| `inputs` | Inputs | Research Agent 所需输入 |
| `outputs` | Outputs | 标准输出结构 |
| `workflow` | Workflow | 可执行步骤 |
| `required_evidence` | Required Evidence | 必需证据类型和最低要求 |
| `counter_evidence` | Counter Evidence | 反证和替代解释要求 |
| `failure_cases` | Failure Cases | 常见失效和误用 |
| `confidence` | Confidence | 置信度计算规则 |
| `benchmark_mapping` | Benchmark Mapping | 测试用例映射方式 |
| `future_prompt_mapping` | Future Prompt Mapping | 后续 Prompt 生成约束 |
| `future_skill_mapping` | Future Skill Mapping | 后续 Skill 编排约束 |
| `future_score_mapping` | Future Score Mapping | 后续评分维度映射 |

## 6. 语法规范

DSL 推荐使用 YAML 或 JSON 表达。Markdown 文档是人类可读版本，DSL 是机器可验证版本。字段文本可以是字符串、数组或对象，但转换为 Markdown 时必须形成对应章节的实质内容。

```yaml
workflow:
  - step: 1
    action: 明确产业边界
    output: 产业链层级表
  - step: 2
    action: 收集产能和认证证据
    output: 证据卡集合
```

## 7. 最小示例

```yaml
methodology:
  id: risk
  name: Risk Analysis
  zh_name: 风险分析
  version: 0.2.0
  milestone: M2
  disclaimer_required: true
  sections:
    purpose: "识别研究结论失效条件、影响路径和监测指标。"
    theory: "基于风险管理、情景分析和假设检验。"
    background: "服务 AIRS Evaluation Layer 和 Report Layer。"
    applicable_scenarios:
      - "所有形成投资研究结论的报告。"
    non_applicable_scenarios:
      - "用户要求保证收益或规避责任。"
    inputs:
      - "核心结论"
      - "关键假设"
      - "证据链"
    outputs:
      - "风险矩阵"
      - "触发条件"
      - "监测指标"
    workflow:
      - "拆解关键假设"
      - "识别风险类型"
      - "评估影响和可能性"
    required_evidence:
      - "历史案例、公告、政策或行业数据"
    counter_evidence:
      - "缓释因素和替代解释"
    failure_cases:
      - "模板化风险提示"
    confidence: "由证据质量、触发变量可观测性和缓释强度决定。"
    benchmark_mapping: "检查 Agent 是否识别关键假设失效条件。"
    future_prompt_mapping: "生成风险矩阵 Prompt。"
    future_skill_mapping: "映射 risk、evidence、report Skill。"
    future_score_mapping: "映射影响程度、发生可能性、可监测性等评分。"
```

## 8. 验证要求

Methodology DSL 的验证应满足：

1. 16 个 section 字段全部存在。
2. 每个字段有实质内容，不得为空字符串、空数组或占位符。
3. `disclaimer_required` 为 `true` 时，Markdown 文档必须出现免责声明。
4. `future_*_mapping` 字段必须说明后续 Prompt、Skill、Score 的具体用途。
5. 任何输出字段不得包含买入、卖出、目标价或收益承诺。

