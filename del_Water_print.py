# coding: utf-8
# usage:python filename.py(win) python filename.py(linux)
# request: cv2, numpy
import cv2
import numpy as np
import os


def nothing(x):
    pass


def channel_option(channel_name):
    cv2.namedWindow("image")  # 创建一个窗口
    print('''[INFO]:
                    鼠标拖动滚动条调节阈值
                    按‘q’退出，按‘s’保存
                    ''')
    cv2.createTrackbar("threshold", "image", 0, 255, nothing)  # 创建一个滚动条
    while True:

        mythreshold = cv2.getTrackbarPos("threshold", "image")
        ret, image_bin = cv2.threshold(channel_name, mythreshold, 255,cv2.THRESH_BINARY)
        cv2.imshow("image", image_bin)
        # 按‘q’退出，按‘s’保存
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("退出!")
            cv2.destroyWindow("image")
            break

        elif cv2.waitKey(1) & 0xFF == ord("s"):
            cv2.imwrite("results/%s_result.png" % channel, image_bin)
            print("结果已保存")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break


def draw_rectangle_r(event, x, y, flags, param):
    global x1, y1, x2, y2
    if event==cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        print("point1:=", x1, y1)
    elif event == cv2.EVENT_LBUTTONUP:
        x2, y2 = x, y
        print("point2:=", x2, y2)
        print("width=",x2-x1)
        print("height=", y2 - y1)

        roi_area = image[y1:y2, x1:x]
        # cv2.imshow("")
        # cv2.imwrite('roi_area.jpg', roi_area)
        hsv_image = cv2.cvtColor(roi_area, cv2.COLOR_BGR2HSV)
        high_range = np.array([180, 255, 255])
        low_range = np.array([156, 43, 46])
        high_range1 = np.array([10, 255, 255])
        low_range1 = np.array([0, 43, 46])
        th = cv2.inRange(hsv_image, low_range, high_range)
        th1 = cv2.inRange(hsv_image, low_range1, high_range1)

        dst = cv2.inpaint(roi_area, th + th1, 3, cv2.INPAINT_TELEA)
        # cv2.imshow('dst', dst)

        image[y1:y2, x1:x2] = 2dst
        # cv2.imshow("image", img)
        # cv2.imwrite("new_img.jpg", image)
        # while(1):
        cv2.imshow("image", image)
        if cv2.waitKey(0) & 0xFF == ord('s'):
            cv2.imwrite("results/roi_red_removed.jpg", image)
            print("图像已经保存")


def draw_rectangle_b(event, x, y, flags, param):
    global x1, y1, x2, y2
    if event==cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        print("point1:=", x1, y1)
    elif event==cv2.EVENT_LBUTTONUP:
        x2, y2 = x, y
        print("point2:=", x2, y2)
        print("width=",x2-x1)
        print("height=", y2 - y1)

        roi_area = image[y1:y2, x1:x]
        # cv2.imshow("")
        # cv2.imwrite('roi_area.jpg', roi_area)
        hsv_image = cv2.cvtColor(roi_area, cv2.COLOR_BGR2HSV)
        high_range = np.array([124, 255, 255])
        low_range = np.array([100, 43, 46])
        # high_range1 = np.array([10, 255, 255])
        # low_range1 = np.array([0, 43, 46])
        th = cv2.inRange(hsv_image, low_range, high_range)
        # th1 = cv2.inRange(hsv_image, low_range1, high_range1)

        dst = cv2.inpaint(roi_area, th    , 3, cv2.INPAINT_TELEA)
        # cv2.imshow('dst', dst)

        image[y1:y2, x1:x2] = dst
        # cv2.imshow("image", img)
        # cv2.imwrite("results/result_removed.jpg", image)
        # while(1):
        cv2.imshow("image", image)
        if cv2.waitKey(0) & 0xFF == ord('s'):
            cv2.imwrite("results/roi_blue_removed.jpg", image)
            print("图像已经保存")
            cv2.destroyAllWindows()


print("[INFO]:程序启动中……")
# path 为输入待处理图像地址
path = "src/input1.png "
while True:

    option = input("请选择操作：1、分离色道；2、鼠标选择抹除印章")

    if option == '1':
        image = cv2.imread(path)
        cols, rows, dims = image.shape  # 获取图片高、宽、维度
        B_channel, G_channel, R_channel = cv2.split(image)
        print("进入分离色道操作")

        channel = input('''请选择通道：
            r:红色通道
            g:绿色通道
            b:蓝色通道
            q:返回上一级菜单
            ''')
        while channel == 'r':
            channel_option(R_channel)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

        while channel == 'g':
            channel_option(G_channel)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

        while channel == 'b':
            channel_option(B_channel)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

        while channel == 'q':
            break
        else:
            # print("[INFO]:输入错误,重新选择操作")
            continue

    elif option == '2':
        # hsv_mode()
        print('2')
        image = cv2.imread(path)
        # hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # RGB转HSV
        print("进入HSV鼠标标定操作")

        print_type = input('''
            印章颜色：
            1、红色印章
            2、蓝色印章
            q、返回上一级目录
        ''')
        if print_type == '1':
            print("请使用鼠标标出红色印章位置。按's'保存")
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', draw_rectangle_r)

            cv2.imshow('image', image)
            # if cv2.waitKey(0) & 0xFF == ord('q'):
            #     break
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif print_type == '2':
            print("请使用鼠标标出蓝色印章位置。按's'保存")
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', draw_rectangle_b)

            cv2.imshow('image', image)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif print_type == 'q':
            continue
            # return
        else:
            # print("[INFO]:输入错误,重新选择操作")
            continue
    else:
        print("[INFO]:输入错误，重新选择")
