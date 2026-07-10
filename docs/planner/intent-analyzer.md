# Intent Analyzer

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Intent Analyzer 将 Research Goal 映射为研究意图，并选择 Methodology、Connector 和 Skill 的候选集合。它不执行研究，也不读取外部数据。

## 支持意图

- Company Research：公司研究。
- Industry Research：行业研究。
- Theme Research：主题研究。
- Supply Chain Research：供应链研究。
- Chokepoint Research：卡点研究。
- Policy Research：政策研究。
- Portfolio Research：组合研究。
- Comparative Research：对比研究。

## 输出字段

- `primary_intent`
- `required_methodologies`
- `required_skills`
- `required_connectors`
- `report_depth`
- `review_required`

## 治理规则

意图识别只决定研究路径，不输出结论。所有 Methodology、Skill 和 Connector 都通过引用进入计划，避免 Planner 重复定义 M2-M8 的业务规则。

## 与 Planner / Runtime 的关系

Intent Analyzer 是 Planner 内部组件，输出只能交回 Planning Engine。Runtime 不能直接调用 Intent Analyzer，也不能把原始用户目标交给 Intent Analyzer 后跳过 Research Plan。正确链路是：Planner 调用 Intent Analyzer，Planner 生成 Research Plan，Runtime 再执行 Planner 产物。
