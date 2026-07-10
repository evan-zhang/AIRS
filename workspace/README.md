# AI Research Workspace

`workspace/` 是 FEATURE-007 的最小可运行实现，提供统一 Research Workspace 入口，用于管理 Project、Session、Task Board、Timeline、Artifact、Memory、Snapshot、Version、Replay、Export、Collaboration 和 Audit。

## 使用方式

```python
from workspace import ResearchWorkspace

workspace = ResearchWorkspace()
project = workspace.create_project("AI 服务器供应链", "分析 AI 服务器供应链卡点")
session = workspace.open_session(project.project_id, "supply-chain-workflow")
workspace.register_artifact(project.project_id, session.session_id, "research_report", "研究报告草稿", "reports/demo.md")
print(workspace.dashboard(project.project_id))
```

## 边界

Workspace 是用户交互和研究资产管理入口。Agent 执行仍由 FEATURE-006 Runtime 调度，Workspace 不直接驱动 Methodology、Evidence、Knowledge Graph、Score、Evaluation 或 Report 业务模块。

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
