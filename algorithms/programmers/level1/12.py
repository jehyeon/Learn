# 자연수 뒤집어 배열로 만들기

def solution(n):
    result = []
    n = str(n)
    for i in range(len(n),0,-1):
        result.append(int(n[i-1:i]))
    return result

    # return [int(i) for i in str(n)][::-1]     # [::-1] 뒤에서부터 1씩 
    # return list(map(int, reversed(str(n))))