# AIRS Install Guide

免责声明：本安装指南仅用于 AIRS 工程部署和研究流程演示，不构成投资建议。

## Requirements

- Python 3.11+
- Git
- 可选：Docker 与 Docker Compose

## Local Install

```bash
git clone <repo-url> AIRS
cd AIRS
python3 cli/airs.py init
python3 cli/airs.py validate
python3 cli/airs.py demo nvidia
```

AIRS Platform 1.0 的 CLI、API、Web UI 均使用 Python 标准库和静态文件，不需要安装第三方 Python 包。

