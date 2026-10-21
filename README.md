# python-playground

个人 Python 小工具试验场，附带静态演示页。

**线上地址：** https://junx1226.github.io/python-playground/

## 内容

| 文件 | 说明 |
|---|---|
| `index.html` | 站点入口页，链到 demo 与脚本说明 |
| `test.htm` | 文本框悬浮显示字体信息 demo 页（纯前端，无外部依赖） |
| `dedup_excel.py` | Excel 去重工具：按指定列去除重复行，仅保留唯一记录，支持自动生成输出文件名 |
| `test.py` | 总和差值计算器：`结果 = A × 28.97 + (sum − A) × 21.72`，交互式循环计算 |

## 本地使用

```bash
# Excel 去重
python dedup_excel.py -i input.xlsx -o output.xlsx -c "姓名,部门"

# 计算器
python test.py
```

依赖：`pandas`、`openpyxl`（仅 `dedup_excel.py` 需要）。

## 日常更新流程

改完文件后三行命令，线上站点约 1 分钟内自动更新：

```bash
git add .
git commit -m "改了什么"
git push
```

无需再进 GitHub Settings 配置。

> 刷新后看不到变化时，等半分钟或按 `Ctrl + F5` 强制刷新。  
> 在 GitHub 仓库的 **Actions** 页可以看到每次部署的执行记录。

## 部署说明

站点由 **GitHub Pages** 托管，配置为：

| 项 | 值 |
|---|---|
| Source | Deploy from a branch |
| Branch | `main` |
| Folder | `/ (root)` |
| 访问方式 | `https://<用户名>.github.io/<仓库名>/` |

因为源目录就是仓库根目录，**新增的 `.html` 文件 push 后即可直接访问**，路径与仓库中的相对路径一致。

### 注意事项

- 仓库为 **Public**，站点对全网可见，可能被搜索引擎收录。**不要提交含公司内部信息的内容。**
- 页面若是纯静态资源（HTML/CSS/JS，不依赖后端），都能直接部署；需要后端的脚本（如 `dedup_excel.py`）无法在 Pages 上运行，只能本地执行。

## 局域网临时演示（备选）

不想公开到外网时，可在本机起静态服务：

```bash
cd test
python -m http.server 8080 --bind 0.0.0.0
```

同网络下的同事用 `http://<本机IPv4>:8080/test.htm` 访问。本机 IP 用 `ipconfig` 查看。

- 关闭终端即停止服务。
- 若同事打不开，通常是 Windows 防火墙拦截：首次启动时弹出的「允许访问」提示勾选**专用网络**即可；未弹窗则需在防火墙高级设置中手动放行 TCP 8080。
