"""一个字典记录一个作业，列表保存多个作业。时间单位：分钟。"""

# 将一个 Lot 当前的一次加工抽象为单工序作业。
# id：作业编号；p：加工时间；r：释放时刻；d：期望完成的交期。
# 练习：增加一个 p=3 的作业，预测总加工时间，再运行核对。
jobs = [
    {"id": "J1", "p": 4, "r": 2, "d": 6},
    {"id": "J2", "p": 1, "r": 2, "d": 6},
    {"id": "J3", "p": 2, "r": 2, "d": 10},
]

total_processing = 0
for job in jobs:
    print(job["id"], "加工时间", job["p"], "释放", job["r"], "交期", job["d"])
    total_processing = total_processing + job["p"]

print("作业数量", len(jobs))
print("总加工时间", total_processing)
