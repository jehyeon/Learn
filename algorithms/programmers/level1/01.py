# 가운데 글자 가져오기

def solution (s):
    start = 0
    end = len(s)

    while start < end:
        start += 1
        end -= 1

    return s[start-1:end+1]
