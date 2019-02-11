# 소수 찾기

def solution(n):
    answer = 0
    numbers = [True for i in range(n+1)]      # 0 ~ n-1 까지의 숫자
    sosu = []      # 소수 list
    for number in range(2, int(n**(1/2)) + 2):
        if numbers[number] == True:
            if not number in sosu:
                sosu.append(number)
            for i in range(number*2, n+1, number):
                numbers[i] = False

    for i in range(2, n+1):
        if numbers[i] == True:
            answer += 1

    return answer