# APP-001 Equity Research App Self Review

## 评审结论

APP-001 已完成应用层最小可用闭环，能够从用户输入生成 15 段股票研究报告，并保留 Planner、Committee、Runtime、Connector、Evidence、KG、Score、Report、Memory 与 Learning 的追溯结果。当前质量门禁建议为 `CONDITIONAL_PASS`：工程链路完整，但真实数据覆盖仍需增强。

免责声明：本文档仅用于 AIRS 工程自评和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 评审维度

### 证据完整性

- 已完成 Evidence Card 转换和 Evidence Chain 汇总。
- 已记录 Connector Mock/SKIP 降级说明。
- 缺口：真实财报、真实行情、公司公告、行业份额和供应链订单数据仍不足。

### 逻辑一致性

- 主流程与任务要求一致：User Input → Parser → Resolver → Planner → Committee → Runtime → Connector → Engine → Evidence/KG/Score → Committee → Report → Memory → Learning。
- 所有报告 section 均拆分 Facts / Inference / Assumption / Opinion。
- Score Card 只表达研究质量门禁，不表达投资评级。

### 反方观点强度

- Data Collector 自动加入反方证据：数据源不足可能削弱结论。
- Committee 二次审议保留 unresolved questions 和 minority report。
- 缺口：反方观点仍偏治理和证据层，后续应接入更多公司与行业反方资料。

### 不确定性标注

- Mock/SKIP 均进入 degradation notes。
- Resolver 未命中时返回 NEED_REVIEW。
- Valuation 在缺少完整价格、盈利和现金流序列时不输出精确价格预测。

### 报告格式

- 15 个 section 完整。
- 每节包含四类陈述。
- 附录保留 Sources / Traceability。

## 风险

- 真实数据 Connector 未配置时，案例只能证明流程可运行，不能证明研究结论充分。
- 本地公司目录覆盖有限，长尾股票需要后续接入证券主数据。
- APP-001 复用当前 Investment Engine 最小实现，分析深度会受基础模块成熟度限制。

## 建议

- APP-002 或后续迭代优先补充证券主数据 Resolver。
- 为 Yahoo Finance、SEC EDGAR、HKEX 或交易所公告增加真实可用 Connector。
- 将 15 段报告 Schema 接入 jsonschema 校验，提升自检严格度。

