# 행렬의 덧셈

def solution(arr1, arr2):
    # answer = ''
    # for i in range(len(str(arr1))):
    #     try: answer += str(int(str(arr1)[i]) + int(str(arr2)[i]))
    #     except ValueError: answer += str(arr1)[i]

    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer