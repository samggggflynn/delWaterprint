# -*- coding: utf-8 -*-
"""
@title: 去除印章
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("src/input.png",cv2.IMREAD_COLOR)   # 以BGR色彩读取图片
# image = cv2.resize(image0,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)  # 缩小图片0.5倍（图片太大了）
cols, rows, dims =image.shape                         # 获取图片高、宽、维度
B_channel,G_channel,R_channel=cv2.split(image)        # 注意cv2.split()返回通道顺序（因为是按照BGR读取的）

cv2.imshow('Blue channel',B_channel)
cv2.imshow('Green channel',G_channel)
cv2.imshow('Red channel',R_channel)

pixelSequence=R_channel.reshape([rows*cols,1])    # 红色通道的histgram 变换成一维向量
numberBins=256                                    # 统计直方图的组数
plt.figure()                                      # 计算直方图
'''
返回的Figure实例会被传递给后端的新图像管理器new_figure_manager，
这将允许定制的Figure类到pylab接口，
额外饿参数会被传递给图形初始化函数
'''
manager = plt.get_current_fig_manager()
histogram,bins,patch=plt.hist(pixelSequence,
                              numberBins,
                              facecolor='red',
                              histtype='bar')     # facecolor设置为黑色
'''
matplotlib.pyplot.hist(
    x, bins=None, range=None, 
    density=None, weights=None, cumulative=False, 
    bottom=None, histtype='bar', align='mid', 
    orientation='vertical', rwidth=None, log=False, 
    color=None, label=None, stacked=False, normed=None, 
    hold=None, data=None, **kwargs)
    参数：
    x : (n,) n维数组或者n维数组序列，多维数组长度不要求一致
    bins : 整数，序列，或者 ‘auto’, 可选
    color:颜色
    histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, 默认"bar",
'''
# 设置坐标范围
y_maxValue=np.max(histogram)
plt.axis([0,255,0,y_maxValue])
'''
    参数一：X轴坐标最小值
    参数二：X轴坐标最大值
    参数三：Y轴坐标最小值
    参数四：Y轴坐标最大值
    
'''
# 设置坐标轴
plt.xlabel("gray Level",fontsize=20)
plt.ylabel('number of pixels',fontsize=20)
plt.title("Histgram of red channel", fontsize=25)
plt.xticks(range(0,255,10))
# 显示直方图
# plt.pause(0.05)

# 保存直方图
plt.savefig("results/histgram.png", dpi=None, bbox_inches=None)
'''
参数(fname, dpi=None, facecolor=’w’, edgecolor=’w’, 
orientation=’portrait’, papertype=None, format=None, 
transparent=False, bbox_inches=None, pad_inches=0.1, 
frameon=None)
'''
plt.show()

# 红色通道阈值(调节好函数阈值为160-190时效果最好，太小显示不完整，太大黑色太多)
dims, RedThresh = cv2.threshold(R_channel,160,255,0)  # THRESH_BINARY二元阈值
'''
像素高于阈值时，给像素赋予新值，否则，赋予另外一种颜色
HRESH_BINARY二元阈值

cv2.threshold (src, thresh, maxval, type)
    第一个原图像，
    第二个进行分类的阈值，
    第三个是高于（低于）阈值时赋予的新值，
    第四个是一个方法选择参数，常用的有： 
    --------------------------------------------
    • cv2.THRESH_BINARY（黑白二值）       （或者0)
    • cv2.THRESH_BINARY_INV（黑白二值反转）(或者1） 
    • cv2.THRESH_TRUNC （得到的图像为多像素值） 
    • cv2.THRESH_TOZERO 
    • cv2.THRESH_TOZERO_INV 
    --------------------------------------------
    或者：
    --------------------------------------------
    阈值	|小于阈值的像素点	|大于阈值的像素点
    0	    |置0	            |置填充色
    1	    |置填充色	        |置0
    2	    |保持原色	        |置灰色
    3	    |置0	            |保持原色
    4	    |保持原色	        |置0
    --------------------------------------------
该函数有两个返回值：
第一个retVal（得到的阈值值（在后面一个方法中会用到）），
第二个就是阈值化后的图像数组。 
'''

# 显示效果
cv2.imshow('original color image', image)
cv2.imshow("RedThresh", RedThresh)

# 保存图像
cv2.imwrite('results/scale_image.jpg', image)
cv2.imwrite('results/RedThresh.jpg', RedThresh)

# 膨胀操作（可以省略）
# element = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
# erode = cv2.erode(RedThresh, element)
# cv2.imshow("erode",erode)
# cv2.imwrite("erode.jpg",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
