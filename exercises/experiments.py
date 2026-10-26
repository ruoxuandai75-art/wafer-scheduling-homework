"""读取教学实例，调用已完成的排序、排程、指标与自查函数。

默认运行三个实例与三个规则，共九组实验，并保存逐作业排程。
--template 生成待填结果表；--output 指定汇总结果路径。
--schedules-output 指定逐作业排程路径。
可以在 RULES 和数据文件中增加实验设置。
"""

import argparse
import csv
import json
from pathlib import Path
import platform
import shlex
import sys

from scheduling import flow_time, order_jobs, schedule_in_order, summarize_schedule, tardiness
from validate_schedule import validate_schedule


ROOT = Path(__file__).resolve().parents[1]
RULES = ["FCFS", "SPT", "EDD"]
FIELDS = [
    "instance", "rule", "order", "cmax", "mean_flow", "total_tardiness",
    "unit", "code_commit", "python_version", "command",
]
SCHEDULE_FIELDS = [
    "instance", "rule", "id", "p", "r", "d", "start", "finish", "flow_time", "tardiness",
]


def load_instances(path):
    """读取 {实例名: 作业列表} 格式的 JSON 文件。"""
    with open(path, encoding="utf-8") as stream:
        return json.load(stream)


def run_experiments(instances):
    """返回 (汇总记录列表, 逐作业记录列表)；教学 TODO 完成后即可运行。"""
    records = []
    schedule_records = []
    for instance, jobs in instances.items():
        for rule in RULES:
            ordered = order_jobs(jobs, rule)
            rows = schedule_in_order(ordered)
            validation_result = validate_schedule(jobs, rows)
            if validation_result is not None:
                raise ValueError("validate_schedule 检查成功时应返回 None，发现错误时抛出 ValueError")
            result = summarize_schedule(rows)
            records.append({
                "instance": instance,
                "rule": rule,
                "order": " ".join(row["id"] for row in rows),
                "cmax": result["cmax"],
                "mean_flow": result["mean_flow"],
                "total_tardiness": result["total_tardiness"],
                "unit": "minute",
            })
            for row in rows:
                schedule_records.append({
                    "instance": instance,
                    "rule": rule,
                    "id": row["id"],
                    "p": row["p"],
                    "r": row["r"],
                    "d": row["d"],
                    "start": row["start"],
                    "finish": row["finish"],
                    "flow_time": flow_time(row),
                    "tardiness": tardiness(row),
                })
    return records, schedule_records


def make_template(instances):
    """保留每组实验的实例名、规则与单位，其余值供填写。"""
    records = []
    for instance in instances:
        for rule in RULES:
            records.append({"instance": instance, "rule": rule, "unit": "minute"})
    return records


def write_csv(output, fieldnames, records):
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print("已写入", len(records), "行：", output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "data" / "instances.json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--schedules-output", type=Path)
    parser.add_argument("--commit", default="", help="用于本次实验的代码提交编号")
    parser.add_argument("--template", action="store_true", help="生成待填结果表")
    args = parser.parse_args()
    instances = load_instances(args.data)
    if args.template:
        records = make_template(instances)
        schedule_records = []
        default_name = "results_template.csv"
        default_schedule_name = "schedules_template.csv"
    else:
        records, schedule_records = run_experiments(instances)
        default_name = "experiment_results.csv"
        default_schedule_name = "schedules.csv"
        # CSV 保存本次运行使用的解释器版本和命令，便于个人复现。
        for record in records:
            record["code_commit"] = args.commit
            record["python_version"] = platform.python_version()
            record["command"] = shlex.join([sys.executable] + sys.argv)
    output = args.output or ROOT / "results" / default_name
    schedules_output = args.schedules_output or ROOT / "results" / default_schedule_name
    if output.resolve() == schedules_output.resolve():
        raise ValueError("汇总表与逐作业排程表请使用两个文件路径")
    write_csv(output, FIELDS, records)
    write_csv(schedules_output, SCHEDULE_FIELDS, schedule_records)


if __name__ == "__main__":
    main()
