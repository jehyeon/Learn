# 최솟값 만들기

def solution(a, b):
    tot = 0
    a = sorted(a)
    b = sorted(b, reverse=True)
    for i in range(len(a)):
        tot += a[i] * b[i]
    return tot