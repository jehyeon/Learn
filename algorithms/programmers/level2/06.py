# 다음 큰 숫자

def solution(n):
    result = n
    nOne = bin(n).count('1')

    while True:
        result += 1
        if bin(result).count('1') == nOne:
            return result