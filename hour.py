#!/usr/bin/python3

import json
import matplotlib.pyplot as plt

import time
import collections

# Python 字典类型转换为 JSON 对象
hi = 'data/a-hou.json'
f = open(hi, encoding='utf-8')  
data = f.read()  # 读文件

lists = json.loads(data)

hoursDict = [
    "00",
    "01",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
]

aDays = collections.OrderedDict()
bDays = collections.OrderedDict()
for h in hoursDict:
    aDays[h] = 0
for h in hoursDict:
    bDays[h] = 0

xB = []
yB = []
xA = []
yA = []

for item in lists:
    timeObj = time.localtime(item['msgCreateTime'])
    hour = time.strftime("%H", timeObj)
    timeFormat = time.strftime("%m-%d %H:%M", timeObj)
    if item['mesDes'] == 1:
        aDays.setdefault(hour, 0)
        aDays[hour] = aDays[hour] + 1
    else:
        bDays.setdefault(hour, 0)
        bDays[hour] = bDays[hour] + 1

for numbers in aDays:
    xA.append(numbers)
    yA.append(aDays[numbers])

for number in bDays:
    xB.append(number)
    yB.append(bDays[number])

print(xA, yA)
print(xB, yB)
# exit()
# plt.figure()
plt.plot(xA, yA, label="a")
plt.plot(xB, yB, label="b")
plt.xlabel('hour')
plt.ylabel('records')

plt.legend()
plt.show()
# plt.savefig('day.jpg')

# print("Python 原始数据：", repr(lists))
