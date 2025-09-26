# /usr/bin/python

import os
from datetime import datetime

# 动态输入日期
date1_str = input("请输入第一个日期 (格式: YYYY-MM-DD): ")
date2_str = input("请输入第二个日期 (格式: YYYY-MM-DD): ")

# 转换为 datetime 对象
date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# 计算日期差
difference_days = (date2 - date1).days
difference_seconds = (date2 - date1).total_seconds()

print(f"两个日期之间的天数差: {difference_days}")
print(f"两个日期之间的秒数差: {difference_seconds}")