#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
找出所有不在Pass列表中的任务ID
"""
import os
import re
from pathlib import Path

def extract_task_id_and_result(file_path):
    """从文件中提取任务ID和Result"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 提取任务ID (格式: Task: HumanEval/122)
        task_match = re.search(r'Task:\s*HumanEval/(\d+)', content)
        if not task_match:
            return None, None
            
        task_id = int(task_match.group(1))
        
        # 提取Result (格式: Result: PASS 或 Result: Pass)
        result_match = re.search(r'Result:\s*(PASS|Pass|pass|FAIL|Fail|fail|ERROR|Error|error)', content, re.IGNORECASE)
        if not result_match:
            return None, None
            
        result = result_match.group(1).upper()
        
        return task_id, result
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None

def main():
    # 获取当前脚本所在目录
    script_dir = Path(__file__).parent
    eval_logs_dir = script_dir
    
    # 查找所有 evaluation_result_*.txt 文件
    result_files = list(eval_logs_dir.glob("evaluation_result_*.txt"))
    
    pass_task_ids = set()
    all_task_ids = set()
    task_id_to_result = {}
    
    print(f"正在处理 {len(result_files)} 个文件...\n")
    
    for file_path in sorted(result_files):
        task_id, result = extract_task_id_and_result(file_path)
        
        if task_id is not None:
            all_task_ids.add(task_id)
            task_id_to_result[task_id] = result
            
            if result == 'PASS':
                pass_task_ids.add(task_id)
    
    # 找出所有不在Pass列表中的任务ID
    non_pass_ids = sorted(all_task_ids - pass_task_ids)
    
    # 找出可能缺失的任务ID（0-163范围内但不在文件中的）
    max_id = max(all_task_ids) if all_task_ids else 163
    all_possible_ids = set(range(0, max_id + 1))
    missing_ids = sorted(all_possible_ids - all_task_ids)
    
    print("="*60)
    print("统计结果")
    print("="*60)
    print(f"总任务数: {len(all_task_ids)}")
    print(f"Pass任务数: {len(pass_task_ids)}")
    print(f"非Pass任务数: {len(non_pass_ids)}")
    print(f"缺失任务数（0-{max_id}范围内）: {len(missing_ids)}")
    
    print("\n" + "="*60)
    print("不在Pass列表中的任务ID（有结果文件）:")
    print("="*60)
    if non_pass_ids:
        for task_id in non_pass_ids:
            result = task_id_to_result.get(task_id, 'UNKNOWN')
            print(f"  Task ID {task_id}: {result}")
    else:
        print("  无")
    
    print("\n" + "="*60)
    print(f"缺失的任务ID（0-{max_id}范围内但无结果文件）:")
    print("="*60)
    if missing_ids:
        print(f"  {missing_ids}")
        print(f"  共 {len(missing_ids)} 个")
    else:
        print("  无")
    
    print("\n" + "="*60)
    print("所有不在Pass列表中的ID（包括缺失的）:")
    print("="*60)
    all_non_pass = sorted(set(non_pass_ids) | set(missing_ids))
    if all_non_pass:
        print(f"  {all_non_pass}")
        print(f"  共 {len(all_non_pass)} 个")
    else:
        print("  无")

if __name__ == "__main__":
    main()
