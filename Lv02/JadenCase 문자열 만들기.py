def solution(s):
    list_s = list(s.split(' '))
    print(list_s)
    answer = []
    for i in list_s:
        answer.append(i.capitalize())

    return ' '.join(answer)