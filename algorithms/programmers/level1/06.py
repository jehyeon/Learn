# 문자열을 정수로 바꾸기

def solution(s):
    result = 0
    digit = 1
    
    for i in range(len(s)-1, 0, -1):
        result += int(s[i]) * digit
        digit *= 10

    if s[0].isdigit():
        result += int(s[0]) * digit
    elif s[0] == '-':
        result *= -1

    return result
