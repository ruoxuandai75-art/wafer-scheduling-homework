"""先预测输出，再运行程序。时间单位：分钟。"""

# 练习：把 start 改为 5，其他值保持原样，预测完工时刻。
# 再改变 processing，观察输出；尝试修复一次变量拼写错误。
job_id = "J1"
start = 2
processing = 4
finish = start + processing

print("作业", job_id)
print("开始时刻", start)
print("加工时间", processing)
print("完工时刻", finish)
