def solution(s):
    answer = True
    A = s.count('P') + s.count('p')
    B = s.count('Y') + s.count('y')

    if A != B:
        answer = False

    return answer

print(solution(input()))

