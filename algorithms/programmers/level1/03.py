# 두 정수 사이의 합

def solution (a, b):
    result = 0
    if a - b > 0:
        b, a = a, b
    for i in range(a, b + 1):
        result += i
    return result
