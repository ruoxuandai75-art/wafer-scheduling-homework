# 实验结果

`results_template.csv` 预留三个实例与三个规则的九行结果。空白单元格表示待填写；数值为零的结果写 `0`。

| 字段 | 含义 |
| --- | --- |
| instance | 实例名称，如 S1 |
| rule | 规则名称：FCFS、SPT、EDD |
| order | 实际加工顺序，以空格分隔编号 |
| cmax | 最大完工时刻 |
| mean_flow | 平均流动时间 |
| total_tardiness | 总拖期时间 |
| unit | `minute`，单位为分钟 |
| code_commit | 运行所用代码的提交编号，使用 Git 时填写 |
| python_version | 实际 Python 版本 |
| command | 实际运行命令 |

基础规则实验使用单机、单工序、非抢占、同时释放、零准备时间与零搬运时间的模型。FCFS 按输入登记顺序；SPT 按 `(p, id)`；EDD 按 `(d, id)`。编号以字符串升序处理并列。

`data/instances.json` 中的 `family` 表示配方族，供扩展任务使用；基础实验直接沿用 `p` 作为加工时间。

完成任务单要求的指标、排序和排程自查函数后，运行：

```sh
python exercises/experiments.py
```

程序将九行汇总写入 `results/experiment_results.csv`，将逐作业排程写入 `results/schedules.csv`。逐作业表包含实例、规则、作业编号、原始数据、开始时刻、完工时刻、流动时间和拖期时间，共 30 行。

如需记录代码版本，可先用 `git rev-parse HEAD` 查询，再以 `--commit 实际提交编号` 运行。`--output 汇总表路径` 与 `--schedules-output 排程表路径` 可保存到另外两个文件，方便比较不同版本。

`schedules_template.csv` 提供逐作业表的表头。使用 `--template` 可重新生成九行待填汇总表和逐作业空表。

按任务单完成对结果的解释，将文字或图表放入主题记录。临时输出放入 `results/tmp/`。
