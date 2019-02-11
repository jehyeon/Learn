# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    ck = True
    for i in s:
        if i == ' ':
            answer += i
            ck = True
        elif ck == True:
            answer += i.upper()
            ck = False
        else:
            answer += i.lower()
    return answer

    # return s.title()
        

