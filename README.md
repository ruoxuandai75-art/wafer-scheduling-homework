# 晶圆调度学习项目

第一周面向 Windows 初学者：理解 AI、建立个人项目、配置工具、完成场景作业并 commit 和 push。第2周起按对应任务单逐步使用 Python 练习代码，保留尚未要求完成的 TODO。

## 第一周从这里开始

先读 [第一周 Windows 学习指南](docs/week01_windows.md)，逐步向 AI 提问、追问、操作并核验。

1. 注册 GitHub，验证邮箱并接受师兄模板的访问邀请。
2. 打开师兄模板 <https://github.com/HawkW1027/wafer-scheduling-learning>，用 **Use this template** 创建自己名下的公开（Public）仓库 `wafer-scheduling-homework`，邀请师兄 `HawkW1027` 读取。
3. 安装或核对 VS Code、Git for Windows、Conda；亲手创建空文件夹 `C:\Users\你的Windows用户名\Projects\wafer-scheduling-homework`，在 VS Code 用“打开文件夹”打开它。
4. 按指南向 AI 询问如何把**个人仓库** clone 到当前空目录，检查文件层级与 `origin`。克隆后不再执行 `git init`。
5. 根据 `environment.yml` 创建或核对 `wafer-scheduling` 环境（Python 3.11）；选好 VS Code 解释器，在项目根目录运行 `python scripts/check_env.py`。
6. 推荐复制 [Word 作业模板](docs/notes/W01_作业模板.docx) 为 `docs/notes/W01_我的作业.docx`，用 Word 或 WPS 填写；[Markdown 版](docs/notes/W01_作业模板.md) 可选，只需提交一种。向 AI 学习 commit 与 push，并核对 GitHub 上的提交。

本周不要求修改 `hello.py` 或实现算法。离线模板仅供受阻时暂时练习，GitHub 获取与推送仍需补验。提交方式见 [提交说明](docs/submission.md)，Git 提问引导见 [Git 操作](docs/git_workflow.md)。

## 第一周文件位置

以下路径相对于项目根目录，即本 README 与 environment.yml 所在文件夹。

- [先读这里](docs/week01/先读这里.txt)、[任务清单（Word）](docs/week01/任务清单.docx)、[学习材料（Word）](docs/week01/学习材料.docx)。
- 正式模板：`docs/notes/W01_作业模板.docx`；可选格式：`docs/notes/W01_作业模板.md`。
- 自己的答案：`docs/notes/W01_我的作业.docx` 或 `docs/notes/W01_我的作业.md`；附件：`docs/notes/W01_附件/`。

Word 文件若不能在线预览，请下载后用 Word 或 WPS 打开。本周不要求会渲染 Markdown。

## 后续练习与目录

基础练习使用 Python 标准库，时间单位统一为分钟。`exercises/` 按任务单逐项完成；`data/` 放教学实例；`results/` 放结果；`scripts/check_env.py` 显示目录和解释器；`docs/` 保存学习记录、任务卡与交接。环境目录不放入作业仓库。

每周要求以当周任务清单为准。已保存的代码、结果和记录继续沿用；不要让 AI 提前补全后续 TODO。
