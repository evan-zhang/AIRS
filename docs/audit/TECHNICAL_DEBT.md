# 技术债务清单 (TECHNICAL_DEBT)

## 🔴 高优先级（阻塞）

### TD-001: orchestrator/ 目录物理缺失
- **影响**：FEATURE-005 完整链路不可用
- **根因**：Sub-agent 可能写入到错误目录或文件未同步
- **修复**：重新生成 orchestrator/ 实现代码

### TD-002: memory/ 目录物理缺失
- **影响**：FEATURE-011 完整链路不可用
- **根因**：同 TD-001
- **修复**：重新生成 memory/ 实现代码

### TD-003: validate_* 脚本未做物理存在性检查
- **影响**：25 个验证脚本可能全部虚假 PASS
- **根因**：验证逻辑主要检查 import 和字符串匹配，未做 `Path.exists()` 前置断言
- **修复**：每个 validate 脚本头部增加 `assert_all_files_exist()` 前置检查

## 🟡 中优先级

### TD-004: 47 个 Schema 碎片化
- **影响**：维护成本高，容易不一致
- **修复**：统一到 `schemas/airs.json` 引用式管理

### TD-005: src/ 空目录
- **影响**：混淆
- **修复**：删除或明确用途

### TD-006: benchmark/ 与 docs/benchmark/ 内容重叠
- **修复**：benchmark/ 只放数据，docs/ 只放文档

### TD-007: REST API 无鉴权
- **影响**：不可公网部署
- **修复**：增加 API Key 中间件

### TD-008: validate 脚本数量膨胀（25 个）
- **影响**：维护负担
- **修复**：合并为 ~10 个按域分组

## 🟢 低优先级

### TD-009: Builder 模板与 Core 模板部分重叠
### TD-010: 缺少统一 CLI test coverage
### TD-011: Docker 未实际构建验证
### TD-012: Web UI 为静态原型，无完整交互
