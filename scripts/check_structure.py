#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIRS 项目目录结构完整性检查脚本

检查 AIRS 项目的目录结构和必需文件是否存在。
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

# 必需的顶层文件
TOP_LEVEL_FILES = [
    "README.md",
    "ROADMAP.md",
    "ARCHITECTURE.md",
    "AGENTS.md",
    "SKILL.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "CHANGELOG.md",
]

# 必需的目录
REQUIRED_DIRS = [
    "docs",
    "skills",
    "prompts",
    "schemas",
    "scoring",
    "evaluation",
    "benchmark",
    "examples",
    "templates",
    "scripts",
    ".github",
]

# docs 子目录
DOCS_SUBDIRS = [
    "overview",
    "architecture",
    "methodology",
    "research-engine",
    "evidence-engine",
    "score-engine",
    "report-engine",
    "evaluation-engine",
    "knowledge-graph",
    "data-sources",
    "production",
    "governance",
]

# skills 子目录
SKILLS_SUBDIRS = [
    "master",
    "hot-topic",
    "industry",
    "supply-chain",
    "chokepoint",
    "financial",
    "news",
    "evidence",
    "committee",
    "valuation",
    "risk",
    "report",
    "verification",
]

# prompts 子目录
PROMPTS_SUBDIRS = [
    "_dsl",
    "hot-topic",
    "industry",
    "supply-chain",
    "chokepoint",
    "financial",
    "news",
    "evidence",
    "committee",
    "valuation",
    "risk",
    "report",
]

# schemas 子目录
SCHEMAS_SUBDIRS = [
    "common",
    "research",
    "evidence",
    "score",
    "report",
    "evaluation",
]

# benchmark 子目录
BENCHMARK_SUBDIRS = [
    "ai",
    "semiconductor",
    "innovative-drug",
    "robotics",
    "new-energy",
    "general",
]

# examples 子目录
EXAMPLES_SUBDIRS = [
    "reports",
    "evidence",
    "scores",
    "workflows",
]


def check_file_exists(file_path: Path) -> bool:
    """检查文件是否存在"""
    return file_path.exists() and file_path.is_file()


def check_dir_exists(dir_path: Path) -> bool:
    """检查目录是否存在"""
    return dir_path.exists() and dir_path.is_dir()


def check_top_level_files() -> Tuple[int, int, List[str]]:
    """检查顶层文件"""
    passed = 0
    failed = []
    
    print("\n=== 检查顶层文件 ===")
    
    for file_name in TOP_LEVEL_FILES:
        file_path = PROJECT_ROOT / file_name
        if check_file_exists(file_path):
            print(f"✓ {file_name} exists")
            passed += 1
        else:
            print(f"✗ {file_name} missing")
            failed.append(file_name)
    
    return passed, len(TOP_LEVEL_FILES), failed


def check_required_dirs() -> Tuple[int, int, List[str]]:
    """检查必需目录"""
    passed = 0
    failed = []
    
    print("\n=== 检查必需目录 ===")
    
    for dir_name in REQUIRED_DIRS:
        dir_path = PROJECT_ROOT / dir_name
        if check_dir_exists(dir_path):
            print(f"✓ {dir_name}/ exists")
            passed += 1
        else:
            print(f"✗ {dir_name}/ missing")
            failed.append(dir_name)
    
    return passed, len(REQUIRED_DIRS), failed


def check_subdirs(parent_dir: str, subdirs: List[str]) -> Tuple[int, int, List[str]]:
    """检查子目录"""
    passed = 0
    failed = []
    
    print(f"\n=== 检查 {parent_dir}/ 子目录 ===")
    
    parent_path = PROJECT_ROOT / parent_dir
    if not check_dir_exists(parent_path):
        print(f"✗ {parent_dir}/ does not exist, skipping subdirectory check")
        return 0, len(subdirs), subdirs
    
    for subdir_name in subdirs:
        subdir_path = parent_path / subdir_name
        if check_dir_exists(subdir_path):
            print(f"✓ {parent_dir}/{subdir_name}/ exists")
            passed += 1
        else:
            print(f"✗ {parent_dir}/{subdir_name}/ missing")
            failed.append(f"{parent_dir}/{subdir_name}")
    
    return passed, len(subdirs), failed


def check_dir_readmes() -> Tuple[int, int, List[str]]:
    """检查主要目录的 README"""
    passed = 0
    failed = []
    
    print("\n=== 检查主要目录 README ===")
    
    readme_dirs = [
        "docs",
        "skills",
        "prompts",
        "schemas",
        "scoring",
        "evaluation",
        "benchmark",
        "examples",
        "templates",
        "scripts",
    ]
    
    for dir_name in readme_dirs:
        readme_path = PROJECT_ROOT / dir_name / "README.md"
        if check_file_exists(readme_path):
            print(f"✓ {dir_name}/README.md exists")
            passed += 1
        else:
            print(f"✗ {dir_name}/README.md missing")
            failed.append(f"{dir_name}/README.md")
    
    return passed, len(readme_dirs), failed


def check_templates() -> Tuple[int, int, List[str]]:
    """检查模板文件"""
    passed = 0
    failed = []
    
    print("\n=== 检查模板文件 ===")
    
    templates = [
        "templates/report-template.md",
        "templates/evidence-card-template.md",
        "templates/score-card-template.md",
        "templates/benchmark-case-template.md",
        "templates/skill-template.md",
    ]
    
    for template in templates:
        template_path = PROJECT_ROOT / template
        if check_file_exists(template_path):
            print(f"✓ {template} exists")
            passed += 1
        else:
            print(f"✗ {template} missing")
            failed.append(template)
    
    return passed, len(templates), failed


def check_scripts() -> Tuple[int, int, List[str]]:
    """检查脚本文件"""
    passed = 0
    failed = []
    
    print("\n=== 检查脚本文件 ===")
    
    scripts = [
        "scripts/check_structure.py",
        "scripts/validate_m1.py",
    ]
    
    for script in scripts:
        script_path = PROJECT_ROOT / script
        if check_file_exists(script_path):
            print(f"✓ {script} exists")
            passed += 1
        else:
            print(f"✗ {script} missing")
            failed.append(script)
    
    return passed, len(scripts), failed


def main():
    """主函数"""
    print("=" * 60)
    print("AIRS 项目目录结构完整性检查")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    all_failed = []
    
    # 检查顶层文件
    passed, total, failed = check_top_level_files()
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查必需目录
    passed, total, failed = check_required_dirs()
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 docs 子目录
    passed, total, failed = check_subdirs("docs", DOCS_SUBDIRS)
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 skills 子目录
    passed, total, failed = check_subdirs("skills", SKILLS_SUBDIRS)
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 prompts 子目录
    passed, total, failed = check_subdirs("prompts", PROMPTS_SUBDIRS)
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 schemas 子目录
    passed, total, failed = check_subdirs("schemas", SCHEMAS_SUBDIRS)
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 benchmark 子目录
    passed, total, failed = check_subdirs("benchmark", BENCHMARK_SUBDIRS)
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 examples 子目录
    passed, total, failed = check_subdirs("examples", EXAMPLES_SUBDIRS)
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 scoring 子目录
    passed, total, failed = check_subdirs("scoring", ["rubrics"])
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 evaluation 子目录
    passed, total, failed = check_subdirs("evaluation", ["rubrics"])
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查 .github 子目录
    passed, total, failed = check_subdirs(".github", ["ISSUE_TEMPLATE"])
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查主要目录 README
    passed, total, failed = check_dir_readmes()
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查模板文件
    passed, total, failed = check_templates()
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 检查脚本文件
    passed, total, failed = check_scripts()
    total_passed += passed
    total_failed += (total - passed)
    all_failed.extend(failed)
    
    # 输出总结
    print("\n" + "=" * 60)
    print("检查总结")
    print("=" * 60)
    print(f"通过: {total_passed}")
    print(f"失败: {total_failed}")
    print(f"总计: {total_passed + total_failed}")
    
    if all_failed:
        print("\n缺失项目:")
        for item in all_failed:
            print(f"  - {item}")
    
    print("\n" + "=" * 60)
    if total_failed == 0:
        print("结果: PASS")
        print("=" * 60)
        return 0
    else:
        print(f"结果: FAIL ({total_passed}/{total_passed + total_failed})")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
