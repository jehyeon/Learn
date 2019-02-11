# 최대공약수와 최소공배수

'''
최대 공약수 = G, 최소 공배수 = L
A * B = L * G
L = G * a * b
A = G * a, B = G * b
'''

def solution(a, b):
    g = 0
    bigger = a if a > b else b
    smaller = b if a > b else a
    for i in range(smaller, 0, -1):
        if smaller % i == 0 and bigger % i == 0:
            g = i
            break
    l = int(a * b / g)

    return [g, l]

'''
    # 유클리드 호제법
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return = [c, int(a*b/c)]
'''

