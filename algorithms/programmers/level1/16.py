# 정수 내림차순으로 배치하기

def solution(n):
    result = ''
    n = sorted([i for i in str(n)])
    # n.sort(reverse=True)
    for i in range(len(n), 0, -1):
        result += str(n[i-1])

    return int(result)