#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统计日志文件中的[EVALUATION RESULT]字段
"""
import re
from pathlib import Path
from collections import defaultdict

def analyze_logs(log_dir):
    """
    分析日志目录中的所有日志文件
    
    Args:
        log_dir: 日志目录路径
    """
    log_dir = Path(log_dir)
    
    # 统计结果
    pass_files = []
    fail_files = []
    no_result_files = []
    multiple_result_files = defaultdict(list)  # {文件名: [结果列表]}
    
    # 遍历所有日志文件
    log_files = sorted(log_dir.glob("*.log"))
    
    print(f"正在分析 {len(log_files)} 个日志文件...\n")
    
    for log_file in log_files:
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找所有[EVALUATION RESULT]行
            pattern = r'\[EVALUATION RESULT\]\s+(PASS|FAIL)'
            matches = re.findall(pattern, content)
            
            if not matches:
                no_result_files.append(log_file.name)
            elif len(matches) == 1:
                result = matches[0]
                if result == 'PASS':
                    pass_files.append(log_file.name)
                else:
                    fail_files.append(log_file.name)
            else:
                # 多个结果 - 只记录在multiple_result_files中，不重复添加到pass_files/fail_files
                multiple_result_files[log_file.name] = matches
                    
        except Exception as e:
            print(f"处理文件 {log_file.name} 时出错: {e}")
            no_result_files.append(log_file.name)
    
    # 打印统计结果
    print("=" * 80)
    print("统计结果")
    print("=" * 80)
    
    print(f"\n【PASS】共 {len(pass_files)} 个文件:")
    for fname in sorted(pass_files):
        print(f"  - {fname}")
    
    print(f"\n【FAIL】共 {len(fail_files)} 个文件:")
    for fname in sorted(fail_files):
        print(f"  - {fname}")
    
    print(f"\n【无[EVALUATION RESULT]字段】共 {len(no_result_files)} 个文件:")
    for fname in sorted(no_result_files):
        print(f"  - {fname}")
    
    print(f"\n【多个[EVALUATION RESULT]字段】共 {len(multiple_result_files)} 个文件:")
    for fname, results in sorted(multiple_result_files.items()):
        result_str = " -> ".join(results)
        print(f"  - {fname}: {result_str} ({len(results)}个结果)")
    
    print("\n" + "=" * 80)
    print("汇总统计")
    print("=" * 80)
    print(f"总文件数: {len(log_files)}")
    print(f"PASS: {len(pass_files)}")
    print(f"FAIL: {len(fail_files)}")
    print(f"无结果字段: {len(no_result_files)}")
    print(f"多个结果字段: {len(multiple_result_files)}")
    print(f"合计: {len(pass_files) + len(fail_files) + len(no_result_files) + len(multiple_result_files)}")
    
    # 保存结果到文件
    output_file = log_dir / "log_analysis_result.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("日志分析结果\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"【PASS】共 {len(pass_files)} 个文件:\n")
        for fname in sorted(pass_files):
            f.write(f"  {fname}\n")
        
        f.write(f"\n【FAIL】共 {len(fail_files)} 个文件:\n")
        for fname in sorted(fail_files):
            f.write(f"  {fname}\n")
        
        f.write(f"\n【无[EVALUATION RESULT]字段】共 {len(no_result_files)} 个文件:\n")
        for fname in sorted(no_result_files):
            f.write(f"  {fname}\n")
        
        f.write(f"\n【多个[EVALUATION RESULT]字段】共 {len(multiple_result_files)} 个文件:\n")
        for fname, results in sorted(multiple_result_files.items()):
            result_str = " -> ".join(results)
            f.write(f"  {fname}: {result_str} ({len(results)}个结果)\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("汇总统计\n")
        f.write("=" * 80 + "\n")
        f.write(f"总文件数: {len(log_files)}\n")
        f.write(f"PASS: {len(pass_files)}\n")
        f.write(f"FAIL: {len(fail_files)}\n")
        f.write(f"无结果字段: {len(no_result_files)}\n")
        f.write(f"多个结果字段: {len(multiple_result_files)}\n")
        f.write(f"合计: {len(pass_files) + len(fail_files) + len(no_result_files) + len(multiple_result_files)}\n")
    
    print(f"\n结果已保存到: {output_file}")


if __name__ == "__main__":
    log_dir = Path(__file__).parent / "logs"
    analyze_logs(log_dir)

