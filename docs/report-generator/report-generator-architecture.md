# Research Report Generator 架构

**Feature**：FEATURE-003 Research Report Generator  
**版本**：v0.1.0  
**状态**：MVP 可运行交付  

**免责声明**：本文档仅用于 AIRS 工程开发、研究质量控制和系统验证，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 设计目标

Research Report Generator 负责把 AIRS 既有层级输出组合成统一研究报告。它不采集数据、不创建投资建议、不改变 Scorecard 分数，也不替代 Research Agent 的方法论判断。它的边界是把已经产生的 Evidence、Knowledge Graph、Score/Evaluation、Prompt 和 Skill 输出编排成可审查、可回归验证的 Markdown 报告。

## 2. 架构位置

FEATURE-003 位于 Report Layer，向上服务 Research Agent、Review Agent 和 Verification Agent，向下引用既有成果：

- M1：沿用项目结构、生产治理、Completion Report 和回归流程。
- M2：通过 `methodology_refs` 引用 Methodology Layer。
- M3：通过 Evidence Card 和 Evidence Chain 引用 Evidence Engine。
- FEATURE-002：通过 Knowledge Graph Summary 引用节点、关系、路径和卡点分析。
- M4：通过 `prompt_ref` 引用 Report Prompt。
- M5：通过 `skill_ref` 引用 Report Skill。
- M6：通过 Score Summary 引用 Scorecard、Quality Gate 和 Evaluation 输出。

## 3. 模块结构

```text
report_generator/
├── model.py                # ResearchReport 与 ReportSection 数据模型
├── evidence_citation.py    # Evidence Card 引用表与缺失证据汇总
├── kg_summary.py           # Knowledge Graph 汇总
├── score_summary.py        # Scorecard 汇总
├── composer.py             # 12 核心章节 Composer
├── pipeline.py             # Pipeline 入口、输入归一化和一致性校验
└── __init__.py
```

## 4. 核心对象

`ReportPipeline` 接收标准 payload，执行输入归一化、一致性校验和报告渲染。`ReportComposer` 创建 `ResearchReport`。`SectionComposer` 固定输出 12 个核心章节，确保报告结构稳定。`EvidenceCitationBuilder`、`KGSummaryBuilder` 和 `ScoreSummaryBuilder` 负责把 M3、FEATURE-002、M6 的输出转换为报告片段。

## 5. 12 个核心章节

1. 报告元数据
2. 研究问题与范围
3. 方法论引用
4. 核心观点
5. Evidence 引用表
6. Evidence Chain 汇总
7. Knowledge Graph 汇总
8. Score Summary
9. 反方观点
10. 不确定性与缺口
11. 风险提示
12. 免责声明

这些章节是验证脚本的验收标准，也是 Review Agent 评审报告时的最低结构要求。

## 6. 合规边界

报告生成器必须保留免责声明，并禁止输出荐股、交易指令、自动交易、目标价和收益承诺。Scorecard 的 Quality Gate 只代表研究质量门禁，不代表投资评级。Evidence 和 Knowledge Graph 的摘要只表示来源和逻辑链路，不表示确定性预测。

