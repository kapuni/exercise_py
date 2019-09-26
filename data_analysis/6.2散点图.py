# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:31:24 2019

@author: kapuni
"""

import pandas 
import matplotlib
import matplotlib.pyplot as plt

data = pandas.read_csv(
        'D:/PDABook/第六章/6.2 散点图/散点图.csv',
        engine='python', encoding='utf-8'
        )


#选择字体
font = matplotlib.font_manager.FontProperties(
        fname = 'D:/PDABook/SourceHanSansCN-Light.otf', size=10
        )

#配置主题颜色， RGB[0,1]
mainColor = (91/255, 155/255, 213/255, 1)

# =============================================================================
# #绘制散点图
# plt.scatter(data['广告费用'], data['购买用户数'],
#             c=mainColor)
# 
# #设置坐标标签，字体和颜色
# plt.xlabel('广告费用', color=mainColor, fontproperties=font)
# plt.ylabel('购买用户数', color = mainColor, fontproperties=font)
# 
# #设置坐标轴的刻度仰视，颜色和字体
# plt.xticks(
#         color = mainColor,
#         fontproper=font
#         )
# plt.yticks(
#         color=mainColor,
#         fontproper=font
#         )
# =============================================================================

plt.figure()
#颜色粉色
pinkColor = (255/255, 0/ 255, 102/255, 1)
#蓝色
blueColor = (91/255, 155/ 255, 213/255, 1)
#'o'标记促销的点
#通过s参数设置点的大小，直接用渠道数太小
#所以比例放大30倍，
plt.scatter(
        data[data['促销'] == '是']['广告费用'],
        data[data['促销'] == '是']['购买用户数'],
        c = pinkColor, marker='o',
        s=data[data['促销'] == '是']['渠道数'] * 30
        )
#'x'标记不促销的点
plt.scatter(
        data[data['促销'] == '否']['广告费用'],
        data[data['促销'] == '否']['购买用户数'],
        c = blueColor, marker='x',
        s=data[data['促销'] == '是']['渠道数'] * 30
        )

plt.xlabel('广告费用', color=mainColor, fontproperties=font)
plt.ylabel('购买用户数', color = mainColor, fontproperties=font)

plt.xticks(
         color = mainColor,
         fontproperties=font
         )
plt.yticks(
         color=mainColor,
         fontproperties=font
         )
#加图例
legend = plt.legend(labels=['促销', '不促销'], prop= font)
