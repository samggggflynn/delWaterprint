# -*- coding: utf-8 -*-
import cv2
import numpy as np

np.set_printoptions(threshold=np.inf)
'''
set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None)
precision : int, optional，float输出的精度，即小数点后维数，默认8
threshold : int, optional，当数组数目过大时，设置显示几个数字，其余用省略号
edgeitems : int, optional，边缘数目
linewidth : int, optional，The number of characters per line for the purpose of inserting line breaks (default 75).
suppress  : bool, optional，是否压缩由科学计数法表示的浮点数
nanstr    : str, optional，String representation of floating point not-a-number (default nan).
infstr    : str, optional，String representation of floating point infinity (default inf).
np.set_printoptions(threshold=np.nan) 
'''
image = cv2.imread('src/input1.png')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # RGB转HSV

low_range = np.array([150, 103, 100])
# high_range = np.array([180, 255, 255])
# low_range = np.array([156, 43, 46])
high_range = np.array([180, 255, 255])

th = cv2.inRange(hsv_image, low_range, high_range)
'''
cv2.inRange(hsv, lower_red, upper_red) #lower20===>0,upper200==>0
第一个参数：hsv指的是原图
第二个参数：lower_red指的是图像中低于这个lower_red的值，图像值变为0
第三个参数：upper_red指的是图像中高于这个upper_red的值，图像值变为0
而在lower_red～upper_red之间的值变成255
'''
index1 = th == 255
cv2.imshow("th是啥", th)  # th是印章# 的掩膜
# 给mask加膨胀操作（可以省略）

element = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilate_mask = cv2.dilate(th, element)
cv2.imshow("dilate",dilate_mask )  # 黑底白印的掩膜

# cv2.imwrite("dilate.jpg",dilate)
# cv2.imshow('mask', dilate)
# cv2.imwrite('mask.png', dilate)

mask = cv2.imread('mask.png', 0)
img = np.zeros(image.shape, np.uint8)
img[:, :] = (255, 255, 255)  # 背景全白
img[index1] = image[index1]  # (0,0,255)  # img : 白底的彩色印章提取

dst = cv2.inpaint(image, dilate_mask , 3, cv2.INPAINT_TELEA)
# dst = cv2.inpaint(image, th, 3, cv2.INPAINT_NS)
'''
dst = cv2.inpaint（src，mask, inpaintRadius，flags）
参数：
    src：输入8位1通道或3通道图像。
    inpaintMask：修复掩码，8位1通道图像。非零像素表示需要修复的区域。
    dst：输出与src具有相同大小和类型的图像。
    inpaintRadius：算法考虑的每个点的圆形邻域的半径。
    flags：
        INPAINT_NS基于Navier-Stokes的方法
        Alexandru Telea的INPAINT_TELEA方法
'''

cv2.imshow('original_img', image)
cv2.imshow('extract_img', img)
cv2.imshow('dst',dst)
# print(cv2.__version__)
cv2.waitKey(0)
cv2.destroyAllWindows()