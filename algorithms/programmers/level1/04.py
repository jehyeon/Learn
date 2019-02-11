# 문자열 다루기 기본

def solution(s):

    if not (len(s) == 4 or len(s) == 6):
        return False

    # len(s) in (4, 6)이 더 명료

    for i in s:
        if not (ord(i) >= 48 and ord(i) <= 57):
            return False

    # s.isdigit()

    return True