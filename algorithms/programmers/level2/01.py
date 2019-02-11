# 피보나치 수

# n번째 피보나치 수 / 1234567을 return
def solution(n):
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return a % 1234567
    if n == 1: return 0
    
print(solution(2))