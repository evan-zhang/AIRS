# News Connector Test Plan

## 1. 目标

验证 News Connector 能把新闻事件转换为 AIRS 可审查的结构化事件与 Evidence 引用，并保持合规边界。

## 2. Cases

| Case ID | 场景 | 输入 | 期望结果 |
|---------|------|------|----------|
| NEWS-T001 | 正常新闻 | 官方来源、URL、发布时间完整 | 输出 normalized_event 与 evidence_refs |
| NEWS-T002 | 冲突来源 | 两个来源对事件影响表述不同 | 输出 counter_sources |
| NEWS-T003 | 低可信来源 | 来源不明或缺少 URL | 返回 `FAIL_SOURCE_UNTRUSTED` |
| NEWS-T004 | 合规失败 | 用户要求给出买卖动作 | 返回 `FAIL_COMPLIANCE` |

## 3. 回归要求

- Schema 可被 JSON 解析。
- Skill 引用 M5 Skill Engine。
- Prompt 引用 M4 Prompt Engine。
- Benchmark 引用 M7 Benchmark。
- 所有输出保留免责声明。

## 4. 免责声明

本测试计划仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

