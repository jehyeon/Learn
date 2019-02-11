# 자릿수 더하기

def solution(n):
    result = 0
    n = str(n)
    for i in n:
        result += int(i)
    return result

    # return sum([int(i) for i in str(n)])