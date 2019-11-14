#!/usr/bin/python3
import json
import time

hi = 'data/a-hou.json'
f = open(hi, encoding='utf-8')
data = f.read()

lists = json.loads(data)
txtA = ''
txtB = ''
countA = 1
countB = 1
questions = ''
we = ''
for item in lists:
    timeObj = time.localtime(item['msgCreateTime'])
    timeFormat = time.strftime("%m-%d %H:%M", timeObj)
    msg = timeFormat + item['msgContent']

    if item['messageType'] != 1:
        continue

    if item['mesDes'] == 1:
        we += '\na' + msg
        txtA += ' ' + msg
        countA = countA + 1
    else:
        we += '\nb' + msg
        txtB += ' ' + msg
        countB = countB + 1
    if '？' in item['msgContent']:
        questions += '\n' + msg

print(countA, countB)
print(we)
file = open('output/weTalk.txt', mode='w')
file.write(we)
