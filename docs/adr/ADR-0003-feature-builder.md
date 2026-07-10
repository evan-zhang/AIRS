# ADR-0003: FEATURE-001 AIRS Builder

**状态**：Accepted  
**日期**：2026-07-10  
**Feature**：FEATURE-001 AIRS Builder  

## 背景

AIRS v1.0.0 已完成 M1-M8 生产级规范库，但新增 Feature 的开发输入仍需要人工整理 Issue、ADR、Spec、Skill、Prompt、Schema、Tests、Benchmark、PR Checklist 和 Release Notes。为了让 Code Agent 能在 Go 模式下稳定开发，需要一个标准化 Feature Package 生成机制。

## 决策

新增 AIRS Builder：

- 文档位于 `docs/builder/`。
- 入口位于 `builder/main.py`。
- 模板注册位于 `builder/registry.py`。
- 输入 Schema 位于 `schemas/builder/`。
- 生成模板位于 `templates/builder/`。
- 示例输出位于 `builder-output/`。
- 自检脚本位于 `scripts/validate_builder.py`。

Builder 采用本地轻量模板生成，不引入运行时服务，不改变 M1-M8 已验收资产。

## 原因

- Feature Package 是工程开发入口，不应散落在多个手写文档中。
- Builder 可以把合规、引用和回归要求前置。
- 通过模板引用 M4、M5、M7，可避免重复定义 Prompt、Skill 和 Benchmark 规则。

## 影响

正向影响：

- Code Agent 获得完整开发包。
- Review Agent 获得可审查材料。
- Verification Agent 获得测试和 Benchmark 输入。
- Feature 开发更容易被 CHANGELOG、ADR 和 Completion Report 追踪。

限制：

- 当前 Builder 只生成文件，不执行运行时调度。
- 生成物仍需人工或 Agent 审查。
- 若未来需要图数据库、API 接入或 UI，需要新增 Feature 和 ADR。

## 合规

Builder 生成物必须包含免责声明，不得输出荐股、自动交易、交易指令、目标价或收益承诺。Builder 只用于 AIRS 工程开发与研究质量控制，不构成投资建议。

## 免责声明

本 ADR 仅用于 AIRS 工程治理和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

