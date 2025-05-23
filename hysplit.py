# -*- coding: utf-8 -*-
"""
Created on Wed May 21 12:21:03 2025

@author: wukai
"""

import act
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 读取数据
ds = act.io.read_hysplit('D:/3/houstonaug300.0summer2025050100')

# 原代码的读取方式会报错
# filename = DATASETS.fetch('D:/3/houstonaug300.0summer2010080100')

# 创建绘图对象
disp = act.plotting.GeographicPlotDisplay(ds)

# 绘图并获取 axes 对象
ax = disp.geoplot('PRESSURE', cartopy_feature=['STATES', 'OCEAN', 'LAND'])

# 设置显示经纬度的范围
ax.set_extent([-100, -80, 30, 40])

# 设置字体样式
label_style = {'fontsize': 12, 'fontname': 'Arial'}

# 获取 Gridliner 对象并设置标签字体样式和边界显示控制
gridliner = ax.gridlines(draw_labels=True)
gridliner.xlabel_style = label_style
gridliner.ylabel_style = label_style

# ✅ 关闭右侧和上侧标签
gridliner.right_labels = False
gridliner.top_labels = False

# plt.show()
plt.rcParams['font.sans-serif'] = ['Arial'] 

picpath = 'HYSPLIT.png'
plt.savefig(picpath,dpi=600,bbox_inches = 'tight')