# 올바른 괄호

def solution(n):
    stack = []
    for i in n:
        if i == ')':
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
        else:
            stack.append(i)

    if len(stack) > 0 and stack[-1] == '(':
        return False
    return True