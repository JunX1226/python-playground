# python-playground

个人 Python 小工具试验场。

## 内容

| 文件 | 说明 |
|---|---|
| `dedup_excel.py` | Excel 去重工具：按指定列去除重复行，仅保留唯一记录，支持自动生成输出文件名 |
| `test.py` | 总和差值计算器：`结果 = A × 28.97 + (sum − A) × 21.72`，交互式循环计算 |
| `test.htm` | 文本框悬浮显示字体信息 demo 页 |

## 使用

```bash
# Excel 去重
python dedup_excel.py -i input.xlsx -o output.xlsx -c "姓名,部门"

# 计算器
python test.py
```

依赖：`pandas`、`openpyxl`（仅 dedup_excel.py 需要）。
