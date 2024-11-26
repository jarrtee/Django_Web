import cv2
import numpy as np
import pandas
import matplotlib.pyplot as plt


#定义class
class Visual:
    def __init__(self):
        pass

    def ImageGray(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray
