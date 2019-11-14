#!/usr/bin/python3
import json
import jieba
import jieba.analyse
# 图像处理库
from PIL import Image
import collections  # 词频统计库
import wordcloud  # 词云展示库
import matplotlib.pyplot as plt  # 图像展示库
import numpy as np  # numpy数据处理库
import time

hi = 'data/a-hou.json'
f = open(hi, encoding='utf-8')
data = f.read()  # 读文件

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


# todo 两个人的对话，目前只能改变量，以后改成对话框
seg_list_exact = jieba.lcut_for_search(txtA)
remove_words = [u'的', u'，', ' ', '/']  # 自定义去除词库

object_list = []
for word in seg_list_exact:  # 循环读出每个分词
    if word not in remove_words:  # 如果不在去除词库中
        object_list.append(word)  # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list)  # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
print(word_counts_top10)  # 输出检查

# 词频展示
mask = np.array(Image.open('resource/wordcloud.jpg'))  # 定义词频背景
# 注意 这个是 mac的字体，具体
wc = wordcloud.WordCloud(
    font_path='/Library/Fonts/Songti.ttc',  # 设置字体格式
    mask=mask,  # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=100  # 字体最大值
)

wc.generate_from_frequencies(word_counts)  # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
plt.imshow(wc)  # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图像
