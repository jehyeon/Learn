# 제일 작은 수 제거하기

def solution(arr):
    if len(arr) == 1: 
        return [-1]
    arr.remove(sorted(arr)[0])
    return arr

    # return [i for i in arr: if i > min(arr)]