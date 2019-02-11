# 최댓값과 최솟값

def solution(s):
    array = sorted([int(i) for i in s.split()])
    return str(array[0]) + ' ' + str(array[-1])