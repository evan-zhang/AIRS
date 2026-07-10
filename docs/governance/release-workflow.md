# AIRS Release Workflow（发布流程）

**版本**：v1.0.0  
**适用范围**：AIRS V1.0 及后续发布

## 1. 发布角色

- Release Manager：负责版本范围、发布窗口和最终决策。
- Code Agent：负责文件变更、脚本修复和文档更新。
- Review Agent：负责内容质量、逻辑一致性和合规审查。
- Verification Agent：负责执行验证脚本和生产检查。

## 2. Branch 策略

推荐分支：

- `main`：稳定生产分支。
- `release/vX.Y.Z`：发布准备分支。
- `feature/*`：功能或文档新增。
- `fix/*`：补丁修复。

发布分支只能接受与当前版本相关的修复，不接受无关重构。

## 3. Tag 策略

正式发布使用：

```text
v1.0.0
v1.0.1
v1.1.0
```

预发布使用：

```text
v1.1.0-alpha.1
v1.1.0-beta.1
v1.1.0-rc.1
```

Tag 必须对应已经通过 `scripts/production_check.py` 的 commit。

## 4. Release 流程

1. 创建 Issue 或 Release Task。
2. 确认版本号和发布范围。
3. 创建 release 分支。
4. 完成变更并更新 CHANGELOG。
5. 若修改核心文件，新增 ADR。
6. 运行全部 validate 脚本。
7. 运行 `scripts/production_check.py`。
8. 完成 PR Review。
9. 合并到 main。
10. 创建 tag。
11. 发布 Release Notes。

## 5. CI/CD 要求

最低 CI 要求：

- 运行全部 `scripts/validate_*.py`。
- 运行 `scripts/production_check.py`。
- 检查 Python 脚本退出码。
- 保存验证输出。

未来 CI 可增强：

- Markdown link check。
- JSON Schema lint。
- 禁止投资建议表达扫描。
- Benchmark runner 和 Scorecard runner。

## 6. 回滚流程

如果发布失败：

- Patch 问题：创建 `fix/vX.Y.Z` 分支，修复后发布 patch。
- 合规问题：立即标记当前 release 不推荐使用，优先发布修复版本。
- 结构问题：新增 ADR，说明是否需要 Major 版本处理。

## 7. 免责声明

Release Workflow 用于管理 AIRS 工程发布，不代表任何投资结论、评分或研究报告有效，不构成投资建议，不提供交易指令或收益承诺。
