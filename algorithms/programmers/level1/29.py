# 콜라츠 추측

def solution(num):
    count = 0
    while not num == 1:
        if count > 500: return -1
        if num % 2: num = num*3 + 1
        else: num /= 2
        count += 1
    return count