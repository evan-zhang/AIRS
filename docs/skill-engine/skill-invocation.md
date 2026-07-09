# Skill Invocation（Skill 调用协议）

## 1. 调用目标

Skill Invocation 定义 Agent 调用 Skill 时必须传入什么、必须返回什么、如何记录依赖和如何处理失败。调用协议保证后续 Review Agent 与 Verification Agent 能够复核每次研究执行。

## 2. 请求结构

标准调用请求包含：

```json
{
  "skill_id": "airs.skill.supply_chain.v1",
  "request_id": "req-20260710-001",
  "research_question": "研究问题",
  "scope": {
    "industry": "行业",
    "company": "可选公司",
    "time_range": "时间范围",
    "region": "地域范围"
  },
  "constraints": {
    "data_source_preference": ["公开财报", "公告", "权威新闻"],
    "output_format": "structured_markdown",
    "language": "zh-CN"
  },
  "context_refs": {
    "prompt_refs": [],
    "methodology_refs": [],
    "evidence_chain_ids": []
  }
}
```

## 3. 响应结构

标准响应包含：

- `status`：PASS、PARTIAL、FAIL。
- `skill_id` 与 `skill_version`。
- `used_prompts`：实际调用的 M4 Prompt 路径和版本。
- `used_methodologies`：实际引用的 M2 文档。
- `used_evidence_components`：Evidence Card、Evidence Chain、验证流程引用。
- `result`：结构化研究发现或报告片段。
- `evidence_chain`：Evidence Card ID、supports、refutes、missing_evidence、traceability 摘要。
- `uncertainty`：不确定性等级与原因。
- `failure`：失败类型、缺失输入、重试建议。
- `disclaimer`：合规免责声明。

## 4. 调用约束

Skill 调用必须遵守：

- 不允许绕过 Prompt Engine 直接生成生产研究输出。
- 不允许调用未注册、未审查或不存在的 Prompt。
- 不允许用 Skill 自定义方法论替代 M2 文档。
- 不允许用自由文本证据替代 M3 Evidence Card。
- 不允许省略反方观点和缺失证据。
- 不允许输出交易指令、收益承诺或价格预测。

## 5. 失败协议

失败不是异常，而是协议的一部分。输入缺失时返回 `FAIL_INPUT_INCOMPLETE`；证据不足时返回 `FAIL_EVIDENCE_INSUFFICIENT`；Prompt 不可用时返回 `FAIL_PROMPT_UNAVAILABLE`；方法论不匹配时返回 `FAIL_METHODOLOGY_MISMATCH`；输出不合规时返回 `FAIL_COMPLIANCE`。

## 6. 审计记录

每次调用必须保留 request_id、Skill 版本、Prompt 路径、Methodology 路径、Evidence Chain ID、生成时间、审查状态和免责声明状态。审计记录用于 M6 Evaluation Engine 与 M7 Benchmark，不用于直接投资决策。

## 7. 合规说明

调用协议产生的任何研究内容仅供研究参考，不构成投资建议。投资有风险，使用者应自行判断并承担决策责任。

