# Python-openCV发票去印章

`python-openCV`写了一个去除发票红色印章水印的小工具。鼠标拖拽，模拟`inpaint`图像修复的操作去除红色印章。修改HSV颜色值还可以用来去蓝色印章。

## 文档结构

主程序为`del_Water_print.py`；

包含选择操作：

	1、分离色道；
		channel = input('''请选择通道：
            r:红色通道
            g:绿色通道
            b:蓝色通道
            q:返回上一级菜单
            ''')
	2、鼠标选择抹除印章")
		印章颜色：
            1、红色印章
            2、蓝色印章
            q、返回上一级目录

测试程序`scale_with_Trackbar.py`用来观察不同阈值下的图像二值化变化。

测试程序`show_histogram.py`用来输出观察灰度的直方图分布，并且设置固定阈值二值化。

测试程序`hsv_12121.py`用来输出观察灰度的直方图分布，并且设置固定阈值二值化。

## 代码说明

输入图像:

```python
# path 为输入待处理图像地址
path = "src/input1.png "
```
处理结果保存在`/results`。

## 操作说明

读取待处理图像：

```python
img = cv2.imread("input1.png")  #加载图片
```

鼠标拖拽完成去印章效果：

![](/results/roi_red_removed.jpg)

颜色通道二值化去印章效果：

![](/results/r_results.png)

英文输入法下，按`s`保存：

```python
    if cv2.waitKey(0) & 0xFF == ord('s'):
        cv2.imwrite("results/roi_red_removed.jpg", image)
        print("图像已经保存")
```

运行时`Console`控制台输出结果为鼠标点击坐标，`point1`左上角起始点，`point2`右下角终止点，`width`为点击横跨宽幅，`heigh`为横跨高。
