
import cv2
import numpy as np
from PIL import Image
from pytesseract import image_to_string

def get_string(img_path):
    img = cv2.imread(img_path)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 60, 255, 0)
    cv2.imshow('ok',thr)


    print(image_to_string(thr, lang='kor'))
    cv2.waitKey(0)


def contour(img_path):
    img = cv2.imread(img_path)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 80, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour('images/dia.jpg')
# get_string('images/ok.png')