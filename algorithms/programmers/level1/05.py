# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    result = []

    for element in arr:
        if element % divisor == 0:
            result.append(element)
    
    if len(result) == 0:
        result.append(-1)

    return sorted(result)