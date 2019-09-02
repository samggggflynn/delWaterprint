import cv2
import numpy as np


def nothing(x):
    pass


def mythreshold(image):
    # 打开图片
    image_org = cv2.imread(image)
    # 转为灰度
    image_gray = cv2.cvtColor(image_org, cv2.COLOR_RGB2GRAY)

    cv2.namedWindow("image", flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)  # 创建一个窗口
    cv2.createTrackbar("threshold", "image", 0, 255, nothing)  # 创建一个滚动条
    '''
    cv2.createTrackbar(c1,c2,c3,c4,c5)
    参数1：滚动条名字
    参数2：窗口名字
    参数3：滚动条最小值
    参数4：滚动条可以达到的最大值位置
    参数5：默认值为0，指向回调函数
    参数6：默认值为0，用户传给回调函数的数据值
    '''

    while True:
        mythreshold = cv2.getTrackbarPos("threshold", "image")
        '''
        cv2.getTrackbarPos(c1,c2)
        参数1：滚动条的名字
        参数2：滚动条所在窗口的名字
        '''
        ret, image_bin = cv2.threshold(image_gray, mythreshold, 255,
                                       cv2.THRESH_BINARY)
        cv2.imshow("image", image_bin)


        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


def main():
    path = "src/input1.png"
    mythreshold(path)


if __name__ == '__main__':
    main()