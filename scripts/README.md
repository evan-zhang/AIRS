# AIRS Scripts 目录

本目录包含 AIRS 项目的自检脚本。

---

## 目录结构

```
scripts/
├── README.md          # 本文件
├── check_structure.py # 目录结构完整性检查
└── validate_m1.py     # M1 验收标准检查
```

---

## 脚本说明

### check_structure.py

检查 AIRS 项目目录结构完整性。

**功能**：
- 检查所有必需目录是否存在
- 检查所有必需顶层文件是否存在
- 输出 PASS/FAIL 结果

**使用**：
```bash
python scripts/check_structure.py
```

**输出示例**：
```
✓ docs/ exists
✓ skills/ exists
✗ prompts/ missing
...
PASS: 45/46
```

**归属 Milestone**：M1

---

### validate_m1.py

验证 M1 里程碑的验收标准。

**功能**：
- 检查 M1 所有交付物
- 逐项输出 ✓/✗
- 最终给出 PASS/FAIL

**使用**：
```bash
python scripts/validate_m1.py
```

**输出示例**：
```
M1 验收标准检查：

结构标准：
✓ 所有必需顶层文件存在
✓ 所有必需目录存在
✓ 主要目录包含 README.md
✓ 自检脚本可运行

内容标准：
✓ README.md 有实际内容
✓ ARCHITECTURE.md 有实际内容
✓ AGENTS.md 有实际内容
✓ SKILL.md 有实际内容
✓ ROADMAP.md 有实际内容
✓ CONTRIBUTING.md 有实际内容

质量标准：
✓ 无空文件
✓ 有实际内容
✓ 有免责声明

最终结果：PASS
```

**归属 Milestone**：M1

---

## 脚本开发规范

### Python 脚本规范

1. **文件头**：
   ```python
   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-
   """
   脚本说明
   """
   ```

2. **函数命名**：
   - 使用蛇形命名法
   - ✅ `check_directory_exists()`
   - ❌ `checkDirectoryExists()`

3. **输出格式**：
   - 使用 ✓/✗ 表示通过/失败
   - 使用 PASS/FAIL 表示最终结果

### 脚本质量标准

- 可在 Python 3.7+ 运行
- 有清晰的输出
- 有错误处理
- 有使用说明

---

## 后续扩展

### M2-M8 扩展计划

- 添加 M2-M8 验证脚本
- 添加质量检查脚本
- 添加性能测试脚本

---

**最后更新**：2026-07-10
**归属 Milestone**：M1: Architecture Foundation
