# Knowledge Graph Engine 架构

**归属 Feature**：FEATURE-002 Knowledge Graph Engine  
**适用层级**：Methodology Layer、Evidence Layer、Research Skill Layer、Review Layer  
**免责声明**：本文档仅用于 AIRS 工程开发、投资研究质量控制和系统验证，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 目标

Knowledge Graph Engine 将 AIRS 研究过程中产生的产业、公司、产品、政策、事件、证据、命题和风险组织为可验证的图谱。它解决三个问题：

- 把 M2 Methodology 的研究框架落到结构化实体与关系。
- 把 M3 Evidence Card 绑定到节点和边，确保结论可以追溯。
- 为路径分析、供应链卡脖子分析和 Review Agent 质量检查提供统一数据结构。

## 2. 组件

### Graph Model

`knowledge_graph/model.py` 定义 `KnowledgeGraph`、`GraphNode`、`GraphEdge` 和 `EvidenceBinding`。节点类型受控为 `company`、`industry`、`product`、`supply_chain_node`、`policy`、`event`、`evidence`、`claim`、`risk`；关系类型受控为 `supports`、`refutes`、`depends_on`、`belongs_to`、`affected_by`、`competes_with`、`has_risk`。

### Builder

`knowledge_graph/builder.py` 提供最小构建器，支持从字典或 JSON 文件装载图谱，也支持按节点和边逐步构建。Builder 不采集外部数据，不替代 Research Agent，只负责把已获得的证据与研究拆解结果组合成图谱。

### Validator

`knowledge_graph/validator.py` 检查节点类型、关系类型、节点引用、Evidence 引用、Methodology 引用和免责声明。它是 Review Agent 与 Verification Agent 的共同质量门禁。

### Path Analyzer

`knowledge_graph/path_analyzer.py` 对有向图做简单路径枚举，输出节点路径、边路径、关系序列、证据覆盖和路径置信度。它用于回答“某个上游约束如何传导到下游命题”。

### Chokepoint Analyzer

`knowledge_graph/chokepoint_analyzer.py` 按供给稀缺、替代难度、扩产难度、认证周期、议价能力和证据质量给供应链节点评分。评分只表示研究中的瓶颈强弱，不是投资评级。

## 3. 与 M2-M8 的兼容关系

- M2 Methodology：图谱必须写入 `methodology_refs`，例如 `supply-chain-chokepoint`、`evidence-chain`、`counter-consensus`。
- M3 Evidence：图谱必须在 `evidence_cards` 中保存 Evidence Card，并在节点 `evidence_bindings` 与边 `evidence_refs` 中引用。
- M4 Prompt：图谱生成 Prompt 应引用 `templates/prompt-template.md` 与 `prompts/_dsl/prompt-dsl.md`，不新增 Prompt DSL。
- M5 Skill：图谱 Skill 应作为 Research Skill 的结构化输出步骤，不替代 Master Skill 调度规则。
- M6 Score 与 Evaluation：卡点分数需要附带证据、反证和缺口，不能被解释为收益概率或评级。
- M7 Benchmark：图谱 Benchmark 必须包含标准答案、失败用例和评估标准。
- M8 Production：生产使用必须保留免责声明、版本和回归测试结果。

## 4. 数据流

1. Research Agent 根据研究问题选择 M2 Methodology。
2. Evidence Agent 或 Research Agent 生成 Evidence Card。
3. Knowledge Graph Builder 将实体、关系和 Evidence 绑定为图谱。
4. Validator 检查结构、Evidence 引用、反证、缺口和免责声明。
5. Path Analyzer 输出传导路径。
6. Chokepoint Analyzer 输出关键瓶颈节点、分数、证据、反证和缺口。
7. Review Agent 根据图谱与报告做一致性评审。

## 5. 设计边界

本 Feature 不引入图数据库、不做实时搜索、不做自动交易，也不从图谱评分推导任何证券价格或交易动作。当前实现是内存模型和 JSON 示例，足以支撑 M1-M8 验收、生产示例和后续运行时扩展。

