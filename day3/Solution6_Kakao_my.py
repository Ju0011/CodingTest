# 올바른 괄호 문자열인지 확인
def right_str(p):
    if len(p)% 2 != 0:
        return False

    stack = []
    for i in p:
        stack.append(i)

        if len(stack) > 1 and stack[-2] + stack[-1] == '()':
            stack.pop()
            stack.pop()

    if len(stack) != 0:
        print(stack)
        return False
    return True

# 균형잡힌 문자열, uv 분리
def balance_str(w):
    u = []
    countA = 0
    countB = 0
    index = 0

    for i in range(len(w)):
        if w[i] == '(':
            countA += 1
        elif w[i] == ')':
            countB += 1
        if countA == countB:
            index = i
            break

    u = w[:index+1]
    v = w[index+1:]

    return u,v

# def solution(p):
#     answer = ''
#     u,v = balance_str(p)
#     if right_str(u):
#         return u+solution(v)
#     else:
#
#     return answer



#print(solution("()))((()"))
#print(balance_str("(()())()"))
#print(balance_str("()))((()"))