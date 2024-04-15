def solution(n, lost, reserve):
    students = []
    for i in range(n):
        students.append(1)

    for i in range(n):
        if i+1 in reserve:
            students[i] += 1
        if i+1 in lost:
            students[i] -= 1

    for i in range(n):
        if students[i] == 0:
            if i-1 > 0 and students[i-1] == 2:
                students[i] = 1
                students[i-1] -= 1
            elif i+1 < n and students[i+1] == 2:
                students[i] = 1
                students[i - 1] -= 1

    return n-students.count(0)

#print(solution(1, [1], [1]))
#print(solution(5, [2,4], [1,3,5]))
#print(solution(5, [2,4], [3]))
#print(solution(3, [3], [1]))
print(solution(3, [1], [2]))