# x만큼 간격이 있는 n개의 숫자
# fail 1 case

def solution(x, n):
    if x == 0: return [0]
    return [i for i in range(x, x*n+x, x)]