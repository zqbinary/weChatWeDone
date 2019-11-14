# 微信聊天记录分析

## 项目来源
难以启齿。

## 目前的功能
通过下载微信聊天记录：

* 聊天条数/day*person，统计每天的聊天条数，并做成折线图；
* 聊天条数/hour, 统计每小时的聊天条数，看下哪个时间点聊天比较多；
* 把微信聊天记录转成纯文本；
* 词频分析，高频词，做成 word cloud；


## 环境和配置

主要是如何获取微信聊天记录的问题，这个可以看相关文章
[土办法导出 Mac 版微信聊天记录](https://www.v2ex.com/t/466053)

这个有点没有提到
> 用来浏览之前提到的*.db 文件（每个 db 都使用的相同的 key ）,注意：打开数据库的时候选择(raw key), 然后输入 0x,再输入刚才那 64 个字符;

encryption settings 选择  SQLCipher 3 defaults;

ps: 密码有66位，需要一个一个打。

我是把聊天记录转换成json，然后py分析。

## 具体功能
1. outputToText：把聊天记录整成文档;
2. date.py：统计每天的聊天条数，并做成折线图；
3. hour.py：统计每小时的聊天条数，看下哪个时间点聊天比较多；
4. frequent.py：统计词频，做成频率图；

# 参考
* [土办法导出 Mac 版微信聊天记录](https://www.v2ex.com/t/466053)
* [QQ聊天记录分析（R-3.5）](https://blog.csdn.net/ylb1327532664/article/details/82895401)
* [别再瞎猜了，心上人喜不喜欢你，看聊天记录就知道！](https://www.jfdaily.com/news/detail?id=55378)
* [Python 分词及词云绘图](https://blog.csdn.net/kk185800961/article/details/78610745)
