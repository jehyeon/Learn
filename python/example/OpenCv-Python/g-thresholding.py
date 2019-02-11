import numpy as np
import cv2
import matplotlib.pyplot as plt

def GThresholding():
    img = cv2.cv2.imread('images/dia.jpg', cv2.cv2.IMREAD_GRAYSCALE)

    # img = cv2.cv2.GaussianBlur(img, (5, 5), 0)
    res = cv2.cv2.threshold(img, 127, 255, cv2.cv2.THRESH_BINARY)
    
    
    plt.imshow(res[1], 'gray')
    plt.title('good')
    plt.show()

# GThresholding()

def OtsuTresholding():
    img = cv2.cv2.imread('images/dia.jpg', cv2.cv2.IMREAD_GRAYSCALE)
    blur = cv2.cv2.GaussianBlur(img, (5,5), 0)
    otsu = cv2.cv2.threshold(blur, 0, 255, cv2.cv2.THRESH_BINARY+cv2.cv2.THRESH_OTSU)

    plt.imshow(otsu[1], 'gray')
    plt.title('good')
    plt.show()

# OtsuTresholding()

def contour():
    img = cv2.imread('images/dia.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 80, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()