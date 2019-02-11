# 문자열 내림차순으로 배치하기
def solution(s):
    answer = sorted([ord(i) for i in s], reverse=True)
    return ''.join(chr(i) for i in answer)
    # answer = ''.join(sorted(s, reverse=True))