"""按任务单逐步补全的排程练习。

MODE='schedule'：跟踪固定顺序下的开始与完成时刻。
MODE='metrics'：补全 flow_time 和 tardiness 后观察指标。
MODE='rules'：再补全 order_jobs 中的 SPT、EDD 后比较规则。
NotImplementedError 提示当前需要完成的函数。
时间单位：分钟；单机、单工序、非抢占、无准备和搬运时间。
"""

MODE = "schedule"

# 实例 S1。固定顺序排程使用输入顺序。
jobs = [
    {"id": "J1", "p": 4, "r": 2, "d": 6},
    {"id": "J2", "p": 1, "r": 2, "d": 6},
    {"id": "J3", "p": 2, "r": 2, "d": 10},
]


def schedule_in_order(ordered_jobs):
    """按给定顺序排程，返回含 start、finish 的新字典列表。"""
    current = 0
    result = []
    for job in ordered_jobs:
        start = max(current, job["r"])
        finish = start + job["p"]
        row = job.copy()
        row["start"] = start
        row["finish"] = finish
        result.append(row)
        current = finish
    return result


def flow_time(row):
    # TODO：将下一行改成 return 完工时刻减去释放时刻。
    raise NotImplementedError("请补全 flow_time：计算流动时间")


def tardiness(row):
    # TODO：将下一行改成 return max(0, 完工时刻减去交期)。
    raise NotImplementedError("请补全 tardiness：计算拖期时间")


def processing_key(job):
    """加工时间相同时，按字符串编号升序处理并列。"""
    return (job["p"], job["id"])


def due_key(job):
    return (job["d"], job["id"])


def order_jobs(data, rule):
    """基础规则比较使用同一实例内同时释放、编号唯一的作业。"""
    if not data:
        raise ValueError("请提供至少一个作业")
    for job in data:
        if job["r"] != data[0]["r"]:
            raise ValueError("本练习使用同时释放的数据；分时到达需维护就绪集合")
    if rule == "FCFS":
        return list(data)  # 同时到达时，沿用输入中的登记顺序。
    if rule == "SPT":
        # TODO：使用 sorted(data, key=processing_key)。
        raise NotImplementedError("请补全 order_jobs 中的 SPT 排序")
    if rule == "EDD":
        # TODO：使用 sorted 和 due_key。
        raise NotImplementedError("请补全 order_jobs 中的 EDD 排序")
    raise ValueError("未知规则：" + rule)


def summarize_schedule(rows):
    """调用个人完成的指标函数，汇总排程结果。"""
    if not rows:
        raise ValueError("请提供至少一行排程结果")
    total_flow = 0
    total_tardiness = 0
    for row in rows:
        total_flow = total_flow + flow_time(row)
        total_tardiness = total_tardiness + tardiness(row)
    return {
        "cmax": max(row["finish"] for row in rows),
        "mean_flow": total_flow / len(rows),
        "total_tardiness": total_tardiness,
    }


def main():
    if MODE not in ("schedule", "metrics", "rules"):
        raise ValueError("MODE 可选 schedule、metrics、rules")
    rules = ["FCFS"]
    if MODE == "rules":
        rules = ["FCFS", "SPT", "EDD"]
    for rule in rules:
        ordered = list(jobs)
        if MODE == "rules":
            ordered = order_jobs(jobs, rule)
        rows = schedule_in_order(ordered)
        print("规则/顺序", rule)
        for row in rows:
            print(row["id"], "开始", row["start"], "完成", row["finish"])
        if MODE in ("metrics", "rules"):
            result = summarize_schedule(rows)
            print("最大完工时刻", result["cmax"])
            print("平均流动时间", result["mean_flow"])
            print("总拖期时间", result["total_tardiness"])


if __name__ == "__main__":
    main()
