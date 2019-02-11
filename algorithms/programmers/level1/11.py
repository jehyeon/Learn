# 문자열 내 p와 y의 개수

def solution(s):
    s = s.upper()
    nP = 0
    nY = 0
    for i in s:
        if i == 'P':
            nP += 1
        elif i == 'Y':
            nY += 1
    return nP == nY

    # return s.lower().count('p') == s.lower().count('y')