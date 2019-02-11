# 시저 암호

def solution(s, n):
    result = ''
    for i in s:
        # i.isupper():
        if 65 <= ord(i) and ord(i) <= 90:
            if ord(i) + n > 90:
                result += chr(ord(i) + n - 26)
            else:
                result += chr(ord(i) + n)

        # i.islower():
        elif 97 <= ord(i) and ord(i) <= 122:
            if ord(i) + n > 122:
                result += chr(ord(i) + n - 26)
            else:
                result += chr(ord(i) + n)
        else:
            result += i
    return result