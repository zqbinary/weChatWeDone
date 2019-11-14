#!/usr/bin/python3

import json
import matplotlib.pyplot as plt

import time

f = open('data/chat.json', encoding='utf-8')
data = f.read()
# 载入聊天记录，这个是统计每日的聊天记录
lists = json.loads(data)
aDays = {}
bDays = {}
xB = []
yB = []
xA = []
yA = []

for item in lists:
    timeObj = time.localtime(item['msgCreateTime'])
    day = time.strftime("%m-%d\n%u", timeObj)
    # day = time.strftime("%H", timeObj)
    timeFormat = time.strftime("%m-%d %H:%M", timeObj)
    if item['mesDes'] == 1:
        aDays.setdefault(day, 0)
        aDays[day] = aDays[day] + 1
    else:
        bDays.setdefault(day, 0)
        bDays[day] = bDays[day] + 1

for numbers in aDays:
    xA.append(numbers)
    yA.append(aDays[numbers])

for number in bDays:
    xB.append(number)
    yB.append(bDays[number])

# 打开，查看坐标信息
print(xA, xB, yA, yB)
# exit()

# plt.figure()
plt.plot(xA, yA, label="a")
plt.plot(xB, yB, label="b")
plt.xlabel('date')
plt.ylabel('records')

plt.legend()

# 显示或者下载
plt.show()
# plt.savefig('day.jpg')

# print("Python 原始数据：", repr(lists))
