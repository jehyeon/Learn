import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny():
    img = cv2.imread('images/ingame.jpg', cv2.IMREAD_GRAYSCALE)

    edge = cv2.Canny(img, 245, 255)

    cv2.imshow('original', img)
    cv2.imshow('Canny Edge', edge)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()