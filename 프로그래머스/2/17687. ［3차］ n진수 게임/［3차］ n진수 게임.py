def change_number(n, base):
    # 16진수
    temp = "0123456789ABCDEF"
    q, r = divmod(n, base)

    if q == 0:
        return temp[r]
    else:
        return change_number(q, base) + temp[r]

def solution(n, t, m, p):
    answer = ''

    num = 0
    while True:
        answer += change_number(num, n)

        if len(answer) >= t * m:
            answer = answer[:t*m]
            return answer[p-1:t * m:m]
        num += 1