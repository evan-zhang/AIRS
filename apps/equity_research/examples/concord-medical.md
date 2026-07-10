# China Medical System Holdings Limited 股票研究报告

- Request ID：`APP-001-61E761B9FB`
- Symbol：`0867.HK`
- Market：`HK`
- Research Question：分析 0867.HK 康哲药业的财务、行业位置和风险

免责声明：本报告仅供 AIRS 投资研究流程验证和研究参考，不构成投资建议。 本应用不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. Executive Summary

### Facts
- 研究请求 ID：APP-001-61E761B9FB
- 解析对象：China Medical System Holdings Limited / 0867.HK
- 证据卡数量：5

### Inference
- 若真实 Connector 不可用，结论置信度必须随数据降级下降。
- 行业、供应链、估值与风险章节需要共同引用证据链。

### Assumption
- 本次流程允许使用 Mock/SKIP 作为工程降级信号，但不得冒充真实研究证据。
- 后续人工复核可替换或补充 Connector 证据。

### Opinion
- 当前输出适合作为研究工作底稿和二次尽调清单。
- 不输出买入、卖出、持有、目标价或收益承诺。

## 2. Company Profile

### Facts
- 公司识别状态：RESOLVED_LOCAL_DIRECTORY
- 代码：0867.HK；市场：HK；交易所：HKEX
- 行业：Pharmaceuticals；板块：Healthcare

### Inference
- 若公司识别为 NEED_REVIEW，则后续所有公司特定分析必须降级。

### Assumption
- 本地公司目录中的基础信息用于流程路由，仍需外部权威源复核。

### Opinion
- 在证据不足前，研究应以问题清单和证据缺口为主。

## 3. Industry Position

### Facts
- 行业分类来自 Resolver：Pharmaceuticals
- Engine 行业发现模块：UNKNOWN

### Inference
- 行业地位需要财报、市场份额和同行数据共同验证。

### Assumption
- 若 Connector 未提供真实行业数据，则暂以行业方法论框架占位。

### Opinion
- 行业部分适合进入二次研究，而非形成确定性判断。

## 4. Supply Chain / Chokepoint

### Facts
- {'component': 'supply_chain', 'methodology_refs': ['docs/methodology/supply-chain-chokepoint.md'], 'skill_refs': ['skills/supply-chain/supply-chain-skill.md'], 'nodes': [{'node_id': 'upstream', 'label': '需求变化', 'type': 'supply_chain_node'}, {'node_id': 'midstream', 'label': '供给约束', 'type': 'supply_chain_node'}, {'node_id': 'downstream', 'label': 'China Medical System Holdings Limited 股票研究', 'type': 'industry'}], 'edges': [{'from': 'upstream', 'to': 'midstream', 'relation': 'depends_on', 'evidence_refs': ['ev-01']}, {'from': 'midstream', 'to': 'downstream', 'relation': 'supports', 'evidence_refs': ['ev-02']}], 'company_roles': [{'name': 'Company A', 'role': '需求变化', 'evidence_ref': 'ev-01'}, {'name': 'Company B', 'role': '供给约束', 'evidence_ref': 'ev-02'}, {'name': 'Company C', 'role': '政策催化', 'evidence_ref': 'ev-03'}]}

### Inference
- {'component': 'chokepoint', 'methodology_refs': ['docs/methodology/supply-chain-chokepoint.md'], 'knowledge_graph_refs': ['schemas/knowledge-graph/knowledge-graph.schema.json'], 'chokepoints': [{'chokepoint_id': 'cp-01', 'node_id': 'upstream', 'label': '需求变化', 'severity': 0.6599999999999999, 'evidence_refs': ['ev-01'], 'counter_evidence_refs': ['ev-counter-01'], 'missing_evidence': ['需要更多订单、产能、价格或政策证据交叉验证']}, {'chokepoint_id': 'cp-02', 'node_id': 'midstream', 'label': '供给约束', 'severity': 0.6, 'evidence_refs': ['ev-02'], 'counter_evidence_refs': ['ev-counter-02'], 'missing_evidence': ['需要更多订单、产能、价格或政策证据交叉验证']}]}

### Assumption
- 供应链节点来自通用 Investment Engine 模板，需公司级真实资料复核。

### Opinion
- 卡点分析可用于组织研究问题，不应解读为交易信号。

## 5. Financial Analysis

### Facts
- {'connector_id': 'yahoo_finance', 'source': 'Yahoo Finance', 'source_type': 'trusted_third_party', 'url': 'https://finance.yahoo.com/quote/AAPL', 'timestamp': '2026-07-10T10:39:04.209245+00:00', 'version': '0.1.0', 'trace_id': 'TRACE-030E518AECD3', 'data': {'symbol': 'AAPL', 'currency': 'USD', 'last_price': 100.0, 'url': 'https://finance.yahoo.com/quote/AAPL'}, 'traceability': {'connector': 'yahoo_finance', 'request_id': 'TRACE-030E518AECD3', 'cache_hit': False, 'transformations': ['mock_fetch', 'normalize']}, 'disclaimer': '仅供 AIRS 工程开发和研究质量控制使用，不构成投资建议。'}

### Inference
- 当前财务分析只能确认数据可用性与追溯性，不能替代三表分析。

### Assumption
- news 使用 Mock 降级数据，不能冒充真实外部数据。
- rss 返回错误：missing required fields: ['feed_url']
- rss 使用 Mock 降级数据，不能冒充真实外部数据。

### Opinion
- 财务结论应在真实财报与审计口径齐备后再提升置信度。

## 6. Valuation

### Facts
- 真实 Connector 数据可用：False

### Inference
- 缺少完整价格、盈利和现金流序列时，不计算目标价或买卖评级。

### Assumption
- 估值只能记录待计算指标：PE、PS、EV/EBITDA、DCF 敏感性。

### Opinion
- 估值章节以方法和缺口为主，避免伪造精确值。

## 7. Catalysts

### Facts
- {'component': 'catalyst', 'methodology_refs': ['docs/methodology/policy-driven.md'], 'catalysts': [{'catalyst_id': 'cat-01', 'name': 'China Medical System Holdings Limited 股票研究 订单或招标披露', 'time_horizon': '1-2 quarters', 'evidence_refs': ['ev-01']}, {'catalyst_id': 'cat-02', 'name': 'China Medical System Holdings Limited 股票研究 政策或监管更新', 'time_horizon': 'event-driven', 'evidence_refs': ['ev-03']}, {'catalyst_id': 'cat-03', 'name': 'China Medical System Holdings Limited 股票研究 产能或良率改善', 'time_horizon': '2-4 quarters', 'evidence_refs': ['ev-02']}]}

### Inference
- 来自 Investment Engine 的结构化分析结果，需绑定真实证据后提升置信度。

### Assumption
- Engine 结果为研究框架输出，不等同于真实公司结论。

### Opinion
- 本节用于提示后续研究方向。

## 8. Risks

### Facts
- {'component': 'risk', 'topic': 'China Medical System Holdings Limited 股票研究', 'methodology_refs': ['docs/methodology/risk.md', 'skills/risk/risk-skill.md'], 'risks': [{'risk_id': 'risk-demand', 'name': '需求兑现风险', 'severity': 'medium', 'evidence_refs': ['ev-counter-01']}, {'risk_id': 'risk-margin', 'name': '竞争和利润率风险', 'severity': 'medium', 'evidence_refs': ['ev-counter-02']}, {'risk_id': 'risk-policy', 'name': '政策或监管变化风险', 'severity': 'low', 'evidence_refs': ['ev-03']}], 'risk_summary': 'China Medical System Holdings Limited 股票研究 的主要风险来自需求、利润率、政策和证据缺口，需要持续复核。'}

### Inference
- 来自 Investment Engine 的结构化分析结果，需绑定真实证据后提升置信度。

### Assumption
- Engine 结果为研究框架输出，不等同于真实公司结论。

### Opinion
- 本节用于提示后续研究方向。

## 9. Counter View

### Facts
- 降级说明数量：3

### Inference
- 数据降级会降低结论强度，并要求 Committee 二次审议。

### Assumption
- 部分公开源可能存在延迟、抽样偏差或不可访问。

### Opinion
- 如果关键证据持续缺失，应输出 CONDITIONAL_PASS 或 FAIL。

## 10. Evidence Chain

### Facts
- Evidence Chain ID：chain-APP-001-61E761B9FB
- 证据卡：APP001-EV-01, APP001-EV-02, APP001-EV-03, APP001-EV-04, APP001-EV-COUNTER-01

### Inference
- 整体置信度：0.48

### Assumption
- 人工复核
- 公司公告原文
- 可复核行业数据
- 真实数据源凭证
- 真实财务明细

### Opinion
- 证据链优先用于追溯和复核，不直接推出投资动作。

## 11. Knowledge Graph

### Facts
- KG ID：kg-APP-001-61E761B9FB
- 节点数：4；边数：2

### Inference
- {'path': ['company', 'industry', 'report'], 'confidence': 0.6}

### Assumption
- 图谱结构依赖当前证据卡，证据更新后需重建。

### Opinion
- KG 适合发现研究路径和薄弱环节。

## 12. Score Card

### Facts
- Scorecard ID：score-app001-ev-01
- Quality Gate：FAIL

### Inference
- Overall Score：48；Confidence：0.48

### Assumption
- 按证据卡数量与追溯字段评分。
- Mock/SKIP 越多，降级越强。
- 继承 Investment Engine 质量门禁。

### Opinion
- 评分用于研究质量控制，不是投资评级。

## 13. Committee Decision

### Facts
- Committee Session：aic-plan-APP-001-61E761B9FB
- Vote：FAIL

### Inference
- 允许在限定范围内进入 Research Engine 继续研究，所有结论仅供研究质量控制。

### Assumption
- 关键证据尚未由 Connector 采集验证。
- Scorecard 尚未由 M6 计算。

### Opinion
- Bear Analyst 要求在证据不足时降级结论。

## 14. Final Report

### Facts
- # China Medical System Holdings Limited AIRS Report Generator 输出

**Report ID**：reportgen-APP-001-61E761B9FB
**版本**：0.1.0
**方法论引用**：`docs/methodology/evidence-chain.md`, `docs/methodology/supply-chain-chokepoint.md`, `docs/methodology/valuation.md`, `docs/methodology/risk.md`

**免责声明**：本报告仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 报告元数据

- Report ID：`reportgen-APP-001-61E761B9FB`
- 研究主题：China Medical System Holdings Limited AIRS Report Generator 输出
- Prompt 引用：`prompts/report/generation.md`
- Skill 引用：`skills/report/report-skill.md`
- Evidence 数量：5
- KG 引用：`kg-APP-001-61E761B9FB`
- Scorecard 引用：`score-app001-ev-01`

## 2. 研究问题与范围

分析 0867.HK 康哲药业的财务、行业位置和风险

## 3. 方法论引用

- `docs/methodology/evidence-chain.md`：沿用 M2 方法论，不在报告层重写研究规则。
- `docs/methodology/supply-chain-chokepoint.md`：沿用 M2 方法论，不在报告层重写研究规则。
- `docs/methodology/valuation.md`：沿用 M2 方法论，不在报告层重写研究规则。
- `docs/methodology/risk.md`：沿用 M2 方法论，不在报告层重写研究规则。

## 4. 核心观点

当前结论应作为研究跟踪框架，而非投资动作依据。 该观点至少引用 [APP001-EV-01] China Medical System Holdings Limited yahoo_finance 数据（来源：Yahoo Finance；等级：L2；置信度：0.7），并由 KG 卡点 `upstream` 与 Scorecard `score-app001-ev-01` 共同约束。

## 5. Evidence 引用表

| Evidence ID | 标题 | 类别 | 来源类型 | 等级 | 权重 | 支持命题 | 反方或限制 |
|---|---|---|---|---|---:|---|---|
| APP001-EV-01 | China Medical System Holdings Limited yahoo_finance 数据 | connector_result | trusted_third_party | L2 | 0.7 | 研究流程已记录该数据源的可用性与追溯字段。 | 若结果为 Mock 或 SKIP，则反驳真实数据完整可用的假设。 |
| APP001-EV-02 | China Medical System Holdings Limited news 数据 | connector_result | public_news | L3 | 0.35 | 研究流程已记录该数据源的可用性与追溯字段。 | 若结果为 Mock 或 SKIP，则反驳真实数据完整可用的假设。 |
| APP001-EV-03 | China Medical System Holdings Limited rss 数据 | connector_result | public_news | L2 | 0.7 | 研究流程已记录该数据源的可用性与追溯字段。 | 若结果为 Mock 或 SKIP，则反驳真实数据完整可用的假设。 |
| APP001-EV-04 | China Medical System Holdings Limited rss 数据 | connector_result | public_news | L3 | 0.35 | 研究流程已记录该数据源的可用性与追溯字段。 | 若结果为 Mock 或 SKIP，则反驳真实数据完整可用的假设。 |
| APP001-EV-COUNTER-01 | 反方证据占位：数据源不足可能削弱结论 | counter_evidence | internal_quality_control | L2 | 0.65 | 已检查，暂无直接记录 | 证据不充分时不得输出高确信度结论。 |

## 6. Evidence Chain 汇总

- [APP001-EV-01] China Medical System Holdings Limited yahoo_finance 数据（来源：Yahoo Finance；等级：L2；置信度：0.7）
- [APP001-EV-02] China Medical System Holdings Limited news 数据（来源：Public News；等级：L3；置信度：0.35）
- [APP001-EV-03] China Medical System Holdings Limited rss 数据（来源：RSS Feed；等级：L2；置信度：0.7）
- [APP001-EV-04] China Medical System Holdings Limited rss 数据（来源：RSS Feed；等级：L3；置信度：0.35）
- [APP001-EV-COUNTER-01] 反方证据占位：数据源不足可能削弱结论（来源：AIRS governance；等级：L2；置信度：0.65）

## 7. Knowledge Graph 汇总

- KG ID：`kg-APP-001-61E761B9FB`
- 图谱标题：China Medical System Holdings Limited Equity Research Knowledge Graph
- 节点 / 关系 / 路径：4 / 2 / 1
- Top Chokepoint：需求变化（节点：`upstream`；分数：NA；风险：NA）
- 卡点驱动：
- KG Evidence Refs：`APP001-EV-01`, `APP001-EV-COUNTER-01`, `ev-01`, `ev-02`, `ev-counter-01`, `ev-counter-02`

## 8. Score Summary

- Scorecard ID：`score-app001-ev-01`
- Overall Score / Grade：48 / C
- Confidence Score：0.48
- Quality Gate：`FAIL`
- 维度分：unknown: None
- Score Evidence Refs：`APP001-EV-01`, `APP001-EV-02`, `APP001-EV-03`, `APP001-EV-04`, `APP001-EV-COUNTER-01`
- Score Disclaimer：仅供研究参考，不构成投资建议

## 9. 反方观点

- 数据降级会降低结论强度，并要求 Committee 二次审议。
- 如果关键证据持续缺失，应输出 CONDITIONAL_PASS 或 FAIL。

## 10. 不确定性与缺口

- APP001-EV-01: 真实财务明细
- APP001-EV-01: 公司公告原文
- APP001-EV-01: 可复核行业数据
- APP001-EV-02: 真实财务明细
- APP001-EV-02: 公司公告原文
- APP001-EV-02: 可复核行业数据
- APP001-EV-03: 真实财务明细
- APP001-EV-03: 公司公告原文
- APP001-EV-03: 可复核行业数据
- APP001-EV-04: 真实财务明细
- APP001-EV-04: 公司公告原文
- APP001-EV-04: 可复核行业数据
- APP001-EV-COUNTER-01: 真实数据源凭证
- APP001-EV-COUNTER-01: 人工复核

## 11. 风险提示

- {'risk_id': 'risk-demand', 'name': '需求兑现风险', 'severity': 'medium', 'evidence_refs': ['ev-counter-01']}
- {'risk_id': 'risk-margin', 'name': '竞争和利润率风险', 'severity': 'medium', 'evidence_refs': ['ev-counter-02']}
- {'risk_id': 'risk-policy', 'name': '政策或监管变化风险', 'severity': 'low', 'evidence_refs': ['ev-03']}

## 12. 免责声明

本报告仅用于 AIRS 投资研究质量控制，不构成

### Inference
- 完整 Report Generator 输出已纳入本节。

### Assumption
- SKIP：本节暂无可验证内容，需补充证据。

### Opinion
- SKIP：本节暂无可验证内容，需补充证据。

## 15. Appendix (Sources / Traceability)

### Facts
- Request：{'request_id': 'APP-001-61E761B9FB', 'raw_input': '分析 0867.HK 康哲药业的财务、行业位置和风险', 'symbol': '0867.HK', 'company_name': 'China Medical System Holdings', 'market': 'HK', 'time_range': '最近12个月', 'research_question': '分析 0867.HK 康哲药业的财务、行业位置和风险', 'focus_areas': ['financial', 'industry', 'risk'], 'peer_companies': [], 'risk_preference': 'balanced', 'language': 'zh', 'created_at': '2026-07-10', 'disclaimer': '仅用于 AIRS 投资研究流程编排和质量控制，不构成投资建议。'}
- Company Traceability：{'resolver': 'apps/equity_research/company_resolver.py', 'input': {'request_id': 'APP-001-61E761B9FB', 'raw_input': '分析 0867.HK 康哲药业的财务、行业位置和风险', 'symbol': '0867.HK', 'company_name': 'China Medical System Holdings', 'market': 'HK', 'time_range': '最近12个月', 'research_question': '分析 0867.HK 康哲药业的财务、行业位置和风险', 'focus_areas': ['financial', 'industry', 'risk'], 'peer_companies': [], 'risk_preference': 'balanced', 'language': 'zh', 'created_at': '2026-07-10', 'disclaimer': '仅用于 AIRS 投资研究流程编排和质量控制，不构成投资建议。'}}
- Evidence Refs：['APP001-EV-01', 'APP001-EV-02', 'APP001-EV-03', 'APP001-EV-04', 'APP001-EV-COUNTER-01']

### Inference
- 所有章节均保留 Facts / Inference / Assumption / Opinion 标记。

### Assumption
- 附录中的 Connector 结果可能包含 Mock/SKIP 降级。

### Opinion
- 发布前应由 Review Agent 复核来源与语气。
