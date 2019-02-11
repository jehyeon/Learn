import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage():
    imgfile = 'images/shiva2.jpg'
    
    # cv2.imread: 이미지 파일을 읽기 위한 객체를 리턴
    # 첫 번째 인자는 파일 경로, 두 번째 인자는 이미지 파일을 읽는 방식을 나타내는 플래그
    '''
    cv2.IMREAD_COLOR: 컬러 이미지로 로드, 투명한 부분 모드 무시, default flag, 정수 값은 1
    cv2.IMREAD_GRAYSCALE: 흑백 이미지로 로드, 정수 값은 0
    cv2.IMREAD_UNCHANGED: 알파 채널을 포함하며 이미 그대로 로드, 정수 값은 -1
    '''
    img = cv2.cv2.imread(imgfile, cv2.cv2.IMREAD_COLOR)
    
    '''
    cv2.WINDOW_AUTOSIZE: 원본 이미지 크기로 고정하여 윈도우 생성
    cv2.WINDOW_NORMAL: 원본 이미지 크기로 윈도우를 생성하지만 사용자가 크기를 조절할 수 있음
    '''
    cv2.cv2.namedWindow('shiva', cv2.cv2.WINDOW_NUOMAL)

    # cv2.imread()에 의해 반환된 이미지 객체를 화면에 나타내기 위한 함수
    # 첫 번째 인자는 윈도우 타이틀이며, 두번째 인자는 화면에 표시할 이미지 객체이다.
    cv2.cv2.imshow('shiva', img)

    # cv2.waitKey(): 지정된 시간 동안 키보드 입력을 기다리는 함수, 단위는 1/1000초(ms)
    # 이 함수의 리턴 값은 사용자가 누른 키보드 값
    key = cv2.cv2.waitKey(0) & 0xFF # 운영체제가 64 비트인 경우 '&' 연산 필요
    
    if key == 27:
        cv2.cv2.destroyAllWindows()
    elif key == ord('c'):
        cv2.cv2.imwrite('images/shiva_copy.jpg', img)
        cv2.cv2.destroyAllWindows()

def usingPltShowImage():
    imgfile = 'images/shiva2.jpg'

    # 이미지를 흑백으로 읽는다.
    '''
    OpenCV BGR, Matplotlib RGB를 다루기 때문에,
    OpenCV로 읽은 컬러 이미지를 Matplotlib에 그대로 사용하면 제대로 된 컬러가 나오지 않는다.
    ''' 
    img = cv2.cv2.imread(imgfile, cv2.cv2.IMREAD_GRAYSCALE)

    # Matplotlib의 imshow 함수를 이용하여 화면에 이미지를 디스플레이 하는 방법을 정의한다.
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    
    # Matplotlib은 기본적으로 x, y축으로 눈금 표시를 한다.
    # 눈금 표시 없이 이미지 표시
    plt.xticks([])
    plt.yticks([])
    plt.title('shiva')
    plt.show()

# showImage()
usingPltShowImage()