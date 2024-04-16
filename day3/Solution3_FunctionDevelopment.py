from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))