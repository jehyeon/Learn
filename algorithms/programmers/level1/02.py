# 같은 숫자는 싫어

def solution (arr):
    answer = [-1]
    for i in arr:
        if not i == answer[-1]:
            answer.append(i)
    return answer[1:]