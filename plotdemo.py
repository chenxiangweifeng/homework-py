# -*- coding: utf-8 -*-
import time
import wordcloud
print(time.time())
print(time.daylight)

cy = wordcloud.WordCloud()                           # 生成词云对象
cy.generate("wordcloud by Python")                   # 加载词云文本
cy.to_file("wordcloud.png")                          # 输出词云文件