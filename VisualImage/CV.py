import cv2
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    img = np.zeros((512, 512, 3), np.uint8)
    drawing = False  # 如果按下鼠标，则为真
    mode = True  # 如果为真，绘制矩形。按 m 键可以切换到曲线
    ix, iy = -1, -1


    # 鼠标回调函数
    def draw_circle(event, x, y, flags, param):
        global ix, iy, drawing, mode
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                if mode == True:
                    cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
                else:
                    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
