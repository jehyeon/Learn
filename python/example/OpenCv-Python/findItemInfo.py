import numpy as np
import matplotlib.pyplot as plt

import cv2

def findItemInfo(img_path):
    # 이미지 읽기
    img = cv2.imread(img_path)
    origin_img = img

    # 블러로 노이즈 제거 
    #### Blur 좀 더 알아보기
    blur = cv2.GaussianBlur(img, (9, 9), 0)
    gray_img = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    
    # edge 추출
    edge = cv2.Canny(gray_img, 25, 50)
    # sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=1)

    # edge, contours, hierarchy = cv2.findContours(sobelx, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # cv2.drawContours(sobelx, contours, -1, (0, 255, 0), 3)

    plt.imshow(edge, cmap='gray'), plt.title('edge'), plt.xticks([]), plt.yticks([])

    plt.show()

findItemInfo('images/ingame.jpg')

def contour_approx():
    img = cv2.imread('images/ingame.jpg')
    origin_img = img.copy()
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    gray_img = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray_img, 35, 70)

    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

    edge, contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # print(contours)
    # 외곽이 하나만 추출되기 때문에
    # cnt = contours[50]  # 외곽을 하나만 정해서
    
    f = open('check.txt','w')
    # real_check = []
    # for cnt in contours:
    #     ###
    #     epsilon = 0.1 * cv2.arcLength(cnt, True)    # contours 둘레의 길이를 계산
    #     approx = cv2.approxPolyDP(cnt, epsilon, True)       # 다각형을 대상으로 꼭지점을 점점 줄임
    #     # cv2.drawContours(img, [approx], -1, (0, 0, 255), 1)
    #     if len(approx) == 4:
    #         real_check.append(approx)
    #         f.write(str(approx) + '\n')

    for cnt in contours:
        # print(cnt)
        # if len(cnt) >= 0:
            # print(cnt)
        # epsilon = 0.05 * cv2.arcLength(cnt, True)    # contours 둘레의 길이를 계산

        epsilon = cv2.arcLength(cnt, True)
        # approx = cv2.
        if epsilon >= 4:
        
            if epsilon >= 4000:
                f.write(str(epsilon) + '\n')
                cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)
    f.close()
    # for ok in real_check:
    #     cv2.drawContours(img, [ok], -1, (0, 0, 255), 1)
    # f.close()
    edgE = cv2.resize(edge, (960, 540))
    cv2.imshow('edge', edgE)
    imG = cv2.resize(img, (960, 540))
    # cv2.resizeWindow('Contour', 1000,531)
    cv2.imshow('Contour', imG)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def contour(img_path):
    img = cv2.imread(img_path)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 80, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# contour_approx()

# contour('images/ingame.jpg')