# 정수 제곱근 판별

import math

def solution(n):
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        return int((math.sqrt(n)+1)**2)
    else:
        return -1

    # sqrt = n ** (1/2)
    # if sqrt % 1 == 0:
    #   return (sqrt + 1) ** 2
    # return -1