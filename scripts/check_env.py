"""显示运行环境。可分别从终端、VS Code 与 AI 工具运行并比较。"""

from pathlib import Path
import os
import sys

root = Path(__file__).resolve().parents[1]
print("工作目录 cwd:", Path.cwd())
print("项目目录:", root)
print("Python 路径:", sys.executable)
print("Python 版本:", sys.version.split()[0])
print("Python prefix:", sys.prefix)
print("Conda 环境变量:", os.environ.get("CONDA_DEFAULT_ENV", "未设置"))
print("Conda prefix 变量:", os.environ.get("CONDA_PREFIX", "未设置"))
print("处于项目根目录:", Path.cwd().resolve() == root)
print("练习文件存在:", (root / "exercises" / "hello.py").is_file())
print("请核对 Python 路径，并与编辑器选择的解释器路径比较。")
