"""用小例子学习排程自查，只使用 Python 标准库。

直接运行：查看一个释放时刻检查示例。
加 --check：调用待完成的 validate_schedule，并运行正常与错误案例。
本文件包含独立数据，直接运行时无需导入其他练习。
"""

import argparse
from copy import deepcopy


JOBS = [
    {"id": "J1", "p": 4, "r": 2, "d": 6},
    {"id": "J2", "p": 1, "r": 2, "d": 6},
    {"id": "J3", "p": 2, "r": 2, "d": 10},
]

SAMPLE_ROWS = [
    {"id": "J1", "p": 4, "r": 2, "d": 6, "start": 2, "finish": 6},
    {"id": "J2", "p": 1, "r": 2, "d": 6, "start": 6, "finish": 7},
    {"id": "J3", "p": 2, "r": 2, "d": 10, "start": 7, "finish": 9},
]


def check_release_example(job, row):
    """示例：用原始作业的释放时刻核对一行安排。"""
    if row["start"] < job["r"]:
        raise ValueError(job["id"] + " 的开始时刻早于释放时刻")


def validate_schedule(jobs, rows):
    """检查成功返回 None；发现错误时抛出 ValueError 并说明原因。

    jobs 是原始作业；rows 按机器实际加工顺序排列。
    原始作业编号唯一，且加工时间为正。
    """
    # TODO：核对每个原始作业恰好出现一次，安排中的编号均来自 jobs。
    # TODO：按编号找到原始作业，核对 start >= r。
    # TODO：核对 finish - start == p；p、r 使用原始 jobs 中的数值。
    # TODO：核对相邻两行：前一行 finish <= 后一行 start。
    raise NotImplementedError("请补全 validate_schedule 的四类检查")


def run_checks():
    """可继续添加手算例和错误案例；每次构造独立副本。"""
    validate_schedule(JOBS, SAMPLE_ROWS)
    print("正常安排：通过")

    bad_release = deepcopy(SAMPLE_ROWS)
    bad_release[0]["start"] = 1
    bad_release[0]["finish"] = 5

    bad_duration = deepcopy(SAMPLE_ROWS)
    bad_duration[0]["finish"] = 5

    bad_overlap = deepcopy(SAMPLE_ROWS)
    bad_overlap[1]["start"] = 5
    bad_overlap[1]["finish"] = 6

    missing_job = deepcopy(SAMPLE_ROWS[:-1])
    duplicate_job = deepcopy(SAMPLE_ROWS)
    duplicate_job[-1] = deepcopy(duplicate_job[1])
    unknown_job = deepcopy(SAMPLE_ROWS)
    unknown_job[-1]["id"] = "JX"

    cases = [
        ("提前开始", bad_release),
        ("加工时长有误", bad_duration),
        ("机器占用重叠", bad_overlap),
        ("作业遗漏", missing_job),
        ("作业重复", duplicate_job),
        ("额外作业编号", unknown_job),
    ]
    for name, rows in cases:
        try:
            validate_schedule(JOBS, rows)
        except ValueError as error:
            print(name + "：已识别；", error)
        else:
            raise AssertionError(name + "：请补充相应检查")
    print("已通过正常案例与全部错误案例")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="运行个人完成的完整检查")
    args = parser.parse_args()
    if args.check:
        run_checks()
    else:
        check_release_example(JOBS[0], SAMPLE_ROWS[0])
        print("示例 J1：开始 2，释放 2，释放时刻检查通过")
        print("补全 validate_schedule 后运行：python exercises/validate_schedule.py --check")


if __name__ == "__main__":
    main()
