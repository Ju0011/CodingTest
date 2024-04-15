def solution(people, limit):
    count = 0
    _people = sorted(people)

    while len(_people) > 1:
        if _people[0] + _people[-1] <= limit:  # 최댓값과 최솟값 묶어서 보트태움
            count += 1
            _people.pop(0)  # 최소 빼내고
            _people.pop(-1)  # 최대 빼내고
        else:
            count += 1
            _people.pop(-1)

        print(_people)

    if _people:  # _people에 1명 남아있는 경우 처리
        count += 1
    return count

print(solution([70,50,80,50], 100))
print(solution([70,80,50], 100))