# 이상한 문자 만들기

def solution(s):
    answer = ''
    
    ck = True
    for i in s:
        if i == ' ':
            answer += ' '
            ck = True
        else:
            if ck == True:
                answer += i.upper()
                ck = False
            else:
                answer += i.lower()
                ck = True
    return answer
        
print(solution('try hello world'))