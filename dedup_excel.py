#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Excel 去重工具 - 根据指定列去除重复行，仅保留唯一记录。
用法示例：
    python dedup_excel.py -i input.xlsx -o output.xlsx -c "姓名,部门"
    python dedup_excel.py -i input.xlsx -c "订单号"   # 自动生成输出文件名
"""

import pandas as pd
import argparse
import os
import sys


def deduplicate_excel(input_file, output_file=None, columns=None, keep='first'):
    """
    读取 Excel 文件，按指定列去重，保存结果。

    Parameters:
        input_file (str): 输入 Excel 文件路径。
        output_file (str): 输出文件路径，若为 None 则自动生成。
        columns (list): 用于去重的列名列表，若为 None 则按整行去重。
        keep (str): 保留重复项中的哪一个，可选 'first', 'last', False。
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"文件不存在: {input_file}")

    # 读取 Excel
    print(f"正在读取文件: {input_file}")
    df = pd.read_excel(input_file, engine='openpyxl')  # 支持 .xlsx
    print(f"原始行数: {len(df)}")

    # 检查指定的列是否存在
    if columns is not None:
        missing_cols = [col for col in columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"以下列在文件中不存在: {missing_cols}")
    else:
        # 未指定列，则使用所有列（整行去重）
        columns = df.columns.tolist()
        print("未指定去重列，将按整行去重。")

    # 去重
    print(f"按列 [{', '.join(columns)}] 去重，保留 '{keep}' 项...")
    df_dedup = df.drop_duplicates(subset=columns, keep=keep)
    print(f"去重后行数: {len(df_dedup)}")

    # 确定输出文件名
    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_deduped{ext}"
    print(f"保存结果到: {output_file}")

    # 保存 Excel
    df_dedup.to_excel(output_file, index=False, engine='openpyxl')
    print("去重完成！")


def main():
    parser = argparse.ArgumentParser(description="去除 Excel 文件中指定列的重复行")
    parser.add_argument('-i', '--input', required=True, help="输入的 Excel 文件路径 (.xlsx)")
    parser.add_argument('-o', '--output', help="输出的 Excel 文件路径 (默认在输入文件名后加 _deduped)")
    parser.add_argument('-c', '--columns', help="用于去重的列名，多个列用英文逗号分隔，例如 '姓名,部门'。若不指定，则按整行去重。")
    parser.add_argument('-k', '--keep', default='first', choices=['first', 'last', 'False'],
                        help="保留重复项中的哪一个：'first' 保留第一次出现的，'last' 保留最后一次，'False' 删除所有重复（即只保留完全唯一的行）。默认 'first'。")

    args = parser.parse_args()

    # 解析列名
    columns = None
    if args.columns:
        columns = [col.strip() for col in args.columns.split(',') if col.strip()]
        if not columns:
            print("警告: 未提供有效列名，将按整行去重。")
            columns = None

    try:
        deduplicate_excel(
            input_file=args.input,
            output_file=args.output,
            columns=columns,
            keep=args.keep
        )
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()