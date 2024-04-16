from collections import deque


def solution(progresses, speeds):
    times = deque()
    answer = []
    count = 0

    for i in range(len(progresses)):
        time = 0
        while True:
            if (progresses[i] + time * speeds[i]) >= 100:
                times.append(time)
                break
            else: time += 1

    while times:
        head = times.popleft()
        if head > times[0]:
            count += 1
    answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))