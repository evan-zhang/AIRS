#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIRS M1 验收标准检查脚本

检查 M1 里程碑的所有验收标准。
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent


def read_file_content(file_path: Path) -> str:
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return ""


def check_file_has_content(file_path: Path, min_length: int = 100) -> bool:
    """检查文件是否有实际内容"""
    if not file_path.exists() or not file_path.is_file():
        return False
    
    content = read_file_content(file_path)
    return len(content) >= min_length


def check_file_contains(file_path: Path, keywords: List[str]) -> bool:
    """检查文件是否包含关键词"""
    if not file_path.exists() or not file_path.is_file():
        return False
    
    content = read_file_content(file_path).lower()
    for keyword in keywords:
        if keyword.lower() not in content:
            return False
    return True


def check_structure_standards() -> Tuple[bool, List[str]]:
    """检查结构标准"""
    print("\n=== 结构标准 ===")
    
    passed = True
    issues = []
    
    # 检查顶层文件
    top_level_files = [
        "README.md", "ROADMAP.md", "ARCHITECTURE.md", 
        "AGENTS.md", "SKILL.md", "CONTRIBUTING.md", 
        "LICENSE", "CHANGELOG.md"
    ]
    
    print("检查顶层文件:")
    for file_name in top_level_files:
        file_path = PROJECT_ROOT / file_name
        if file_path.exists():
            print(f"  ✓ {file_name} 存在")
        else:
            print(f"  ✗ {file_name} 缺失")
            passed = False
            issues.append(f"缺失顶层文件: {file_name}")
    
    # 检查必需目录
    required_dirs = [
        "docs", "skills", "prompts", "schemas", 
        "scoring", "evaluation", "benchmark", 
        "examples", "templates", "scripts"
    ]
    
    print("检查必需目录:")
    for dir_name in required_dirs:
        dir_path = PROJECT_ROOT / dir_name
        if dir_path.exists() and dir_path.is_dir():
            print(f"  ✓ {dir_name}/ 存在")
        else:
            print(f"  ✗ {dir_name}/ 缺失")
            passed = False
            issues.append(f"缺失目录: {dir_name}")
    
    # 检查主要目录 README
    print("检查主要目录 README:")
    readme_dirs = [
        "docs", "skills", "prompts", "schemas", 
        "scoring", "evaluation", "benchmark", 
        "examples", "templates", "scripts"
    ]
    
    for dir_name in readme_dirs:
        readme_path = PROJECT_ROOT / dir_name / "README.md"
        if readme_path.exists():
            print(f"  ✓ {dir_name}/README.md 存在")
        else:
            print(f"  ✗ {dir_name}/README.md 缺失")
            passed = False
            issues.append(f"缺失 README: {dir_name}/README.md")
    
    # 检查自检脚本
    print("检查自检脚本:")
    scripts = [
        "scripts/check_structure.py",
        "scripts/validate_m1.py"
    ]
    
    for script in scripts:
        script_path = PROJECT_ROOT / script
        if script_path.exists():
            print(f"  ✓ {script} 存在")
        else:
            print(f"  ✗ {script} 缺失")
            passed = False
            issues.append(f"缺失脚本: {script}")
    
    return passed, issues


def check_content_standards() -> Tuple[bool, List[str]]:
    """检查内容标准"""
    print("\n=== 内容标准 ===")
    
    passed = True
    issues = []
    
    # 检查 README.md 内容
    print("检查 README.md:")
    readme_path = PROJECT_ROOT / "README.md"
    readme_keywords = [
        "AIRS", "投资研究", "证据", "免责声明"
    ]
    
    if check_file_contains(readme_path, readme_keywords):
        print("  ✓ README.md 有实际内容")
    else:
        print("  ✗ README.md 内容不完整")
        passed = False
        issues.append("README.md 内容不完整")
    
    # 检查 ARCHITECTURE.md 内容
    print("检查 ARCHITECTURE.md:")
    architecture_path = PROJECT_ROOT / "ARCHITECTURE.md"
    architecture_keywords = [
        "架构", "Evidence", "Score", "Report"
    ]
    
    if check_file_contains(architecture_path, architecture_keywords):
        print("  ✓ ARCHITECTURE.md 有实际内容")
    else:
        print("  ✗ ARCHITECTURE.md 内容不完整")
        passed = False
        issues.append("ARCHITECTURE.md 内容不完整")
    
    # 检查 AGENTS.md 内容
    print("检查 AGENTS.md:")
    agents_path = PROJECT_ROOT / "AGENTS.md"
    agents_keywords = [
        "Agent", "Code Agent", "Research Agent"
    ]
    
    if check_file_contains(agents_path, agents_keywords):
        print("  ✓ AGENTS.md 有实际内容")
    else:
        print("  ✗ AGENTS.md 内容不完整")
        passed = False
        issues.append("AGENTS.md 内容不完整")
    
    # 检查 SKILL.md 内容
    print("检查 SKILL.md:")
    skill_path = PROJECT_ROOT / "SKILL.md"
    skill_keywords = [
        "Master Skill", "证据", "反方观点"
    ]
    
    if check_file_contains(skill_path, skill_keywords):
        print("  ✓ SKILL.md 有实际内容")
    else:
        print("  ✗ SKILL.md 内容不完整")
        passed = False
        issues.append("SKILL.md 内容不完整")
    
    # 检查 ROADMAP.md 内容
    print("检查 ROADMAP.md:")
    roadmap_path = PROJECT_ROOT / "ROADMAP.md"
    roadmap_keywords = [
        "M1", "M2", "里程碑"
    ]
    
    if check_file_contains(roadmap_path, roadmap_keywords):
        print("  ✓ ROADMAP.md 有实际内容")
    else:
        print("  ✗ ROADMAP.md 内容不完整")
        passed = False
        issues.append("ROADMAP.md 内容不完整")
    
    # 检查 CONTRIBUTING.md 内容
    print("检查 CONTRIBUTING.md:")
    contributing_path = PROJECT_ROOT / "CONTRIBUTING.md"
    contributing_keywords = [
        "贡献", "Skill", "Prompt"
    ]
    
    if check_file_contains(contributing_path, contributing_keywords):
        print("  ✓ CONTRIBUTING.md 有实际内容")
    else:
        print("  ✗ CONTRIBUTING.md 内容不完整")
        passed = False
        issues.append("CONTRIBUTING.md 内容不完整")
    
    return passed, issues


def check_quality_standards() -> Tuple[bool, List[str]]:
    """检查质量标准"""
    print("\n=== 质量标准 ===")
    
    passed = True
    issues = []
    
    # 检查空文件
    print("检查空文件:")
    important_files = [
        "README.md", "ROADMAP.md", "ARCHITECTURE.md",
        "AGENTS.md", "SKILL.md", "CONTRIBUTING.md"
    ]
    
    for file_name in important_files:
        file_path = PROJECT_ROOT / file_name
        if check_file_has_content(file_path, min_length=50):
            print(f"  ✓ {file_name} 有实际内容")
        else:
            print(f"  ✗ {file_name} 内容过少或为空")
            passed = False
            issues.append(f"{file_name} 内容过少或为空")
    
    # 检查免责声明
    print("检查免责声明:")
    disclaimer_keywords = [
        "不构成投资建议", "免责", "风险"
    ]
    
    files_with_disclaimer = [
        "README.md", "LICENSE", "SKILL.md"
    ]
    
    for file_name in files_with_disclaimer:
        file_path = PROJECT_ROOT / file_name
        if check_file_contains(file_path, disclaimer_keywords):
            print(f"  ✓ {file_name} 包含免责声明")
        else:
            print(f"  ✗ {file_name} 缺少免责声明")
            passed = False
            issues.append(f"{file_name} 缺少免责声明")
    
    # 检查 AIRS 定位
    print("检查 AIRS 定位:")
    positioning_keywords = [
        "不是荐股", "不是自动交易", "研究框架"
    ]
    
    readme_path = PROJECT_ROOT / "README.md"
    if check_file_contains(readme_path, positioning_keywords):
        print("  ✓ README.md 正确定位 AIRS")
    else:
        print("  ✗ README.md AIRS 定位不清晰")
        passed = False
        issues.append("README.md AIRS 定位不清晰")
    
    return passed, issues


def check_template_files() -> Tuple[bool, List[str]]:
    """检查模板文件"""
    print("\n=== 模板文件 ===")
    
    passed = True
    issues = []
    
    templates = [
        "templates/report-template.md",
        "templates/evidence-card-template.md",
        "templates/score-card-template.md",
        "templates/benchmark-case-template.md",
        "templates/skill-template.md"
    ]
    
    print("检查模板文件:")
    for template in templates:
        template_path = PROJECT_ROOT / template
        if check_file_has_content(template_path, min_length=100):
            print(f"  ✓ {template} 存在并有内容")
        else:
            print(f"  ✗ {template} 缺失或内容过少")
            passed = False
            issues.append(f"{template} 缺失或内容过少")
    
    return passed, issues


def main():
    """主函数"""
    print("=" * 60)
    print("AIRS M1 验收标准检查")
    print("=" * 60)
    
    all_passed = True
    all_issues = []
    
    # 检查结构标准
    structure_passed, structure_issues = check_structure_standards()
    all_passed = all_passed and structure_passed
    all_issues.extend(structure_issues)
    
    # 检查内容标准
    content_passed, content_issues = check_content_standards()
    all_passed = all_passed and content_passed
    all_issues.extend(content_issues)
    
    # 检查质量标准
    quality_passed, quality_issues = check_quality_standards()
    all_passed = all_passed and quality_passed
    all_issues.extend(quality_issues)
    
    # 检查模板文件
    template_passed, template_issues = check_template_files()
    all_passed = all_passed and template_passed
    all_issues.extend(template_issues)
    
    # 输出总结
    print("\n" + "=" * 60)
    print("验收总结")
    print("=" * 60)
    
    print("\n结构标准:")
    print("  " + ("✓ 通过" if structure_passed else "✗ 不通过"))
    
    print("\n内容标准:")
    print("  " + ("✓ 通过" if content_passed else "✗ 不通过"))
    
    print("\n质量标准:")
    print("  " + ("✓ 通过" if quality_passed else "✗ 不通过"))
    
    print("\n模板文件:")
    print("  " + ("✓ 通过" if template_passed else "✗ 不通过"))
    
    if all_issues:
        print("\n发现问题:")
        for issue in all_issues:
            print(f"  - {issue}")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("最终结果: PASS")
        print("=" * 60)
        print("\n✓ M1 验收标准全部通过")
        return 0
    else:
        print("最终结果: FAIL")
        print("=" * 60)
        print(f"\n✗ M1 验收标准未完全通过，发现 {len(all_issues)} 个问题")
        return 1


if __name__ == "__main__":
    sys.exit(main())
