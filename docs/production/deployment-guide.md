# AIRS Deployment Guide（部署指南）

**版本**：v1.0.0  
**适用范围**：AIRS 文档型生产发布  
**面向角色**：Code Agent、运维人员、Release Manager

## 1. 部署形态

AIRS V1.0 的部署不是传统服务部署，而是生产级知识库与规范库发布。部署目标是确保仓库中的文档、Prompt、Skill、Schema、Benchmark、Example 和验证脚本处于一致、可验证、可回滚的状态。

## 2. 环境要求

最低要求：

- Python 3.10 或以上。
- 可读取项目根目录的本地文件系统。
- 能执行 `python3 scripts/*.py`。
- Git 可用，用于分支、Tag、变更追踪和回滚。

推荐执行目录：

```bash
cd /Users/evan/.openclaw/gateways/life/state/workspace-life/projects/AIRS
```

## 3. 部署前检查

部署前必须确认：

- `README.md` 标注 V1.0 Production 状态。
- `CHANGELOG.md` 包含 `1.0.0` 发布记录。
- `ROADMAP.md` 标注 M1-M8 完成。
- `docs/production/release-checklist.md` 已完成。
- `.github/` 下 Issue、PR、CODEOWNERS、SECURITY、SUPPORT 文件完整。
- `scripts/production_check.py` 输出最终 PASS。

## 4. 部署步骤

1. 从主分支或 release 分支获取最新代码。
2. 运行 `python3 scripts/production_check.py`。
3. 检查 `docs/production/M8_COMPLETION_REPORT.md`、`PROJECT_HEALTH_REPORT.md` 和 `FINAL_REVIEW.md`。
4. 确认无未解释的核心文件变更。
5. 按 `docs/governance/release-workflow.md` 创建 release tag。
6. 发布 Release Notes。

## 5. 回滚策略

如果部署后发现问题：

- 文档错误：创建 patch 分支，修正文档，运行完整检查，发布 patch 版本。
- 验证脚本错误：修复脚本并增加失败样例说明，发布 patch 版本。
- 治理规则错误：新增 ADR，说明规则变更和影响范围。
- 严重合规风险：立即撤回 Release Notes 中的问题条目，标记版本为不推荐使用，并发布修复版本。

## 6. 部署验收

部署完成后应形成以下记录：

- 发布版本号。
- Git commit SHA。
- Tag 名称。
- 完整自检结果。
- 已知风险和技术债。
- 发布负责人和复核人。

## 7. 免责声明

AIRS 部署结果仅表示研究框架、文档和自检脚本满足项目定义的生产验收标准，不代表任何投资结论有效，不构成投资建议，不提供交易指令或收益承诺。
